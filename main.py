import pygame
import time
import random
import os
import sys
pygame.font.init()
sys.path.append('./models/')
sys.path.append('./config')

import ship
import player as p
import enemy as e
import config

WIDTH,HEIGHT = config.windowsize()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SPACE INVADERS")

BG = pygame.transform.scale(pygame.image.load("./images/background.jpg"),(WIDTH, HEIGHT))

def main():
    run = True
    FPS = 60
    clock = pygame.time.Clock()
    level = 0
    lives = 5
    main_font = pygame.font.Font("./fonts/space_invaders.ttf",20)
    lost_font = pygame.font.Font("./fonts/space_invaders.ttf",30)
    player_vel = 5
    enemy_vel = 1
    player = p.Player((WIDTH/2) - 25,430)
    enemies = []
    wave_length = 5
    lost = False
    lost_count = 0
    laser_vel = 4

    def redraw_window():
        WIN.blit(BG,(0,0))
        lives_label = main_font.render(f"Lives: {lives}",1,(255,255,255))
        level_label = main_font.render(f"Level: {level}",1,(255,255,255))

        WIN.blit(lives_label, (10,10))
        WIN.blit(level_label, (WIDTH - level_label.get_width() -10,10))


        for enemy in enemies:
            enemy.draw(WIN)
        
        player.draw(WIN)

        if lost:
            lost_label = lost_font.render("YOU LOST!!",1,(255,255,255))
            WIN.blit(lost_label, (WIDTH/2 - lost_label.get_width()/2,HEIGHT/2))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        if lives <= 0 or player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS * 3:
                run = False
            else:
                continue

        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = e.Enemy(random.randrange(50,WIDTH - 50), random.randrange(-1500,-100), random.choice(["blue","green","purple"]))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - player_vel > 0:
            player.x -= player_vel
        if keys[pygame.K_RIGHT] and player.x + player_vel + player.get_width() < WIDTH:
            player.x += player_vel
        if keys[pygame.K_UP] and player.y - player_vel > 0:
            player.y -= player_vel
        if keys[pygame.K_DOWN] and player.y + player_vel + player.get_height() < HEIGHT:
            player.y += player_vel
        if keys[pygame.K_SPACE]:
            player.shoot()
        
        for enemy in enemies[:]:
            enemy.move(enemy_vel)
            enemy.move_lasers(laser_vel,player)

            if random.randrange(0,3 * FPS) == 1:
                enemy.shoot()
            
            if ship.collide(enemy,player):
                player.health -= 10
                enemies.remove(enemy)
            elif enemy.y + enemy.get_height() > HEIGHT:
                lives -= 1
                enemies.remove(enemy)
                
        player.move_lasers(-laser_vel,enemies)

def main_menu():
    title_font = pygame.font.Font("./fonts/space_invaders.ttf",20)
    run = True
    while run:
        WIN.blit(BG,(0,0))
        title_label = title_font.render("Press the mouse to begin..", 1, (255,255,255))
        WIN.blit(title_label,(WIDTH/2 - title_label.get_width()/2, HEIGHT/2))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.quit()

main_menu()