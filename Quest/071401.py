#PyQt 타이머 예제
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
from PyQt5.QtCore import QTimer


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기 고정
        self.setFixedSize(400,300)
        #창 제목 설정
        self.setWindowTitle('MyApp')

        self.num=0
        self.label = QLabel(self)
        #타이머 생성
        self.qtimer=QTimer(self)
        #타이머에 호출할 함수 연결
        self.qtimer.timeout.connect(self.timer)
        # 1(=1000밀리초)초마다 연결된 함수를 실행
        self.qtimer.start(1000)

        #창띄우기
        self.show()

    def timer(self):
                                #좌표        #너비와 높이
        self.label.setGeometry(100, 100, 100, 100)
        self.label.setText(str(self.num))
        self.num = self.num + 1

  #직접실행할때만 실행
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyApp()
    sys.exit(app.exec_())