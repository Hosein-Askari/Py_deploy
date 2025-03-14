import sys
from PySide6.QtWidgets import QApplication,QMainWindow,QGraphicsBlurEffect,QFrame,QGridLayout,QSizePolicy
from PySide6.QtGui import QKeySequence, QShortcut
from design import Ui_MainWindow
import requests
import datetime


class  MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.main_widget = self.ui.main_frame 
        self.background_widget = self.ui.bg_frame
        self.content_widget = self.ui.content_frame

        
        grid_layout = self.main_widget.layout()  
        if not grid_layout:
            grid_layout = QGridLayout(self.main_widget)
            self.main_widget.setLayout(grid_layout)

        
        self.main_widget.setStyleSheet("background-color: rgba(255,255,255,0);border : 0px solid red;border-radius : 15px;")
        self.background_widget.setStyleSheet("background-color: rgba(255,255,255,30);border-radius : 10px;")
        self.content_widget.setStyleSheet("background-color: rgba(255,255,255,0);border : 0px solid red;border-radius : 10px;")
        
        self.blur_effect = QGraphicsBlurEffect()
        self.blur_effect.setBlurRadius(10)
        self.background_widget.setGraphicsEffect(self.blur_effect)

        
        grid_layout.addWidget(self.background_widget, 0, 1)
        grid_layout.addWidget(self.content_widget, 0, 1)
        self.background_widget.setGeometry(self.main_widget.rect())
        self.content_widget.setGeometry(self.main_widget.rect())

        self.content_widget.raise_()

        self.ui.label_2.hide()
        self.ui.label_3.hide()
        self.ui.label_4.hide()
        self.ui.label_5.hide()
        self.ui.bg_frame.hide()

        self.ui.pushButton.clicked.connect(lambda:self.search(self.ui.lineEdit.text()) if self.ui.lineEdit.text() != "" else None )
        shortcut = QShortcut(QKeySequence("Return"), self)
        shortcut.activated.connect(self.ui.pushButton.click)

        BASE_DIR = Path(__file__).resolve().parent  

        self.images_path = BASE_DIR / "images"







    def search(self,city):
        resposnse=requests.get(url=f"https://goweather.herokuapp.com/weather/{city}")
        
        if  resposnse.status_code==200:
            weather = resposnse.json()
            self.show_(weather)
        
        

        




    def show_(self,weather):
        temp=weather['temperature']
        wind=weather['wind']
        condition=weather['description']
        forecast=weather['forecast']
        

        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        today_index = datetime.datetime.today().weekday()






        #   Qiqihar,apia

        self.ui.label_6.setText(
            '<p style="text-align: right;">'
            '<span style="font-family: Tahoma; font-size: 48px; color: rgb(189, 57, 107) ;">Today</span><br>'
            '<span style="font-family: Arial; font-size: 40px; color: white;"><strong>{}</strong></span><br>'
            '<span style="font-family: Courier New; font-size: 36px; color: white;">{}</span><br>'
            '<span style="font-family: Courier New ;font-size: 36px; color: white;">{}</span>'
            '</p>'.format(condition,temp,wind,)
        )

        if condition == "Blizzard" or "storm" in condition.lower():
            condition="storm"
        elif "snow"in condition.lower() :
            condition="snow"
        elif "rain" in condition.lower():
            condition = "rainy"
        elif "clear" in condition.lower():
            condition="clear"
        html_text = f"""
    <div style="display: flex; align-items: left;">
        <!-- تصویر در سمت چپ -->
<img src="{self.images_path}/{condition}.png" width="100" height="100" style="margin-right: 10px;"></div>
"""

        self.ui.label.setText(html_text)




        self.ui.label_3.setText(
            '<p style="text-align: center;">'
            '<span style="font-family: Tahoma; font-size: 40px; color: rgb(22, 17, 23);">{}</span><br>'
            '<span style="font-family: Courier New; font-size: 36px; color: white;">{}</span><br>'
            '<span style="font-family: Courier New; font-size: 36px; color: white;">{}</span>'
            '</p>'.format(days[(today_index+1)%7],forecast[0]['temperature'],forecast[0]['wind'])
        )

        self.ui.label_4.setText(
            '<p style="text-align: center;">'
            '<span style="font-family: Tahoma; font-size: 40px; color: rgb(22, 17, 23);">{}</span><br>'
            '<span style="font-family: Courier New; font-size: 36px; color: white;">{}</span><br>'
            '<span style="font-family: Courier New; font-size: 36px; color: white;">{}</span>'
            '</p>'.format(days[(today_index+2)%7],forecast[1]['temperature'],forecast[1]['wind'])
        )

        self.ui.label_5.setText(
            '<p style="text-align: center;">'
            '<span style="font-family: Tahoma; font-size: 40px; color: rgb(22, 17, 23);">{}</span><br>'
            '<span style="font-family: Courier New; font-size: 36px; color: white;">{}</span><br>'
            '<span style="font-family: Courier New; font-size: 36px; color: white;">{}</span>'
            '</p>'.format(days[(today_index+3)%7],forecast[2]['temperature'],forecast[2]['wind'])
        )

        self.ui.label_2.show()
        self.ui.label_3.show()
        self.ui.label_4.show()
        self.ui.label_5.show()
        self.ui.bg_frame.show()
app = QApplication(sys.argv)




main_window = MainWindow()
main_window.show()
app.exec()


