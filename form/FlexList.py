import wx
import cv2
import os
import subprocess
import webbrowser
import time
from EditForm import *
from model.dbconnect import *
from props.InputProp import *
from props.FormField import *
import wx.lib.scrolledpanel as scrolled
from datetime import datetime  
from datetime import timedelta 
from ConnectDialog import *

class FlexList(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, size=(1400, 700), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )

        self._db = DB()
        max_row = self._db.get_row()
        get_all = self._db.get_all()
        field = FormField()
        # menubar = field.setMenuBar()

        self.Bind(wx.EVT_CLOSE, self.onClose)

        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("STEEL BLUE")
        form_panel = wx.Panel(self.panel, size=(1300, 40))
        form_panel.SetBackgroundColour("STEEL BLUE")

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        refresh_panel = wx.Panel(self.panel, size=(1300, 200))

        # header = wx.Panel(self.panel, size=(1400, 80), style=wx.RAISED_BORDER)
        # header.SetBackgroundColour("MEDIUM SLATE BLUE")

        # font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD)
        # self.header_title = wx.StaticText(header, 1, "Banana Data System", style = wx.ALIGN_CENTER, size=(1200, 200))
        # self.header_title.SetFont(font)
        # vbox.Add(header, 0, wx.SHAPED, 0)

        label_data = wx.Font(14, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        self.refresh_btn = wx.Button(refresh_panel, label='Refresh', size=(100, 30) )
        hbox.Add(self.refresh_btn, 0,  wx.ALIGN_CENTER_VERTICAL, 50)
        self.Bind(wx.EVT_BUTTON, lambda event: self.refreshFrame(event), self.refresh_btn)

        self.connect_btn = wx.Button(refresh_panel, label='Connect', size=(100, 30) )
        hbox.Add(self.connect_btn, 1,  wx.ALIGN_CENTER_VERTICAL, 50)
        self.Bind(wx.EVT_BUTTON, lambda event: self.showConnectDiag(event), self.connect_btn)

        # refresh_panel.SetSizer(hbox)
        vbox.Add(hbox, 0,  wx.ALIGN_TOP, 50)

        label_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        label_data = wx.Font(14, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)

        fgs = wx.FlexGridSizer(int(max_row[0]) + 1, 9, 20,50)
        self.scrolled_panel = scrolled.ScrolledPanel(self.panel, -1, size=(1300, 300), style = wx.TAB_TRAVERSAL|wx.SUNKEN_BORDER, name="panel1")
        self.scrolled_panel.SetBackgroundColour("STEEL BLUE")
        self.scrolled_panel.SetAutoLayout(1)
        self.scrolled_panel.SetupScrolling()

        self._width = wx.StaticText(form_panel, label = "Width")
        self._width.SetFont(label_font)
        self._height = wx.StaticText(form_panel, label = "Height")
        self._height.SetFont(label_font)
        self._weight = wx.StaticText(form_panel, label = "Weight")
        self._weight.SetFont(label_font)
        self._image = wx.StaticText(form_panel, label = "Front")
        self._image.SetFont(label_font)
        self._filter = wx.StaticText(form_panel, label = "Back")
        self._filter.SetFont(label_font)
        self._status = wx.StaticText(form_panel, label = "Status")
        self._status.SetFont(label_font)
        self._quality = wx.StaticText(form_panel, label="Quality")
        self._quality.SetFont(label_font)
        self._ripen = wx.StaticText(form_panel, label="Ripen")
        self._ripen.SetFont(label_font)
        self._action = wx.StaticText(form_panel, label="Action")
        self._action.SetFont(label_font)

        fgs.AddMany([
            (self._width, 1, wx.EXPAND),
            (self._height, 1, wx.EXPAND),
            (self._weight, 1, wx.EXPAND),
            (self._image, 1, wx.EXPAND),
            (self._filter, 1, wx.EXPAND),
            (self._status, 1, wx.EXPAND),
            (self._quality, 1, wx.EXPAND),
            (self._ripen, 1, wx.EXPAND),
            (self._action, 1, wx.EXPAND)
        ])

        form_panel.SetSizer(fgs)
        vbox.Add(form_panel, 0, wx.ALIGN_TOP|wx.ALIGN_CENTER_HORIZONTAL, 0)
        
        count = 1
        for i in get_all:

            homedir = os.path.expanduser('~')
            dir_path = os.path.dirname(os.path.realpath(__file__))

            if not wx.Image().CanRead(dir_path + "\\..\\images\\front\\" + str(i[5])):
                continue

            self.__weight = wx.StaticText(self.scrolled_panel, 1, str(i[1]))
            self.__weight.SetFont(label_data)

            self.__height = wx.StaticText(self.scrolled_panel, 1, str(i[2]))
            self.__height.SetFont(label_data)

            self.__width = wx.StaticText(self.scrolled_panel, 1, str(i[3]))
            self.__width.SetFont(label_data)

            if wx.Image().CanRead(dir_path + "\\..\\images\\front\\" + str(i[5])):
                self.img = wx.Image(dir_path + "\\..\\images\\front\\" + str(i[5]), wx.BITMAP_TYPE_ANY)
            else:
                self.img = wx.Image(dir_path + "\\..\\No-image-available.jpg", wx.BITMAP_TYPE_JPEG)
            
            self.img = self.img.Scale(100, 100)
            self.img = wx.StaticBitmap(self.scrolled_panel, wx.ID_ANY, wx.Bitmap(self.img))

            if wx.Image().CanRead(dir_path + "\\..\\images\\back\\" + str(i[6])):
                self.__filter = wx.Image(dir_path + "\\..\\images\\back\\" + str(i[6]), wx.BITMAP_TYPE_ANY)
            else:
                self.__filter = wx.Image(dir_path + "\\..\\No-image-available.jpg", wx.BITMAP_TYPE_JPEG)
            
            self.__filter = self.__filter.Scale(100, 100)
            self.__filter = wx.StaticBitmap(self.scrolled_panel, wx.ID_ANY, wx.Bitmap(self.__filter))

            self.__quality = wx.StaticText(self.scrolled_panel, 1, str(i[9]) + "%")
            self.__quality.SetFont(label_data)

            self.__status = wx.StaticText(self.scrolled_panel, 1, str(i[10]))
            self.__status.SetFont(label_data)
            
            dateripen = "Empty"
            if i[9] is not None:
                dateripen = i[13] + timedelta(days=i[11])
            
            self.__life = wx.StaticText(self.scrolled_panel, 1, str(dateripen))
            self.__life.SetFont(label_data)

            self.capture_btn = wx.Button(self.scrolled_panel, label='View', size=(50, 20) )
            self.capture_btn.id = i[0]

            fgs.AddMany([
            (self.__width, 1, wx.EXPAND),
            (self.__height, 1, wx.EXPAND),
            (self.__weight, 1, wx.EXPAND),
            (self.img, 1, wx.EXPAND),
            (self.__filter, 1, wx.EXPAND),
            (self.__status, 1, wx.EXPAND),
            (self.__quality, 1, wx.EXPAND),
            (self.__life, 1, wx.EXPAND),
            (self.capture_btn, 1, wx.EXPAND)
            ])

            self.Bind(wx.EVT_BUTTON, lambda event: self.insertData(event), self.capture_btn)
            count += 1

        self.scrolled_panel.SetSizer(fgs)
        vbox.Add(self.scrolled_panel, 0, wx.ALIGN_TOP|wx.ALIGN_CENTER_HORIZONTAL, 20)

        btn_h = wx.BoxSizer(wx.HORIZONTAL)
        back_eval = wx.Button(self.panel, label='Back to evaluate', size=(150, 100))
        btn_h.Add(back_eval, 1, wx.ALIGN_LEFT, 20)
        btn_h.AddSpacer(130)
        cancel_btn = wx.Button(self.panel, label='Cancel', size=(150, 100))
        btn_h.Add(cancel_btn, 1, wx.ALIGN_LEFT, 20)
        vbox.AddSpacer(50)
        vbox.Add(btn_h, 1, wx.ALIGN_CENTER_HORIZONTAL, 20)

        # self.SetMenuBar(menubar)
        self.Bind(wx.EVT_BUTTON, lambda event: self.goToEvaluate(event, self), back_eval)
        self.Bind(wx.EVT_BUTTON, lambda event: self.goToMenu(event, self), cancel_btn)
        # self.Bind(wx.EVT_MENU, lambda event: field.menuHandler(event, self))
        self.panel.SetSizer(vbox)
        self.Centre()
        self.Show(True)

    def insertData(self, event):
        _id = event.GetEventObject().id
        rec_window = EditForm(self, 'Rec window', id = _id)
        rec_window.Show()
        self.Hide()

    def onClose(self, event):
        self.Destroy()

    def refreshFrame(self, event):
        self.Destroy()
        flex = FlexList("Banana Detection")
        flex.Show(True)

    def goToEvaluate(self, event, parent):
        capture = cv2.VideoCapture(0)
        frame = wx.Frame(None)
        module = __import__("CameraCapture")
        cam = getattr(module, "CameraCapture")(frame, capture)
        cam.Show()
        parent.Hide()

    def goToMenu(self, event, parent):
        module = __import__("MenuForm")
        menu = getattr(module, "MenuForm")("Main Menu")
        menu.Show()
        parent.Hide()

    def showConnectDiag(self, event):
        self.Destroy()
        con = ConnectDialog("Connect")
        con.Show()







