#게임화면 가져오기
import retro

#게임 환경 생성
env=retro.make(game='SuperMarioBros-Nes',state='Level1-1')
#새 게임 시작
env.reset()

#화면 가져오기
screen=env.get_screen()

print(screen.shape[0],screen.shape[1])
print(screen)


