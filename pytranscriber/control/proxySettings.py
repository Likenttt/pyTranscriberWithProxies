from PyQt5 import QtCore, QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog, QFileDialog, QMessageBox,QLineEdit
from PyQt5.QtCore import Qt
from pathlib import Path
from pytranscriber.model.param_autosub import Param_Autosub
from pytranscriber.util.util import MyUtil
from pytranscriber.control.thread_exec_autosub import Thread_Exec_Autosub
from pytranscriber.control.thread_cancel_autosub import Thread_Cancel_Autosub
import os
from PyQt5.QtGui import QIntValidator

class ProxySettingsWindow(object):
    def setupUi(self, dialog):
        proxySettingsFilePath = Path.home() / 'pyTranscriber_proxy_settings.json'
        dialog.setObjectName("proxyDialog")

        dialog.resize(577, 169)

        self.centralDialog = QtWidgets.QWidget(dialog)
        self.centralDialog.setObjectName("centralDialog")

        self.httpProxyLabel = QtWidgets.QLabel(self.centralDialog)
        self.httpProxyLabel.setGeometry(QtCore.QRect(20, 10, 531, 16))
        self.httpProxyLabel.setText("")
        self.httpProxyLabel.setObjectName("httpProxyLabel")

        self.httpPrefixEditor = QLineEdit(self.centralDialog)
        self.httpPrefixEditor.setGeometry(QtCore.QRect(20, 30, 121, 21))
        self.httpPrefixEditor.setText("socks5://127.0.0.1:")
        self.httpPrefixEditor.setEnabled(False)


        intValidator = QIntValidator(1, 65535, dialog)
        self.httpPortEditor = QLineEdit(self.centralDialog)
        self.httpPortEditor.setValidator(intValidator)
        self.httpPortEditor.setGeometry(QtCore.QRect(150, 30, 71, 21))

        self.httpsProxyLabel = QtWidgets.QLabel(self.centralDialog)
        self.httpsProxyLabel.setGeometry(QtCore.QRect(20, 60, 531, 16))
        self.httpsProxyLabel.setText("")
        self.httpsProxyLabel.setObjectName("httpsProxyLabel")

        self.httpsPrefixEditor = QLineEdit(self.centralDialog)
        self.httpsPrefixEditor.setGeometry(QtCore.QRect(20, 80, 121, 21))
        self.httpsPrefixEditor.setText("socks5://127.0.0.1:")
        self.httpsPrefixEditor.setEnabled(False)

        self.httpsPortEditor = QLineEdit(self.centralDialog)
        self.httpsPortEditor.setValidator(intValidator)
        self.httpsPortEditor.setGeometry(QtCore.QRect(150,80, 71, 21))

        self.saveButton = QtWidgets.QPushButton(self.centralDialog)
        self.saveButton.setEnabled(True)
        self.saveButton.setGeometry(QtCore.QRect(220, 120, 113, 32))

        self.retranslateUi(dialog)
    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("proxyDialog", "Proxy Settings"))
        dialog.setWindowFlags(Qt.WindowCloseButtonHint)
        self.httpProxyLabel.setText(_translate("proxyDialog", "http proxy. current only supports local socks5 proxy, so just input the port(0~65535)"))
        self.httpsProxyLabel.setText(_translate("proxyDialog", "https proxy. current only supports local socks5 proxy, so just input the port(0~65535)"))
        self.saveButton.setText(_translate("proxyDialog", "Save"))