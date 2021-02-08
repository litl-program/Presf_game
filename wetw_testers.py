import pygame
import random
from os import path



WIDTH = 1200
HEIGHT = 800
FPS = 60

caunt_bool = 30

mobkil = (20, 50)
mobkil_bese = (20, 50)
# Р—Р°РґР°РµРј С†РІРµС‚Р°
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# РЎРѕР·РґР°РµРј РёРіСЂСѓ Рё РѕРєРЅРѕ
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BABAK AMMM")
clock = pygame.time.Clock()

#pygame.mixer.music.load('love_tension.ogg')
#pygame.mixer.music.set_volume(0.5)
#pygame.mixer.music.play()
pygame.mixer.music.load('litl_oprel.ogg')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
      

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -8
        if keystate[pygame.K_RIGHT]:
            self.speedx = 8
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        
    

    def shoot(self,):
        bullet = Bullet(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)
        
        



class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = meteor_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(1, 10)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
        

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y += self.speedy
        # СѓР±РёС‚СЊ, РµСЃР»Рё РѕРЅ Р·Р°С…РѕРґРёС‚ Р·Р° РІРµСЂС…РЅСЋСЋ С‡Р°СЃС‚СЊ СЌРєСЂР°РЅР°
        if self.rect.bottom < 0:
            self.kill()



# Р—Р°РіСЂСѓР·РєР° РІСЃРµР№ РёРіСЂРѕРІРѕР№ РіСЂР°С„РёРєРё
background = pygame.image.load("Space.jpg")
background_rect = background.get_rect()
player_img = pygame.image.load("p1_front.png")
player_img = pygame.transform.scale(player_img,(80,20))
meteor_img = pygame.image.load("oponents.jpg")
meteor_img = pygame.transform.scale(meteor_img,(40,58))
bullet_img = pygame.image.load("bol.jpg")
bullet_img = pygame.transform.scale(bullet_img,mobkil)
backgrounds = pygame.image.load("bg.webp")
background_rects = background.get_rect()
backgrounds = pygame.transform.scale(backgrounds,(WIDTH,HEIGHT))


font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)




all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(15):
    m = Mob()
    all_sprites.add(m)  
    mobs.add(m)


score = 0
caunt_bool = 10

status = True

# Р¦РёРєР» РёРіСЂС‹
running = True
while running:
    bullet_img = pygame.transform.scale(bullet_img,mobkil)
    # Р”РµСЂР¶РёРј С†РёРєР» РЅР° РїСЂР°РІРёР»СЊРЅРѕР№ СЃРєРѕСЂРѕСЃС‚Рё
    clock.tick(FPS)
    # Р’РІРѕРґ РїСЂРѕС†РµСЃСЃР° (СЃРѕР±С‹С‚РёСЏ)
    for event in pygame.event.get():
        # РїСЂРѕРІРµСЂРєР° РґР»СЏ Р·Р°РєСЂС‹С‚РёСЏ РѕРєРЅР°
        if event.type == pygame.QUIT:
            pygame.time.wait (120)
            screen.blit(background, background_rect)
            running = False
        # if caunt_bool == 0:
        #     status = False
        elif event.type == pygame.KEYDOWN:
            if status == True:
                if event.key == pygame.K_SPACE:
                    player.shoot()
                    caunt_bool -= 1
                # if event.key == pygame.K_r:
                #     caunt_bool = 30
            if caunt_bool == 0:
                status = False
                if event.key == pygame.K_r:
                    caunt_bool = 5
                    score = 1
                    status = True
            # elif status == False:
            #     if event.key == pygame.K_DOWN:
            #         status = True
            #         caunt_bool += 30




    # РћР±РЅРѕРІР»РµРЅРёРµ
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        m = Mob()
        caunt_bool += random.randint(0,3)
        score += 1
        mobkil = (mobkil_bese[0], mobkil_bese[1] + score // 10)
        all_sprites.add(m)
        mobs.add(m)

    

    # РџСЂРѕРІРµСЂРєР°, РЅРµ СѓРґР°СЂРёР» Р»Рё РјРѕР± РёРіСЂРѕРєР°
    hits = pygame.sprite.spritecollide(player, mobs, True)
    if hits:
        score -= 10
        if score < 0:
            screen.blit(backgrounds, background_rects)
            pygame.display.flip()
            #pygame.mixer.music.play()
            pygame.time.wait (14000)
            running = False


    
    # Р РµРЅРґРµСЂРёРЅРі
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    text = pygame.font.SysFont('serif',14)
    text1 = text.render(f"Знищено Бабаків {score}", False,WHITE)
    bull = pygame.font.SysFont('serif',18)
    text3 = bull.render(f"Лабораторні роботи {caunt_bool}", True , RED)

    screen.blit(text1,(5,5))
    screen.blit(text3,(1000,700))
    all_sprites.draw(screen)

    # РџРѕСЃР»Рµ РѕС‚СЂРёСЃРѕРІРєРё РІСЃРµРіРѕ, РїРµСЂРµРІРѕСЂР°С‡РёРІР°РµРј СЌРєСЂР°РЅ
    pygame.display.flip()

pygame.quit()