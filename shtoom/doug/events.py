# Copyright (C) 2004 Anthony Baxter

class Event(object):
    """
    """
    def getEventName(self):
        return self.__class__.__name__

class    DTMFReceivedEvent(Event):
    """ Received some DTMF keystrokes.
    """
    def __init__(self, digits):
        self.digits = digits

class        DTMFTimeoutEvent(DTMFReceivedEvent):
    """ A timeout occurred while collecting DTMF.

        Any digits collected will be returned in this object's digits
        attribute.
    """

class    MediaDoneEvent(Event):
    """ A media play/record completed
    """

class        MediaPlayDoneEvent(MediaDoneEvent):
    """ A mediaPlay completed
    """

class            MediaPlayContentDoneEvent(MediaPlayDoneEvent):
    """ A mediaPlay completed because it finished with the content
    """

class            MediaPlayContentFailedEvent(MediaPlayDoneEvent):
    """ A mediaPlay completed because the source of audio failed
    """

class            MediaPlayUserBargeInEvent(DTMFReceivedEvent,
                                           MediaPlayDoneEvent):
    """ A mediaPlay completed because the user hit a key
    """

class            MediaPlayTimerExpiredEvent(MediaPlayDoneEvent):
    """ A mediaPlay completed because a timeout was exceeded
    """

class            MediaPlayRemoteClosedEvent(MediaPlayDoneEvent):
    """
    """


class        MediaRecordDoneEvent(MediaDoneEvent):
    """ media record done
    """

class            MediaRecordRemoteClosedEvent(MediaRecordDoneEvent):
    """ A media record ended because the remote end closed the call
    """

class            MediaRecordTimeoutExceededEvent(MediaRecordDoneEvent):
    """ A media record ended because a specified timeout was exceeded
    """

class            MediaRecordFailedEvent(MediaRecordDoneEvent):
    """ A media record failed
    """

class                MediaRecordStoreFailedEvent(MediaRecordDoneEvent):
    """ A media record failed because the storage didn't work
    """

class    CallStartedEvent(Event):
    """ A call started
    """

class        InboundCallStartedEvent(CallStartedEvent):
    """ A new inbound call started
    """

class        OutboundCallStartedEvent(CallStartedEvent):
    """ A new outbound call started
    """

class    CallEndedEvent(Event):
    """ A call under the control of this VoiceApp ended.
    """

class    TimeoutEvent(Event):
    """ A user-specified timeout occurred.

        The value of this exception is the timer that expired.
    """

class    ApplicationSpecificEvent(Event):
    """ An Application-Specific Event.
        Subclass this to implement your own events
    """
