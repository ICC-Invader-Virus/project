
import pygame
import os
from pygame import mixer
from subprocess import call


pygame.init()

screen = pygame.display.set_mode((650, 650))
bg = pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Backgrounds", "menu.png")), (650, 650))

pygame.display.set_caption("Main Menu")
NAVE_icono = pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Naves", "nave1.png")), (20, 20))
pygame.display.set_icon(NAVE_icono)

mixer.music.load("Platinum101.wav")
mixer.music.play()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    play_Sound = mixer.Sound('fire.wav')
                    play_Sound.play()

                    class CallPy(object):

                        def __init__(self, path = '/Users/Dcecco_Z/PycharmProjects/InvaderVirus/Main/Main1.py'):
                            self.path = path
                        def call_file(self):
                            call(["Python3", "{}".format(self.path)])

                    if __name__ == "__main__":
                        c = CallPy()
                        c.call_file()
                        running = False

                if event.key == pygame.K_2:
                    play_Sound = mixer.Sound('fire.wav')
                    play_Sound.play()

                    class CallPy(object):

                        def __init__(self, path = '/Users/Dcecco_Z/PycharmProjects/InvaderVirus/Main/Main2.py'):
                            self.path = path
                        def call_file(self):
                            call(["Python3", "{}".format(self.path)])

                    if __name__ == "__main__":
                        c = CallPy()
                        c.call_file()
                        running = False

                if event.key == pygame.K_3:
                    play_Sound = mixer.Sound('fire.wav')
                    play_Sound.play()

                    class CallPy(object):

                        def __init__(self, path = '/Users/Dcecco_Z/PycharmProjects/InvaderVirus/Main/Main3.py'):
                            self.path = path
                        def call_file(self):
                            call(["Python3", "{}".format(self.path)])

                    if __name__ == "__main__":
                        c = CallPy()
                        c.call_file()
                        running = False

    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))

    pygame.display.update()
