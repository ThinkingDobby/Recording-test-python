import sys
from recording_func import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn_record = QPushButton('녹음 시작', self)
        self.btn_record.setCheckable(True)
        self.btn_record.toggle()
        self.btn_record.clicked.connect(self.start_btn_clicked)

        self.btn_stop = QPushButton(self)
        self.btn_stop.setText('중지')
        self.btn_stop.clicked.connect(self.stop_btn_clicked)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn_record)
        vbox.addWidget(self.btn_stop)

        self.btn_record.setEnabled(True)
        self.btn_stop.setEnabled(False)

        self.setLayout(vbox)
        self.setWindowTitle('RecorderTest')
        self.setGeometry(300, 300, 500, 300)
        self.show()

    def start_btn_clicked(self):
        self.btn_record.setEnabled(False)
        self.btn_stop.setEnabled(True)
        start_recording()

    def stop_btn_clicked(self):
        self.btn_record.setEnabled(True)
        self.btn_stop.setEnabled(False)
        stop_recording()

    def set_path(self):
        file = str(QFileDialog.getExistingDirectory(self, "Select Directory"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())