#!/usr/bin/env python
# generated by wxGlade 0.3.2 on Tue Mar 23 10:57:02 2004

import wx

MENU_PREFS = 101
MENU_EXIT = 102
MENU_HELP_CONTENTS = 103

class ShtoomMainWindow(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ShtoomMainWindow.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        
        # Menu Bar
        self.shtoom_frame_menubar = wx.MenuBar()
        self.SetMenuBar(self.shtoom_frame_menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(MENU_PREFS, "Preferences", "Edit Shtoom preferences", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(MENU_EXIT, "Exit", "", wx.ITEM_NORMAL)
        self.shtoom_frame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(MENU_HELP_CONTENTS, "Contents", "", wx.ITEM_NORMAL)
        self.shtoom_frame_menubar.Append(wxglade_tmp_menu, "Help")
        # Menu Bar end
        self.shtoom_frame_statusbar = self.CreateStatusBar(1, 0)
        self.label_1 = wx.StaticText(self, -1, "Address:", style=wx.ALIGN_CENTRE)
        self.combo_address = wx.ComboBox(self, -1, choices=["choice 1"], style=wx.CB_DROPDOWN)
        self.button_call = wx.Button(self, -1, "Call")
        self.button_hangup = wx.Button(self, -1, "Hang Up")
        self.button_register = wx.Button(self, -1, "Register")
        self.button_more = wx.Button(self, -1, "+")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

        wx.EVT_MENU(self, MENU_EXIT, self.DoExit)

    def __set_properties(self):
        # begin wxGlade: ShtoomMainWindow.__set_properties
        self.SetTitle("Shtoom")
        self.shtoom_frame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        shtoom_frame_statusbar_fields = ["shtoom_frame_statusbar"]
        for i in range(len(shtoom_frame_statusbar_fields)):
            self.shtoom_frame_statusbar.SetStatusText(shtoom_frame_statusbar_fields[i], i)
        self.combo_address.SetSelection(0)
        self.button_more.SetSize((20, 27))
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ShtoomMainWindow.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.label_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(self.combo_address, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_4.Add(self.button_call, 1, wx.ALL, 5)
        sizer_4.Add(self.button_hangup, 1, wx.ALL, 5)
        sizer_4.Add(self.button_register, 1, wx.ALL, 5)
        sizer_4.Add(self.button_more, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_2.Add(sizer_4, 0, wx.EXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        sizer_2.SetSizeHints(self)
        self.Layout()
        # end wxGlade

    def DoExit(self, event):
        self.Close(True)
        #reactor.stop()

# end of class ShtoomMainWindow


