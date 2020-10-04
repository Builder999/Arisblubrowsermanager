import sys
import subprocess
from PySide2.QtWidgets import QApplication,QMainWindow, QPushButton, QMessageBox, QLabel, QWidget
from PySide2.QtGui import QIcon, QPixmap
from browserappalts import *

class Window (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Browser Selection")
        self.setGeometry(450,300,300,300)
        self.setMinimumHeight(300)
        self.setMinimumWidth(450)
        self.setMaximumWidth(450)
        self.setMaximumHeight(300)
        self.setIcon()
        self.setButton()

    def shownew(self, checked):
        self.w = Altwindow()
        self.w.show()


    def setIcon(self):
        appIcon = QIcon("browsericon.png")
        self.setWindowIcon(appIcon)




    def setButton(self):

        labelpic = QPixmap("firefoxicon.png")
        firefoxinstall = QPushButton("Install Firefox", self)
        firefoxinstall.move(150,0)
        firefoxinstall.resize(200,20)
        firefoxinstall.setIcon(labelpic)
        firefoxinstall.setStyleSheet("background-color: green")

        firefoxuninstall = QPushButton("Uninstall Firefox", self)
        firefoxuninstall.move(150,20)
        firefoxuninstall.resize(200,20)
        firefoxuninstall.setIcon(labelpic)
        firefoxuninstall.setStyleSheet("background-color: red")

        labelpic = QPixmap("chromiumicon.png")
        chromiuminstall = QPushButton("Install Chrome", self)
        chromiuminstall.move(150,50)
        chromiuminstall.resize(200,20)
        chromiuminstall.setIcon(labelpic)
        chromiuminstall.setStyleSheet("background-color: green")

        chromiumuninstall = QPushButton("Uninstall Chrome", self)
        chromiumuninstall.move(150,70)
        chromiumuninstall.resize(200,20)
        chromiumuninstall.setIcon(labelpic)
        chromiumuninstall.setStyleSheet("background-color: red")

        labelpic = QPixmap("browsericon.png")
        dotinstall = QPushButton("Install Dot", self)
        dotinstall.move(150,100)
        dotinstall.resize(200,20)
        dotinstall.setIcon(labelpic)
        dotinstall.setStyleSheet("background-color: green")


        dotuninstall = QPushButton("Uninstall Dot", self)
        dotuninstall.move(150,120)
        dotuninstall.resize(200,20)
        dotuninstall.setIcon(labelpic)
        dotuninstall.setStyleSheet("background-color: red")

        labelpic = QPixmap("edge.jpg")
        edgeinstall = QPushButton("Install Edge", self)
        edgeinstall.move(150,150)
        edgeinstall.resize(200,20)
        edgeinstall.setIcon(labelpic)
        edgeinstall.setStyleSheet("background-color: green")

        edgeuninstall = QPushButton("Uninstall Edge", self)
        edgeuninstall.move(150,170)
        edgeuninstall.resize(200,20)
        edgeuninstall.setIcon(labelpic)
        edgeuninstall.setStyleSheet("background-color: red")

        labelpic = QPixmap("vivaldilogo.png")
        vivaldiinstall = QPushButton("Install Vivaldi", self)
        vivaldiinstall.move(150,200)
        vivaldiinstall.resize(200,20)
        vivaldiinstall.setIcon(labelpic)
        vivaldiinstall.setStyleSheet("background-color: green")

        vivaldiuninstall = QPushButton("Uninstall Vivaldi", self)
        vivaldiuninstall.move(150,220)
        vivaldiuninstall.resize(200,20)
        vivaldiuninstall.setIcon(labelpic)
        vivaldiuninstall.setStyleSheet("background-color: red")

        alts = QPushButton("Alternatives", self)
        alts.move(150,250)
        alts.resize(200,20)


        firefoxinstall.clicked.connect(self.installfirefox)
        firefoxuninstall.clicked.connect(self.uninstallfirefox)
        chromiuminstall.clicked.connect(self.installchromium)
        chromiumuninstall.clicked.connect(self.uninstallchromium)
        dotinstall.clicked.connect(self.installdot)
        dotuninstall.clicked.connect(self.uninstalldot)
        edgeinstall.clicked.connect(self.installedge)
        edgeuninstall.clicked.connect(self.uninstalledge)
        vivaldiinstall.clicked.connect(self.installvivaldi)
        vivaldiuninstall.clicked.connect(self.uninstallvivaldi)
        alts.clicked.connect(self.shownew)

    def installfirefox(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to install firefox?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh installfirefox", shell=True)
        elif response == QMessageBox.No:
            pass




    def uninstallfirefox(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall firefox?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstallfirefox", shell=True)
        elif response == QMessageBox.No:
            pass

    def installchromium(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to install chromium?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh installchromium", shell=True)
        elif response == QMessageBox.No:
            pass

    def uninstallchromium(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall chromium?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstallchromium", shell=True)
        elif response == QMessageBox.No:
            pass
    def installdot(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to install dot?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh installdot", shell=True)
        elif response == QMessageBox.No:
            pass
    def uninstalldot(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall dot?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstalldot", shell=True)
        elif response == QMessageBox.No:
            pass

    def installedge(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to install edge?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh installedge", shell=True)
        elif response == QMessageBox.No:
            pass

    def uninstalledge(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall edge?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstalledge", shell=True)
        elif response == QMessageBox.No:
            pass

    def installvivaldi(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to install Vivaldi?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh installvivaldi", shell=True)
        elif response == QMessageBox.No:
            pass

    def uninstallvivaldi(self):
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall Vivaldi?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstallvivaldi", shell=True)
        elif response == QMessageBox.No:
            pass



myApp = QApplication(sys.argv)
window = Window()
window.show()
myApp.exec_()
#sys.exit(0)
