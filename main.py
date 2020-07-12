import pygame
import math
import os
pygame.font.init()

X = 650
Y = 900
ventana = pygame.display.set_mode((X, Y))
pygame.display.set_caption("Virus Invaders")

#viruses
#virus 1
max_virus1 = 12
VIRUS_1 = [pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "1a.png")), (50, 50)) for x in range(max_virus1)]
x_virus1 = [x for x in range(0, 600, 50)]
y_virus1 = [200 for x in range(max_virus1)]
cambio_x_virus1 = [1 for x in range(max_virus1)]
cambio_y_virus1 = [50 for x in range(max_virus1)]
contador = 0

max_virus2 = 12
VIRUS_2 = [pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "2a.png")), (50, 50)) for x in range(max_virus2)]
x_virus2 = [x for x in range(50, 650, 50)]
y_virus2 = [150 for x in range(max_virus2)]
cambio_x_virus2 = [-1 for x in range(max_virus2)]
cambio_y_virus2 = [50 for x in range(max_virus2)]

max_virus3 = 8
VIRUS_3 = [pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "3a.png")), (75, 75)) for x in range(max_virus3)]
x_virus3 = [x for x in range(0, 600, 75)]
y_virus3 = [75 for x in range(max_virus3)]
cambio_x_virus3 = [1 for x in range(max_virus3)]
cambio_y_virus3 = [50 for x in range(max_virus3)]

max_virus4 = 8
VIRUS_4 = [pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "4a.png")), (75, 75)) for x in range(max_virus4)]
x_virus4 = [x for x in range(50, 650, 75)]
y_virus4 = [0 for x in range(max_virus4)]
cambio_x_virus4 = [-1 for x in range(max_virus4)]
cambio_y_virus4 = [50 for x in range(max_virus4)]


max_virus5 = 5
VIRUS_5 = [pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "5a.png")), (120, 120)) for x in range(max_virus5)]
x_virus5 = [x for x in range(0, 600, 120)]
y_virus5 = [-200 for x in range(max_virus5)]
cambio_x_virus5 = [1 for x in range(max_virus5)]
cambio_y_virus5 = [50 for x in range(max_virus5)]
vida_virus_5 = [2 for x in range(max_virus5)]

max_virus6 = 1
VIRUS_6 = [pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "corona1.png")), (200, 200)) for x in range(max_virus6)]
x_virus6 = [x for x in range(50, 650, 300)]
y_virus6 = [-550 for x in range(max_virus6)]
cambio_x_virus6 = [-1 for x in range(max_virus6)]
cambio_y_virus6 = [50 for x in range(max_virus6)]
vida_virus_6 = [5 for x in range(max_virus6)]

max_virus_tot = max_virus1 + max_virus2 + max_virus3 + max_virus4 + max_virus5 + max_virus6

#bala
BALA_NAVE = pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "vacuna.png")), (30, 30))
x_bala = 300
y_bala = 850
cambio_x_bala = 0
cambio_y_bala = 5
bala_estado = 'ready'


#personaje
NAVE = pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "nave1.png")), (50, 50))
x_jugador = 300
y_jugador = 850
cambio_x_jugador = 0

#Fondo
FONDO = pygame.transform.scale(pygame.image.load(os.path.join("Fotos", "Fondo.png")), (X, Y))

puntuacion = 0
font = pygame.font.Font('freesansbold.ttf', 15)
puntx = 10
punty = 10

game_over_font = pygame.font.Font('freesansbold.ttf', 75)


def mostrar_puntuacion(x, y):
    puntaje = font.render("Puntuacion: " + str(puntuacion), True, (255, 255, 255))
    ventana.blit(puntaje, (x, y))


def texto_game_over():
    game_over_texto = game_over_font.render("GAME OVER", True, (255, 255, 255))
    ventana.blit(game_over_texto, (100, 250))


def texto_you_win():
    you_win_texto = game_over_font.render("YOU WIN!!", True, (255, 94, 59))
    ventana.blit(you_win_texto, (120, 250))


def jugador(x, y):
    ventana.blit(NAVE, (x, y))


def virus1(x, y, a):
    ventana.blit(VIRUS_1[a], (x, y))


def virus2(x, y, a):
    ventana.blit(VIRUS_2[a], (x, y))


def virus3(x, y, a):
    ventana.blit(VIRUS_3[a], (x, y))


def virus4(x, y, a):
    ventana.blit(VIRUS_4[a], (x, y))


def virus5(x, y, a):
    ventana.blit(VIRUS_5[a], (x, y))


def virus6(x, y, a):
    ventana.blit(VIRUS_6[a], (x, y))


def disparo(x, y):
    global bala_estado
    bala_estado = 'disparo'
    ventana.blit(BALA_NAVE, (x + 12, y - 20))


def colapsan_1_2(x_blanco, y_blanco, x_bala, y_bala):
    distancia = math.sqrt(((x_blanco-x_bala)**2)+((y_blanco - y_bala)**2))
    if distancia < 30:
        return True


def colapsan_3_4(x_blanco, y_blanco, x_bala, y_bala):
    distancia = math.sqrt(((x_blanco-x_bala)**2)+((y_blanco - y_bala)**2))
    if distancia < 60:
        return True


def colapsan_5(x_blanco, y_blanco, x_bala, y_bala):
    distancia = math.sqrt(((x_blanco-x_bala)**2)+((y_blanco - y_bala)**2))
    if distancia < 90:
        return True


def colapsan_6(x_blanco, y_blanco, x_bala, y_bala):
    distancia = math.sqrt(((x_blanco-x_bala)**2)+((y_blanco - y_bala)**2))
    if distancia < 150:
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
                cambio_x_jugador = -2
            if evento.key == pygame.K_RIGHT or evento.key == pygame.K_d:
                cambio_x_jugador = 2
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

    for a in range(12):
        if y_virus1[a] > 800 or y_virus2[a] > 800:
            for b in range(12):
                y_virus1[b] = 1000
                y_virus2[b] = 1000
            for b in range(8):
                y_virus3[b] = 1000
                y_virus4[b] = 1000
            for b in range(5):
                y_virus5[b] = 1000
            for b in range(1):
                y_virus6[b] = 1000
            texto_game_over()
            break
        elif contador == max_virus_tot:
            texto_you_win()
            break

    for a in range(8):
        if y_virus3[a] > 800 or y_virus3[a] > 800:
            for b in range(12):
                y_virus1[b] = 1000
                y_virus2[b] = 1000
            for b in range(8):
                y_virus3[b] = 1000
                y_virus4[b] = 1000
            for b in range(5):
                y_virus5[b] = 1000
            for b in range(1):
                y_virus6[b] = 1000
            texto_game_over()
            break

    for a in range(5):
        if y_virus5[a] > 800:
            for b in range(12):
                y_virus1[b] = 1000
                y_virus2[b] = 1000
            for b in range(8):
                y_virus3[b] = 1000
                y_virus4[b] = 1000
            for b in range(5):
                y_virus5[b] = 1000
            for b in range(1):
                y_virus6[b] = 1000
            texto_game_over()
            break

    for a in range(1):
        if y_virus6[a] > 800:
            for b in range(12):
                y_virus1[b] = 1000
                y_virus2[b] = 1000
            for b in range(8):
                y_virus3[b] = 1000
                y_virus4[b] = 1000
            for b in range(5):
                y_virus5[b] = 1000
            for b in range(1):
                y_virus6[b] = 1000
            texto_game_over()
            break

    for a in range(max_virus1):
        x_virus1[a] += cambio_x_virus1[a]
        if x_virus1[a] <= 0:
            cambio_x_virus1[a] = 1
            y_virus1[a] += cambio_y_virus1[a]
        elif x_virus1[a] >= X-50:
            cambio_x_virus1[a] = -1
            y_virus1[a] += cambio_y_virus1[a]
        colapso1 = colapsan_1_2(x_virus1[a], y_virus1[a], x_bala, y_bala)
        if colapso1:
            y_bala = 850
            bala_estado = 'ready'
            puntuacion += 100
            x_virus1[a] = 1000
            y_virus1[a] = -100000
            cambio_x_virus1[a] = 0
            cambio_y_virus1[a] = 0
            contador += 1
        virus1(x_virus1[a], y_virus1[a], a)

    for a in range(max_virus2):
        x_virus2[a] += cambio_x_virus2[a]
        if x_virus2[a] <= 0:
            cambio_x_virus2[a] = 1
            y_virus2[a] += cambio_y_virus2[a]
        elif x_virus2[a] >= X-50:
            cambio_x_virus2[a] = -1
            y_virus2[a] += cambio_y_virus2[a]
        colapso2 = colapsan_1_2(x_virus2[a], y_virus2[a], x_bala, y_bala)
        if colapso2:
            y_bala = 850
            bala_estado = 'ready'
            puntuacion += 100
            x_virus2[a] = 1000
            y_virus2[a] = -100000
            cambio_x_virus2[a] = 0
            cambio_y_virus2[a] = 0
            contador += 1
        virus2(x_virus2[a], y_virus2[a], a)

    for a in range(max_virus3):
        x_virus3[a] += cambio_x_virus3[a]
        if x_virus3[a] <= 0:
            cambio_x_virus3[a] = 1
            y_virus3[a] += cambio_y_virus3[a]
        elif x_virus3[a] >= X-50:
            cambio_x_virus3[a] = -1
            y_virus3[a] += cambio_y_virus3[a]
        colapso3 = colapsan_3_4(x_virus3[a], y_virus3[a], x_bala, y_bala)
        if colapso3:
            y_bala = 850
            bala_estado = 'ready'
            puntuacion += 200
            x_virus3[a] = 1000
            y_virus3[a] = -100000
            cambio_x_virus3[a] = 0
            cambio_y_virus3[a] = 0
            contador += 1
        virus3(x_virus3[a], y_virus3[a], a)

    for a in range(max_virus4):
        x_virus4[a] += cambio_x_virus4[a]
        if x_virus4[a] <= 0:
            cambio_x_virus4[a] = 1
            y_virus4[a] += cambio_y_virus4[a]
        elif x_virus4[a] >= X-50:
            cambio_x_virus4[a] = -1
            y_virus4[a] += cambio_y_virus4[a]
        colapso4 = colapsan_3_4(x_virus4[a], y_virus4[a], x_bala, y_bala)
        if colapso4:
            y_bala = 850
            bala_estado = 'ready'
            puntuacion += 200
            x_virus4[a] = 1000
            y_virus4[a] = -100000
            cambio_x_virus4[a] = 0
            cambio_y_virus4[a] = 0
            contador += 1
        virus4(x_virus4[a], y_virus4[a], a)

    for a in range(max_virus5):
        x_virus5[a] += cambio_x_virus5[a]
        if x_virus5[a] <= 0:
            cambio_x_virus5[a] = 1
            y_virus5[a] += cambio_y_virus5[a]
        elif x_virus5[a] >= X-100:
            cambio_x_virus5[a] = -1
            y_virus5[a] += cambio_y_virus5[a]
        colapso5 = colapsan_5(x_virus5[a], y_virus5[a], x_bala, y_bala)
        if colapso5:
            vida_virus_5[a] -= 1
            y_bala = 850
            bala_estado = 'ready'
            if vida_virus_5[a] == 0:
                y_bala = 850
                bala_estado = 'ready'
                puntuacion += 500
                x_virus5[a] = 1000
                y_virus5[a] = -100000
                cambio_x_virus5[a] = 0
                cambio_y_virus5[a] = 0
                contador += 1
        virus5(x_virus5[a], y_virus5[a], a)

    for a in range(max_virus6):
        x_virus6[a] += cambio_x_virus6[a]
        if x_virus6[a] <= 0:
            cambio_x_virus6[a] = 1
            y_virus6[a] += cambio_y_virus6[a]
        elif x_virus6[a] >= X-200:
            cambio_x_virus6[a] = -1
            y_virus6[a] += cambio_y_virus6[a]
        colapso6 = colapsan_6(x_virus6[a], y_virus6[a], x_bala, y_bala)
        if colapso6:
            vida_virus_6[a] -= 1
            y_bala = 850
            bala_estado = 'ready'
            if vida_virus_6[a] == 0:
                y_bala = 850
                bala_estado = 'ready'
                puntuacion += 1000
                x_virus6[a] = 1000
                y_virus6[a] = -100000
                cambio_x_virus6[a] = 0
                cambio_y_virus6[a] = 0
                contador += 1
        virus6(x_virus6[a], y_virus6[a], a)

    if y_bala <= 0:
        y_bala = 850
        bala_estado = 'ready'

    if bala_estado == 'disparo':
        disparo(x_bala, y_bala)
        y_bala -= cambio_y_bala

    jugador(x_jugador, y_jugador)
    mostrar_puntuacion(puntx, punty)
    pygame.display.update()
