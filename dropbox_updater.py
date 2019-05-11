from PyQt5 import QtCore, QtGui, QtWidgets
import dropbox
from dropbox.files import WriteMode
import sys

dpb= dropbox.Dropbox('ueOY-W077NAAAAAAAAAAC8Tu8-9Ukc86kDebBzROFKGcOttE68SYe6V-x427Yz5C')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        def update_files():
                try:
                        file1 = open('dropbox_files/articoli.DBF','rb')
                        file2 = open('dropbox_files/lista.csv','rb')
                except FileNotFoundError:
                        print('Errore: files non trovati!')
                try:
                        dpb.files_upload(file1.read(),'/user1/articoli.DBF',mute=True,mode=dropbox.files.WriteMode.overwrite)
                        dpb.files_upload(file2.read(),'/user1/lista.csv',mute=True,mode=dropbox.files.WriteMode.overwrite)
                except:
                        print('Error: files not updated!')
                finally:
                        file1.close()
                        file2.close()
        
        def open_dropbox():
                import webbrowser
                webbrowser.open('https://www.dropbox.com')
        
        def exit():
                sys.exit()

        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(400, 380)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(400, 380))
        MainWindow.setMaximumSize(QtCore.QSize(400, 380))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/dpb1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(-40, -40, 441, 591))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setStyleSheet("QLabel#background{\n"
"      background-color: #ffffff;\n"
"\n"
"}")
        self.background.setText("")
        self.background.setObjectName("background")
        self.update = QtWidgets.QPushButton(self.centralwidget)
        self.update.setGeometry(QtCore.QRect(110, 220, 171, 61))
        self.update.setStyleSheet("QPushButton#update{\n"
"    background-color: #3098e8;\n"
"    border-radius: 20px;\n"
"    color: #ffffff;\n"
"    font-family: \'Signika,sans-serif\';\n"
"    font-size: 15px;\n"
"    z-index: 1;\n"
"}\n"
"\n"
"QPushButton#update:hover{\n"
"    background-color: #4aacf7;\n"
"}")
        self.update.setObjectName("update")
        self.header = QtWidgets.QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(10, 10, 371, 171))
        self.header.setStyleSheet("QLabel#header{\n"
"     background-image: url(update.png);\n"
"\n"
"}")
        self.header.setText("")
        self.header.setPixmap(QtGui.QPixmap("images/uploader1.png"))
        self.header.setObjectName("header")
        self.dropbox = QtWidgets.QPushButton(self.centralwidget)
        self.dropbox.setGeometry(QtCore.QRect(20, 220, 71, 61))
        self.dropbox.setToolTip("")
        self.dropbox.setToolTipDuration(1)
        self.dropbox.setStyleSheet("QPushButton#dropbox{\n"
"     background-color: #3098e8;\n"
"     border-radius: 15px;\n"
"     border: solid 1px;\n"
"     color: #ffffff;\n"
"     font-family: sans-serif;\n"
"    font-size: 15px;\n"
"    z-index: 1;\n"
"}\n"
"\n"
"\n"
"QPushButton#dropbox:hover{\n"
"    background-color: #4aacf7;\n"
"}")
        self.dropbox.setObjectName("dropbox")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(300, 220, 71, 61))
        self.exit.setStyleSheet("QPushButton#exit{\n"
"     background-color: #3098e8;\n"
"     border-radius: 15px;\n"
"     border: solid 1px;\n"
"     color: #ffffff;\n"
"     font-family: sans-serif;\n"
"    font-size: 15px;\n"
"    z-index: 1;\n"
"}\n"
"\n"
"\n"
"QPushButton#exit:hover{\n"
"    background-color: #4aacf7;\n"
"}")
        self.exit.setObjectName("exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #connect buttons to functions
        self.update.clicked.connect(update_files)
        self.dropbox.clicked.connect(open_dropbox)
        self.exit.clicked.connect(exit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dropbox Updater"))
        self.update.setText(_translate("MainWindow", "Aggiorna files"))
        self.dropbox.setText(_translate("MainWindow", "Dropbox"))
        self.exit.setText(_translate("MainWindow", "Uscita"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

