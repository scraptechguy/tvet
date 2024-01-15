#!/usr/bin/env python3

"""

Installation:

  pip3 install tk
  pip3 install pyopengl
  pip3 install pyopengltk
  pip3 install vispy

Alternatively:

  apt-get install python3-tk
  apt-get install python3-opengl
  ...

"""

import wx 
 
app = wx.App() 
window = wx.Frame(None, title = "wxPython Frame", size = (300,200)) 
panel = wx.Panel(window) 
label = wx.StaticText(panel, label = "Hello World", pos = (100,50)) 
window.Show(True) 
app.MainLoop()