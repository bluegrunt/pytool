#Boa:Frame:Frame1
# -*- :encoding:utf8 -*-

import wx
import os
import string
import shutil

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1CHECKBOX1, 
 wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, wxID_FRAME1STATUSBAR1, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(8)]

[wxID_FRAME1MENU1ITEMS0] = [wx.NewId() for _init_coll_menu1_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menu1, title=u'File')

    def _init_coll_menu1_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'', id=wxID_FRAME1MENU1ITEMS0, kind=wx.ITEM_NORMAL,
              text=u'Quit')
        self.Bind(wx.EVT_MENU, self.OnMenu1Items0Menu,
              id=wxID_FRAME1MENU1ITEMS0)

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.menu1 = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menu1_Items(self.menu1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(504, 295), size=wx.Size(404, 271),
              style=wx.DEFAULT_FRAME_STYLE,
              title=u'Directory synchronize tool')
        self._init_utils()
        self.SetClientSize(wx.Size(396, 237))
        self.SetToolTipString(u'Directory')
        self.SetMenuBar(self.menuBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.SetStatusBar(self.statusBar1)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'\u540c\u6b65\u6587\u4ef6\u5939', name='staticText1',
              parent=self, pos=wx.Point(64, 48), size=wx.Size(60, 14), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'\u53c2\u7167\u6587\u4ef6\u5939', name='staticText2',
              parent=self, pos=wx.Point(64, 96), size=wx.Size(60, 14), style=0)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME1CHECKBOX1,
              label=u'\u540c\u65f6\u66f4\u65b0\u53c2\u7167\u6587\u4ef6\u5939',
              name='checkBox1', parent=self, pos=wx.Point(136, 136),
              size=wx.Size(136, 14), style=0)
        self.checkBox1.SetValue(True)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(160, 44), size=wx.Size(152, 22),
              style=0, value=u'')
        self.textCtrl1.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl1TextEnter,
              id=wxID_FRAME1TEXTCTRL1)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self, pos=wx.Point(160, 96), size=wx.Size(152, 22),
              style=0, value=u'')
        self.textCtrl2.Bind(wx.EVT_TEXT_ENTER, self.OnTextCtrl2TextEnter,
              id=wxID_FRAME1TEXTCTRL2)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label=u'\u5f00\u59cb',
              name='button1', parent=self, pos=wx.Point(136, 160),
              size=wx.Size(75, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.path1 = '' # 欲更新文件夹
        self.path2 = '' # 参照文件夹
        
    def OnTextCtrl1TextEnter(self, event):
        dlg = wx.DirDialog(self,'Please select a directory')
        if dlg.ShowModal() == wx.ID_OK :
            self.textCtrl1.SetValue(dlg.GetPath())
        dlg.Destroy()

    def OnMenu1Items0Menu(self, event):
        self.Destroy()

    def OnTextCtrl2TextEnter(self, event):
        dlg = wx.DirDialog(self,'Please select a directory')
        if dlg.ShowModal() == wx.ID_OK :
            self.textCtrl2.SetValue(dlg.GetPath())
        dlg.Destroy()

    def OnButton1Button(self, event):
        path1 = self.textCtrl1.GetValue()
        path2 = self.textCtrl2.GetValue()
        if not os.path.isdir(path1):
            wx.MessageBox(path1 + " is not a directory!")
            return 
    
        if not os.path.isdir(path2):
            wx.MessageBox(path2 + " is not a directory!")
            return 
            
        if path1 == path2 :
            wx.MessageBox("The Same direcotry !")
            return 
                
        self._dir_syn(path2,path1)
        print '======================================================'
        if self.checkBox1.GetValue():
            self._dir_syn(path1,path2)
            print '======================================================'

    def _dir_syn(self, path_from, path_to):    
        for root,dirs,files in os.walk(path_from):
            for f in files:
                full_name = os.path.join(root,f)
                tt = os.path.getmtime(full_name)
                file_other = string.replace(full_name,path_from,path_to,1)
                dir_other = os.path.dirname(file_other)
                if not os.path.exists(dir_other):
                    os.makedirs(dir_other)
                if not os.path.exists(file_other):
                    shutil.copy2(full_name, file_other)
                    self.statusBar1.SetStatusText('From ' + full_name + " to "+ file_other)
                    #print 'From ' + full_name + " to "+ file_other
                else :
                    tt_other = os.path.getmtime(file_other)
                    if tt_other < tt :
                        shutil.copy2(full_name, file_other)
                        self.statusBar1.SetStatusText('From ' + full_name + " to "+ file_other)
                        #print 'From ' + full_name + " to "+ file_other
        # end for                        
                    
                    


