import pygame
import math
import os
pygame.font.init()

X = 650
Y = 650
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Invader Virus")

#viruses
#virus 1
max_virus1 = 12
VIRUS_1 = [pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Assets", "1a.png")), (50, 50)) for x in range(max_virus1)]
x_virus1 = [x for x in range(0, 600, 50)]
y_virus1 = [100 for x in range(max_virus1)]
cambio_x_virus1 = [1 for x in range(max_virus1)]
cambio_y_virus1 = [50 for x in range(max_virus1)]
contador = 0


VIRUS_2 = pygame.image.load(os.path.join("Sources/Graphics/Assets", "2a.png"))
VIRUS_3 = pygame.image.load(os.path.join("Sources/Graphics/Assets", "3a.png"))
VIRUS_4 = pygame.image.load(os.path.join("Sources/Graphics/Assets", "4a.png"))
VIRUS_5 = pygame.image.load(os.path.join("Sources/Graphics/Assets", "5a.png"))
VIRUS_6 = pygame.image.load(os.path.join("Sources/Graphics/Assets", "corona1.png"))

#you win / game over
you_win_img = pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Backgrounds", "BG_WIN.png")), (X, Y))
game_over_img = pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Backgrounds", "BG_OVER.png")), (X, Y))

#bala
BALA_NAVE = pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Assets", "vacuna.png")), (30, 30))
x_bala = 300
y_bala = 600
cambio_x_bala = 0
cambio_y_bala = 10
bala_estado = 'ready'


#personaje
NAVE = pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Naves", "nave2.png")), (50, 50))
x_jugador = 300
y_jugador = 600
cambio_x_jugador = 0

#Fondo
FONDO = pygame.transform.scale(pygame.image.load(os.path.join("Sources/Graphics/Backgrounds", "BG2.png")), (X, Y))

puntuacion = 0
font = pygame.font.Font('freesansbold.ttf', 15)
puntx = 10
punty = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 75)

def mostrar_puntuacion(x, y):
    puntaje = font.render("Puntuacion: " + str(puntuacion), True, (255, 255, 255))
    ventana.blit(puntaje, (x, y))


def game_over():
    ventana.fill((0, 0, 0))
    ventana.blit(game_over_img, (0, 0))


def you_win():
    ventana.fill((0, 0, 0))
    ventana.blit(you_win_img, (0, 0))


def jugador(x, y):
    ventana.blit(NAVE, (x, y))


def virus1(x, y, a):
    ventana.blit(VIRUS_1[a], (x, y))


def disparo(x, y):
    global bala_estado
    bala_estado = 'disparo'
    ventana.blit(BALA_NAVE, (x + 12, y - 20))


def colapsan(x_blanco, y_blanco, x_bala, y_bala):
    distancia = math.sqrt(((x_blanco-x_bala)**2)+((y_blanco - y_bala)**2))
    if distancia < 30:
        return True


run = True
while run:
    ventana.fill((0, 0, 0))
    ventana.blit(FONDO, (0, 0))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            quit()
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_a:
                cambio_x_jugador = -5
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                cambio_x_jugador = 5
            if evento.key == pygame.K_SPACE:
                if bala_estado == 'ready':
                    x_bala = x_jugador
                    disparo(x_bala, y_bala)

        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT or evento.key == pygame.K_d or evento.key == pygame.K_a:
                cambio_x_jugador = 0

    x_jugador += cambio_x_jugador
    if x_jugador <= 0:
        x_jugador = 0
    elif x_jugador >= X-50:
        x_jugador = X-50

    for a in range(max_virus1):
        if y_virus1[a] > 550:
            for b in range(max_virus1):
                y_virus1[b] = 1000
            game_over()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
        elif contador == max_virus1:
            you_win()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit()
        
        x_virus1[a] += cambio_x_virus1[a]
        if x_virus1[a] <= 0:
            cambio_x_virus1[a] = 1
            y_virus1[a] += cambio_y_virus1[a]
        elif x_virus1[a] >= X-50:
            cambio_x_virus1[a] = -1
            y_virus1[a] += cambio_y_virus1[a]
        colapso = colapsan(x_virus1[a], y_virus1[a], x_bala, y_bala)
        if colapso:
            y_bala = 600
            bala_estado = 'ready'
            puntuacion += 100
            x_virus1[a] = 1000
            y_virus1[a] = -100000
            cambio_x_virus1[a] = 0
            cambio_y_virus1[a] = 0
            contador += 1
        virus1(x_virus1[a], y_virus1[a], a)

    if y_bala <= 0:
        y_bala = 600
        bala_estado = 'ready'

    if bala_estado == 'disparo':
        disparo(x_bala, y_bala)
        y_bala -= cambio_y_bala

    jugador(x_jugador, y_jugador)
    mostrar_puntuacion(puntx, punty)
    pygame.display.update()
