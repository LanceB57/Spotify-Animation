import lib.qr_code as qr
import lib.logo as logo
import pygame
import sys

## Variables to change
fill_color = (29, 185, 84)
back_color = (0, 0, 0)
link = "https://spotify.com"

## Generate images used in animation
qr.generate_qr_code(link, fill_color, back_color)
logo.generate_colored_logo(fill_color)

## Initialize Pygame
pygame.init()

## Set up some constants
screen_width, screen_height = 800, 600
FPS = 60

## Create the game window
screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

## Set up the clock for a smooth FPS
clock = pygame.time.Clock()

screen.fill(back_color)

qr_code_img = pygame.image.load('tmp/qr_code.png').convert()
qr_rect = qr_code_img.get_rect(center=(screen_width // 2, screen_height // 2))

spotify_img = pygame.image.load('tmp/logo.png').convert_alpha()
spotify_rect = spotify_img.get_rect(center=(screen_width // 2, screen_height // 2))

## Define the animation variables
x = 0
y = 0
dx = 6
dy = 6

## Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.VIDEORESIZE:  ## Handle window resize
            screen_width = event.w
            screen_height = event.h
            screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)

            spotify_rect.center = (screen_width // 2, screen_height // 2)
            spotify_width = int(screen_width * 0.75)
            spotify_height = int(spotify_img.get_height() * (spotify_width / spotify_img.get_width())) ## Scale height accordingly
            spotify_img = pygame.transform.scale(pygame.image.load("tmp/logo.png"), (spotify_width, spotify_height))
            
            x = min(x, screen_width - qr_rect.width)
            y = min(y, screen_height - qr_rect.height)

    ## Fill the screen and place the spotify logo
    screen.fill(back_color)
    screen.blit(spotify_img, (screen.get_width() // 2 - spotify_img.get_width() // 2, screen.get_height() // 2 - spotify_img.get_height() // 2))

    ## Outline the qr code
    outer_rect = qr_rect.inflate(20, 20)
    pygame.draw.rect(screen, fill_color, outer_rect, 10)  # border width

    ## Place the qr code
    screen.blit(qr_code_img, qr_rect)
    qr_rect.x = x
    qr_rect.y = y

    ## Update the qr code's position
    x += dx
    y += dy

    ## Bounce the qr code off the edges
    if x < 0 or x > screen_width - qr_rect.width:
        dx *= -1
    if y < 0 or y > screen_height - qr_rect.height:
        dy *= -1

    ## Update the display
    pygame.display.flip()

    ## Cap the frame rate
    clock.tick(FPS)