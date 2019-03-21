import wx
import cv2
from model.dbconnect import *
from props.InputProp import *
from props.FormField import *
from MenuForm import *
from form.FlexList import *

class LoginForm(wx.Frame):
	def __init__(self, title, id = 0): 
		wx.Frame.__init__(self, None, title=title, size=(500, 300), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )

		self._db = DB()
		
		img_width = 550
		img_height = 600

		panel = wx.Panel(self)
		field = FormField()	

		form_panel = field.setFormField(panel, size=(500, 300))

		sizer = wx.GridBagSizer(10,10)

		hbox = wx.BoxSizer(wx.HORIZONTAL)
		vbox = wx.BoxSizer(wx.VERTICAL)

		header = field.setFormHeader(panel, size=(500, 100))

		font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD)
		self.header_title = wx.StaticText(header, 1, "Login Form", style = wx.ALIGN_CENTER, size=(500, 300))
		self.header_title.SetFont(font)
		vbox.Add(header, -1, wx.ALIGN_CENTER_VERTICAL, 1)

		label_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		self.label = wx.StaticText(form_panel, 1, "Username")
		self.label.SetFont(label_font)
		sizer.Add(self.label, pos = (0, 0), flag = wx.ALL, border = 10)

		input_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		self.input_user = wx.TextCtrl(form_panel, size=(250, 20), value="admin")
		self.input_user.SetFont(input_font)
		sizer.Add(self.input_user, pos = (0, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

		label_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		self.label = wx.StaticText(form_panel, 1, "Password")
		self.label.SetFont(label_font)
		sizer.Add(self.label, pos = (1, 0), flag = wx.ALL, border = 10)

		input_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		self.input_pass = wx.TextCtrl(form_panel, size=(250, 20), style = wx.TE_PASSWORD, value="admin123")
		self.input_pass.SetFont(input_font)
		sizer.Add(self.input_pass, pos = (1, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

		self.capture_btn = wx.Button(form_panel, label='Submit', size=(200, 30))
		sizer.Add(self.capture_btn, pos = (2, 1), span = (2, 2), flag = wx.EXPAND|wx.ALL, border = 10)

		form_panel.SetSizer(sizer)
		# hbox.Add(form_panel, 2, wx.ALIGN_LEFT, border = 10)
		vbox.Add(form_panel, 1, wx.ALIGN_TOP, 1)

		panel.SetSizer(vbox)

		self.Bind(wx.EVT_BUTTON, lambda event: self.login(event, self), self.capture_btn)

		self.Centre()
		self.Show(True)

	def login(self, event, parent):
		inputuser = self.input_user.GetValue()
		inputpass = self.input_pass.GetValue()
		login = self._db.get_login(inputuser, inputpass)
		if login == None:
			LoginDialog(self, "Dialog").ShowModal()
		else:
			module = __import__("MenuForm")
			menu = getattr(module, "MenuForm")("Main Menu")
			menu.Show()
			parent.Hide()



class LoginDialog(wx.Dialog):
	def __init__(self, parent, title):
		super(LoginDialog, self).__init__(parent, title = title, size = (250, 150))
		panel = wx.Panel(self)
		hbox = wx.BoxSizer(wx.HORIZONTAL)

		label_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
		self.label = wx.StaticText(panel, 1, "Login Failed")
		self.label.SetFont(label_font)

		hbox.Add(self.label, 1, wx.ALIGN_CENTER_HORIZONTAL, border = 10)


if __name__ == "__main__":
	app = wx.App(False)
	login = LoginForm("Banana Detection")
	app.MainLoop()