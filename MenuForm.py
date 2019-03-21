import wx
import cv2
import wx.html2
from model.dbconnect import *
from props.InputProp import *
from props.FormField import *
from form.FlexList import *
from CameraCapture import *

class MenuForm(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, title=title, size=(500, 500), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )

		panel = wx.Panel(self)
		
		field = FormField()
		menubar = field.setMenuBar()
		sizer = wx.GridBagSizer(10,10)

		form_panel = field.setFormField(panel, size=(500, 500))

		# header = field.setFormHeader(panel, size=(500, 100))

		vbox = wx.BoxSizer(wx.VERTICAL)

		# font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD)
		# header_title = wx.StaticText(header, 1, "Menu", style = wx.ALIGN_CENTER, size=(500, 300))
		# header_title.SetFont(font)
		# vbox.Add(header, -1, wx.ALIGN_CENTER_VERTICAL, 1)

		font = wx.Font(20, wx.MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

		capture_btn = wx.Button(form_panel, label='Evaluate', size=(300, 70))
		capture_btn.SetFont(font)
		sizer.Add(capture_btn, pos = (1, 5), span = (1, 4), flag = wx.ALIGN_CENTER, border = 10)

		record_btn = wx.Button(form_panel, label='Records', size=(300, 70))
		record_btn.SetFont(font)
		sizer.Add(record_btn, pos = (3, 5), span = (1, 4), flag = wx.ALIGN_CENTER, border = 10)

		form_panel.SetSizer(sizer)

		vbox.Add(form_panel, 1, wx.ALIGN_CENTER_VERTICAL, 1)

		panel.SetSizer(vbox)

		self.SetMenuBar(menubar)
		self.Bind(wx.EVT_BUTTON, lambda event: self.goToEvaluate(event, self), capture_btn)
		self.Bind(wx.EVT_BUTTON, lambda event: self.goToRecord(event, self), record_btn)
		self.Bind(wx.EVT_CLOSE, self.onClose)
		self.Bind(wx.EVT_MENU, lambda event: field.menuHandler(event, self))
		self.Centre()
		self.Show(True)

	def goToEvaluate(self, event, parent):
		capture = cv2.VideoCapture(0)
		frame = wx.Frame(None)
		module = __import__("CameraCapture")
		cam = getattr(module, "CameraCapture")(frame, capture)
		cam.Show()
		parent.Hide()

	def goToRecord(self, event, parent):
		flex = FlexList("Records")
		flex.Show()
		parent.Hide()
		
	def onClose(self, event):
		self.Destroy()

