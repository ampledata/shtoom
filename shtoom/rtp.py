# Feed it hostname, port, and an audio file (in 8bit ulaw - sox -t ul)
# Or skip the audio file and it'll read from the microphone
# See also rtprecv.py for something that listens to a port and dumps it to
# the audio device
#
# 'use_setitimer' will give better results - needs
# http://polykoira.megabaud.fi/~torppa/py-itimer/
# $Id: rtp.py,v 1.8 2003/11/16 03:47:30 anthonybaxter Exp $
#

import time, signal, struct, random
from time import time, sleep

from select import select as Select

try:
    import itimer
except ImportError:
    itimer = None

from twisted.internet import reactor
from twisted.internet.protocol import DatagramProtocol

from shtoom.audio import getAudioDevice


# XXX anthony, suggested strategies to try:
# 1. without itimer, using LoopingCall for sending packets,
#    don't use doRead hack. This should wake reactor often
#    enough that it should be fine. Perhaps add another LoopingCall
#    with slightly  higher resolution that does nothing, just
#    wakes reactor.
# 2. with itimer... have the itimer do a reactor.wakeUp() every 10ms,
#    and using LoopingCall to schedule writes.

class LoopingCall:
    """Move into twisted if this helps."""
    def __init__(self, f, *a, **kw):
        self.f = f
        self.a = a
        self.kw = kw
        self.running = True

    def loop(self, interval):
        self._loop(time.time(), 0, interval)

    def stop(self):
        self.running = False
        if hasattr(self, "call"):
            self.call.cancel()
    
    def _loop(self, starttime, count, interval):
        if hasattr(self, "call"):
            del self.call
        self.f(*self.a, **self.kw)
        now = time.time()
        while self.running:
            count += 1
            fromStart = count * interval
            fromNow = starttime - now
            delay = fromNow + fromStart
            if delay > 0:
                self.call = reactor.callLater(delay, self._loop, starttime, count, interval)
                return


class RTPProtocol(DatagramProtocol):
    """Implementation of the RTP protocol.

    Also manages a RTCP instance.
    """
    
    if itimer:
        use_setitimer = 1
    else:
        use_setitimer = 0
    _cbDone = None
    fp = None
    outfp = None

    def createRTPSocket(self):
        """Start listening on UDP ports for RTP and RTCP.

        Return (rtpPortNo, rtcpPortNo).
        """
        from twisted.internet.error import CannotListenError
        import rtcp
        self.RTCP = rtcp.RTCPProtocol()

        # RTP port must be even, RTCP must be odd
        rtpPort = 30000 + random.randint(0, 20000)
        if (rtpPort % 2) == 1:
            rtpPort += 1
        while True:
            try:
                self.rtpListener = reactor.listenUDP(rtpPort, self)
            except CannotListenError:
                rtpPort += 2
                continue
            else:
                break
        
        rtcpPort = rtpPort + 1
        while True:
            try:
                self.rtcpListener = reactor.listenUDP(rtcpPort, self.RTCP)
            except CannotListenError:
                self.rtpListener.stopListening()
                rtpPort = rtpPort + 2
                rtcpPort = rtpPort + 1
                continue
            else:
                break
        return (rtpPort, rtcpPort)

    def whenDone(self, cbDone):
        self._cbDone = cbDone

    def stopSendingAndReceiving(self):
        self.Done = 1
        self.rtpListener.stopListening()
        self.rtcpListener.stopListening()
        if hasattr(self, "fp"):
            del self.fp
        if hasattr(self, "outfp"):
            del self.outfp

    def startReceiving(self, fp=None):
        if fp is None:
            self.outfp = getAudioDevice('w')
        else:
            self.outfp = fp

    def startSending(self, dest, fp=None):
        self.dest = dest
        if fp is None:
            self.fp = getAudioDevice('r')
        else:
            self.fp = fp
        self.sendFirstData()

    def startSendingAndReceiving(self, dest, fp=None):
        self.dest = dest
        if fp is None:
            self.fp = getAudioDevice('rw')
        else:
            self.fp = fp
        self.outfp = self.fp
        self.sendFirstData()

    def sendFirstData(self):
        from twisted.internet import reactor
        self.seq = self.genRandom(bits=16)
        self.ts = self.genInitTS()
        self.ssrc = self.genSSRC()
        self.sample = None
        self.packets = 0
        self.Done = 0
        self.sent = 0
        try:
            self.sample = self.fp.read(160)
        except IOError: # stupid sound devices
            self.sample = None
            pass
        if not self.use_setitimer:
            reactor.callLater(0.015, self.nextpacket)
        else:
            import signal, itimer 
            signal.signal(signal.SIGALRM, self.nextpacket)
            itimer.setitimer(itimer.ITIMER_REAL, 0.019, 0.019)

    def datagramReceived(self, datagram, addr):
        # XXX keep stats
        if self.outfp:
            if len(datagram) != 172:
                print "datagram len %d!!"%(len(datagram))
            try:
                self.outfp.write(datagram[12:])
            except IOError:
                pass

    def genSSRC(self):
        # Python-ish hack at RFC1889, Appendix A.6
        import md5, time, os, socket
        m = md5.new()
        m.update(str(time.time()))
        m.update(str(os.getuid()))
        m.update(str(os.getgid()))
        m.update(str(socket.gethostname()))
        hex = m.hexdigest()
        nums = hex[:8], hex[8:16], hex[16:24], hex[24:]
        nums = [ int(x, 16) for x in nums ]
        ssrc = 0
        for n in nums: ssrc = ssrc ^ n
        return ssrc

    def genInitTS(self):
        # Python-ish hack at RFC1889, Appendix A.6
        import md5, time, os, socket
        m = md5.new()
        m.update(str(self.genSSRC()))
        m.update(str(time.time()))
        hex = m.hexdigest()
        nums = hex[:8], hex[8:16], hex[16:24], hex[24:]
        nums = [ int(x, 16) for x in nums ]
        ts = 0
        for n in nums: ts = ts ^ n
        return ts

    def genRandom(self, bits):
        import md5
        m = md5.new()
        m.update(open('/dev/urandom').read(128))
        hex = m.hexdigest()
        random = int(hex[:bits//4],16)
        return random

    def nextpacket(self, n=None, f=None, pack=struct.pack):
        if self.Done:
            if self.use_setitimer:
                import itimer
                itimer.setitimer(itimer.ITIMER_REAL, 0.0, 0.0)
            if self._cbDone:
                self._cbDone()
            return
        if not self.use_setitimer:
            reactor.callLater(0.015, self.nextpacket)
        #t = time()
        #if self.last is not None:
        #    print "%d"%(1000*(t- self.last))
        #self.last = t
        self.packets += 1
        if self.sample is not None:
            self.sent += 1
            # This bit is hardcoded for G711 ULAW. When other codecs are
            # done, the first two bytes will change (but should be mostly
            # constant across a RTP session).
            hdr = pack('!BBHII', 0x80, 0x0, self.seq, self.ts, self.ssrc)
            self.transport.write(hdr+self.sample, self.dest)
            self.sample = None
        else:
            print "skipping audio, %s/%s sent"%(self.sent, self.packets)
        self.seq += 1
        self.ts += 160
        try:
            if self.fp:
                self.sample = self.fp.read(160)
        except IOError:
            pass

        # We do the select ourself, to stop the UDP listener and the 
        # timer loop from tripping over each other. Kinda sucky.
        r, ignored, ignored = Select([self.rtpListener], [], [], 0.0)
        if r:
            r[0].doRead()
        
        if (self.sample is not None) and (len(self.sample) == 0):
            print "And we're done!"
            self.Done = 1
