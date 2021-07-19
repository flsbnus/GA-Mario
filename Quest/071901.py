#pyqt위젯 배치
#PyQt 기본요소
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtCore import Qt
import numpy as np
import retro

#게임 환경 생성
env=retro.make(game='SuperMarioBros-Nes',state='Level1-1')
#새 게임 시작
env.reset()

#화면 가져오기
screen=env.get_screen()

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        #창 크기 고정
        self.setFixedSize(screen.shape[0]*2,screen.shape[1]*2)
        #창 제목 설정
        self.setWindowTitle('GA-Mario')





        #이미지
        label_image=QLabel(self)
        image = np.array(screen)
        qimage=QImage(image,image.shape[1],image.shape[0],QImage.Format_RGB888)
        pixmap=QPixmap(qimage)
        pixmap=pixmap.scaled(screen.shape[0]*2,screen.shape[1]*2,Qt.IgnoreAspectRatio)

        label_image.setPixmap(pixmap)
        label_image.setGeometry(0,0,screen.shape[0]*2,screen.shape[1]*2)

        #창띄우기
        self.show()
  #직접실행할때만 실행
if __name__=='__main__':
    app=QApplication(sys.argv)
    window=MyApp()
    sys.exit(app.exec_())