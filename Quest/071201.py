import sys
from PyQt5.QtGui import QPainter, QPen,QBrush,QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QWidget

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기 고정
        self.setFixedSize(200,300)
        #창 제목 설정
        self.setWindowTitle('GA-Mario')
        #창띄우기
        self.show()

    #창이 업데이트 될 때마다 실행되는 함수
    def paintEvent(self, event):
        # 그리기 도구
        painter=QPainter()
        # 그리기 시작
        painter.begin(self)

        # 펜 설정(테두리)
        #painter.setPen(QPen(Qt.blue,2.0, Qt.SolidLine))
        # 선 그리기
        #painter.drawLine(0,10,200,100)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0,0,0),1.0,Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.blue))
        # 직사각형 그리기
        painter.drawRect(0,0,50,50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0,0,0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.white))
        # 직사각형 그리기
        painter.drawRect(50, 0, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0,0,0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        #painter.setBrush(QBrush(Qt.re))
        # 직사각형 그리기
        painter.drawRect(0, 50, 50, 50)

        # RGB 색상으로 펜 설정
        painter.setPen(QPen(QColor.fromRgb(0,0,0), 1.0, Qt.SolidLine))
        # 브러쉬 설정 (채우기)
        painter.setBrush(QBrush(Qt.red))
        # 직사각형 그리기
        painter.drawRect(50, 50, 50, 50)

        # 펜 설정(테두리)
        painter.setPen(QPen(Qt.blue,2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(42.5,162.5,42.5,212.5)
        # 펜 설정(테두리)
        painter.setPen(QPen(Qt.red, 2.0, Qt.SolidLine))
        # 선 그리기
        painter.drawLine(12.5, 162.5, 42.5, 212.5)
        painter.drawLine(72.5, 162.5, 42.5, 212.5)

        painter.setPen(QPen(Qt.black,1.0,Qt.SolidLine))
        # RGB 색상으로 브러쉬 설정
        painter.setBrush(QBrush(Qt.cyan))
        # 타원 그리기
        painter.drawEllipse(0,150,25,25)
        painter.drawEllipse(60, 150, 25, 25)
        painter.setBrush(QBrush(Qt.white))
        painter.drawEllipse(30, 150, 25, 25)
        painter.setBrush(QBrush(Qt.gray))
        painter.drawEllipse(30, 200, 25, 25)






  #직접실행할때만 실행
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyApp()
    sys.exit(app.exec_())