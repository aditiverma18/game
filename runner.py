
import pygame
from sys import exit
import pandas as pd
import os

pygame.init() #starts and initiats all parts of pygame
screen = pygame.display.set_mode((800,400)) #((width,height)) of the game screen
pygame.display.set_caption('runner') #changes the name of the window
clock=pygame.time.Clock()
test_font=pygame.font.Font("graphics\Pixeltype.ttf",50)
game_active=True

high_score_file="highest_score.txt"

if os.path.exists(high_score_file):
    with open(high_score_file, 'r') as file:
        high_score = int(file.read().strip())
else:
    high_score = 0

sky_surface=pygame.image.load('graphics/Sky.png').convert()
ground_surface=pygame.image.load('graphics/ground.png').convert()
score_surf=test_font.render('',False,(64,64,64)) 
score_rect=score_surf.get_rect(center=(400,50))
snail_surface=pygame.image.load('graphics\snail1.png').convert_alpha() #use surface for image information and for placements use rectangles
snail_x_position=600
player_surface=pygame.image.load('graphics\player_walk_1.png').convert_alpha()
player_rect=player_surface.get_rect(midbottom=(80,300))
snail_rect=snail_surface.get_rect(midbottom=(snail_x_position,300))
player_gravity=0
score=0


def display_score():
    score_surf = test_font.render(f'Score: {score}', False, (64, 64, 64))
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)

while True: #our entire game runs inside this loop 
    for event in pygame.event.get():
        if event.type==pygame.QUIT:  #cross button appears to close the window
          pygame.quit()
          exit() #the while true loop also terminate
       # if event.type==pygame.MOUSEMOTION:
          # if player_rect.collidepoint(event.pos):
           #  print("collision")
    #draw all our elements
    #update everything
        if game_active:    
          if event.type==pygame.KEYDOWN:
           if event.key==pygame.K_SPACE and player_rect.bottom>=300:
            player_gravity=-20       
        else:
          if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
           game_active=True
           snail_rect.left=800
          
          
    if game_active:    
     screen.blit(sky_surface,(0,0))  #((from left,from top))
     screen.blit(ground_surface,(0,300)) 
     pygame.draw.rect(screen,(204,224,255),score_rect) #(surface we are drwaing on,colour,rect,optional(for border rounding))
    
     screen.blit(score_surf,score_rect)
     display_score()
     player_rect.left=48

     player_gravity+=1
     player_rect.y+=player_gravity
     if player_rect.bottom>=300:
        player_rect.bottom=300
     screen.blit(player_surface,player_rect)
     snail_rect.x-=8
     if snail_rect.right <=0:
        score=score+1
        snail_rect.left=800
    #print(player_rect.colliderect(snail_rect)) #returns zero/false if there is no collision and returns 1/true if there is  collison
     mouse_pos=pygame.mouse.get_pos()
    #print(player_rect.collidepoint(mouse_pos))
     screen.blit(snail_surface,snail_rect)

     if snail_rect.colliderect(player_rect):
        game_active=False
    else:
      screen.fill('black')
      game_surf=test_font.render('GAME OVER',False,(223,233,79))
      game_rect=game_surf.get_rect(center=(400,90))
      screen.blit(game_surf,game_rect)
      score=0
      high_score_surf = test_font.render(f'High Score: {high_score}', False, (223, 233, 79))
      high_score_rect = high_score_surf.get_rect(center=(400, 150))
      screen.blit(high_score_surf, high_score_rect)

    pygame.display.update() #it updates the upper display surface
    clock.tick(60) #tells the computer that the while true loop should not run faster than 60 times per second

   
    
    
