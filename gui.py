# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 425)
        MainWindow.setMinimumSize(QtCore.QSize(400, 425))
        MainWindow.setMaximumSize(QtCore.QSize(400, 425))
        MainWindow.setMouseTracking(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.windowHeading = QtWidgets.QLabel(parent=self.centralwidget)
        self.windowHeading.setGeometry(QtCore.QRect(140, 0, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.windowHeading.setFont(font)
        self.windowHeading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.windowHeading.setObjectName("windowHeading")
        self.first_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.first_name.setGeometry(QtCore.QRect(180, 80, 181, 21))
        self.first_name.setObjectName("first_name")
        self.last_name = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.last_name.setGeometry(QtCore.QRect(180, 110, 181, 21))
        self.last_name.setObjectName("last_name")
        self.first_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.first_name_label.setGeometry(QtCore.QRect(40, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.first_name_label.setFont(font)
        self.first_name_label.setObjectName("first_name_label")
        self.last_name_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.last_name_label.setGeometry(QtCore.QRect(40, 110, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.last_name_label.setFont(font)
        self.last_name_label.setObjectName("last_name_label")
        self.score = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.score.setGeometry(QtCore.QRect(290, 150, 71, 21))
        self.score.setObjectName("score")
        self.score_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(110, 150, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.score_label.setFont(font)
        self.score_label.setObjectName("score_label")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 340, 91, 31))
        self.pushButton.setObjectName("submit_button")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 340, 91, 31))
        self.pushButton_2.setObjectName("view_button")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 340, 91, 31))
        self.pushButton_3.setObjectName("clear_button")
        self.message = QtWidgets.QLabel(parent=self.centralwidget)
        self.message.setGeometry(QtCore.QRect(20, 30, 361, 41))
        self.message.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.message.setObjectName("message")
        self.final_result = QtWidgets.QLabel(parent=self.centralwidget)
        self.final_result.setGeometry(QtCore.QRect(30, 180, 341, 141))
        self.final_result.setText("")
        self.final_result.setObjectName("final_result")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grade Calculator"))
        self.windowHeading.setText(_translate("MainWindow", "Grade Calculator"))
        self.first_name_label.setText(_translate("MainWindow", "First Name:"))
        self.last_name_label.setText(_translate("MainWindow", "Last Name:"))
        self.score_label.setText(_translate("MainWindow", "Enter Student\'s Score:"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.pushButton_2.setText(_translate("MainWindow", "View Results"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear All Data"))
        self.message.setText(_translate("MainWindow", "Enter a student\'s name and score and click \"Submit\"\n"
"To see the final results of all students, click \"View Results\"\n"
"To clear all student names and scores, click \"Clear All Data\""))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
