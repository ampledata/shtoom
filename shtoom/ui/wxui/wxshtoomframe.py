#!/usr/bin/env python
# generated by wxGlade 0.3.2 on Thu Apr 29 21:11:39 2004

import wx

class ShtoomMainFrame(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: ShtoomMainFrame.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.advanced = wx.Panel(self, -1)
        
        # Menu Bar
        self.shtoom_frame_menubar = wx.MenuBar()
        self.SetMenuBar(self.shtoom_frame_menubar)
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.MENU_REGISTER, "Register", "Register as a different user", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.MENU_PREFS, "Preferences", "Edit Shtoom preferences", wx.ITEM_NORMAL)
        wxglade_tmp_menu.Append(self.MENU_EXIT, "Exit", "Exit Shtoom", wx.ITEM_NORMAL)
        self.shtoom_frame_menubar.Append(wxglade_tmp_menu, "File")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.MENU_ERRORLOG, "Error Log", "View any error or debug messages", wx.ITEM_NORMAL)
        self.shtoom_frame_menubar.Append(wxglade_tmp_menu, "View")
        wxglade_tmp_menu = wx.Menu()
        wxglade_tmp_menu.Append(self.MENU_HELP_CONTENTS, "Contents", "Give me some help", wx.ITEM_NORMAL)
        self.shtoom_frame_menubar.Append(wxglade_tmp_menu, "Help")
        # Menu Bar end
        self.shtoom_frame_statusbar = self.CreateStatusBar(1, 0)
        self.label_1 = wx.StaticText(self, -1, "Address:", style=wx.ALIGN_CENTRE)
        self.combo_address = wx.ComboBox(self, -1, choices=["choice 1"], style=wx.CB_DROPDOWN)
        self.button_call = wx.Button(self, self.BUTT_CALL, "Call")
        self.button_lookup = wx.Button(self, self.BUTT_LOOKUP, "Lookup Address")
        self.button_advanced = wx.Button(self, self.BUTT_ADVANCED, "-")
        self.button_1 = wx.Button(self.advanced, self.BUTT_1, "1", style=wx.BU_EXACTFIT)
        self.button_2 = wx.Button(self.advanced, self.BUTT_2, "2", style=wx.BU_EXACTFIT)
        self.button_3 = wx.Button(self.advanced, self.BUTT_3, "3", style=wx.BU_EXACTFIT)
        self.button_4 = wx.Button(self.advanced, self.BUTT_4, "4", style=wx.BU_EXACTFIT)
        self.button_5 = wx.Button(self.advanced, self.BUTT_5, "5", style=wx.BU_EXACTFIT)
        self.button_6 = wx.Button(self.advanced, self.BUTT_6, "6", style=wx.BU_EXACTFIT)
        self.button_7 = wx.Button(self.advanced, self.BUTT_7, "7", style=wx.BU_EXACTFIT)
        self.button_8 = wx.Button(self.advanced, self.BUTT_8, "8", style=wx.BU_EXACTFIT)
        self.button_9 = wx.Button(self.advanced, self.BUTT_9, "9", style=wx.BU_EXACTFIT)
        self.button_star = wx.Button(self.advanced, self.BUTT_STAR, "*", style=wx.BU_EXACTFIT)
        self.button_0 = wx.Button(self.advanced, self.BUTT_0, "0", style=wx.BU_EXACTFIT)
        self.button_hash = wx.Button(self.advanced, self.BUTT_HASH, "#", style=wx.BU_EXACTFIT)
        self.bitmap_1 = wx.StaticBitmap(self.advanced, -1, wx.Image("/home/andyh/projects/external/shtoom/shtoom/ui/gnomeui/shtoom.gif", wx.BITMAP_TYPE_GIF).ConvertToBitmap())

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: ShtoomMainFrame.__set_properties
        self.SetTitle("Shtoom")
        self.shtoom_frame_statusbar.SetStatusWidths([-1])
        # statusbar fields
        shtoom_frame_statusbar_fields = ["shtoom_frame_statusbar"]
        for i in range(len(shtoom_frame_statusbar_fields)):
            self.shtoom_frame_statusbar.SetStatusText(shtoom_frame_statusbar_fields[i], i)
        self.combo_address.SetSelection(0)
        self.button_call.SetToolTipString("Place a call")
        self.button_advanced.SetSize((20, 27))
        self.button_advanced.SetToolTipString("Display extra controls")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: ShtoomMainFrame.__do_layout
        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1 = wx.BoxSizer(wx.HORIZONTAL)
        grid_sizer_1 = wx.GridSizer(4, 3, 0, 0)
        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(self.label_1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_3.Add(self.combo_address, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)
        sizer_4.Add(self.button_call, 1, wx.ALL, 5)
        sizer_4.Add(self.button_lookup, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_4.Add(self.button_advanced, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_2.Add(sizer_4, 0, wx.EXPAND, 0)
        grid_sizer_1.Add(self.button_1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_3, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_5, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_6, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_7, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_8, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_9, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_star, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_0, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        grid_sizer_1.Add(self.button_hash, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(grid_sizer_1, 0, wx.EXPAND, 0)
        sizer_1.Add(self.bitmap_1, 1, wx.ALL|wx.EXPAND, 5)
        self.advanced.SetAutoLayout(1)
        self.advanced.SetSizer(sizer_1)
        sizer_1.Fit(self.advanced)
        sizer_1.SetSizeHints(self.advanced)
        sizer_2.Add(self.advanced, 1, wx.EXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_2)
        sizer_2.Fit(self)
        #sizer_2.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class ShtoomMainFrame


