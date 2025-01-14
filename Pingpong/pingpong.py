from pygame import *
from random import randint
#подгружаем отдельно функции для работы со шрифтом
#нам нужны такие картинки:
img_back = "player1.png" #фон игры
img_hero = "player1.png" #герой
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
class Player(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_UP] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_DOWN] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
class Player2(GameSprite):
   #метод для управления спрайтом стрелками клавиатуры
   def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 5:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - 80:
           self.rect.x += self.speed
#класс спрайта-врага  
win_width = 700
win_height = 500
display.set_caption("Шутер")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))
#создаём спрайты
player1 = Player(img_hero, 5, win_height - 100, 80, 100, 10)
player2 = Player(img_hero, 5, 200 - 200, 200, 200, 10)
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
       #событие нажатия на пробел - спрайт стреляет
       elif e.type == KEYDOWN :
           if e.key == K_SPACE:
               player1.fire()
 #сама игра: действия спрайтов, проверка правил игры, перерисовка
   if not finish:
       #обновляем фон
       window.blit(background,(0,0))
       #производим движения спрайтов
       player1.update()
       player2.update()
       #обновляем их в новом местоположении при каждой итерации цикла
       player1.reset()
    
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