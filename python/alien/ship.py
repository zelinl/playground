import pygame

class Ship():

    def __init__(self, screen):
        """初始化飞船及其位置"""
        self.screen = screen

        #加载飞船图像并获取外接矩形
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)
