from eventgui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget

import sys
import time
import threading


class AnotherWindow(QWidget):

    def __init__(self):
        super(QWidget,self).__init__()
        
        self.label = QLabel(self)
        self.label.setGeometry(0, 0, 1920, 1200)
        self.label.setText('Hello World')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet('font-size:40px')


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Label")
        
        global width
        global height
        width = self.frameGeometry().width()
        height = self.frameGeometry().height()
        
        self.ui.label.setText('Lutfen Yeni Pencereyi Acmak icin mikrofonu takiniz.\nAcilan Pencereyi Kapatmak Icin mikrofonu cikartiniz.')
        self.ui.label.setAlignment(Qt.AlignCenter)
        self.ui.label.setStyleSheet('font-size:10px')

        event_button_handle_thread=threading.Thread(target=self.event_button_handle)
        event_button_handle_thread.start()

    def event_button_handle(self):
        #import evdev
        from evdev import InputDevice, categorize, ecodes
        
        mic = InputDevice('/dev/input/event13')
        
        
        w = AnotherWindow()
        
        for event in mic.read_loop():
            if event.type == ecodes.EV_SW:
                if event.value == 0:
                    self.ui.label.setText('2. Pencere Kapali...')
                    w.hide()
                    
                    
                elif event.value == 1:
                    self.ui.label.setText('2. Pencere Acik...')
                    w.setWindowFlags(Qt.WindowCloseButtonHint | Qt.WindowType_Mask)
                    w.setAttribute(Qt.WA_DeleteOnClose)
                    w.move(1920,0)
                    w.setWindowFlags(Qt.FramelessWindowHint)
                    w.showFullScreen()
                    w.show()
                    




if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())
