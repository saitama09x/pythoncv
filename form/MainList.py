import wx
import cv2
from form.EditForm import *
from model.dbconnect import *
from props.InputProp import *

class MainList(wx.Frame):
    def __init__(self, title):  	
        wx.Frame.__init__(self, None, title=title, size=(1000, 700), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )

        self._db = DB()
        # max_row = self._db.get_row()
        # get_all = self._db.get_all()

        self.panel = wx.Panel(self)
        form_panel = wx.Panel(self.panel, size=(1000, 500), style=wx.RAISED_BORDER)
        form_panel.SetBackgroundColour("STEEL BLUE")

        grid = wx.GridBagSizer(10, 10)

        vbox = wx.BoxSizer(wx.VERTICAL)

        header = wx.Panel(self.panel, size=(1200, 150), style=wx.RAISED_BORDER)
        header.SetBackgroundColour("MEDIUM SLATE BLUE")

        font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD) 
        self.header_title = wx.StaticText(header, 1, "Banana Data System", style = wx.ALIGN_CENTER, size=(1000, 300))
        self.header_title.SetFont(font) 
        vbox.Add(header, 0, wx.SHAPED, 0)

        label_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        label_data = wx.Font(14, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL) 

        self.label = wx.StaticText(form_panel, 1, "ID")
        self.label.SetFont(label_font) 
        grid.Add(self.label, pos = (0, 0), flag = wx.ALL, border = 10)

        self.label = wx.StaticText(form_panel, 1, "Kilo")
        self.label.SetFont(label_font) 
        grid.Add(self.label, pos = (0, 1), flag = wx.ALL, border = 10)

        self.label = wx.StaticText(form_panel, 1, "Size")
        self.label.SetFont(label_font) 
        grid.Add(self.label, pos = (0, 2), flag = wx.ALL, border = 10)
        
        self.label = wx.StaticText(form_panel, 1, "Quantity")
        self.label.SetFont(label_font) 
        grid.Add(self.label, pos = (0, 3), flag = wx.ALL, border = 10)

        self.label = wx.StaticText(form_panel, 1, "Action")
        self.label.SetFont(label_font) 
        grid.Add(self.label, pos = (0, 4), flag = wx.ALL, border = 10)


        count = 1
        # for i in get_all:
        # 	self.label = wx.StaticText(form_panel, 1, str(i[0]))
        # 	self.label.SetFont(label_font) 
        # 	grid.Add(self.label, pos = (count, 0), flag = wx.ALL, border = 10)

        # 	self.label = wx.StaticText(form_panel, 1, str(i[1]))
        # 	self.label.SetFont(label_font) 
        # 	grid.Add(self.label, pos = (count, 1), flag = wx.ALL, border = 10)

        # 	self.label = wx.StaticText(form_panel, 1, str(i[2]))
        # 	self.label.SetFont(label_font) 
        # 	grid.Add(self.label, pos = (count, 2), flag = wx.ALL, border = 10)

        # 	self.label = wx.StaticText(form_panel, 1, str(i[3]))
        # 	self.label.SetFont(label_font) 
        # 	grid.Add(self.label, pos = (count, 3), flag = wx.ALL, border = 10)

        # 	capture_btn = wx.Button(form_panel, label='View', size=(50, 30) )
        # 	capture_btn.id = i[0]
        # 	grid.Add(capture_btn, pos = (count, 4), flag = wx.ALL, border = 10)

        # 	self.Bind(wx.EVT_BUTTON, lambda event: self.insertData(event), capture_btn)
        # 	count += 1

        form_panel.SetSizer(grid)
        vbox.Add(form_panel, -1, wx.ALIGN_TOP, 0)
        self.panel.SetSizer(vbox)

        self.Centre() 
        self.Show(True)

    def insertData(self, event):
    	_id = event.GetEventObject().id
    	rec_window = EditForm('Rec window', id = _id)
    	rec_window.Show()





