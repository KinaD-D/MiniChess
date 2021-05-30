from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import time
import sys


class Uid_MainWindow(object):

    def ChoiceOfFigure():
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(192, 121)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        centralwidget = QtWidgets.QWidget(MainWindow)
        centralwidget.setObjectName("centralwidget")
        label = QtWidgets.QLabel(centralwidget)
        label.setGeometry(QtCore.QRect(10, 10, 181, 16))
        label.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        label.setObjectName("label")
        pushButton = QtWidgets.QPushButton(centralwidget)
        pushButton.setGeometry(QtCore.QRect(10, 30, 81, 31))
        pushButton.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        pushButton.setObjectName("pushButton")
        pushButton_2 = QtWidgets.QPushButton(centralwidget)
        pushButton_2.setGeometry(QtCore.QRect(100, 30, 81, 31))
        pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        pushButton_2.setObjectName("pushButton_2")
        pushButton_3 = QtWidgets.QPushButton(centralwidget)
        pushButton_3.setGeometry(QtCore.QRect(10, 70, 81, 31))
        pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        pushButton_3.setObjectName("pushButton_3")
        pushButton_4 = QtWidgets.QPushButton(centralwidget)
        pushButton_4.setGeometry(QtCore.QRect(100, 70, 81, 31))
        pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(centralwidget)
        menubar = QtWidgets.QMenuBar(MainWindow)
        menubar.setGeometry(QtCore.QRect(0, 0, 192, 21))
        menubar.setObjectName("menubar")
        MainWindow.setMenuBar(menubar)
        statusbar = QtWidgets.QStatusBar(MainWindow)
        statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(statusbar)

        Uid_MainWindow.retranslateUiOfFigure(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUiOfFigure(MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        label.setText(_translate("MainWindow", "Какую фигуру хотите поставить?"))
        pushButton.setText(_translate("MainWindow", "Конь"))
        pushButton_2.setText(_translate("MainWindow", "Слон"))
        pushButton_3.setText(_translate("MainWindow", "Ферзь"))
        pushButton_4.setText(_translate("MainWindow", "Ладья"))



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(411, 348)

        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 36, 341, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton15 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton15.setObjectName("pushButton15")
        self.gridLayout.addWidget(self.pushButton15, 8, 4, 1, 1)
        self.pushButton36 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton36.setText("")
        self.pushButton36.setObjectName("pushButton36")
        self.gridLayout.addWidget(self.pushButton36, 5, 5, 1, 1)
        self.pushButton86 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton86.setObjectName("pushButton86")
        self.gridLayout.addWidget(self.pushButton86, 0, 5, 1, 1)
        self.pushButton76 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton76.setObjectName("pushButton76")
        self.gridLayout.addWidget(self.pushButton76, 1, 5, 1, 1)
        self.pushButton66 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton66.setText("")
        self.pushButton66.setObjectName("pushButton66")
        self.gridLayout.addWidget(self.pushButton66, 2, 5, 1, 1)
        self.pushButton46 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton46.setText("")
        self.pushButton46.setObjectName("pushButton46")
        self.gridLayout.addWidget(self.pushButton46, 4, 5, 1, 1)
        self.pushButton77 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton77.setObjectName("pushButton77")
        self.gridLayout.addWidget(self.pushButton77, 1, 6, 1, 1)
        self.pushButton16 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton16.setObjectName("pushButton16")
        self.gridLayout.addWidget(self.pushButton16, 8, 5, 1, 1)
        self.pushButton26 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton26.setObjectName("pushButton26")
        self.gridLayout.addWidget(self.pushButton26, 6, 5, 1, 1)
        self.pushButton47 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton47.setText("")
        self.pushButton47.setObjectName("pushButton47")
        self.gridLayout.addWidget(self.pushButton47, 4, 6, 1, 1)
        self.pushButton64 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton64.setText("")
        self.pushButton64.setObjectName("pushButton64")
        self.gridLayout.addWidget(self.pushButton64, 2, 3, 1, 1)
        self.pushButton31 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton31.setText("")
        self.pushButton31.setObjectName("pushButton31")
        self.gridLayout.addWidget(self.pushButton31, 5, 0, 1, 1)
        self.pushButton71 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton71.setObjectName("pushButton71")
        self.gridLayout.addWidget(self.pushButton71, 1, 0, 1, 1)
        self.pushButton54 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton54.setText("")
        self.pushButton54.setObjectName("pushButton54")
        self.gridLayout.addWidget(self.pushButton54, 3, 3, 1, 1)
        self.pushButton27 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton27.setObjectName("pushButton27")
        self.gridLayout.addWidget(self.pushButton27, 6, 6, 1, 1)
        self.pushButton53 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton53.setText("")
        self.pushButton53.setObjectName("pushButton53")
        self.gridLayout.addWidget(self.pushButton53, 3, 2, 1, 1)
        self.pushButton51 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton51.setText("")
        self.pushButton51.setObjectName("pushButton51")
        self.gridLayout.addWidget(self.pushButton51, 3, 0, 1, 1)
        self.pushButton21 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton21.setObjectName("pushButton21")
        self.gridLayout.addWidget(self.pushButton21, 6, 0, 1, 1)
        self.pushButton41 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton41.setText("")
        self.pushButton41.setObjectName("pushButton41")
        self.gridLayout.addWidget(self.pushButton41, 4, 0, 1, 1)
        self.pushButton52 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton52.setText("")
        self.pushButton52.setObjectName("pushButton52")
        self.gridLayout.addWidget(self.pushButton52, 3, 1, 1, 1)
        self.pushButton61 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton61.setText("")
        self.pushButton61.setObjectName("pushButton61")
        self.gridLayout.addWidget(self.pushButton61, 2, 0, 1, 1)
        self.pushButton82 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton82.setObjectName("pushButton82")
        self.gridLayout.addWidget(self.pushButton82, 0, 1, 1, 1)
        self.pushButton22 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton22.setObjectName("pushButton22")
        self.gridLayout.addWidget(self.pushButton22, 6, 1, 1, 1)
        self.pushButton32 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton32.setText("")
        self.pushButton32.setObjectName("pushButton32")
        self.gridLayout.addWidget(self.pushButton32, 5, 1, 1, 1)
        self.pushButton12 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton12.setObjectName("pushButton12")
        self.gridLayout.addWidget(self.pushButton12, 8, 1, 1, 1)
        self.pushButton42 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton42.setText("")
        self.pushButton42.setObjectName("pushButton42")
        self.gridLayout.addWidget(self.pushButton42, 4, 1, 1, 1)
        self.pushButton13 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton13.setObjectName("pushButton13")
        self.gridLayout.addWidget(self.pushButton13, 8, 2, 1, 1)
        self.pushButton62 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton62.setText("")
        self.pushButton62.setObjectName("pushButton62")
        self.gridLayout.addWidget(self.pushButton62, 2, 1, 1, 1)
        self.pushButton17 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton17.setObjectName("pushButton17")
        self.gridLayout.addWidget(self.pushButton17, 8, 6, 1, 1)
        self.pushButton18 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton18.setObjectName("pushButton18")
        self.gridLayout.addWidget(self.pushButton18, 8, 7, 1, 1)
        self.pushButton81 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton81.setObjectName("pushButton81")
        self.gridLayout.addWidget(self.pushButton81, 0, 0, 1, 1)
        self.pushButton28 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton28.setObjectName("pushButton28")
        self.gridLayout.addWidget(self.pushButton28, 6, 7, 1, 1)
        self.pushButton43 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton43.setText("")
        self.pushButton43.setObjectName("pushButton43")
        self.gridLayout.addWidget(self.pushButton43, 4, 2, 1, 1)
        self.pushButton73 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton73.setObjectName("pushButton73")
        self.gridLayout.addWidget(self.pushButton73, 1, 2, 1, 1)
        self.pushButton83 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton83.setObjectName("pushButton83")
        self.gridLayout.addWidget(self.pushButton83, 0, 2, 1, 1)
        self.pushButton33 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton33.setText("")
        self.pushButton33.setObjectName("pushButton33")
        self.gridLayout.addWidget(self.pushButton33, 5, 2, 1, 1)
        self.pushButton23 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton23.setObjectName("pushButton23")
        self.gridLayout.addWidget(self.pushButton23, 6, 2, 1, 1)
        self.pushButton74 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton74.setObjectName("pushButton74")
        self.gridLayout.addWidget(self.pushButton74, 1, 3, 1, 1)
        self.pushButton63 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton63.setText("")
        self.pushButton63.setObjectName("pushButton63")
        self.gridLayout.addWidget(self.pushButton63, 2, 2, 1, 1)
        self.pushButton44 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton44.setText("")
        self.pushButton44.setObjectName("pushButton44")
        self.gridLayout.addWidget(self.pushButton44, 4, 3, 1, 1)
        self.pushButton84 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton84.setObjectName("pushButton84")
        self.gridLayout.addWidget(self.pushButton84, 0, 3, 1, 1)
        self.pushButton72 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton72.setObjectName("pushButton72")
        self.gridLayout.addWidget(self.pushButton72, 1, 1, 1, 1)
        self.pushButton85 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton85.setObjectName("pushButton85")
        self.gridLayout.addWidget(self.pushButton85, 0, 4, 1, 1)
        self.pushButton65 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton65.setText("")
        self.pushButton65.setObjectName("pushButton65")
        self.gridLayout.addWidget(self.pushButton65, 2, 4, 1, 1)
        self.pushButton24 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton24.setObjectName("pushButton24")
        self.gridLayout.addWidget(self.pushButton24, 6, 3, 1, 1)
        self.pushButton14 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton14.setObjectName("pushButton14")
        self.gridLayout.addWidget(self.pushButton14, 8, 3, 1, 1)
        self.pushButton34 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton34.setText("")
        self.pushButton34.setObjectName("pushButton34")
        self.gridLayout.addWidget(self.pushButton34, 5, 3, 1, 1)
        self.pushButton75 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton75.setObjectName("pushButton75")
        self.gridLayout.addWidget(self.pushButton75, 1, 4, 1, 1)
        self.pushButton55 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton55.setText("")
        self.pushButton55.setObjectName("pushButton55")
        self.gridLayout.addWidget(self.pushButton55, 3, 4, 1, 1)
        self.pushButton56 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton56.setText("")
        self.pushButton56.setObjectName("pushButton56")
        self.gridLayout.addWidget(self.pushButton56, 3, 5, 1, 1)
        self.pushButton25 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton25.setObjectName("pushButton25")
        self.gridLayout.addWidget(self.pushButton25, 6, 4, 1, 1)
        self.pushButton35 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton35.setText("")
        self.pushButton35.setObjectName("pushButton35")
        self.gridLayout.addWidget(self.pushButton35, 5, 4, 1, 1)
        self.pushButton57 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton57.setText("")
        self.pushButton57.setObjectName("pushButton57")
        self.gridLayout.addWidget(self.pushButton57, 3, 6, 1, 1)
        self.pushButton78 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton78.setObjectName("pushButton78")
        self.gridLayout.addWidget(self.pushButton78, 1, 7, 1, 1)
        self.pushButton48 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton48.setText("")
        self.pushButton48.setObjectName("pushButton48")
        self.gridLayout.addWidget(self.pushButton48, 4, 7, 1, 1)
        self.pushButton87 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton87.setObjectName("pushButton87")
        self.gridLayout.addWidget(self.pushButton87, 0, 6, 1, 1)
        self.pushButton38 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton38.setText("")
        self.pushButton38.setObjectName("pushButton38")
        self.gridLayout.addWidget(self.pushButton38, 5, 7, 1, 1)
        self.pushButton88 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton88.setObjectName("pushButton88")
        self.gridLayout.addWidget(self.pushButton88, 0, 7, 1, 1)
        self.pushButton11 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton11.setAutoFillBackground(False)
        self.pushButton11.setObjectName("pushButton11")
        self.gridLayout.addWidget(self.pushButton11, 8, 0, 1, 1)
        self.pushButton58 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton58.setText("")
        self.pushButton58.setObjectName("pushButton58")
        self.gridLayout.addWidget(self.pushButton58, 3, 7, 1, 1)
        self.pushButton67 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton67.setText("")
        self.pushButton67.setObjectName("pushButton67")
        self.gridLayout.addWidget(self.pushButton67, 2, 6, 1, 1)
        self.pushButton37 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton37.setText("")
        self.pushButton37.setObjectName("pushButton37")
        self.gridLayout.addWidget(self.pushButton37, 5, 6, 1, 1)
        self.pushButton68 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton68.setText("")
        self.pushButton68.setObjectName("pushButton68")
        self.gridLayout.addWidget(self.pushButton68, 2, 7, 1, 1)
        self.pushButton45 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton45.setText("")
        self.pushButton45.setObjectName("pushButton45")
        self.gridLayout.addWidget(self.pushButton45, 4, 4, 1, 1)



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 280, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 280, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 280, 16, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 280, 16, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 280, 16, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(270, 280, 16, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 280, 16, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(350, 280, 16, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 250, 16, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 220, 16, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 190, 16, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 160, 16, 16))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(30, 130, 16, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(30, 100, 16, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 70, 16, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(30, 40, 16, 16))
        self.label_16.setObjectName("label_16")
        MainWindow.setCentralWidget(self.centralwidget)


        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 411, 21))
        self.menubar.setObjectName("menubar")
        self.menuMiniChess = QtWidgets.QMenu(self.menubar)
        self.menuMiniChess.setObjectName("menuMiniChess")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMiniChess.menuAction())


        self.pushButton11.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton12.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton13.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton14.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton15.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton16.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton17.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton18.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.pushButton21.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton22.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton23.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton24.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton25.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton26.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton27.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton28.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.pushButton31.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton32.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton33.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton34.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton35.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton36.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton37.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton38.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.pushButton41.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton42.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton43.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton44.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton45.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton46.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton47.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton48.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.pushButton51.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton52.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton53.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton54.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton55.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton56.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton57.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton58.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.pushButton61.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton62.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton63.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton64.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton65.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton66.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton67.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton68.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.pushButton71.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton72.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton73.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton74.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton75.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton76.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton77.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton78.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))

        self.pushButton81.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton82.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton83.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton84.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton85.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton86.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton87.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))
        self.pushButton88.setCursor(QtGui.QCursor(QtCore.Qt.ClosedHandCursor))




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton15.setText(_translate("MainWindow", "♔"))
        self.pushButton86.setText(_translate("MainWindow", "♝"))
        self.pushButton76.setText(_translate("MainWindow", "♟️"))
        self.pushButton77.setText(_translate("MainWindow", "♟️"))
        self.pushButton16.setText(_translate("MainWindow", "♗"))
        self.pushButton26.setText(_translate("MainWindow", "♙"))
        self.pushButton71.setText(_translate("MainWindow", "♟️"))
        self.pushButton27.setText(_translate("MainWindow", "♙"))
        self.pushButton21.setText(_translate("MainWindow", "♙"))
        self.pushButton82.setText(_translate("MainWindow", "♞"))
        self.pushButton22.setText(_translate("MainWindow", "♙"))
        self.pushButton12.setText(_translate("MainWindow", "♘"))
        self.pushButton13.setText(_translate("MainWindow", "♗"))
        self.pushButton17.setText(_translate("MainWindow", "♘"))
        self.pushButton18.setText(_translate("MainWindow", "♖"))
        self.pushButton81.setText(_translate("MainWindow", "♜"))
        self.pushButton28.setText(_translate("MainWindow", "♙"))
        self.pushButton73.setText(_translate("MainWindow", "♟️"))
        self.pushButton83.setText(_translate("MainWindow", "♝"))
        self.pushButton23.setText(_translate("MainWindow", "♙"))
        self.pushButton74.setText(_translate("MainWindow", "♟️"))
        self.pushButton84.setText(_translate("MainWindow", "♛"))
        self.pushButton72.setText(_translate("MainWindow", "♟️"))
        self.pushButton85.setText(_translate("MainWindow", "♚"))
        self.pushButton24.setText(_translate("MainWindow", "♙"))
        self.pushButton14.setText(_translate("MainWindow", "♕"))
        self.pushButton75.setText(_translate("MainWindow", "♟️"))
        self.pushButton25.setText(_translate("MainWindow", "♙"))
        self.pushButton78.setText(_translate("MainWindow", "♟️"))
        self.pushButton87.setText(_translate("MainWindow", "♞"))
        self.pushButton88.setText(_translate("MainWindow", "♜"))
        self.pushButton11.setText(_translate("MainWindow", "♖"))


        self.label.setText(_translate("MainWindow", "  A"))
        self.label_2.setText(_translate("MainWindow", "B"))
        self.label_3.setText(_translate("MainWindow", " C"))
        self.label_4.setText(_translate("MainWindow", "  D"))
        self.label_5.setText(_translate("MainWindow", "E"))
        self.label_6.setText(_translate("MainWindow", " F"))
        self.label_7.setText(_translate("MainWindow", " G"))
        self.label_8.setText(_translate("MainWindow", "   H"))
        self.label_9.setText(_translate("MainWindow", "1"))
        self.label_10.setText(_translate("MainWindow", "2"))
        self.label_11.setText(_translate("MainWindow", "3"))
        self.label_12.setText(_translate("MainWindow", "4"))
        self.label_13.setText(_translate("MainWindow", "5"))
        self.label_14.setText(_translate("MainWindow", "6"))
        self.label_15.setText(_translate("MainWindow", "7"))
        self.label_16.setText(_translate("MainWindow", "8"))
        self.menuMiniChess.setTitle(_translate("MainWindow", "MiniChess"))



    def Chess(self):


        MainWindow = QtWidgets.QMainWindow()
        _translate = QtCore.QCoreApplication.translate


        
        check = open('walker.db', 'r')
        check = str(check.readlines())
        print(check)


        if check == '[]' or check == "['white']" or check == "['Black']" or check == "Black'" and QtWidgets.QWidget().sender().text() != '': # Black'

            if check == '[]':
                check = "['white']"

            chel = 9
            chessname = QtWidgets.QWidget().sender().text()
            coords = QtWidgets.QWidget().sender().objectName()

            # White

            if check == "['white']":

                if QtWidgets.QWidget().sender().text() == '♙':
                    chessname = 'white pawn'

                if QtWidgets.QWidget().sender().text() == '♖':
                    chessname = 'white rook'

                if QtWidgets.QWidget().sender().text() == '♘':
                    chessname = 'white horse'

                if QtWidgets.QWidget().sender().text() == '♗':
                    chessname = 'white elephant'

                if QtWidgets.QWidget().sender().text() == '♕':
                    chessname = 'white queen'

                if QtWidgets.QWidget().sender().text() == '♔':
                    chessname = 'white king'

            # Black 

            elif check == "['Black']":

                if QtWidgets.QWidget().sender().text() == '♟️':
                    chessname = 'Black pawn'

                if QtWidgets.QWidget().sender().text() == '♜':
                    chessname = 'Black rook'

                if QtWidgets.QWidget().sender().text() == '♞':
                    chessname = 'Black horse'

                if QtWidgets.QWidget().sender().text() == '♝':
                    chessname = 'Black elephant'

                if QtWidgets.QWidget().sender().text() == '♛':
                    chessname = 'Black queen'

                if QtWidgets.QWidget().sender().text() == '♚':
                    chessname = 'Black king'

            else:
                print('Выбрана фигура другого цвета')
            
            print('Координата x = ', coords[-1], 'Координата y = ', coords[-2])

            print('Внимание, ожидаеться ход ')

            if chessname != QtWidgets.QWidget().sender().text():

                with open('walker.db', 'w') as fileadd:
                    fileadd.write('start as x//' + coords[-1] + '//x y//' + coords[-2] + '//y chessname//' + chessname + '//chessname end')

                QtWidgets.QWidget().sender().setText(_translate("MainWindow", ''))

        else:
            with open('field.db', 'r') as fileadd:
                field = str(fileadd.readlines())

            with open('walker.db', 'r') as fileadd:
                chessname = str(fileadd.readlines())
                print(chessname)

                if chessname != '[]':
                    chessstartx = int(chessname[chessname.find('x//') + 3: chessname.find('//x')])
                    chessstarty = int(chessname[chessname.find('y//') + 3: chessname.find('//y')])

                chessname = chessname[chessname.find('chessname//') + 11: chessname.find('//chessname')]
                chessnamecolor = chessname[:5]
                print(chessnamecolor)
                chessmove = 'UnAllowed'

            coords = QtWidgets.QWidget().sender().objectName()


            print('-->', chessname, '<--')

            if chessname == 'white pawn':
                chessname = '♙'
                chel = QtWidgets.QWidget().sender().text()
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif chel == '♚' or chel == '♛' or chel == '♝' or chel == '♞' or chel == '♜' or chel == '♟️':
                    if int(coords[-2]) - chessstarty == 1 and int(coords[-1]) - chessstartx == 1 or int(coords[-1]) - chessstartx == -1:
                        print('Exelent!')
                        chessmove = 'Allowed'
                        

                    else:
                        chessmove = 'UnAllowed'
                elif int(coords[-2]) == 4 and int(coords[-2]) - chessstarty == 2 and int(coords[-1]) - chessstartx == 0 and field.find('/// location// x/%(xlocation)s/x y/3/y name/' % {'xlocation': chessstartx}) == -1:
                    print('Exelent!')
                    chessmove = 'Allowed'
                elif int(coords[-2]) - chessstarty == 1 and int(coords[-1]) - chessstartx == 0 and chel != '♚' and chel != '♛' and chel != '♝' and chel != '♞' and chel != '♜' and chel != '♟️':
                    print('Exelent!')
                    chessmove = 'Allowed'
                else:
                    chessmove = 'UnAllowed'


                #if int(coords[-2]) == 8 and chessmove == 'Allowed':
                #    Uid_MainWindow.ChoiceOfFigure()
                    


            if chessname == 'white rook':
                chessname = '♖'
                
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'

                elif chessstartx - int(coords[-1]) == 0:
                    print('Exelent!')
                    chessmove = 'Allowed'

                    if chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstarty - int(coords[-2])):
                            print(chessstartx, chessstarty - i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'
                                print(chessstartx, chessstarty - i, 'here here here')

                    else:
                        for i in range(1, int(coords[-2]) - chessstarty):
                            print(chessstartx, chessstarty + i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                elif chessstarty - int(coords[-2]) == 0:
                    print('Exelent!')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            print(chessstartx - i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed'

                    else:
                        for i in range(1, int(coords[-1]) - chessstartx):
                            print(chessstartx + i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed' 

                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'white horse':
                chessname = '♘'
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif (int(coords[-1]) - chessstartx) * (int(coords[-2]) - chessstarty) == 2 or (int(coords[-1]) - chessstartx) * (int(coords[-2]) - chessstarty) == -2:
                    print('Exelent')
                    chessmove = 'Allowed'
                else:
                    chessmove = 'UnAllowed'

                
            elif chessname == 'white elephant':
                chessname = '♗'
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif int(coords[-2]) - chessstarty == 0 or int(coords[-1]) - chessstartx == 0:
                    chessmove = 'UnAllowed'
                    print('...')
                elif (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == 1 or (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == -1:
                    print('Exelent')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'

                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'white queen':
                chessname = '♕'
                
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif chessstartx - int(coords[-1]) == 0 or chessstarty - int(coords[-2]) == 0:
                    print('Exelent')
                    chessmove = 'Allowed'

                    if chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstarty - int(coords[-2])):
                            print(chessstartx, chessstarty - i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'
                                print(chessstartx, chessstarty - i, 'here here here')

                    else:
                        for i in range(1, int(coords[-2]) - chessstarty):
                            print(chessstartx, chessstarty + i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                elif chessstarty - int(coords[-2]) == 0:
                    print('Exelent!')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            print(chessstartx - i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed'

                    else:
                        for i in range(1, int(coords[-1]) - chessstartx):
                            print(chessstartx + i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed' 

                elif (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == 1 or (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == -1:
                    print('Exelent')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'
                                
                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'white king':
                chessname = '♔'
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif int(coords[-1]) - chessstartx >= -1 and int(coords[-1]) - chessstartx <= 1 and int(coords[-2]) - chessstarty >= -1 and int(coords[-2]) - chessstarty <= 1:
                    print('Exelent')
                    chessmove = 'Allowed' 

                else:
                    chessmove = 'UnAllowed'


            # Black 

            elif chessname == 'Black pawn':
                chessname = '♟️'
                chel = QtWidgets.QWidget().sender().text()
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif chel == '♖' or chel == '♘' or chel == '♗' or chel == '♕' or chel == '♔' or chel == '♙':
                    if int(coords[-2]) - chessstarty == -1 and int(coords[-1]) - chessstartx == 1 or int(coords[-1]) - chessstartx == -1:
                        print('Exelent!')
                        chessmove = 'Allowed'
                elif int(coords[-2]) == 5 and int(coords[-2]) - chessstarty == -2 and int(coords[-1]) - chessstartx == 0 and field.find('/// location// x/%(xlocation)s/x y/6/y name/' % {'xlocation': chessstartx}) == -1:
                    print('Exelent!')
                    chessmove = 'Allowed'
                elif int(coords[-2]) - chessstarty == -1 and int(coords[-1]) - chessstartx == 0 and chel != '♖' and chel != '♘' and chel != '♗' and chel != '♕' and chel != '♔' and chel != '♙':
                    print('Exelent!')
                    chessmove = 'Allowed'
                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'Black rook':
                chessname = '♜'
                
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'

                elif chessstartx - int(coords[-1]) == 0:
                    print('Exelent!')
                    chessmove = 'Allowed'

                    if chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstarty - int(coords[-2])):
                            print(chessstartx, chessstarty - i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'
                                print(chessstartx, chessstarty - i, 'here here here')

                    else:
                        for i in range(1, int(coords[-2]) - chessstarty):
                            print(chessstartx, chessstarty + i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                elif chessstarty - int(coords[-2]) == 0:
                    print('Exelent!')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            print(chessstartx - i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed'

                    else:
                        for i in range(1, int(coords[-1]) - chessstartx):
                            print(chessstartx + i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed' 

                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'Black horse':
                chessname = '♞'
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif (int(coords[-1]) - chessstartx) * (int(coords[-2]) - chessstarty) == 2 or (int(coords[-1]) - chessstartx) * (int(coords[-2]) - chessstarty) == -2:
                    print('Exelent')
                    chessmove = 'Allowed'
                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'Black elephant':
                chessname = '♝'
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif int(coords[-2]) - chessstarty == 0 or int(coords[-1]) - chessstartx == 0:
                    chessmove = 'UnAllowed'
                    print('...')
                elif (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == 1 or (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == -1:
                    print('Exelent')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'

                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'Black queen':
                chessname = '♛'
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif chessstartx - int(coords[-1]) == 0 or chessstarty - int(coords[-2]) == 0:
                    print('Exelent')
                    chessmove = 'Allowed'

                    if chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstarty - int(coords[-2])):
                            print(chessstartx, chessstarty - i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'
                                print(chessstartx, chessstarty - i, 'here here here')

                    else:
                        for i in range(1, int(coords[-2]) - chessstarty):
                            print(chessstartx, chessstarty + i)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                elif chessstarty - int(coords[-2]) == 0:
                    print('Exelent!')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            print(chessstartx - i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed'

                    else:
                        for i in range(1, int(coords[-1]) - chessstartx):
                            print(chessstartx + i, chessstarty)
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty}) != -1:
                                chessmove = 'UnAllowed' 

                elif (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == 1 or (int(coords[-1]) - chessstartx) / (int(coords[-2]) - chessstarty) == -1:
                    print('Exelent')
                    chessmove = 'Allowed'

                    if chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) > 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1])):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx - i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) < 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty + i}) != -1:
                                chessmove = 'UnAllowed'

                    elif chessstartx - int(coords[-1]) < 0 and chessstarty - int(coords[-2]) > 0:
                        for i in range(1, chessstartx - int(coords[-1]) * -1):
                            if field.find('/// location// x/%(xlocation)s/x y/%(ylocation)s/y name/' % {'xlocation': chessstartx + i, 'ylocation': chessstarty - i}) != -1:
                                chessmove = 'UnAllowed'

                else:
                    chessmove = 'UnAllowed'


            elif chessname == 'Black king':
                chessname = '♚'
                if chessstarty - int(coords[-2]) == 0 and chessstartx - int(coords[-1]) == 0:
                    chessmove = 'Staying'
                elif int(coords[-1]) - chessstartx >= -1 and int(coords[-1]) - chessstartx <= 1 and int(coords[-2]) - chessstarty >= -1 and int(coords[-2]) - chessstarty <= 1:
                    print('Exelent')
                    chessmove = 'Allowed'
                else:
                    chessmove = 'UnAllowed'


            print(chessname)


            # Защита от битья своих
            if chessname == '♖' or chessname == '♘' or chessname == '♗' or chessname == '♕' or chessname == '♔' or chessname == '♙':
                chel = QtWidgets.QWidget().sender().text()
                if chel == '♖' or chel == '♘' or chel == '♗' or chel == '♕' or chel == '♔' or chel == '♙':
                    chessmove = 'UnAllowed'
                if chel == '♚':
                    print('Чёрные победили! ')
                    for i in range(1, 5):
                        print('Закрытие через', 5 - i, 'сек')
                        time.sleep(1)
                    sys.exit()


            if chessname == '♚' or chessname == '♛' or chessname == '♝' or chessname == '♞' or chessname == '♜' or chessname == '♟️':
                chel = QtWidgets.QWidget().sender().text()
                if chel == '♚' or chel == '♛' or chel == '♝' or chel == '♞' or chel == '♜' or chel == '♟️':
                    chessmove = 'UnAllowed'
                if chel == '♚':
                    print('Чёрные победили! ')
                    for i in range(1, 5):
                        print('Закрытие через', 5 - i, 'сек')
                        time.sleep(1)
                    sys.exit()

            if chessnamecolor == 'white':
                chessnamecolor = 'Black'
            elif chessnamecolor == 'Black':
                chessnamecolor = 'white'

            if chessmove == 'Staying' and chessnamecolor == 'white':
                chessnamecolor = 'Black'
            elif chessmove == 'Staying' and chessnamecolor == 'Black':
                chessnamecolor = 'white'


            if chessmove == 'Allowed' or chessmove == 'Staying':

                if QtWidgets.QWidget().sender().text() == '♔':
                    print('Чёрные победили!')
                if QtWidgets.QWidget().sender().text() == '♚':
                    print('Белые победили!')

                QtWidgets.QWidget().sender().setText(_translate("MainWindow", '%(chessname)s' % {"chessname": chessname}))

                with open('walker.db', 'w') as fileadd:
                    fileadd.write(chessnamecolor)


            if chessmove == 'Allowed':

                with open('field.db', 'r') as fileadd:
                    field = str(fileadd.readlines())

                    namer = field[field.find('x/%(xlocation)s/x y/%(ylocation)s/y' % {'xlocation': chessstartx, 'ylocation': chessstarty}) + 12: field.find('x/%(xlocation)s/x y/%(ylocation)s/y' % {'xlocation': chessstartx, 'ylocation': chessstarty}) + 37]
                    namer = namer[namer.find('name/') + 5: namer.find('/name')]

                    variable = ' %(name)s/// location// x/%(xlocation)s/x y/%(ylocation)s/y' % {'name': namer ,'xlocation': int(coords[-1]), 'ylocation': int(coords[-2])}

                    before = field[: field.find('%(name)s///' % {'name': namer})]
                    after = field[field.find('///%(name)s' % {'name': namer}) + 3 + len(namer):]

                    retraim = 'previouslocation// x/%(previouslocationx)s/x y/%(previouslocationy)s/y //previouslocation' % {'previouslocationx': chessstartx, 'previouslocationy': chessstarty}

                    namer = field[field.find('%(name)s///' % {'name': namer}): field.find('///%(name)s' % {'name': namer}) + 3 + len(namer)]
                    namer = namer[: namer.find('previouslocation//')] + retraim + namer[namer.find('//previouslocation') + 18:]
                    print(before, '   <--   ', namer, '   -->   ', after)

                    namer = variable + namer[namer.find('/y name/') + 2:]

                    # YAY (☞ﾟヮﾟ)☞ ☜(⌒▽⌒)☞  ☜(ﾟヮﾟ☜) YAY

                with open('field.db', 'w') as filedd:
                    before = before[before.find('WhiteRook1///'):]
                    after = after[: after.find('///BlackRook8') + 13]
                    filedd.write(before + namer + after)



open('walker.db', 'w')
with open('field.db', 'w') as fileadd:

    fileadd.write(' WhiteRook1/// location// x/1/x y/1/y name/WhiteRook1/name //location previouslocation// none //previouslocation ///WhiteRook1 ')
    fileadd.write(' WhiteRook2/// location// x/8/x y/1/y name/WhiteRook2/name //location previouslocation// none //previouslocation ///WhiteRook2 ')
    fileadd.write(' BlackRook1/// location// x/1/x y/8/y name/BlackRook1/name //location previouslocation// none //previouslocation ///BlackRook1 ')
    fileadd.write(' BlackRook2/// location// x/8/x y/8/y name/BlackRook2/name //location previouslocation// none //previouslocation ///BlackRook2 ')

    fileadd.write(' WhiteHorse1/// location// x/2/x y/1/y name/WhiteHorse1/name //location previouslocation// none //previouslocation ///WhiteHorse1 ')
    fileadd.write(' WhiteHorse2/// location// x/7/x y/1/y name/WhiteHorse2/name //location previouslocation// none //previouslocation ///WhiteHorse2 ')
    fileadd.write(' BlackHorse1/// location// x/2/x y/8/y name/BlackHorse1/name //location previouslocation// none //previouslocation ///BlackHorse1 ')
    fileadd.write(' BlackHorse2/// location// x/7/x y/8/y name/BlackHorse2/name //location previouslocation// none //previouslocation ///BlackHorse2 ')

    fileadd.write(' WhiteElephant1/// location// x/3/x y/1/y name/WhiteElephant1/name //location previouslocation// none //previouslocation ///WhiteElephant1 ')
    fileadd.write(' WhiteElephant2/// location// x/6/x y/1/y name/WhiteElephant2/name //location previouslocation// none //previouslocation ///WhiteElephant2 ')
    fileadd.write(' BlackElephant1/// location// x/3/x y/8/y name/BlackElephant1/name //location previouslocation// none //previouslocation ///BlackElephant1 ')
    fileadd.write(' BlackElephant2/// location// x/6/x y/8/y name/BlackElephant2/name //location previouslocation// none //previouslocation ///BlackElephant2 ')

    fileadd.write(' WhiteQueen1/// location// x/4/x y/1/y name/WhiteQueen1/name //location previouslocation// none //previouslocation ///WhiteQueen1 ')
    fileadd.write(' BlackQueen1/// location// x/4/x y/8/y name/BlackQueen1/name //location previouslocation// none //previouslocation ///BlackQueen1 ')

    fileadd.write(' BlackKing/// location// x/5/x y/8/y name/BlackKing/name //location previouslocation// none //previouslocation ///BlackKing ')
    fileadd.write(' WhiteKing/// location// x/5/x y/1/y name/WhiteKing/name //location previouslocation// none //previouslocation ///WhiteKing ')


    fileadd.write(' WhitePawn1/// location// x/1/x y/2/y name/WhitePawn1/name //location previouslocation// none //previouslocation ///WhitePawn1 ')
    fileadd.write(' WhitePawn2/// location// x/2/x y/2/y name/WhitePawn2/name //location previouslocation// none //previouslocation ///WhitePawn2 ')
    fileadd.write(' WhitePawn3/// location// x/3/x y/2/y name/WhitePawn3/name //location previouslocation// none //previouslocation ///WhitePawn3 ')
    fileadd.write(' WhitePawn4/// location// x/4/x y/2/y name/WhitePawn4/name //location previouslocation// none //previouslocation ///WhitePawn4 ')
    fileadd.write(' WhitePawn5/// location// x/5/x y/2/y name/WhitePawn5/name //location previouslocation// none //previouslocation ///WhitePawn5 ')
    fileadd.write(' WhitePawn6/// location// x/6/x y/2/y name/WhitePawn6/name //location previouslocation// none //previouslocation ///WhitePawn6 ')
    fileadd.write(' WhitePawn7/// location// x/7/x y/2/y name/WhitePawn7/name //location previouslocation// none //previouslocation ///WhitePawn7 ')
    fileadd.write(' WhitePawn8/// location// x/8/x y/2/y name/WhitePawn8/name //location previouslocation// none //previouslocation ///WhitePawn8 ')

    fileadd.write(' BlackRook1/// location// x/1/x y/7/y name/BlackRook1/name //location previouslocation// none //previouslocation ///BlackRook1 ')
    fileadd.write(' BlackRook2/// location// x/2/x y/7/y name/BlackRook2/name //location previouslocation// none //previouslocation ///BlackRook2 ')
    fileadd.write(' BlackRook3/// location// x/3/x y/7/y name/BlackRook3/name //location previouslocation// none //previouslocation ///BlackRook3 ')
    fileadd.write(' BlackRook4/// location// x/4/x y/7/y name/BlackRook4/name //location previouslocation// none //previouslocation ///BlackRook4 ')
    fileadd.write(' BlackRook5/// location// x/5/x y/7/y name/BlackRook5/name //location previouslocation// none //previouslocation ///BlackRook5 ')
    fileadd.write(' BlackRook6/// location// x/6/x y/7/y name/BlackRook6/name //location previouslocation// none //previouslocation ///BlackRook6 ')
    fileadd.write(' BlackRook7/// location// x/7/x y/7/y name/BlackRook7/name //location previouslocation// none //previouslocation ///BlackRook7 ')
    fileadd.write(' BlackRook8/// location// x/8/x y/7/y name/BlackRook8/name //location previouslocation// none //previouslocation ///BlackRook8 ')


while True:
    if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)

        MainWindow.show()

        



        ui.pushButton11.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton12.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton13.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton14.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton15.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton16.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton17.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton18.clicked.connect(Ui_MainWindow.Chess)


        ui.pushButton21.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton22.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton23.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton24.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton25.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton26.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton27.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton28.clicked.connect(Ui_MainWindow.Chess)


        ui.pushButton31.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton32.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton33.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton34.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton35.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton36.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton37.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton38.clicked.connect(Ui_MainWindow.Chess)


        ui.pushButton41.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton42.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton43.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton44.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton45.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton46.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton47.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton48.clicked.connect(Ui_MainWindow.Chess)


        ui.pushButton51.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton52.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton53.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton54.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton55.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton56.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton57.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton58.clicked.connect(Ui_MainWindow.Chess)


        ui.pushButton61.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton62.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton63.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton64.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton65.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton66.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton67.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton68.clicked.connect(Ui_MainWindow.Chess)


        ui.pushButton71.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton72.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton73.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton74.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton75.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton76.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton77.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton78.clicked.connect(Ui_MainWindow.Chess)


        ui.pushButton81.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton82.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton83.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton84.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton85.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton86.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton87.clicked.connect(Ui_MainWindow.Chess)
        ui.pushButton88.clicked.connect(Ui_MainWindow.Chess)


        sys.exit(app.exec_())
