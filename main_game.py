import pygame, sys
import time
import random
import os

pygame.init()

white =  (52,57,84)          #(30,36,66)-**Dark Blue       #(52,57,84)
black = (0, 0, 0)
red = (238,0,0)
salmon = (250, 128, 114)
green_head = (16,88,0)
green_body = (33,176,1)
white2 = (255, 255, 255)

clock = pygame.time.Clock()

display_width = 800
display_height = 682

snake_block_size = 13
block_size = 9

game_Display = pygame.display.set_mode((display_width, display_height))
border = pygame.image.load(os.path.join('border3.png'))
# png = pygame.image.load(os.path.join('char.gif'))
pygame.display.set_caption('Slytherine')



pygame.display.update()

font = pygame.font.SysFont('Comic Sans MS', 20)
score_font = pygame.font.SysFont('Comic Sans MS', 32)

def message_to_screen(msg, color):
    screen_text = font.render(msg, True, color)
    game_Display.blit(screen_text, (display_width/2, display_height/2))

def score_in_screen(msg, color):
    screen_text = score_font.render(msg, True, color)
    game_Display.blit(screen_text, ((display_width)- 160, (display_height - 30)))

def snake_function(snake_block_size, snakeList):
    counter = 0

    for XnY in snakeList:
        counter += 1
        if counter == len(snakeList):
            game_Display.fill(green_head, rect = [XnY[0], XnY[1], snake_block_size, snake_block_size])
        else:
            game_Display.fill(green_body, rect = [XnY[0], XnY[1], snake_block_size, snake_block_size])

# def game_pause(gamePause):
#     while gamePause:
#         for event in pygame.event.get():
#             print(gamePause)
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     gamePause == False
#     return gamePause

def game_pause():
    while 1:
        e = pygame.event.wait()
        if e.type in (pygame.QUIT, pygame.KEYDOWN):
            return

def gameLoop():

    FPS = 13

    Lead_x = display_width/2
    Lead_y = display_height/2

    randAppleX = display_width/2
    randAppleY = display_height/2

    Lead_x_continue = 0
    Lead_y_continue = 0

    snakeList = []
    snakeLength = 10

    gameExit = False
    gameOver = False
    gamePause = False

    foodEating = 0

    kbhit = 0
    collision = 0
    key_pressed = False
    first_time = 0
    score = -5

    # if(Lead_x == randAppleX or Lead_y == randAppleY):
    #     randAppleX = random.randrange(0, display_width - block_size)
    #     randAppleY = random.randrange(0, display_height - block_size)



    while not gameExit:

        first_time += 1

        while gameOver == True:
            game_Display.fill(salmon)
            message_to_screen("Game Over press C to continue and Q to quit", white)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        gameLoop()

        # for event in pygame.event.get():
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_SPACE:
        #             gamePause = game_pause(gamePause)


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
            # print(event)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and kbhit != 2:
                    Lead_x_continue = -block_size
                    Lead_y_continue = 0
                    kbhit = 1
                    key_pressed = True
                elif event.key == pygame.K_RIGHT and kbhit != 1:
                    Lead_x_continue = block_size
                    Lead_y_continue = 0
                    kbhit = 2
                    key_pressed = True
                elif event.key == pygame.K_UP and kbhit != 4:
                    Lead_y_continue = -block_size
                    Lead_x_continue = 0
                    kbhit = 3
                    key_pressed = True
                elif event.key == pygame.K_DOWN and kbhit != 3:
                    Lead_y_continue = block_size
                    Lead_x_continue = 0
                    kbhit = 4
                    key_pressed = True

                elif event.key == pygame.K_SPACE:
                    # gamePause = True
                    # gamePause = game_pause(gamePause)
                    game_pause()




        if (Lead_x >= display_width-41 or Lead_x < 41 or Lead_y >= display_height-81 or Lead_y < 41):
            gameOver = True

        if((Lead_x >= randAppleX-block_size and Lead_x <= randAppleX+block_size)and(Lead_y >= randAppleY-block_size and Lead_y <= randAppleY+block_size)):
            randAppleX = random.randrange(42, display_width - block_size - 42)
            randAppleY = random.randrange(42, display_height - block_size - 82)
            foodEating += 1
            score += 5
            # print(foodEating)
            # print(randAppleY)

            if(foodEating%3 == 0):
                FPS += 1
                snakeLength += 5
                print(FPS)


        Lead_x += Lead_x_continue
        Lead_y += Lead_y_continue

        snakeHead = []
        snakeHead.append(Lead_x)
        snakeHead.append(Lead_y)

        if len(snakeList) > snakeLength:
            del(snakeList[0])
            for elements in snakeList:
                if(elements[0] == Lead_x and elements[1] == Lead_y):
                    gameOver = True

        if(key_pressed or first_time == 1):
            snakeList.append(snakeHead)


        game_Display.fill(white)
        game_Display.blit(border,(0, 0))
        # game_Display.blit(png, ((display_width)/2, (display_height)/2))
        # pygame.draw.rect(game_Display, black, [400, 300, 100, 100]) this is the way to draw shapes but it aint the graphics accelrating way
        game_Display.fill(red, rect = [randAppleX, randAppleY, block_size, block_size])
        # pygame.draw.circle(game_Display, red, [randAppleX, randAppleY], block_size)
        snake_function(snake_block_size, snakeList)

        score_in_screen("Score : "+str(score), white2)
        pygame.display.update()

        pygame.display.update()
        clock.tick(FPS)


    pygame.quit()
    quit()

gameLoop()
