import pygame

class Ship():

    def __init__(self, screen):
        """初始化飞船及其位置"""
        self.screen = screen

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘新飞船放在底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1
        elif self.moving_up:
            self.rect.centery -= 1
        elif self.moving_down:
            self.rect.centery += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
