import matplotlib.pyplot as plt
from torchvision import models
from PyQt5.QtWidgets import QMainWindow,QFileDialog,QApplication
from Giaodien import Ui_MainWindow
from PyQt5.QtGui import QPixmap,QImage
import cv2,sys,os.path
from remove import RemoveBackground
from torchvision import models
from rem import Rem2
import torch
import torchvision.transforms as T
from rembg import remove

class MainWindow:
    def __init__(self):

        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        self.uic.stackedWidget.setCurrentWidget(self.uic.RemoveB)
        self.uic.change_button.clicked.connect(self.showChangeB)
        self.uic.remove_button.clicked.connect(self.showRemoveB)
        self.uic.run_button.clicked.connect(self.RemoveB)

        #toolbar
        self.uic.actionopen.triggered.connect(self.loadImage)
        self.uic.actionSave.triggered.connect(self.saveImg)
        # self.uic.actionWebcam.triggered.connect(self.Webcam)


        self.directory = os.path.expanduser("~")
        self.path = None
        self.image = None
        self.img = None


        self.RMB = RemoveBackground()


    def show(self):
        self.main_win.show()
    def showChangeB(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.ChangeB)
    def showRemoveB(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.RemoveB)



    #loadimg
    def loadImage(self):
        path = QFileDialog.getOpenFileName( filter="Image (*.jpg *.png)")[0]
        if (path):
            self.path = path
            self.image = cv2.imread(self.path)
            self.setPhoto(self.image)
            self.img=self.image
    #setphoto
    def setPhoto(self, image):
        frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1], frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(image)
        self.uic.pic_1.setPixmap(pixmap)

    def abc(self):
        print("abc")
    def saveImg(self):
        filename = QFileDialog.getSaveFileName( filter="Image (*.jpg *.png)" )
        # print(filename)
        if (filename[0]):
            self.path = filename[0]
            cv2.imwrite(self.path,self.imgrs)
    def RemoveB(self):
        print(self.path)
        img = cv2.imread(self.path)
        self.imgrs = remove(img)
        self.setPhoto(self.imgrs)






if __name__=="__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())