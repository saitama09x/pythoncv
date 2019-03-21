import wx
import cv2
import numpy as np
import os
import time
import datetime
from contour import *
from form.DataForm import *
from form.MainList import *
from form.FlexList import *
from form.EditForm import *
from model.dbconnect import *

class CameraCapture(wx.Frame):
    def __init__(self, parent, capture, fps=15):
        wx.Frame.__init__(self, parent, title = "Demo 2", size=(1400, 700), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )

        self.capture = capture
        ret, frame = self.capture.read()
        height, width = frame.shape[:2]
        res_percent = 70
        
        self.is_front = 1;
        self.is_back = 1;
        self.is_side = 1;

        self.resized_w = int(width * res_percent / 100)
        self.resized_h = int(height * res_percent / 100)
        self.detection = cv2.CascadeClassifier('cascade/BananaCascade.xml')

        img = wx.Image("No-image-available.jpg", wx.BITMAP_TYPE_ANY)
        img_width = 450
        img_height = 500

        panel = wx.Panel(self)
        panel.SetBackgroundColour("BLUE")

        self.imagepanel = wx.Panel(panel, size=(1400, 300))
        self.imagepanel.SetBackgroundColour("BLUE")

        form_panel = wx.Panel(panel, size=(1400, 400))
        form_panel.SetBackgroundColour("BLUE")
        # sizer = wx.GridBagSizer(10,10)

        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # header = wx.Panel(panel, size=(1400, 100), style=wx.RAISED_BORDER)
        # header.SetBackgroundColour("MEDIUM SLATE BLUE")

        # font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD) 
        # self.header_title = wx.StaticText(header, 1, "Banana Data System", style = wx.ALIGN_CENTER, size=(1400, 300))
        # self.header_title.SetFont(font) 
        # vbox.Add(header, 0, wx.ALIGN_CENTER_VERTICAL, 1)

        _hbox = wx.BoxSizer(wx.HORIZONTAL)
    
        self.bmp = wx.Bitmap.FromBuffer(self.resized_w,  self.resized_h, frame)
        self.videobmp = wx.StaticBitmap(self.imagepanel, wx.ID_ANY, self.bmp)
        _hbox.Add(self.videobmp, 0, wx.ALIGN_CENTER_VERTICAL, 1)
        
        _hbox.AddSpacer(10)

        self.bmp2 = wx.Bitmap.FromBuffer(self.resized_w, self.resized_h, frame)
        self.videobmp2 = wx.StaticBitmap(self.imagepanel, wx.ID_ANY, self.bmp2)
        _hbox.Add(self.videobmp2, 1, wx.ALIGN_CENTER_VERTICAL, 1)

        _hbox.AddSpacer(10)

        self.bmp3 = wx.Bitmap.FromBuffer(self.resized_w, self.resized_h, frame)
        self.videobmp3 = wx.StaticBitmap(self.imagepanel, wx.ID_ANY, self.bmp3)
        _hbox.Add(self.videobmp3, 1, wx.ALIGN_CENTER_VERTICAL, 1)

        vbox.Add(_hbox, 1, wx.ALIGN_CENTER_HORIZONTAL, 1)

        vbox.AddSpacer(20)

        btnbox_h = wx.BoxSizer(wx.HORIZONTAL)
        btnbox_v = wx.BoxSizer(wx.VERTICAL)

        btnbox_h.AddSpacer(80)

        front_btn = wx.Button(form_panel, label='Capture Front', size=(300, 70))
        btnbox_h.Add(front_btn, 0, wx.SHAPED, 10)
        
        btnbox_h.AddSpacer(165) 
        
        back_btn = wx.Button(form_panel, label='Capture Back', size=(300, 70))
        btnbox_h.Add(back_btn, 2, wx.SHAPED, 10)

        btnbox_h.AddSpacer(180) 

        side_btn = wx.Button(form_panel, label='Capture Side', size=(300, 70))
        btnbox_h.Add(side_btn, 2, wx.SHAPED, 10)

        btnbox_v.Add(btnbox_h, 0, wx.ALIGN_LEFT, 10)

        btnbox_v.AddSpacer(50)

        submit_btn = wx.Button(form_panel, label='Submit', size=(300, 70))
        btnbox_v.Add(submit_btn, 0, wx.ALIGN_CENTER_HORIZONTAL, 1)

        form_panel.SetSizer(btnbox_v)
        vbox.Add(form_panel, 2, wx.ALIGN_CENTER_HORIZONTAL, 1)
        panel.SetSizer(vbox)

        front_btn.Bind(wx.EVT_BUTTON, self.front_image)
        back_btn.Bind(wx.EVT_BUTTON, self.back_image)
        side_btn.Bind(wx.EVT_BUTTON, self.side_image)
        submit_btn.Bind(wx.EVT_BUTTON, self.submit_data)
        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.timer = wx.Timer(self)
        self.timer.Start(1000./fps)
        self.Bind(wx.EVT_TIMER, self.NextFrame)
        self.Show(True)

    def NextFrame(self, event):
        ret, frame = self.capture.read()
        height, width = frame.shape[:2]
        if ret:
            self.filtered = cv2.resize(frame, (self.resized_w,  self.resized_h), interpolation = cv2.INTER_AREA)
            hsv = cv2.cvtColor(self.filtered, cv2.COLOR_BGR2HSV)
            if self.is_front == 1:
                self.bmp.CopyFromBuffer(self.filtered)

            if self.is_back == 1:
                self.bmp2.CopyFromBuffer(self.filtered)

            if self.is_side == 1:
                self.bmp3.CopyFromBuffer(self.filtered)

        self.Refresh()

    def front_image(self, event):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H%M%S')
        self._front_img = "sample" + str(timestamp) + ".bmp"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cv2.imwrite(dir_path + "\\images\\front\\" + self._front_img, self.filtered)
        self.is_front = 0

    def back_image(self, event):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H%M%S')
        self._back_img = "sample" + str(timestamp) + ".bmp"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cv2.imwrite(dir_path + "\\images\\back\\" + self._back_img, self.filtered)
        self.is_back = 0

    def side_image(self, event):
        timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%H%M%S')
        self._side_img = "sample" + str(timestamp) + ".bmp"
        dir_path = os.path.dirname(os.path.realpath(__file__))
        cv2.imwrite(dir_path + "\\images\\side\\" + self._side_img, self.filtered)
        self.is_side = 0
        
    def submit_data(self, event):
        ret, frame = self.capture.read()
        if ret:
            self.timer.Stop()
            self.capture.release()
            self._db = DB()
            last_id = self._db.insertImage(self._front_img, self._back_img, self._side_img)
            rec_window = EditForm(self, 'Rec window', id = int(last_id[0]))
            rec_window.Show()
            self.Hide()
           

    def onClose(self, event):
        self.Destroy()
