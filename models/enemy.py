import pygame
import ship

YELLOW_SHIP = pygame.image.load("./images/ship.png")
YELLOW_LASER = pygame.image.load("./images/laser.png")

BLUE_ENEMY = pygame.transform.scale(pygame.image.load("./images/enemy_blue.png"),(YELLOW_SHIP.get_width() - 10,YELLOW_SHIP.get_height() - 10))
GREEN_ENEMY = pygame.transform.scale(pygame.image.load("./images/enemy_green.png"),(YELLOW_SHIP.get_width(),YELLOW_SHIP.get_height()))
PURPLE_ENEMY = pygame.transform.scale(pygame.image.load("./images/enemy_purple.png"),(YELLOW_SHIP.get_width(),YELLOW_SHIP.get_height()))

BLUE_LASER = pygame.image.load("./images/enemy_blue_laser.png")
GREEN_LASER = pygame.image.load("./images/enemy_green_laser.png")
PURPLE_LASER = pygame.image.load("./images/enemy_purple_laser.png")

class Enemy(ship.Ship):
    COLOR_MAP = {
                "blue" : (BLUE_ENEMY,BLUE_LASER),
                "green" : (GREEN_ENEMY,GREEN_LASER),
                "purple" : (PURPLE_ENEMY,PURPLE_LASER)
                }
    
    def __init__(self,x,y,color,health=100):
        super().__init__(x,y,health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pygame.mask.from_surface(self.ship_img)

    def move(self,vel):
        self.y += vel