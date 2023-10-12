from random import *
from pygame import *
font.init()
mixer.init()
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0):
        super().__init__()
        self.image_wight = image_wight
        self.image_height = image_height
        self.image = transform.scale(image.load(player_image), (image_wight, image_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.fire = True
        self.fps = 40
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
        self.fps -= 1
        if self.fps <= 0:
            self.fire = True



class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0, hearts=3):
        super().__init__(player_image, player_x, player_y, player_speed, image_wight, image_height)
        self.hearts = hearts
    def move(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < x-70:
            self.rect.x += self.speed
        if keys_pressed[K_SPACE] and self.rect.y > 5:
            self.rect.y -= self.speed


class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed=0, image_wight=0, image_height=0, hearts=1):
        super().__init__(player_image, player_x, player_y, player_speed, image_wight, image_height)
        self.hearts = hearts
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 740:
            self.rect.y = -70
            global skip
            skip += 1
            self.rect.x = randint(30, 380)

class Button():
    def __init__(self, x, y, wight, height, color):
        self.rect = Rect(x, y, wight, height)
        self.color = color
        self.x = x
        self.y = y

    def draw_rect(self, border_color=0, new_color=0):
        if border_color == 0:
            border_color = self.color
        if new_color == 0:
            new_color = self.color
        draw.rect(window, self.color, self.rect)
        draw.rect(window, border_color, self.rect, 5)
    
    def create_text(self, size):
        self.font = font.SysFont('Arial', size)

    def draw_text(self, text_color, text, xofset, yofset):
        question = self.font.render(text, True, text_color)
        window.blit(question, (self.x+xofset, self.y+yofset))


def lose():
    lose = font1.render('YOU LOSE!', True, (255, 0, 0))
    window.blit(lose, (160, 150))
    global end
    end = False

    


x = 700
y = 450
window = display.set_mode((x, y))
display.set_caption('Побег')
background = transform.scale(image.load('background2.jpg'), (x, y))
window.blit(background, (0,0))

hero = Player('herorun.png', 190, 300, 2, 45, 70, 3)






start = Button(150, 300, 150, 65, (255, 255, 255))
start.draw_rect((0, 0, 0))
start.create_text(40)
start.draw_text((0, 0, 0), 'START', 30, 20)

restart = Button(150, 300, 150, 65, (255, 255, 255))




font1 = font.SysFont('Arial', 35)
clock = time.Clock()
end = False
game = True
while game:
    if end:
        window.blit(background, (0,0))
        hero.reset()
        hero.move()
    for e in event.get():
        if e.type == MOUSEBUTTONDOWN and e.button == 1:
            x_button, y_button = e.pos
            if start.rect.collidepoint(x_button, y_button):
                end = True
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(105)   