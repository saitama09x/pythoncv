import wx
import cv2
from model.dbconnect import *
from props.InputProp import *
from form.MainList import MainList

class DataForm(wx.Frame):
    def __init__(self, title, image = "sample.jpg"):  	
        wx.Frame.__init__(self, None, title=title, size=(1000, 700), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )

        self._db = DB()
        self.image = image

        img = wx.Image(self.image , wx.BITMAP_TYPE_ANY)
        img_width = 550
        img_height = 600

        panel = wx.Panel(self)
        imagepanel = wx.Panel(panel, size=(img_width, img_height))
        imagepanel.SetBackgroundColour("BLUE")

        form_panel = wx.Panel(panel, size=(500, img_height))
        form_panel.SetBackgroundColour("STEEL BLUE")
        sizer = wx.GridBagSizer(10,10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        header = wx.Panel(panel, size=(1200, 100), style=wx.RAISED_BORDER)
        header.SetBackgroundColour("MEDIUM SLATE BLUE")

        font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD) 
        self.header_title = wx.StaticText(header, 1, "Banana Data System", style = wx.ALIGN_CENTER, size=(1000, 700))
        self.header_title.SetFont(font) 
        vbox.Add(header, -1, wx.ALIGN_CENTER_VERTICAL, 1)

        img = img.Scale(img_width, img_height)
        self.videobmp = wx.StaticBitmap(imagepanel, wx.ID_ANY, wx.Bitmap(img))
        hbox.Add(imagepanel, 1, wx.ALIGN_LEFT, 1)
        
        label_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        self.label = wx.StaticText(form_panel, 1, "Enter Kilo")
        self.label.SetFont(label_font) 
        sizer.Add(self.label, pos = (0, 0), flag = wx.ALL, border = 10)

        input_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) 
        self.input_kilo = wx.TextCtrl(form_panel, size=(150, 20))
        self.input_kilo.SetFont(input_font) 
        sizer.Add(self.input_kilo, pos = (0, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        self.label = wx.StaticText(form_panel, 1, "Enter Size")
        self.label.SetFont(label_font) 
        sizer.Add(self.label, pos = (1, 0), flag = wx.ALL, border = 10)

        self.input_size = wx.TextCtrl(form_panel, size=(150, 20))
        self.input_size.SetFont(input_font) 
        sizer.Add(self.input_size, pos = (1, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        self.label = wx.StaticText(form_panel, 1, "Quantity: ")
        self.label.SetFont(label_font) 
        sizer.Add(self.label, pos = (2, 0), flag = wx.ALL, border = 10)

        self.input_qty = wx.TextCtrl(form_panel, size=(150, 20))
        self.input_qty.SetFont(input_font) 
        sizer.Add(self.input_qty, pos = (2, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        self.label = wx.StaticText(form_panel, 1, "Texture: ")
        self.label.SetFont(label_font) 
        sizer.Add(self.label, pos = (3, 0), flag = wx.ALL, border = 10)

        self.label = wx.StaticText(form_panel, 1, "ID: ")
        self.label.SetFont(label_font) 
        sizer.Add(self.label, pos = (4, 0), flag = wx.ALL, border = 10)

        self.capture_btn = wx.Button(form_panel, label='Submit', size=(50, 30))
        sizer.Add(self.capture_btn, pos = (5, 0), span = (2, 3), flag = wx.EXPAND|wx.ALL, border = 10)

        form_panel.SetSizer(sizer)
        hbox.Add(form_panel, 2, wx.ALIGN_LEFT, border = 10) 
        vbox.Add(hbox, 1, wx.ALIGN_TOP, 1)
        panel.SetSizer(vbox)

        self.Bind(wx.EVT_BUTTON, lambda event: self.insertData(event), self.capture_btn)

        self.Centre() 
        self.Show(True)


    def insertData(self, event):
        kilo = self.input_kilo.GetValue()
        qty = self.input_qty.GetValue()
        size = self.input_size.GetValue()
        prop = InputProp(kilo, size, qty, self.image)
        self._db.insertData(prop)
        rec_window = MainList('Rec window')
        rec_window.Show()
        self.Hide()