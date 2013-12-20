#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import dir_Frame1

modules ={u'dir_Frame1': [1, 'Main frame of Application', u'dir_Frame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = dir_Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
