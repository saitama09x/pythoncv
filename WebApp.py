import wx
import cv2
import wx.html2
import wx.html
from props.FormField import *
import webbrowser
import subprocess

class WebApp(wx.Frame):
	def __init__(self, title):
		wx.Frame.__init__(self, None, title=title, size=(1000, 500), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )


		panel = wx.Panel(self)
		field = FormField()

		menubar = field.setMenuBar()
		header = field.setFormHeader(panel, size=(500, 100))

		vbox = wx.BoxSizer(wx.VERTICAL)

		font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD)
		header_title = wx.StaticText(header, 1, "Menu", style = wx.ALIGN_CENTER, size=(500, 300))
		header_title.SetFont(font)
		vbox.Add(header, 0, wx.ALIGN_CENTER_VERTICAL, 1)

		webpanel = wx.Panel(panel, size=(1000, 400))

		# web = wx.html2.WebView.New(webpanel, size=(1000, 400))
		# web.SetPage("<iframe src='http://localhost:4200' width='100px' height='100px'></iframe>", "")
		# web.EnableContextMenu(True)

		# html = wx.html.HtmlWindow(webpanel)
		# html.LoadPage("http://localhost:4200") 
		# html.SetPage("htmlbody" \
  #             "h1Error/h1" \
  #             "Some error occurred :-H)" \
  #             "/body/hmtl")
		# html.SetRelatedFrame(self, "HTML : %%s")
		# webbrowser.open("http://localhost:4200", new=0, autoraise=True)
		# vbox.Add(html, 0, wx.ALIGN_CENTER_VERTICAL, 1)
		# os.system("cd C:\\Users\\acer\\laradev\\opencv")
		# os.system("php artisan serve")
		subprocess.call("cd C:\\Users\\acer\\laradev\\opencv", shell=True)
		subprocess.call("php artisan serve", shell=True)
		panel.SetSizer(vbox)

		self.SetMenuBar(menubar)
		self.Centre()
		self.Show(True)


# if __name__ == "__main__":
# 	app = wx.App(False)
# 	login = WebApp("Banana Detection")
# 	app.MainLoop()

