from PyQt5 import QtCore, QtGui, QtWidgets
import os

directory = os.getcwd()

class Cryptor:
		text = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~','\n']
		key = ["Contact developer for keys"]
		def enc(inpt):
			return ''.join([Cryptor.key[Cryptor.text.index(tol)] for tol in inpt if tol in Cryptor.text])
		def dec(inpt):
			de = [inpt[d:d+5] for d in range(0, len(inpt), 5)]
			return ''.join([Cryptor.text[Cryptor.key.index(dr)] for dr in de if dr in Cryptor.key])

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 408)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{directory}/logotk.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.data = 'Encrypt'
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
# =============================================================================================================================
        self.messagebox = QtWidgets.QTextEdit(self.centralwidget)
        self.messagebox.setGeometry(QtCore.QRect(10, 70, 391, 131))
        self.messagebox.setObjectName("messagebox")
# =============================================================================================================================        
        self.outputbox = QtWidgets.QTextEdit(self.centralwidget)
        self.outputbox.setGeometry(QtCore.QRect(10, 240, 291, 131))
        self.outputbox.setObjectName("outputbox")
# =============================================================================================================================        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 261, 41))
        self.label.setObjectName("label")
# =============================================================================================================================        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 200, 201, 41))
        self.label_2.setObjectName("label_2")
# =============================================================================================================================        
        self.Choose = QtWidgets.QComboBox(self.centralwidget)
        self.Choose.setGeometry(QtCore.QRect(280, 40, 121, 22))
        self.Choose.setObjectName("Choose")
        self.Choose.addItem('Encrypt')
        self.Choose.addItem('Decrypt')
        self.Choose.activated[str].connect(self.onPressed)
# =============================================================================================================================        
        self.crypt = QtWidgets.QPushButton(self.centralwidget)  # Cryptor Button
        self.crypt.setGeometry(QtCore.QRect(310, 330, 91, 31))
        self.crypt.setObjectName("crypt")
        self.crypt.clicked.connect(self.onChanged)
# =============================================================================================================================        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 0, 241, 41))
        self.label_3.setAutoFillBackground(False)
        self.label_3.setObjectName("label_3")
# =============================================================================================================================        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(310, 240, 91, 75))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
# =============================================================================================================================
        self.pushButton = QtWidgets.QPushButton(self.widget)   # Clear Button
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clear)
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Cryptor"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Enter Your Message Below</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ff0004;\">Generated Output</span></p></body></html>"))
        self.crypt.setText(_translate("MainWindow", "C R Y P T"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#3300ff;\">GhosTmaN EnCryption</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#3f7f00;\">Click here to</span></p><p><span style=\" font-size:10pt; font-weight:600; color:#3f7f00;\">clear Screen</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Clear"))

    def onPressed(self,text):
        self.data = text

    def onChanged(self):
        text = self.messagebox.toPlainText()
        if self.data == "Encrypt":
            self.outputbox.setPlainText(Cryptor.enc(text))
        elif self.data == "Decrypt":
            self.outputbox.setPlainText(Cryptor.dec(text))
    def clear(self):
        self.messagebox.setPlainText('')
        self.outputbox.setPlainText('')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
