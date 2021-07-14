import sys
from PyQt5.QtWidgets import QApplication,QWidget


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기 고정
        self.setFixedSize(1024,768)
        #창 제목 설정
        self.setWindowTitle('GA Mario')
        #창띄우기
        self.show()
    #키를 누를때
    def keyPressEvent(self, event):
        key=event.key()
        print(str(key)+' press')

    def keyReleaseEvent(self, event):
        key=event.key()
        print(str(key)+' release')
#직접실행할때만 실행
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyApp()
    sys.exit(app.exec_())