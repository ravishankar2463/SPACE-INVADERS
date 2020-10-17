import pygame
import ship
import sys
sys.path.append('../config')

import config

YELLOW_SHIP = pygame.image.load("./images/ship.png")
YELLOW_LASER = pygame.image.load("./images/laser.png")
WIDTH,HEIGHT = config.windowsize()


class Player(ship.Ship):
    def __init__(self,x,y, health = 100):
        super().__init__(x,y,health)
        self.ship_img = YELLOW_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self,vel,objs):
        self.cooldown()
        for laser in self.lasers:
            laser.move(vel)
            if laser.off_screen(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.collision(obj):
                        objs.remove(obj)
                        self.lasers.remove(laser)

    def healthbar(self,window):
        pygame.draw.rect(window, (255,0,0), (self.x,self.y + self.ship_img.get_height()+10, self.ship_img.get_width(),10))
        pygame.draw.rect(window, (0,255,0), (self.x,self.y + self.ship_img.get_height()+10, self.ship_img.get_width() * (self.health/self.max_health),10))

    def draw(self,window):
        super().draw(window)
        self.healthbar(window)