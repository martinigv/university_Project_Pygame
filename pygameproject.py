import pygame
import random # 좀비 생성 시 필요 
import os
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 720
MOVE_SPEED = 5
FPS = 30
check=0
life=5
life_i=0
shootingrange=1
bullet_x=0
bullet_y=0


#zombies 생성을 위한 변수
zombies = []
zombie_x = []
zombie_y = []

zm_speed = 0.5
score = 0


blood_img = pygame.image.load("blood.png")
current_path = os.path.dirname(__file__) # 현재 파일의 위치 반환
image_path = os.path.join(current_path, "images") # images 폴더 위치 반환 

stage = pygame.image.load(os.path.join(image_path, "grassimage1.png"))
stage_size = stage.get_rect().size
stage_height = stage_size[1]


#캐릭터 rect
character = pygame.image.load(os.path.join(image_path, "player.png"))
character_size = character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]


character_bullet = pygame.image.load(os.path.join(image_path, "bullet.png"))

#좀비 생성 함수
def creat_zm():
    global z
    global z_rect
    
    local_create = random.randint(0,5)
    if local_create == 0:
        y = random.randint(680, 719) # 왼쪽 위 모서리에서 생성
        x = random.randint(1, 40)
        zombie_x.append(x)
        zombie_y.append(y)
        z = pygame.image.load('zombie1.png')
        z_rect = z.get_rect()
        zombies.append(z)
    elif local_create == 1:
        y = random.randint(680, 719) # 가운데 위에서 생성
        x = random.randint(480, 520)
        zombie_x.append(x)
        zombie_y.append(y)
        z = pygame.image.load('zombie1.png')
        z_rect = z.get_rect()
        zombies.append(z)
    elif local_create == 2:
        y = random.randint(680, 719) # 오른쪽 위 모서리에서 생성
        x = random.randint(960, 999)
        zombie_x.append(x)
        zombie_y.append(y)
        z = pygame.image.load('zombie1.png')
        z_rect = z.get_rect()
        zombies.append(z)
    elif local_create == 3:
        y = random.randint(1, 40) # 왼쪽 아래 모서리에서 생성
        x = random.randint(1, 40)
        zombie_x.append(x)
        zombie_y.append(y)
        z = pygame.image.load('zombie1.png')
        z_rect = z.get_rect()
        zombies.append(z)
    elif local_create == 4:
        y = random.randint(1, 40) # 가운데 아래에서 생성
        x = random.randint(480, 520)
        zombie_x.append(x)
        zombie_y.append(y)
        z = pygame.image.load('zombie1.png')
        z_rect = z.get_rect()
        zombies.append(z)
    else:
        y = random.randint(1, 40) # 오른쪽 아래 모서리에서 생성
        x = random.randint(960, 999)
        zombie_x.append(x)
        zombie_y.append(y)
        z = pygame.image.load('zombie1.png')
        z_rect = z.get_rect()
        zombies.append(z)


# 좀비 사진 출력 함수            
def zombie(x, y, i):
    screen.blit(zombies[i], (x,y))
    
#좀비 이동 함수
def move_zm():
    global pl_x
    global pl_y
    
    for i in range(len(zombies)):
        
        if (zombie_x[i] > pl_x): 
            zombie_x[i] -= zm_speed
        elif (zombie_x[i] < pl_x):
            zombie_x[i] += zm_speed
        if (zombie_y[i] > pl_y):
            zombie_y[i] -= zm_speed
        elif (zombie_y[i] < pl_y):
            zombie_y[i] += zm_speed

        zombie(zombie_x[i],zombie_y[i], i)
        
        

pl_x = int(SCREEN_WIDTH / 2)
pl_y = int(SCREEN_HEIGHT * 0.5)
pygame.display.set_caption('파이게임')
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# 배경 이미지 로드 후 화면에 맞게 크기 조절
img_bg = pygame.image.load('grassimage1.png')
img_bg = pygame.transform.scale(img_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# 플레이어 이미지 로드 후 크기 조절 및 위치 값 초기화
img_player = pygame.image.load('player.png')
img_player = pygame.transform.scale(
    img_player, (img_player.get_width() , img_player.get_height() ))
player = img_player.get_rect()
player.center = (SCREEN_WIDTH / 2, SCREEN_HEIGHT * 0.5)

img_bullet = pygame.image.load('bullet.png')
img_bullet = pygame.transform.scale(
    img_bullet, (img_bullet.get_width() , img_bullet.get_height() ))
bullet = img_bullet.get_rect()


#총알 발사
def bulletFire():
    global pl_y, pl_x, score
    bullet_x = pl_x
    bullet_y = pl_y

    if pressed_keys[pygame.K_SPACE]:
        if check==1:
            for i in range (100):
                bullet_x=bullet_x-shootingrange
                bullet.center = (bullet_x, bullet_y)
                screen.blit(img_bullet, bullet)
                pygame.display.update()

                for i in range(len(zombies)):
                    zombie_rect = z.get_rect()
                    zombie_rect.left = zombie_x[i]
                    zombie_rect.top = zombie_y[i]
                    bullet_rect=character_bullet.get_rect()
                    bullet_rect.left = bullet_x
                    bullet_rect.top = bullet_y
                    if bullet_rect.colliderect(zombie_rect):
                        score+=1
                    
                        pygame.display.flip()
                        local_create = random.randint(0,5)
                        if local_create == 0:
                            zombie_y[i] = random.randint(680, 719) # 왼쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 1:
                            zombie_y[i] = random.randint(680, 719) # 가운데 위에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        elif local_create == 2:
                            zombie_y[i] = random.randint(680, 719) # 오른쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)
                        elif local_create == 3:
                            zombie_y[i] = random.randint(1, 40) # 왼쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 4:
                            zombie_y[i] = random.randint(1, 40) # 가운데 아래에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        else:
                            zombie_y[i] = random.randint(1, 40) # 오른쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)
        elif check==2:
            for i in range(100):
                bullet_x=bullet_x+shootingrange
                bullet.center = (bullet_x, bullet_y)
                screen.blit(img_bullet, bullet)
                pygame.display.update()

                for i in range(len(zombies)):
                    zombie_rect = z.get_rect()
                    zombie_rect.left = zombie_x[i]
                    zombie_rect.top = zombie_y[i]
                    bullet_rect=character_bullet.get_rect()
                    bullet_rect.left = bullet_x
                    bullet_rect.top = bullet_y
                    if bullet_rect.colliderect(zombie_rect):
                        score+=1
                    
                        pygame.display.flip()
                        local_create = random.randint(0,5)
                        if local_create == 0:
                            zombie_y[i] = random.randint(680, 719) # 왼쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 1:
                            zombie_y[i] = random.randint(680, 719) # 가운데 위에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        elif local_create == 2:
                            zombie_y[i] = random.randint(680, 719) # 오른쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)
                        elif local_create == 3:
                            zombie_y[i] = random.randint(1, 40) # 왼쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 4:
                            zombie_y[i] = random.randint(1, 40) # 가운데 아래에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        else:
                            zombie_y[i] = random.randint(1, 40) # 오른쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)


                          
        elif check==3:
            for i in range(100):
                bullet_y=bullet_y-shootingrange
                bullet.center = (bullet_x, bullet_y)
                screen.blit(img_bullet, bullet)
                pygame.display.update()

                for i in range(len(zombies)):
                    zombie_rect = z.get_rect()
                    zombie_rect.left = zombie_x[i]
                    zombie_rect.top = zombie_y[i]
                    bullet_rect=character_bullet.get_rect()
                    bullet_rect.left = bullet_x
                    bullet_rect.top = bullet_y
                    if bullet_rect.colliderect(zombie_rect):
                        score+=1
                       
                        pygame.display.flip()
                        local_create = random.randint(0,5)
                        if local_create == 0:
                            zombie_y[i] = random.randint(680, 719) # 왼쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 1:
                            zombie_y[i] = random.randint(680, 719) # 가운데 위에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        elif local_create == 2:
                            zombie_y[i] = random.randint(680, 719) # 오른쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)
                        elif local_create == 3:
                            zombie_y[i] = random.randint(1, 40) # 왼쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 4:
                            zombie_y[i] = random.randint(1, 40) # 가운데 아래에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        else:
                            zombie_y[i] = random.randint(1, 40) # 오른쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)

        elif check==4:
            for i in range(100):
                bullet_y=bullet_y+shootingrange 
                bullet.center = (bullet_x, bullet_y)
                screen.blit(img_bullet, bullet)
                pygame.display.update()

                for i in range(len(zombies)):
                    zombie_rect = z.get_rect()
                    zombie_rect.left = zombie_x[i]
                    zombie_rect.top = zombie_y[i]
                    bullet_rect=character_bullet.get_rect()
                    bullet_rect.left = bullet_x
                    bullet_rect.top = bullet_y
                    if bullet_rect.colliderect(zombie_rect):
                        score+=1
                        
                        pygame.display.flip()
                        local_create = random.randint(0,5)
                        if local_create == 0:
                            zombie_y[i] = random.randint(680, 719) # 왼쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 1:
                            zombie_y[i] = random.randint(680, 719) # 가운데 위에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        elif local_create == 2:
                            zombie_y[i] = random.randint(680, 719) # 오른쪽 위 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)
                        elif local_create == 3:
                            zombie_y[i] = random.randint(1, 40) # 왼쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(1, 40)
                        elif local_create == 4:
                            zombie_y[i] = random.randint(1, 40) # 가운데 아래에서 생성
                            zombie_x[i] = random.randint(480, 520)
                        else:
                            zombie_y[i] = random.randint(1, 40) # 오른쪽 아래 모서리에서 생성
                            zombie_x[i] = random.randint(960, 999)
#쿨타임
class Unit():
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
    def fire(self):
        # 0.3초 쿨타임
        now = pygame.time.get_ticks()
        if now-self.last >= self.cooldown:
            self.last = now
            bulletFire()

#체력칸 쿨타임
class HP_cooltime():
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 1000
    def cool(self):
        global life_i
        character_y_pos=pl_y
        character_x_pos=pl_x
        # 1초 쿨타임
        now = pygame.time.get_ticks()
        for i in range(len(zombies)):
            zombie_rect=z.get_rect()
            zombie_rect.left = zombie_x[i]
            zombie_rect.top = zombie_y[i]
            character_rect = character.get_rect()
            character_rect.left = character_x_pos
            character_rect.top = character_y_pos
            if character_rect.colliderect(zombie_rect):
                if now-self.last >= self.cooldown:
                    self.last = now
                    print( "좀비에게 물려 체력이 줄었습니다. (1초 무적)")
                    life_i+=1
                
#HP바
img_hp_bar_1 = pygame.image.load('hp_bar.png')
img_hp_bar_1 = pygame.transform.scale(
    img_hp_bar_1, (img_hp_bar_1.get_width() , img_hp_bar_1.get_height() ))
hp_bar_1 = img_hp_bar_1.get_rect()
hp_bar_1.center = (460, 20)

img_hp_bar_2 = pygame.image.load('hp_bar.png')
img_hp_bar_2 = pygame.transform.scale(
    img_hp_bar_2, (img_hp_bar_2.get_width() , img_hp_bar_2.get_height() ))
hp_bar_2 = img_hp_bar_2.get_rect()
hp_bar_2.center = (480, 20)

img_hp_bar_3 = pygame.image.load('hp_bar.png')
img_hp_bar_3 = pygame.transform.scale(
    img_hp_bar_3, (img_hp_bar_3.get_width() , img_hp_bar_3.get_height() ))
hp_bar_3 = img_hp_bar_3.get_rect()
hp_bar_3.center = (500, 20)

img_hp_bar_4 = pygame.image.load('hp_bar.png')
img_hp_bar_4 = pygame.transform.scale(
    img_hp_bar_4, (img_hp_bar_4.get_width() , img_hp_bar_4.get_height() ))
hp_bar_4 = img_hp_bar_4.get_rect()
hp_bar_4.center = (520, 20)

img_hp_bar_5 = pygame.image.load('hp_bar.png')
img_hp_bar_5 = pygame.transform.scale(
    img_hp_bar_5, (img_hp_bar_5.get_width() , img_hp_bar_5.get_height() ))
hp_bar_5 = img_hp_bar_5.get_rect()
hp_bar_5.center = (540, 20)

# 라벨 생성
def fontsize(size):
    font = pygame.font.SysFont("Arial", size)
    return font
 
font_default = fontsize(20)

labels = []
class Label:
 
	''' CLASS FOR TEXT LABELS ON THE WIN SCREEN SURFACE ''' # 코드 참조
	def __init__(self, screen, text, x, y, size=20, color="white"):
		if size != 20:
			self.font = fontsize(size)
		else:
			self.font = font_default
		self.image = self.font.render(text, 1, color)
		_, _, w, h = self.image.get_rect()
		self.rect = pygame.Rect(x, y, w, h)
		self.screen = screen
		self.text = text
		labels.append(self)
 
	def change_text(self, newtext, color="white"):
		self.image = self.font.render(newtext, 1, color)
 
	def change_font(self, font, size, color="white"):
		self.font = pygame.font.SysFont(font, size)
		self.change_text(self.text, color)
 
	def draw(self):
		self.screen.blit(self.image, (self.rect))
 
 
def show_labels():
	for _ in labels:
		_.draw()
#메인
shootingbullet=Unit()
HP=HP_cooltime()
done = False
while not done:
    HP.cool()
    if life_i == 1:
        img_hp_bar_5 = pygame.image.load('hitted_hp_bar.png')
    elif life_i == 2:
        img_hp_bar_4 = pygame.image.load('hitted_hp_bar.png')
    elif life_i == 3:
        img_hp_bar_3 = pygame.image.load('hitted_hp_bar.png')
    elif life_i == 4:
        img_hp_bar_2 = pygame.image.load('hitted_hp_bar.png')
    elif life_i >= 5:
        img_hp_bar_1 = pygame.image.load('hitted_hp_bar.png')
        screen.fill(0)
        screen.blit(blood_img,(20,20))
        Label(screen, "Game Over", 300, 250, 50)
        show_labels()
        screen.blit(scoretext, (300, 300))
        pygame.display.update()
        pygame.time.delay(1500)
        done = True
        
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed_keys = pygame.key.get_pressed()
    if pressed_keys[pygame.K_LEFT] or pressed_keys[pygame.K_a]:
        if pl_x <= 1:
            pl_x = pl_x + MOVE_SPEED # 벽 넘어가지 않게 하기 위해
            player.left += MOVE_SPEED
        player.left -= MOVE_SPEED
        pl_x = pl_x - MOVE_SPEED
        check=1
        pygame.display.update()
        
    elif pressed_keys[pygame.K_RIGHT] or pressed_keys[pygame.K_d]:
        if pl_x >= 1000:
            pl_x = pl_x - MOVE_SPEED
            player.left -= MOVE_SPEED
        player.left += MOVE_SPEED
        pl_x = pl_x + MOVE_SPEED
        check=2
        pygame.display.update()
    elif pressed_keys[pygame.K_UP] or pressed_keys[pygame.K_w]:
        if pl_y <= 1:
            pl_y = pl_y + MOVE_SPEED
            player.top += MOVE_SPEED
        player.top -= MOVE_SPEED
        pl_y = pl_y - MOVE_SPEED
        check=3
        pygame.display.update()
    elif pressed_keys[pygame.K_DOWN] or pressed_keys[pygame.K_s]:
        if pl_y >= 720:
            pl_y = pl_y - MOVE_SPEED
            player.top -= MOVE_SPEED
        player.top += MOVE_SPEED
        pl_y = pl_y + MOVE_SPEED
        check=4
        pygame.display.update()

    shootingbullet.fire()
    screen.blit(img_bg, (0, 0))
    screen.blit(img_player, player)
    screen.blit(img_bullet, bullet)
    screen.blit(img_hp_bar_1, hp_bar_1)
    screen.blit(img_hp_bar_2, hp_bar_2)
    screen.blit(img_hp_bar_3, hp_bar_3)
    screen.blit(img_hp_bar_4, hp_bar_4)
    screen.blit(img_hp_bar_5, hp_bar_5)
    if len(zombies) <= 50:
        creat_zm()
    
    move_zm()
    
    scoretext = pygame.font.SysFont("monospace", 50).render("SCORE:"+str(score), 1, (255,255,255))
    screen.blit(scoretext, (100, 10))

    pygame.display.update()
    clock.tick(60)

 