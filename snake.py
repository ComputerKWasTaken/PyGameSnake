#Python snake game by Archer Hosford

import pygame
import random
import time

pygame.init()

#colors
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

#display
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake')

#clock
clock = pygame.time.Clock()

#snake
snake_block = 20
snake_speed = 10

#fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#functions
#draws the snake
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, green, [x[0], x[1], snake_block, snake_block])

#displays messages
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    gameDisplay.blit(mesg, [display_width/6, display_height/3])

#main game loop
def game_loop():
    game_over = False
    #starting position of the snake
    game_close = False

    #starting speed of the snake
    x1 = display_width / 2
    y1 = display_height / 2
    #starting position of the food

    x1_change = 0
    #main game loop
    y1_change = 0
        #game over loop

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0

    while not game_over:

        #event loop
        while game_close == True:
            gameDisplay.fill(black)
            message("You Lost! Press C to Play Again or Q to Quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and x1_change != snake_block:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_d and x1_change != -snake_block:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_w and y1_change != snake_block:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_s and y1_change != -snake_block:
                    y1_change = snake_block
        #if the snake hits the edge of the screen
                    x1_change = 0

        if x1 >= display_width or x1 < 0 or y1 >= display_height or y1 < 0:
            game_close = True
        #draws the background
        x1 += x1_change
        #draws the food
        y1 += y1_change
        #draws the snake
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        #if the snake is longer than the length of the snake
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
        #if the snake hits itself
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
        #draws the snake
                game_close = True

        #if the snake eats the food
        our_snake(snake_block, snake_List)

        #sets the speed of the snake
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, display_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, display_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop()
