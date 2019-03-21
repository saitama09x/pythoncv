import wx
import cv2
import os
import numpy as np
import importlib

class FormField:
	
	def __init__(self):
		self.__font = wx.Font(14, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD) 

	def setPanel(self, panel):
		self.__panel = panel

	def setFont(self, size, style = wx.FONTSTYLE_NORMAL):
		self.__font = wx.Font(size, wx.ROMAN, style, wx.FONTWEIGHT_BOLD)

	def setLabel(self, label):
		text = wx.StaticText(self.__panel, 1, label)
		text.SetFont(self.__font)
		return text

	def setTextField(self, value):
		text_input = wx.TextCtrl(self.__panel, size=(150, 20), value = str(value))
		text_input.SetFont(self.__font)
		return text_input

	def setFormField(self, panel, size):
		form_panel = wx.Panel(panel, size=size)
		form_panel.SetBackgroundColour("STEEL BLUE")
		return form_panel

	def setFormHeader(self, panel, size):
		header = wx.Panel(panel, size=size, style=wx.RAISED_BORDER)
		header.SetBackgroundColour("MEDIUM SLATE BLUE")
		return header

	def getParamsRef(self, panel):
		label_data = wx.Font(14, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		refer_grid = wx.FlexGridSizer(4, 7, 10,	50)
		param_label = wx.StaticText(panel, label = "Parameters")
		param_label.SetFont(label_data)
		hand_label1 = wx.StaticText(panel, label = "4 Hands")
		hand_label1.SetFont(label_data)
		hand_label2 = wx.StaticText(panel, label = "5 Hands")
		hand_label2.SetFont(label_data)
		hand_label3 = wx.StaticText(panel, label = "6 Hands")
		hand_label3.SetFont(label_data)
		hand_label4 = wx.StaticText(panel, label = "7 Hands")
		hand_label4.SetFont(label_data)
		hand_label5 = wx.StaticText(panel, label = "8 Hands")
		hand_label5.SetFont(label_data)
		hand_label6 = wx.StaticText(panel, label = "9 Hands")
		hand_label6.SetFont(label_data)

		refer_grid.AddMany([
            (param_label, 1, wx.EXPAND),
            (hand_label1, 1, wx.EXPAND),
            (hand_label2, 1, wx.EXPAND),
            (hand_label3, 1, wx.EXPAND),
            (hand_label4, 1, wx.EXPAND),
            (hand_label5, 1, wx.EXPAND),
            (hand_label6, 1, wx.EXPAND),
        ])

		param_label = wx.StaticText(panel, label = "Fingers Per Hand")
		param_label.SetFont(label_data)
		hand_label1 = wx.StaticText(panel, label = "12 fingers")
		hand_label1.SetFont(label_data)
		hand_label2 = wx.StaticText(panel, label = "12 fingers")
		hand_label2.SetFont(label_data)
		hand_label3 = wx.StaticText(panel, label = "12 fingers")
		hand_label3.SetFont(label_data)
		hand_label4 = wx.StaticText(panel, label = "12 fingers")
		hand_label4.SetFont(label_data)
		hand_label5 = wx.StaticText(panel, label = "12 fingers")
		hand_label5.SetFont(label_data)
		hand_label6 = wx.StaticText(panel, label = "12 fingers")
		hand_label6.SetFont(label_data)
		
		refer_grid.AddMany([
            (param_label, 1, wx.EXPAND),
            (hand_label1, 1, wx.EXPAND),
            (hand_label2, 1, wx.EXPAND),
            (hand_label3, 1, wx.EXPAND),
            (hand_label4, 1, wx.EXPAND),
            (hand_label5, 1, wx.EXPAND),
            (hand_label6, 1, wx.EXPAND),
        ])

		param_label = wx.StaticText(panel, label = "Weight per hand")
		param_label.SetFont(label_data)
		hand_label1 = wx.StaticText(panel, label = "3.4 to 4.0kg")
		hand_label1.SetFont(label_data)
		hand_label2 = wx.StaticText(panel, label = "2.5 to 3.4kg")
		hand_label2.SetFont(label_data)
		hand_label3 = wx.StaticText(panel, label = "1.8 to 2.4kg")
		hand_label3.SetFont(label_data)
		hand_label4 = wx.StaticText(panel, label = "1.8 to 2.0kg")
		hand_label4.SetFont(label_data)
		hand_label5 = wx.StaticText(panel, label = "Min of 1.3kg")
		hand_label5.SetFont(label_data)
		hand_label6 = wx.StaticText(panel, label = "Min of 0.8kg")
		hand_label6.SetFont(label_data)

		refer_grid.AddMany([
            (param_label, 1, wx.EXPAND),
            (hand_label1, 1, wx.EXPAND),
            (hand_label2, 1, wx.EXPAND),
            (hand_label3, 1, wx.EXPAND),
            (hand_label4, 1, wx.EXPAND),
            (hand_label5, 1, wx.EXPAND),
            (hand_label6, 1, wx.EXPAND),
        ])

		param_label = wx.StaticText(panel, label = "Net Weight Per Box")
		param_label.SetFont(label_data)
		hand_label1 = wx.StaticText(panel, label = "")
		hand_label1.SetFont(label_data)
		hand_label2 = wx.StaticText(panel, label = "")
		hand_label2.SetFont(label_data)
		hand_label3 = wx.StaticText(panel, label = "Minimum 13.5 to maximum 14.0kg")
		hand_label3.SetFont(label_data)
		hand_label4 = wx.StaticText(panel, label = "")
		hand_label4.SetFont(label_data)
		hand_label5 = wx.StaticText(panel, label = "")
		hand_label5.SetFont(label_data)
		hand_label6 = wx.StaticText(panel, label = "")
		hand_label6.SetFont(label_data)

		refer_grid.AddMany([
            (param_label, 1, wx.EXPAND),
            (hand_label1, 1, wx.EXPAND),
            (hand_label2, 1, wx.EXPAND),
            (hand_label3, 1, wx.EXPAND),
            (hand_label4, 1, wx.EXPAND),
            (hand_label5, 1, wx.EXPAND),
            (hand_label6, 1, wx.EXPAND),
        ])

		return refer_grid

	def setMenuBar(self):
		menubar = wx.MenuBar()

		logout = wx.Menu()

		item = wx.MenuItem(logout, wx.ID_NEW, text = "logout", kind = wx.ITEM_NORMAL)
		logout.Append(item)

		logout.AppendSeparator()

		menubar.Append(logout, '&Exit')

		return menubar

	def menuHandler(self, event, parent):
		id = event.GetId()
		if id == wx.ID_NEW:
			module = __import__("LoginForm")
			login = getattr(module, "LoginForm")("Banana Detection")
			login.Show()
			parent.Hide()