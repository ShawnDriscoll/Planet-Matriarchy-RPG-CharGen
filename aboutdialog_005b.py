# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutdialog_005b.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_aboutDialog(object):
    def setupUi(self, aboutDialog):
        aboutDialog.setObjectName("aboutDialog")
        aboutDialog.resize(480, 357)
        aboutDialog.setMinimumSize(QtCore.QSize(480, 357))
        aboutDialog.setMaximumSize(QtCore.QSize(480, 357))
        self.aboutOKButton = QtWidgets.QPushButton(aboutDialog)
        self.aboutOKButton.setGeometry(QtCore.QRect(380, 320, 75, 23))
        self.aboutOKButton.setObjectName("aboutOKButton")
        self.textLabel = QtWidgets.QLabel(aboutDialog)
        self.textLabel.setGeometry(QtCore.QRect(140, 20, 321, 261))
        self.textLabel.setTextFormat(QtCore.Qt.RichText)
        self.textLabel.setScaledContents(False)
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setOpenExternalLinks(True)
        self.textLabel.setObjectName("textLabel")
        self.line = QtWidgets.QFrame(aboutDialog)
        self.line.setGeometry(QtCore.QRect(137, 210, 321, 20))
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.retranslateUi(aboutDialog)
        QtCore.QMetaObject.connectSlotsByName(aboutDialog)

    def retranslateUi(self, aboutDialog):
        _translate = QtCore.QCoreApplication.translate
        aboutDialog.setWindowTitle(_translate("aboutDialog", "About EFPM CharGen"))
        self.aboutOKButton.setText(_translate("aboutDialog", "OK"))
        self.textLabel.setText(_translate("aboutDialog", "<html><head/><body><p><span style=\" font-weight:600;\">EFPM CharGen for Windows 10</span></p><p>Version: Total Party Skills Edition</p><p>Build: 0.0.5 (Beta)</p><p>Produced by Shawn Driscoll. Copyright (C) 2021.</p><p>Visit blog at <a href=\"http://shawndriscoll.blogspot.com\"><span style=\" text-decoration: underline; color:#0000ff;\">shawndriscoll.blogspot.com</span></a><br/>For support, email <a href=\"mailto:shawndriscoll@hotmail.com?subject=EFPM CharGen 0.0.5b\"><span style=\" text-decoration: underline; color:#0000ff;\">shawndriscoll@hotmail.com</span></a></p><p>Qt GUI Toolkit is copyright (C) 2020 The Qt Company Ltd</p><p><br/></p><p>The Escape from Planet Matriarchy RPG was written by R. Joshua Holland. Copyright 2021 - 2022, Total Party Skills.</p></body></html>"))
