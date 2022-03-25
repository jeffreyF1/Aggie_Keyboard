# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TESTPIANO.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import winsound

howdy = True;
warhymn = False;
thirdsong = False;

def swapHowdy():
    global howdy
    howdy = True;
    global warhymn
    warhymn = False;
    global thirdsong
    thirdsong = False;
def swapHymn():
    global howdy
    howdy = False;
    global warhymn
    warhymn = True;
    global thirdsong
    thirdsong = False;
def swapThird():
    global howdy
    howdy = False;
    global warhymn
    warhymn = False;
    global thirdsong
    thirdsong = True;

def clicked1():
    if(howdy):
        filename1 = 'howdy1.wav'
        winsound.PlaySound(filename1, winsound.SND_FILENAME)
    elif(warhymn):
        filename01 = 'warhymn1.wav'
        winsound.PlaySound(filename01, winsound.SND_FILENAME)
    else:
        filename001 = 'thirdsong1.wav'
        winsound.PlaySound(filename001, winsound.SND_FILENAME)
def clicked2():
    if(howdy):
        filename2 = 'howdy2.wav'
        winsound.PlaySound(filename2, winsound.SND_FILENAME)
    elif(warhymn):
        filename02 = 'warhymn2.wav'
        winsound.PlaySound(filename02, winsound.SND_FILENAME)
    else:
        filename002 = 'thirdsong2.wav'
        winsound.PlaySound(filename002, winsound.SND_FILENAME)
def clicked3():
    if(howdy):
        filename3 = 'howdy3.wav'
        winsound.PlaySound(filename3, winsound.SND_FILENAME)
    elif(warhymn):
        filename03 = 'warhymn3.wav'
        winsound.PlaySound(filename03, winsound.SND_FILENAME)
    else:
        filename003 = 'thirdsong3.wav'
        winsound.PlaySound(filename003, winsound.SND_FILENAME)
def clicked4():
    if(howdy):
        filename4 = 'howdy4.wav'
        winsound.PlaySound(filename4, winsound.SND_FILENAME)
    elif(warhymn):
        filename04 = 'warhymn4.wav'
        winsound.PlaySound(filename04, winsound.SND_FILENAME)
    else:
        filename004 = 'thirdsong4.wav'
        winsound.PlaySound(filename004, winsound.SND_FILENAME)
def clicked5():
    if(howdy):
        filename5 = 'howdy5.wav'
        winsound.PlaySound(filename5, winsound.SND_FILENAME)
    elif(warhymn):
        filename05 = 'warhymn5.wav'
        winsound.PlaySound(filename05, winsound.SND_FILENAME)
    else:
        filename005 = 'thirdsong5.wav'
        winsound.PlaySound(filename005, winsound.SND_FILENAME)
def clicked6():
    if(howdy):
        filename6 = 'howdy6.wav'
        winsound.PlaySound(filename6, winsound.SND_FILENAME)
    elif(warhymn):
        filename06 = 'warhymn6.wav'
        winsound.PlaySound(filename06, winsound.SND_FILENAME)
    else:
        filename006 = 'thirdsong6.wav'
        winsound.PlaySound(filename006, winsound.SND_FILENAME)
def clicked7():
    if(howdy):
        filename7 = 'howdy7.wav'
        winsound.PlaySound(filename7, winsound.SND_FILENAME)
    elif(warhymn):
        filename07 = 'warhymn7.wav'
        winsound.PlaySound(filename07, winsound.SND_FILENAME)
    else:
        filename007 = 'thirdsong7.wav'
        winsound.PlaySound(filename007, winsound.SND_FILENAME)
def clicked8():
    if(howdy):
        filename8 = 'howdy8.wav'
        winsound.PlaySound(filename8, winsound.SND_FILENAME)
    elif(warhymn):
        filename08 = 'warhymn8.wav'
        winsound.PlaySound(filename08, winsound.SND_FILENAME)
    else:
        filename008 = 'thirdsong8.wav'
        winsound.PlaySound(filename008, winsound.SND_FILENAME)
def clicked9():
    if(howdy):
        filename9 = 'howdy9.wav'
        winsound.PlaySound(filename9, winsound.SND_FILENAME)
    elif(warhymn):
        filename09 = 'warhymn9.wav'
        winsound.PlaySound(filename09, winsound.SND_FILENAME)
    else:
        filename009 = 'thirdsong9.wav'
        winsound.PlaySound(filename009, winsound.SND_FILENAME)
def clicked10():
    if(howdy):
        filename10 = 'howdy10.wav'
        winsound.PlaySound(filename10, winsound.SND_FILENAME)
    elif(warhymn):
        filename010 = 'warhymn10.wav'
        winsound.PlaySound(filename010, winsound.SND_FILENAME)
    else:
        filename0010 = 'thirdsong10.wav'
        winsound.PlaySound(filename0010, winsound.SND_FILENAME)
def clicked11():
    if(howdy):
        filename11 = 'howdy11.wav'
        winsound.PlaySound(filename11, winsound.SND_FILENAME)
    elif(warhymn):
        filename011 = 'warhymn11.wav'
        winsound.PlaySound(filename011, winsound.SND_FILENAME)
    else:
        filename0011 = 'thirdsong11.wav'
        winsound.PlaySound(filename0011, winsound.SND_FILENAME)
def clicked12():
    if(howdy):
        filename12 = 'howdy12.wav'
        winsound.PlaySound(filename12, winsound.SND_FILENAME)
    elif(warhymn):
        filename012 = 'warhymn12.wav'
        winsound.PlaySound(filename012, winsound.SND_FILENAME)
    else:
        filename0012 = 'thirdsong12.wav'
        winsound.PlaySound(filename0012, winsound.SND_FILENAME)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(992, 721)
        MainWindow.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.clicked.connect(clicked1)
        self.button1.setGeometry(QtCore.QRect(80, 380, 91, 281))
        self.button1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.4px;\n"
"border-style:inset;")
        self.button1.setText("")
        self.button1.setObjectName("button1")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(140, 380, 51, 151))
        self.button2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.button2.setText("")
        self.button2.setObjectName("button2")
        self.button2.clicked.connect(clicked2)
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(160, 380, 91, 281))
        self.button3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.4px;\n"
"border-style:inset;")
        self.button3.setText("")
        self.button3.setObjectName("button3")
        self.button3.clicked.connect(clicked3)
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(220, 380, 51, 151))
        self.button4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.button4.setText("")
        self.button4.clicked.connect(clicked4)
        self.button4.setObjectName("button4")
        self.button5 = QtWidgets.QPushButton(self.centralwidget)
        self.button5.setGeometry(QtCore.QRect(240, 380, 91, 281))
        self.button5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.4px;\n"
"border-style:inset;")
        self.button5.setText("")
        self.button5.clicked.connect(clicked5)
        self.button5.setObjectName("button5")
        self.button6 = QtWidgets.QPushButton(self.centralwidget)
        self.button6.setGeometry(QtCore.QRect(320, 380, 91, 281))
        self.button6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.4px;\n"
"border-style:inset;")
        self.button6.setText("")
        self.button6.setObjectName("button6")
        self.button6.clicked.connect(clicked6)
        self.button8 = QtWidgets.QPushButton(self.centralwidget)
        self.button8.setGeometry(QtCore.QRect(400, 380, 91, 281))
        self.button8.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.4px;\n"
"border-style:inset;")
        self.button8.setText("")
        self.button8.setObjectName("button8")
        self.button8.clicked.connect(clicked8)
        self.button10 = QtWidgets.QPushButton(self.centralwidget)
        self.button10.setGeometry(QtCore.QRect(480, 380, 91, 281))
        self.button10.clicked.connect(clicked10)
        self.button10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.4px;\n"
"border-style:inset;")
        self.button10.setText("")
        self.button10.setObjectName("button10")
        self.button12 = QtWidgets.QPushButton(self.centralwidget)
        self.button12.setGeometry(QtCore.QRect(560, 380, 91, 281))
        self.button12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width : 1.4px;\n"
"border-style:inset;")
        self.button12.setText("")
        self.button12.setObjectName("button12")
        self.button12.clicked.connect(clicked12)
        self.button7 = QtWidgets.QPushButton(self.centralwidget)
        self.button7.setGeometry(QtCore.QRect(380, 380, 51, 151))
        self.button7.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.button7.setText("")
        self.button7.clicked.connect(clicked7)
        self.button7.setObjectName("button7")
        self.button9 = QtWidgets.QPushButton(self.centralwidget)
        self.button9.setGeometry(QtCore.QRect(460, 380, 51, 151))
        self.button9.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.button9.setText("")
        self.button9.clicked.connect(clicked9)
        self.button9.setObjectName("button9")
        self.button11 = QtWidgets.QPushButton(self.centralwidget)
        self.button11.setGeometry(QtCore.QRect(540, 380, 51, 151))
        self.button11.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.button11.setText("")
        self.button11.clicked.connect(clicked11)
        self.button11.setObjectName("button11")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 261, 261))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("EkpZRlrA_400x400.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 110, 391, 241))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("RevIXSignaturePhoto-e1548954176255.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 130, 191, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("245.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(410, 10, 311, 61))
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(710, 380, 211, 291))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("210205_NewRev_JKE_4.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.button1.raise_()
        self.button3.raise_()
        self.button5.raise_()
        self.button6.raise_()
        self.button8.raise_()
        self.button10.raise_()
        self.button12.raise_()
        self.button7.raise_()
        self.button9.raise_()
        self.button11.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.button2.raise_()
        self.button4.raise_()
        self.label_3.raise_()
        self.textEdit.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 992, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHowdy = QtWidgets.QAction(MainWindow)
        self.actionHowdy.setObjectName("actionHowdy")
        self.actionfile2 = QtWidgets.QAction(MainWindow)
        self.actionfile2.setObjectName("actionfile2")
        self.actionexit = QtWidgets.QAction(MainWindow)
        self.actionexit.setObjectName("actionexit")
        self.actionaudio3 = QtWidgets.QAction(MainWindow)
        self.actionaudio3.setObjectName("actionaudio3")
        self.menuFile.addAction(self.actionHowdy)
        self.actionHowdy.triggered.connect(swapHowdy)
        self.menuFile.addAction(self.actionfile2)
        self.actionfile2.triggered.connect(swapHymn)
        self.menuFile.addAction(self.actionaudio3)
        self.actionaudio3.triggered.connect(swapThird)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.setStyleSheet("""
        QMenuBar {
            background-color: rgb(255, 255, 255);
            color: rgb(255, 255, 255);
        }
        
        QMenuBar::item {
            background-color: rgb(255, 255, 255);
            color: rgb(0,0,0);
        }
        
        QMenuBar::item::selected {
            border: 1px solid #000;
        }
        
        QMenu {
            background-color: rgb(255, 255, 255);
        }
        QMenu::item::selected{
            color: rgb(0, 0, 0);
            border: 1px solid #000;
        }
""")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">AGGIE KEYBOARD</span></p></body></html>"))
        self.menuFile.setTitle(_translate("MainWindow", "Load Audio File"))
        self.actionHowdy.setText(_translate("MainWindow", "Howdy"))
        self.actionfile2.setText(_translate("MainWindow", "Aggie War Hymn"))
        self.actionexit.setText(_translate("MainWindow", "exit"))
        self.actionaudio3.setText(_translate("MainWindow", "Spirit of Aggieland"))

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
