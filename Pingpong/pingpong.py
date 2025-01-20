from pygame import *
from random import randint
#подгружаем отдельно функции для работы со шрифтом
#нам нужны такие картинки:
img_ball = "ball.png" #фон игры
img_player = "player1.png" #герой
img_player2 = "player2.png" #герой
img_back = "back.jpg" #враг
class GameSprite(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed = player_speed
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class GameSprite2(sprite.Sprite):
 #конструктор класса
   def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed_y, player_speed_x):
       #вызываем конструктор класса (Sprite):
       sprite.Sprite.__init__(self)
       #каждый спрайт должен хранить свойство image - изображение
       self.image = transform.scale(image.load(player_image), (size_x, size_y))
       self.speed_y = player_speed_y
       self.speed_x = player_speed_x
       #каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_DOWN] and self.rect.y < 400:
           self.rect.y += self.speed

class Player2(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_w] and self.rect.y > 5:
           self.rect.y -= self.speed
       if keys[K_s] and self.rect.y < 400:
           self.rect.y += self.speed
class ball(GameSprite2):
    def update(self):
        # Отскок от верхней и нижней границ
        if self.rect.y <= 0 or self.rect.y >= win_height - self.rect.height:
            self.speed_y *= -1
        # Движение по координатам
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.colliderect(Player.rect) or self.rect.colliderect(Player2.rect):
            self.speed_x *= -1
#класс спрайта-врага  
win_width = 700
win_height = 500
display.set_caption("Шутер")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#создаём спрайты
player1 = Player(img_player, 5, 240 - 100, 15, 100, 0.7) #self, player_image, player_x, player_y, size_x, size_y, player_speed
player2 = Player2(img_player2, 680, 240 - 100, 15, 100, 0.7)
ball1 = ball(img_ball, 450, 250, 30, 30, 1, 1)
#создание группы спрайтов-врагов
#переменная "игра закончилась": как только там True, в основном цикле перестают работать спрайты
finish = False
#основной цикл игры:
run = True #флаг сбрасывается кнопкой закрытия окна
while run:
   #событие нажатия на кнопку Закрыть
   for e in event.get():
       if e.type == QUIT:
           run = False
   if not finish:
       #обновляем фон
       window.blit(background,(0,0))
       #производим движения спрайтов
       player1.update()
       player2.update()
       ball1.update()
       #обновляем их в новом местоположении при каждой итерации цикла
       player1.reset()
       player2.reset()
       ball1.reset()
    
       #проверка столкновения пули и монстров (и монстр, и пуля при касании исчезают))
#       #TODO://возможный проигрыш: пропустили слишком много или герой столкнулся с врагом
#       if sprite.spritecollide(player1, player2, False) or lost >= max_lost or sprite.spritecollide(player1, kills, False):
#           hp = hp - 1 #проиграли, ставим фон и больше не управляем спрайтами.
#           max_lost = 0
#       if hp <= 0:
#           finish = True
#           window.blit(lose, (200, 200))
#       ##TODO:проверка выигрыша: сколько очков набрали?
#       if score >= goal:
#           finish = True
#           window.blit(win, (200, 200))
#       #//пишем текст на экране
#       text = font2.render("Счет: " + str(score), 1, (255, 255, 255))
#       window.blit(text, (10, 20))
#       text_lose = font2.render("Пропущено: " + str(lost), 1, (255, 255, 255))
#       window.blit(text_lose, (10, 50))
       display.update()
   #!бонус: автоматический перезапуск игры