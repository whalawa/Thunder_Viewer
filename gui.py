# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ThunderViewer(object):
    def setupUi(self, ThunderViewer):
        ThunderViewer.setObjectName("ThunderViewer")
        ThunderViewer.resize(500, 340)
        ThunderViewer.setMinimumSize(QtCore.QSize(500, 340))
        ThunderViewer.setMaximumSize(QtCore.QSize(500, 340))
        self.centralwidget = QtWidgets.QWidget(ThunderViewer)
        self.centralwidget.setObjectName("centralwidget")
        self.mqtt_id = QtWidgets.QLineEdit(self.centralwidget)
        self.mqtt_id.setGeometry(QtCore.QRect(40, 120, 201, 20))
        self.mqtt_id.setObjectName("mqtt_id")
        self.recording = QtWidgets.QRadioButton(self.centralwidget)
        self.recording.setGeometry(QtCore.QRect(210, 260, 82, 17))
        self.recording.setObjectName("recording")
        self.record = QtWidgets.QPushButton(self.centralwidget)
        self.record.setGeometry(QtCore.QRect(40, 230, 201, 23))
        self.record.setObjectName("record")
        self.stop = QtWidgets.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(260, 230, 201, 23))
        self.stop.setObjectName("stop")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 201, 16))
        self.label_2.setObjectName("label_2")
        self.mqtt = QtWidgets.QCheckBox(self.centralwidget)
        self.mqtt.setGeometry(QtCore.QRect(50, 150, 191, 17))
        self.mqtt.setObjectName("mqtt")
        self.acmi_select = QtWidgets.QPushButton(self.centralwidget)
        self.acmi_select.setGeometry(QtCore.QRect(40, 60, 101, 23))
        self.acmi_select.setObjectName("acmi_select")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(260, 100, 201, 20))
        self.label_3.setObjectName("label_3")
        self.live_telem = QtWidgets.QCheckBox(self.centralwidget)
        self.live_telem.setGeometry(QtCore.QRect(270, 150, 191, 20))
        self.live_telem.setObjectName("live_telem")
        self.launch_tacview_live = QtWidgets.QPushButton(self.centralwidget)
        self.launch_tacview_live.setGeometry(QtCore.QRect(40, 180, 421, 31))
        self.launch_tacview_live.setObjectName("launch_tacview_live")
        self.tacview_select = QtWidgets.QPushButton(self.centralwidget)
        self.tacview_select.setGeometry(QtCore.QRect(40, 20, 101, 23))
        self.tacview_select.setObjectName("tacview_select")
        self.live_telem_port = QtWidgets.QSpinBox(self.centralwidget)
        self.live_telem_port.setGeometry(QtCore.QRect(260, 120, 201, 22))
        self.live_telem_port.setMaximum(9999)
        self.live_telem_port.setProperty("value", 8110)
        self.live_telem_port.setObjectName("live_telem_port")
        self.tacview_path = QtWidgets.QLineEdit(self.centralwidget)
        self.tacview_path.setGeometry(QtCore.QRect(150, 20, 311, 20))
        self.tacview_path.setReadOnly(True)
        self.tacview_path.setObjectName("tacview_path")
        self.acmi_path = QtWidgets.QLineEdit(self.centralwidget)
        self.acmi_path.setGeometry(QtCore.QRect(150, 60, 311, 20))
        self.acmi_path.setReadOnly(True)
        self.acmi_path.setObjectName("acmi_path")
        ThunderViewer.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ThunderViewer)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 500, 21))
        self.menubar.setObjectName("menubar")
        ThunderViewer.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ThunderViewer)
        self.statusbar.setObjectName("statusbar")
        ThunderViewer.setStatusBar(self.statusbar)

        self.retranslateUi(ThunderViewer)
        QtCore.QMetaObject.connectSlotsByName(ThunderViewer)

    def retranslateUi(self, ThunderViewer):
        _translate = QtCore.QCoreApplication.translate
        ThunderViewer.setWindowTitle(_translate("ThunderViewer", "Thunder Viewer"))
        self.mqtt_id.setText(_translate("ThunderViewer", "FlightViewer"))
        self.recording.setText(_translate("ThunderViewer", "Recording"))
        self.record.setText(_translate("ThunderViewer", "Record"))
        self.stop.setText(_translate("ThunderViewer", "Stop"))
        self.label_2.setText(_translate("ThunderViewer", "MQTT Session ID"))
        self.mqtt.setText(_translate("ThunderViewer", "MQTT Messaging Enabled"))
        self.acmi_select.setText(_translate("ThunderViewer", "ACMI Directory:"))
        self.label_3.setText(_translate("ThunderViewer", "Live Telemetry Port"))
        self.live_telem.setText(_translate("ThunderViewer", "Live Telemtry Enabled"))
        self.launch_tacview_live.setText(_translate("ThunderViewer", "Launch TacView for Live Telemetry"))
        self.tacview_select.setText(_translate("ThunderViewer", "TacView Install:"))
        self.tacview_path.setText(_translate("ThunderViewer", "C:\\Program Files (x86)\\Tacview\\Tacview64.exe"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThunderViewer = QtWidgets.QMainWindow()
    ui = Ui_ThunderViewer()
    ui.setupUi(ThunderViewer)
    ThunderViewer.show()
    sys.exit(app.exec_())
