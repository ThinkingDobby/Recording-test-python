import sys
import recording_func
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QFileDialog
import librosa


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
        self.btn_stop.setText('녹음 중지')
        self.btn_stop.clicked.connect(self.stop_btn_clicked)

        self.btn_path = QPushButton(self)
        self.btn_path.setText('저장위치 선택')
        self.btn_path.clicked.connect(self.set_path)

        vbox = QVBoxLayout()
        vbox.addWidget(self.btn_record)
        vbox.addWidget(self.btn_stop)
        vbox.addWidget(self.btn_path)

        self.btn_record.setEnabled(True)
        self.btn_stop.setEnabled(False)

        self.setLayout(vbox)
        self.setWindowTitle('RecorderTest')
        self.setGeometry(300, 300, 500, 300)
        self.show()

    def start_btn_clicked(self):
        self.btn_record.setEnabled(False)
        self.btn_stop.setEnabled(True)
        # 녹음 시작
        recording_func.start_recording()

    def stop_btn_clicked(self):
        self.btn_record.setEnabled(True)
        self.btn_stop.setEnabled(False)
        # 녹음 중지
        recording_func.stop_recording()
        # 녹음한 파일 특징 추출해 출력
        signal, sr = librosa.load(recording_func.storage_path, sr=16000)
        mfcc = librosa.feature.mfcc(y=signal, sr=sr)
        print(mfcc)

    def set_path(self):
        tmp = str(QFileDialog.getExistingDirectory(self, "Select Directory")) + '/test.wav'
        if tmp != '/test.wav':
            recording_func.storage_path = tmp
        print('file_path: ' + recording_func.storage_path)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())