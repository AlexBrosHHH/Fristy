from pygame import *

#создай окно игры
okno = display.set_mode((500,500)) #Размер экрана
game = True
clock = time.Clock()

igrok1 = transform.scale(image.load("sprite1.png"),(60,60))
x1 = 0
y1 = 0

igrok2 = transform.scale(image.load("sprite2.png"),(60,60))
x2 = 0
y2 = 0

fon = image.load("background.png")
fon = transform.scale(fon, (500,500))

while game:
    for i in event.get():
        if i.type == QUIT: 
            game = False
    okno.blit(fon, (0,0))
    okno.blit(igrok1,(x1,y1))
    okno.blit(igrok2,(x2,y2))
    knopki = key.get_pressed()
    if knopki[K_RIGHT] and x1 < 500-30:
        x1 += 10
    if knopki[K_LEFT] and x1 > 0:
        x1 -= 10
    if knopki[K_UP] and y1 > 0:
        y1 -= 10
    if knopki[K_DOWN] and y1 < 500-30:
        y1 += 10
    
    if knopki[K_d] and x2 < 500-30:
        x2 += 10
    if knopki[K_a] and x2 > 0:
        x2 -= 10
    if knopki[K_w] and y2 > 0:
        y2 -= 10
    if knopki[K_s] and y2 < 500-30:
        y2 += 10
    display.update()
    clock.tick(60)
#задай фон сцены


#создай 2 спрайта и размести их на сцене


#обработай событие «клик по кнопке "Закрыть окно"»

