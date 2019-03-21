import wx
import cv2
import os
import numpy as np
from contour import *
from PIL import Image
from model.dbconnect import *
from props.InputProp import *
from props.FormField import *

class EditForm(wx.Frame):
    def __init__(self, parent, title, id = 0):  	
        wx.Frame.__init__(self, parent, title=title, size=(1000, 700), style = wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION )

        self._db = DB()
        self.parent = parent
        get_user = self._db.get_id(id)
        

        # homedir = os.path.expanduser('~')
        dir_path = os.path.dirname(os.path.realpath(__file__))
        img_width = 250
        img_height = 150
        self.finger_weight = 2000
        self.total_weight = 0
        self.status = "Disapproved"

        panel = wx.Panel(self)
        panel.SetBackgroundColour("STEEL BLUE")

        self.imagepanel = wx.Panel(panel, size=(500, 620))
        self.imagepanel.SetBackgroundColour("WHITE")

        form_panel = wx.Panel(panel, size=(500, 500))
        form_panel.SetBackgroundColour("STEEL BLUE")
        sizer = wx.GridBagSizer(10,10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        # header = wx.Panel(panel, size=(1000, 100), style=wx.RAISED_BORDER)
        # header.SetBackgroundColour("MEDIUM SLATE BLUE")

        # font = wx.Font(30, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD) 
        # _vbox = wx.BoxSizer(wx.VERTICAL)
        # self.header_title = wx.StaticText(header, 1, "Banana Data System", style = wx.ALIGN_CENTER, size=(1000, 50))
        # self.header_title.SetFont(font) 
        # _vbox.Add(self.header_title, 0, wx.ALIGN_CENTER_VERTICAL, 1)

        # font = wx.Font(20, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD) 
        # objname = wx.StaticText(header, 1, "Banana 1", style = wx.ALIGN_CENTER, size=(1000, 30))
        # objname.SetFont(font) 
        # _vbox.Add(objname, 1, wx.ALIGN_CENTER_VERTICAL, 1)

        # header.SetSizer(_vbox)

        # vbox.Add(header, 0, wx.ALIGN_CENTER_VERTICAL, 1)

        _hbox = wx.BoxSizer(wx.HORIZONTAL)
        _vbox = wx.BoxSizer(wx.VERTICAL)

        field = FormField()
        menubar = field.setMenuBar()

        field.setPanel(self.imagepanel)
        font = wx.Font(14, wx.ROMAN, wx.ITALIC, wx.FONTWEIGHT_BOLD) 

        label = field.setLabel("Front")
        _vbox.Add(label, 0, wx.ALIGN_CENTER_HORIZONTAL, 1)

        front_box = self.getImage(str(get_user[5]), img_width, img_height, "\\..\\images\\front\\", "front")
        _vbox.Add(front_box, 0, wx.ALIGN_TOP, 1)
        
        label = field.setLabel("Back")
        _vbox.Add(label, 0, wx.ALIGN_CENTER_HORIZONTAL, 1)

        back_box = self.getImage(str(get_user[6]), img_width, img_height, "\\..\\images\\back\\", "back")
        _vbox.Add(back_box, 0, wx.ALIGN_TOP, 1)

        label = field.setLabel("Side")
        _vbox.Add(label, 0, wx.ALIGN_CENTER_HORIZONTAL, 1)

        side_box = self.getImage(str(get_user[7]), img_width, img_height, "\\..\\images\\side\\", "side")
        _vbox.Add(side_box, 0, wx.ALIGN_TOP, 1)

        hbox.Add(_vbox, 0, wx.ALIGN_TOP, 1)

        field = FormField()

        field.setPanel(form_panel)
        field.setFont(14)

        label_font = wx.Font(14, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD) 
        
        label = field.setLabel("Width (CM)") 
        sizer.Add(label, pos = (0, 0), flag = wx.ALL, border = 10)

        input_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
        self.input_width = field.setTextField("")
        sizer.Add(self.input_width, pos = (0, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        label = field.setLabel("Height(CM)") 
        sizer.Add(label, pos = (1, 0), flag = wx.ALL, border = 10)

        self.input_height = field.setTextField("")
        sizer.Add(self.input_height, pos = (1, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        label = field.setLabel("Length(CM)") 
        sizer.Add(label, pos = (2, 0), flag = wx.ALL, border = 10)

        self.input_length = field.setTextField("")
        sizer.Add(self.input_length, pos = (2, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        label = field.setLabel("Weight(GRAMS)") 
        sizer.Add(label, pos = (3, 0), flag = wx.ALL, border = 10)

        self.input_weight = field.setTextField("")
        sizer.Add(self.input_weight, pos = (3, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        label = field.setLabel("Quality") 
        sizer.Add(label, pos = (4, 0), flag = wx.ALL, border = 10)

        self.input_pix = field.setTextField("")
        sizer.Add(self.input_pix, pos = (4, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        label = field.setLabel("Shelf Life") 
        sizer.Add(label, pos = (5, 0), flag = wx.ALL, border = 10)

        self.input_life = field.setTextField("")
        sizer.Add(self.input_life, pos = (5, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        label = field.setLabel("Status") 
        sizer.Add(label, pos = (6, 0), flag = wx.ALL, border = 10)
        
        self.input_stat = field.setTextField("")
        sizer.Add(self.input_stat, pos = (6, 1), span = (1, 2), flag = wx.EXPAND|wx.ALL, border = 10)

        self.submit_btn = wx.Button(form_panel, label='Update', size=(400, 30))
        sizer.Add(self.submit_btn, pos = (7, 0), span = (2, 2), flag = wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, border = 10)

        form_panel.SetSizer(sizer)
        hbox.Add(form_panel, 1, wx.ALIGN_LEFT, border = 10)
        vbox.Add(hbox, 0, wx.ALIGN_TOP, 1)

        btn_panel = wx.Panel(panel, size=(1000, 200))
        btn_panel.SetBackgroundColour("STEEL BLUE")
        btn_hbox = wx.BoxSizer(wx.HORIZONTAL)

        back_record = wx.Button(btn_panel, label='Back to records', size=(150, 50))
        btn_hbox.Add(back_record, 0, wx.SHAPED, border = 1)

        back_eval = wx.Button(btn_panel, label='Back to Evaluate', size=(150, 50))
        btn_hbox.Add(back_eval, 0, wx.SHAPED, border = 1)

        view_sq = wx.Button(btn_panel, label='View S.Q.', size=(150, 50))
        btn_hbox.Add(view_sq, 0, wx.SHAPED, border = 1)

        btn_cancel = wx.Button(btn_panel, label='Cancel', size=(150, 50))
        btn_hbox.Add(btn_cancel, 0, wx.SHAPED, border = 1)

        btn_panel.SetSizer(btn_hbox)
        
        vbox.AddSpacer(30)

        vbox.Add(btn_panel, 1, wx.ALIGN_TOP, 1)

        panel.SetSizer(vbox)

        self.SetMenuBar(menubar)
        self.Bind(wx.EVT_BUTTON, lambda event: self.insertData(event, id), self.submit_btn)
        self.Bind(wx.EVT_BUTTON, lambda event: self.goToEvaluate(event, self), back_eval)
        self.Bind(wx.EVT_BUTTON, lambda event: self.goToRecord(event, self), back_record)
        self.Bind(wx.EVT_BUTTON, lambda event: self.goToMenu(event, self), btn_cancel)
        self.Bind(wx.EVT_BUTTON, lambda event: self.showQualityModal(event), view_sq)
        self.Bind(wx.EVT_MENU, lambda event: field.menuHandler(event, self))
        self.Bind(wx.EVT_CLOSE, self.onClose)
        self.fieldSetValues()
        self.Centre() 
        self.Show(True)


    def insertData(self, event, item_id):
        self.db = DB()  
        prop = InputProp(float(self.total_weight), float(self.height), float(self.width), float(self.length), 1, 
            int(round(self.percent)), self.status, self.life)
        self.db.updateData(prop, item_id)
        SuccessDialog(self, "Success").ShowModal()

    def showQualityModal(self, event):
        QualityModal(self, "Standard Quality").ShowModal()

    def getImage(self, imageStr, img_width, img_height, directory, objtype):
        _hbox = wx.BoxSizer(wx.HORIZONTAL)
        dir_path = os.path.dirname(os.path.realpath(__file__))

        #front filter
        front_filter = wx.Image(dir_path + directory + imageStr, wx.BITMAP_TYPE_ANY)
        _front_filter = cv2.imread(dir_path + directory + imageStr)
        _front_filter = self.adjust_gamma(_front_filter, 2.5)

        filtercol = self.filteredColor(_front_filter)
        front_w = filtercol['width']
        front_h = filtercol['height']
        front_p = filtercol['percent']
        front_i = filtercol['image']
        front_l = filtercol['life']
        
        self.length = 0
        if objtype == "side":
            self.length = front_w
        else:
            self.width = front_w
            self.height = front_h
            self.front_percent = front_p
            self.front_life = front_l

            self.percent = self.front_percent
            self.life = self.front_life

        self.total_weight = round((self.width * self.height * self.length), 2)

        front_filter.SetData(front_i.tostring())

        _front_img = front_filter.Scale(img_width, img_height)
        self.videobmp = wx.StaticBitmap(self.imagepanel, wx.ID_ANY, wx.Bitmap(_front_img))
        _hbox.Add(self.videobmp, 0, wx.ALIGN_CENTER_VERTICAL, 1)

        #front detection
        front_detection = wx.Image(dir_path + directory + imageStr, wx.BITMAP_TYPE_ANY)
        _front_detection = cv2.imread(dir_path + directory + imageStr)

        _front_detection = self.adjust_gamma(_front_detection, 1.5)

        detectioncol = self.detectionObj(_front_detection)
        front_detection.SetData(detectioncol.tostring())

        _front_cascade = front_detection.Scale(img_width, img_height)
        self.videobmp2 = wx.StaticBitmap(self.imagepanel, wx.ID_ANY, wx.Bitmap(_front_cascade))
        _hbox.Add(self.videobmp2, 0, wx.ALIGN_CENTER_VERTICAL, 1)

        return _hbox

    def filteredColor(self, obj):
        # self.filtered = cv2.resize(obj, (self.resized_w,  self.resized_h), interpolation = cv2.INTER_AREA)
        life = 14
        hsv = cv2.cvtColor(obj, cv2.COLOR_BGR2HSV)
        lower_green = np.array([30, 0, 0])
        upper_green = np.array([70, 255, 255])
        mask = cv2.inRange(hsv, lower_green, upper_green)
        no_pixels = cv2.countNonZero(mask)

        res = cv2.bitwise_and(obj, obj, mask= mask)
        
        size = get_size(res)
        percent = (no_pixels / size['size']) * 100
        life = life * (percent/100)
        if percent > 50:
            self.status = "Approved"

        return {'image' : size['image'], 'height' : size['height'], 
        'width' : size['width'], 'percent' : percent, 'life' : life}


    def detectionObj(self, obj):
        detection = cv2.CascadeClassifier('cascade/BananaCascade.xml')
        obj_detect = cv2.cvtColor(obj, cv2.COLOR_BGR2GRAY)
        faces = detection.detectMultiScale(obj_detect, scaleFactor=1.1, minNeighbors=4, 
            maxSize=(400, 400), minSize=(200, 200), flags = cv2.CASCADE_SCALE_IMAGE)

        for (x,y,w,h) in faces:
                cv2.rectangle(obj,(x,y),(x+w,y+h),(255,0,0),2)

        fingers = detection.detectMultiScale(obj_detect, scaleFactor=1.1, minNeighbors=10, maxSize=(30, 70), minSize=(30, 70), flags = cv2.CASCADE_SCALE_IMAGE)
        # self.total_weight +=  len(fingers) * self.finger_weight
        
        for (x,y,w,h) in fingers:
            cv2.rectangle(obj,(x,y),(x+w,y+h),(255,0,0),2)

        return obj

    def fieldSetValues(self):
        self.input_width.SetValue(str(self.width))
        self.input_height.SetValue(str(self.height))
        self.input_pix.SetValue(str(round(self.percent)) + "%")
        self.input_weight.SetValue(str(round(self.total_weight, 2)))
        self.input_stat.SetValue(self.status)
        self.input_life.SetValue(str(round(self.life)))
        self.input_length.SetValue(str(self.length))

    def onClose(self, event):
        self.Destroy()

    def goToEvaluate(self, event, parent):
        capture = cv2.VideoCapture(0)
        frame = wx.Frame(None)
        module = __import__("CameraCapture")
        cam = getattr(module, "CameraCapture")(frame, capture)
        cam.Show()
        parent.Hide()

    def goToRecord(self, event, parent):
        module = __import__("form.FlexList", fromlist=['FlexList'])
        menu = getattr(module, "FlexList")("Record")
        menu.Show()
        parent.Hide()

    def goToMenu(self, event, parent):
        module = __import__("MenuForm")
        menu = getattr(module, "MenuForm")("Main Menu")
        menu.Show()
        parent.Hide()
    
    def adjust_gamma(self, image, gamma=1.0):
        invGamma = 1.0 / gamma
        table = np.array([((i / 255.0) ** invGamma) * 255
            for i in np.arange(0, 256)]).astype("uint8")

        return cv2.LUT(image, table)


class SuccessDialog(wx.Dialog):
    def __init__(self, parent, title):
        super(SuccessDialog, self).__init__(parent, title = title, size = (250, 150))
        panel = wx.Panel(self,)
        hbox = wx.BoxSizer(wx.HORIZONTAL)

        label_font = wx.Font(20, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        self.label = wx.StaticText(panel, 1, "Successfully Update")
        self.label.SetFont(label_font)

        hbox.Add(self.label, 1, wx.ALIGN_CENTER_HORIZONTAL, border = 10)

class QualityModal(wx.Dialog):
    def __init__(self, parent, title):
        super(QualityModal, self).__init__(parent, title = title, size = (500, 400))

        panel = wx.Panel(self, size=(500, 400))

        vbox = wx.BoxSizer(wx.VERTICAL)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        label_font = wx.Font(14, wx.ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        label = wx.StaticText(panel, 1, "Weight (KG)")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        hbox.AddSpacer(10)
        label = wx.StaticText(panel, 1, "Size (CM))")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        vbox.Add(hbox, 0, wx.ALIGN_TOP, border = 10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(panel, 1, "Small \n1.8 KG - 2.4 KG")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        hbox.AddSpacer(10)
        label = wx.StaticText(panel, 1, "Small \n10 cm")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        vbox.Add(hbox, 0, wx.ALIGN_TOP, border = 10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(panel, 1, "Medium \n2.5 KG - 3.4 KG")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        hbox.AddSpacer(10)
        label = wx.StaticText(panel, 1, "Small \n10 cm - 14 cm")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        vbox.Add(hbox, 0, wx.ALIGN_TOP, border = 10)

        hbox = wx.BoxSizer(wx.HORIZONTAL)
        label = wx.StaticText(panel, 1, "Large \n3.5 KG - 4.0 KG")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        hbox.AddSpacer(10)
        label = wx.StaticText(panel, 1, "Large \n15 cm")
        label.SetFont(label_font)
        hbox.Add(label, 1, wx.ALL, border = 10)
        vbox.Add(hbox, 0, wx.ALIGN_TOP, border = 10)

        panel.SetSizer(vbox)