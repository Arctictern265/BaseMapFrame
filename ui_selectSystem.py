# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'selectSystem.ui'
#
# Created: Sat Jun 01 19:22:42 2013
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_DialogSelectSystem(object):
    def setupUi(self, DialogSelectSystem):
        DialogSelectSystem.setObjectName(_fromUtf8("DialogSelectSystem"))
        DialogSelectSystem.resize(199, 205)
        self.verticalLayout = QtGui.QVBoxLayout(DialogSelectSystem)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.groupBox = QtGui.QGroupBox(DialogSelectSystem)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.radioButton_2500 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2500.setObjectName(_fromUtf8("radioButton_2500"))
        self.verticalLayout_2.addWidget(self.radioButton_2500)
        self.radioButton_5000 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_5000.setObjectName(_fromUtf8("radioButton_5000"))
        self.verticalLayout_2.addWidget(self.radioButton_5000)
        self.radioButton_2nd = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2nd.setObjectName(_fromUtf8("radioButton_2nd"))
        self.verticalLayout_2.addWidget(self.radioButton_2nd)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(DialogSelectSystem)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox_system = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_system.setObjectName(_fromUtf8("comboBox_system"))
        self.horizontalLayout.addWidget(self.comboBox_system)
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.buttonBox = QtGui.QDialogButtonBox(DialogSelectSystem)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(DialogSelectSystem)
        self.comboBox_system.setCurrentIndex(-1)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), DialogSelectSystem.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), DialogSelectSystem.reject)
        QtCore.QObject.connect(self.radioButton_2nd, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogSelectSystem.onCheck2nd)
        QtCore.QObject.connect(self.radioButton_5000, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogSelectSystem.onCheck5000)
        QtCore.QObject.connect(self.radioButton_2500, QtCore.SIGNAL(_fromUtf8("clicked()")), DialogSelectSystem.onCheck2500)
        QtCore.QMetaObject.connectSlotsByName(DialogSelectSystem)

    def retranslateUi(self, DialogSelectSystem):
        DialogSelectSystem.setWindowTitle(QtGui.QApplication.translate("DialogSelectSystem", "国土基本図郭プラグイン", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("DialogSelectSystem", "図葉", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2500.setText(QtGui.QApplication.translate("DialogSelectSystem", "2,500分の１", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_5000.setText(QtGui.QApplication.translate("DialogSelectSystem", "5,000分の１", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2nd.setText(QtGui.QApplication.translate("DialogSelectSystem", "二次メッシュ", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("DialogSelectSystem", "平面直角座標系", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("DialogSelectSystem", "系", None, QtGui.QApplication.UnicodeUTF8))

