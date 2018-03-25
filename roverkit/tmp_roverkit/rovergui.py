# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rovergui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Rover(object):
    def setupUi(self, Rover):
        Rover.setObjectName(_fromUtf8("Rover"))
        Rover.resize(800, 600)
        self.centralwidget = QtGui.QWidget(Rover)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.throttle_slider = QtGui.QSlider(self.centralwidget)
        self.throttle_slider.setGeometry(QtCore.QRect(10, 20, 29, 160))
        self.throttle_slider.setMinimum(-10)
        self.throttle_slider.setMaximum(10)
        self.throttle_slider.setOrientation(QtCore.Qt.Vertical)
        self.throttle_slider.setInvertedAppearance(False)
        self.throttle_slider.setInvertedControls(True)
        self.throttle_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.throttle_slider.setTickInterval(1)
        self.throttle_slider.setObjectName(_fromUtf8("throttle_slider"))
        self.connect_rover = QtGui.QPushButton(self.centralwidget)
        self.connect_rover.setGeometry(QtCore.QRect(690, 10, 99, 41))
        self.connect_rover.setObjectName(_fromUtf8("connect_rover"))
        self.steering_slider = QtGui.QSlider(self.centralwidget)
        self.steering_slider.setGeometry(QtCore.QRect(60, 20, 29, 160))
        self.steering_slider.setMinimum(-10)
        self.steering_slider.setMaximum(10)
        self.steering_slider.setOrientation(QtCore.Qt.Vertical)
        self.steering_slider.setInvertedAppearance(False)
        self.steering_slider.setInvertedControls(True)
        self.steering_slider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.steering_slider.setTickInterval(1)
        self.steering_slider.setObjectName(_fromUtf8("steering_slider"))
        self.videoframe = QtGui.QFrame(self.centralwidget)
        self.videoframe.setGeometry(QtCore.QRect(120, 60, 541, 401))
        self.videoframe.setFrameShape(QtGui.QFrame.StyledPanel)
        self.videoframe.setFrameShadow(QtGui.QFrame.Raised)
        self.videoframe.setObjectName(_fromUtf8("videoframe"))
        Rover.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(Rover)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        Rover.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(Rover)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Rover.setStatusBar(self.statusbar)

        self.retranslateUi(Rover)
        QtCore.QMetaObject.connectSlotsByName(Rover)

    def retranslateUi(self, Rover):
        Rover.setWindowTitle(_translate("Rover", "MainWindow", None))
        self.connect_rover.setText(_translate("Rover", "Connect", None))

