from random import randint
from pygame import *
from time import time as timer




# Создание главного окна
window_width = 700
window_height = 500

window = display.set_mode((window_width, window_height))
display.set_caption('Shooooooooooooooooooooooooooooooooooooter!')
background = transform.scale(image.load('galaxy.jpg'), (window_width, window_height))




score = 0
lost = 0


font.init()
font_label = font.SysFont('Papyrus', 32)
font_finish = font.SysFont('calibr', 50)




# Создание класса для ПЕРСОНАЖЕЙ
class Hero(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, p_width, p_height, p_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(p_image), (p_width, p_height))
        self.speed = p_speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
        self.width = p_width
        self.height = p_height










    # Метод отображения
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))




# Создание класса для пуль
class Bullet(Hero):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
class Asteroid(Hero):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > window_height:
            self.rect.x = randint(80, window_width - 80)
            self.rect.y = randint(-200, -50)
            lost += 1


# Создание босса
class Boss(Hero):
    direction = 'RIGHT'
    lives = 30
    def update(self):
        if self.rect.x <= 0:
            self.direction = 'RIGHT'
        elif self.rect.x >= window_width - 250:
            self.direction = 'LEFT'

        if self.direction == 'RIGHT':
            self.rect.x += randint(1, 15)
        elif self.direction == 'LEFT':
            self.rect.x -= randint(1, 15)

    def fire(self):
        bs_blt = Boss_Bullet('nuclear-bomb.png', self.rect.centerx, self.rect.button, 50, 50, 7)
        boss_bullets.add(bs_blt)

# Создание класса для ГЛАВНОГО ГЕРОЯ
class Player(Hero):
    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < window_width - self.width - 5:
            self.rect.x += self.speed
            
    # Метод стрельбы
    def fire(self):
        blt = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 20)
        bullets.add(blt)


# Класс для пуль босса
class Boss_Bullet(Hero):
    def update(self):
        self.rect.x += self.speed 
        if self.rect.y > window_height:
            self.kill()









class Enemy(Hero):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > window_height:
            self.rect.x = randint(80, window_width - 80)
            self.rect.y = randint(-200, -50)
            lost += 1




# Создание персонажей
# картинка, x, y, ширина, высота, скорость
ship = Player('rocket.png', window_width // 2, window_height - 105, 80, 100, 10)




monsters = sprite.Group()
for i in range(6):
    mnstr = Enemy('ufo.png', randint(50, window_width - 80), randint(-200, -50), 75, 50, randint(1, 3))
    monsters.add(mnstr)
bullets = sprite.Group()


asteroids = sprite.Group()
for i in range(2):
    astr = Asteroid('asteroid.png', randint(50, window_width - 80), randint(-200, -50), 75, 75, randint(1, 3))
    asteroids.add(astr)
bullets = sprite.Group()


boss = Boss('boss.png', randint(50, window_width - 150), window_height // 2, 150, 150, randint(1, 15))
boss_bullets = sprite.Group()






#
#
#
#




# Игровой цикл
game = True
finish = False
clock = time.Clock()

# Фаза игры
phase_1 = True
phase_2 = False
phase_boss = False

start_game = timer()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        # Нажате клваиши ждя выстрела
        elif e.type == MOUSEBUTTONDOWN:
            if e.button == 1:
                ship.fire()
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                ship.fire()




    if finish != True:
        # Отображение фона
        window.blit(background, (0, 0))
       
        # Главный герой
        ship.reset()
        ship.update()

        # Пули
        bullets.draw(window)
        bullets.update()


        # Отображение надписей
        score_label = font_label.render('Score:' + str(score), True, (255, 255, 255))
        window.blit(score_label, (10, 10))


        lost_label = font_label.render('Lost:' + str(lost), True, (255, 255, 255))
        window.blit(lost_label, (10, 45))


        # Столкновение пуль с врагами
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for i in collides:
            score += 1
            mnstr = Enemy('ufo.png', randint(50, window_width - 80), randint(-200, -50), 75, 50, randint(1, 3))
            monsters.add(mnstr)


        # Ожидание начала игры
        start_phase = timer()

        if (start_phase - start_game) <= 7:
            start_text = font_label.render('Go to game!', True, (255, 255, 255))
            window.blit(start_text, (70, 200))

        else:
            # Фаза 1
            if phase_1:
                # Отображение противников
                monsters.draw(window)
                monsters.update()



                # Столкновение пуль с врагами
                collides = sprite.groupcollide(monsters, bullets, True, True)
                for i in collides:
                    score += 1
                    mnstr = Enemy('ufo.png', randint(50, window_width - 80), randint(-200, -50), 75, 50, randint(1, 3))
                    monsters.add(mnstr)

                # Переход на следующаю фазу
                if score > 5:
                    phase_2 = True
                    phase_1 = False

            # Фаза 2
            if phase_2:
                
                # Отображение противников
                monsters.draw(window)
                monsters.update()
                # Отоброжение астероидов
                asteroids.draw(window)
                asteroids.update()

                asteroids_collides = sprite.groupcollide(asteroids, bullets, False, True)

                # Столкновение пуль с врагами
                collides = sprite.groupcollide(monsters, bullets, True, True)
                for i in collides:
                    score += 1
                    mnstr = Enemy('ufo.png', randint(50, window_width - 80), randint(-200, -50), 75, 50, randint(1, 3))
                    monsters.add(mnstr)






                # Переход на следующаю фазу
                if score > 20:
                    phase_boss = True
                    phase_2 = False

            # Фаза 3
            if phase_boss:
                # Отображение противников
                boss.reset()
                boss.update()
                
                if sprite.spritecollide(boss, bullets, True):
                    boss.lives -= 1

                boss_health = Rect(window_width - 200, 10, boss.lives * 5, 10)
                draw.rect(window, (255, 0, 0), boss_health)

                chance = randint(1, 100)
                if chance > 95:
                    boss.fire()
                boss_bullets.draw(window)
                boss_bullets.update()

            # Проигрыш
            if lost > 3 or sprite.spritecollide(ship, monsters, False):
                finish_lost = font_finish.render('You LOOOOOOSE!', True, (225, 250, 0))
                window.fill((250, 0 ,0))
                window.blit(finish_lost, (window_width// 2 - 160, window_height// 2 - 30))
                finish = True


            # Выигрыш
            if boss.lives <= 0:
                finish_lost = font_finish.render('Finish!', True, (0, 0, 250))
                window.fill((0, 250 ,0))
                window.blit(finish_lost, (window_width// 2 - 100, window_height// 2 - 30))


    # Обновление экрана
    display.update()
    clock.tick(60)
