#!/usr/bin/env python
# generated by wxGlade 0.3.1 on Mon Apr 19 22:10:30 2004

from wxPython.wx import *

class PreferencesDialog(wxDialog):
    def __init__(self, *args, **kwds):
        # begin wxGlade: PreferencesDialog.__init__
        kwds["style"] = wxDEFAULT_DIALOG_STYLE
        wxDialog.__init__(self, *args, **kwds)
        self.prefs_notebook = wxNotebook(self, -1, style=0)
        self.notebook_1_pane_1 = wxPanel(self.prefs_notebook, -1)
        self.prefs_save = wxButton(self, BUTT_PREFS_SAVE, "Save")
        self.prefs_cancel = wxButton(self, BUTT_PREFS_CANCEL, "Cancel")

        self.__set_properties()
        self.__do_layout()
        # end wxGlade

    def __set_properties(self):
        # begin wxGlade: PreferencesDialog.__set_properties
        self.SetTitle("dialog_1")
        # end wxGlade

    def __do_layout(self):
        # begin wxGlade: PreferencesDialog.__do_layout
        sizer_1 = wxBoxSizer(wxVERTICAL)
        sizer_2 = wxBoxSizer(wxHORIZONTAL)
        self.prefs_notebook.AddPage(self.notebook_1_pane_1, "tab1")
        sizer_1.Add(wxNotebookSizer(self.prefs_notebook), 1, wxEXPAND, 0)
        sizer_2.Add(self.prefs_save, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5)
        sizer_2.Add(self.prefs_cancel, 0, wxALL|wxALIGN_CENTER_HORIZONTAL|wxALIGN_CENTER_VERTICAL, 5)
        sizer_1.Add(sizer_2, 1, wxEXPAND, 0)
        self.SetAutoLayout(1)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        sizer_1.SetSizeHints(self)
        self.Layout()
        # end wxGlade

# end of class PreferencesDialog


