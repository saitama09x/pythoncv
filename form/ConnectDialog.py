import wx
import cv2
import os
import subprocess
import webbrowser
import time

class ConnectDialog(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(500, 300), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )
        
        panel = wx.Panel(self)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        laravel_panel = wx.Panel(panel, size=(500, 300))

        ip_add = wx.StaticText(laravel_panel, 1, "Enter IP Address")
        self.ip_input = wx.TextCtrl(laravel_panel, size=(250, 20), value="127.0.0.1")

        port_add = wx.StaticText(laravel_panel, 1, "Enter Port")
        self.port_input = wx.TextCtrl(laravel_panel, size=(250, 20), value="8000")

        con_btn = wx.Button(laravel_panel, label='Connect', size=(200, 50))

        back_btn = wx.Button(laravel_panel, label='Go Back', size=(200, 50))

        vbox.Add(ip_add, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP, 1)
        vbox.Add(self.ip_input, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP, 1)
        
        vbox.AddSpacer(20) 

        vbox.Add(port_add, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP, 1)
        vbox.Add(self.port_input, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP, 1)
        
        vbox.AddSpacer(20)

        vbox.Add(con_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP, 1)
        vbox.Add(back_btn, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_TOP, 1)
        self.Bind(wx.EVT_BUTTON, lambda event: self.connectApp(event), con_btn)
        self.Bind(wx.EVT_BUTTON, lambda event: self.goBack(event), back_btn)

        panel.SetSizer(vbox)

    def connectApp(self, event):
        ip = self.ip_input.GetValue()
        port = self.port_input.GetValue()

        lav = subprocess.Popen(['php', 'artisan', 'serve', '--host=' + ip, '--port=' + port], shell=True, cwd = "../laravel")
        ang = subprocess.Popen(['npm', 'start'], shell=True, cwd = "../angular")    
        loop = True
        while loop:
            time.sleep(50)
            webbrowser.open('http://localhost:4200', new=0, autoraise=True)
            loop = False

    def goBack(self, event):
    	 self.Destroy()
    	 module = __import__("form.FlexList")
    	 menu = getattr(module, "FlexList")("Main Menu")
    	 menu.Show()