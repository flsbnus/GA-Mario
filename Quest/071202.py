import sys
from PyQt5.QtWidgets import QApplication,QWidget,QLabel
# 텍스트 그리기
#painter.drawText(0,250,'abcd')

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기 고정
        self.setFixedSize(300,300)
        #창 제목 설정
        self.setWindowTitle('GA Mario')
        label_text = QLabel(self)
        #창띄우기
        self.show()
    #키를 누를때
    def keyPressEvent(self, event):
        key = event.key()
        lable=QLabel(self)
        self.label = QLabel(self)
        #self.label.setGeometry(0,0,100,100)
        self.label.setText(str(key)+ ' release')
        self.label.setGeometry(100, 100, 100, 100)
        print(str(key)+' press')


    def keyReleaseEvent(self, event):
        key=event.key()
        print(str(key)+' release')
#직접실행할때만 실행
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyApp()
    sys.exit(app.exec_())