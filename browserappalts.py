import sys
import subprocess
from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon, QPixmap
class Altwindow(QWidget):
    def shownewchromealt(self, checked):
        self.w = chromealtwindow()
        self.w.show()
    def shownewfirefoxalt(self, checked):
        self.w = firefoxaltwindow()
        self.w.show()
    def shownewotheralt(self, checked):
        self.w = otheraltwindow()
        self.w.show()

    def setIcon(self):
        appIcon = QIcon("browsericon.png")
        self.setWindowIcon(appIcon)
    def setButtons(self):
        labelpic = QPixmap("chromiumicon.png")
        Chrome_alts = QPushButton("Chrome Alternatives", self)
        Chrome_alts.move(125,30)
        Chrome_alts.resize(200,40)
        Chrome_alts.setIcon(labelpic)

        labelpic = QPixmap("firefoxicon.png")
        Firefox_alts = QPushButton("Firefox Alternatives", self)
        Firefox_alts.move(125,100)
        Firefox_alts.resize(200,40)
        Firefox_alts.setIcon(labelpic)

        labelpic = QPixmap("browsericon.png")
        Other_alts = QPushButton("Other Alternatives", self)
        Other_alts.move(125,170)
        Other_alts.resize(200,40)
        Other_alts.setIcon(labelpic)

        Chrome_alts.clicked.connect(self.shownewchromealt)
        Firefox_alts.clicked.connect(self.shownewfirefoxalt)
        Other_alts.clicked.connect(self.shownewotheralt)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Alternatives")
        self.setGeometry(450,300,300,300)
        self.setMinimumHeight(300)
        self.setMinimumWidth(450)
        self.setMaximumWidth(450)
        self.setMaximumHeight(300)
        self.setIcon()
        self.setButtons()

class firefoxaltwindow(QWidget):
    def UI(self):
        altpicture = QLabel(self)
        pixmap = QPixmap("firefoxicon.png")
        pixmap = pixmap.scaled(150, 150)
        altpicture.setPixmap(pixmap)
        altpicture.resize(150,150)
        altpicture.move(160,0)
        self.combo = QComboBox(self)
        self.combo.addItems(["Waterfox", "Tor", "GNU IceCat", "LibreWolf", "PaleMoon", "Basilisk", "Konquerer"])
        self.combo.move(170,150)
        install = QPushButton("Install", self)
        install.resize(50,20)
        install.move(170, 180)
        install.setStyleSheet("background-color: green")
        uninstall = QPushButton("Uninstall", self)
        uninstall.resize(60,20)
        uninstall.move(220,180)
        uninstall.setStyleSheet("background-color: red")
        install.clicked.connect(self.install)
        uninstall.clicked.connect(self.uninstall)\

    def install(self):
        install = self.combo.currentText()
        print(install)
        response = QMessageBox.question(self, "Confirmation", "Do you want to install "+install+"?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            print("install"+install.replace(" ", ""))
            subprocess.run("sudo ./browsercheck.sh install"+install.replace(" ",""), shell=True)
        elif response == QMessageBox.No:
            pass

    def uninstall(self):
        uninstall = self.combo.currentText()
        print(uninstall)
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall "+uninstall.replace(" ", "")+"?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstall"+uninstall.replace(" ",""), shell=True)
        elif response == QMessageBox.No:
            pass

        self.show()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Firefox Alternatives")
        self.setGeometry(450,300,300,300)
        self.setMinimumHeight(300)
        self.setMinimumWidth(450)
        self.setMaximumWidth(450)
        self.setMaximumHeight(300)
        self.UI()
class chromealtwindow(QWidget):
    def UI(self):
        altpicture = QLabel(self)
        pixmap = QPixmap("chromiumicon.png")
        pixmap = pixmap.scaled(150, 150)
        altpicture.setPixmap(pixmap)
        altpicture.resize(150,150)
        altpicture.move(160,0)
        self.combo = QComboBox(self)
        self.combo.addItems(["Opera","Brave","Ungoogled Chromium","Iridium","Superbird","Lulumi", "Breaker","Yandex","Dissenter","Slimjet"])
        self.combo.move(170,150)
        install = QPushButton("Install", self)
        install.resize(50,20)
        install.move(170, 180)
        install.setStyleSheet("background-color: green")
        uninstall = QPushButton("Uninstall", self)
        uninstall.resize(60,20)
        uninstall.move(220,180)
        uninstall.setStyleSheet("background-color: red")
        install.clicked.connect(self.install)
        uninstall.clicked.connect(self.uninstall)\

    def install(self):
        install = self.combo.currentText()
        print(install)
        response = QMessageBox.question(self, "Confirmation", "Do you want to install "+install+"?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            print("install"+install.replace(" ", ""))
            subprocess.run("sudo ./browsercheck.sh install"+install.replace(" ",""), shell=True)
        elif response == QMessageBox.No:
            pass

    def uninstall(self):
        uninstall = self.combo.currentText()
        print(uninstall)
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall "+uninstall.replace(" ", "")+"?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstall"+uninstall.replace(" ",""), shell=True)
        elif response == QMessageBox.No:
            pass

        self.show()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chrome Alternatives")
        self.setGeometry(450,300,300,300)
        self.setMinimumHeight(300)
        self.setMinimumWidth(450)
        self.setMaximumWidth(450)
        self.setMaximumHeight(300)
        self.UI()

class otheraltwindow(QWidget):
    def UI(self):
        altpicture = QLabel(self)
        pixmap = QPixmap("browsericon.png")
        pixmap = pixmap.scaled(150, 150)
        altpicture.setPixmap(pixmap)
        altpicture.resize(150,150)
        altpicture.move(150,0)
        self.combo = QComboBox(self)
        self.combo.addItems(["Midori", "NetSurf", "Gnome Web", "Falkon", "Seamonkey", "Links", "Otter Browser", "Min", "Qute", "Seilo", "Sushi", "Servo", "Dooble"])
        self.combo.move(170,150)
        install = QPushButton("Install", self)
        install.resize(50,20)
        install.move(170, 180)
        install.setStyleSheet("background-color: green")
        uninstall = QPushButton("Uninstall", self)
        uninstall.resize(60,20)
        uninstall.move(220,180)
        uninstall.setStyleSheet("background-color: red")
        install.clicked.connect(self.install)
        uninstall.clicked.connect(self.uninstall)\

    def install(self):
        install = self.combo.currentText()
        print(install)
        response = QMessageBox.question(self, "Confirmation", "Do you want to install "+install+"?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            print("install"+install.replace(" ", ""))
            subprocess.run("sudo ./browsercheck.sh install"+install.replace(" ",""), shell=True)
        elif response == QMessageBox.No:
            pass

    def uninstall(self):
        uninstall = self.combo.currentText()
        print(uninstall)
        response = QMessageBox.question(self, "Confirmation", "Do you want to uninstall "+uninstall.replace(" ", "")+"?", QMessageBox.Yes | QMessageBox.No)
        if response == QMessageBox.Yes:
            subprocess.run("sudo ./browsercheck.sh uninstall"+uninstall.replace(" ",""), shell=True)
        elif response == QMessageBox.No:
            pass

        self.show()
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Other Alternatives")
        self.setGeometry(450,300,300,300)
        self.setMinimumHeight(300)
        self.setMinimumWidth(450)
        self.setMaximumWidth(450)
        self.setMaximumHeight(300)
        self.UI()
