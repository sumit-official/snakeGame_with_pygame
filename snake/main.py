#pygame is needed to make the game
import pygame
#time to change snakes speed after a time
import time
#random to place the food randomly
import random

#Intializing the pygame
pygame.init()

#setting the background color and the screen dimensions
background_color = (0,0,0)
(width, height) = (600, 400)

#for sound
eatSound = pygame.mixer.Sound('snake.wav')

eatSound.play()

#color
black = (0,0,0)
green = (34,139,34)
red = (255,0,0)

screen = pygame.display.set_mode((width, height))
#The name on top
pygame.display.set_caption('Snake_Game by Sumit Kumar And Vivek Deep')

#To change snake's speed 
clock = pygame.time.Clock()
#snake food 
snake_block = 10
snake_speed = 15

#font_style to be used
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
#this is for the snake to make the snake and change its lenght
def our_snake(snake_block, snake_list):
    for i in snake_list:
        pygame.draw.rect(screen, green, [i[0], i[1], snake_block, snake_block])

#function for message 
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width/6, height/3])


#The actual game running
#everthing that is happing while the game is running should go here
def gameLoop():
    game_over = False
    game_close = False
    #TO move the snake
    #starting location
    x = width/2 
    y = height/2
    #To change its postion and move the snake
    x_change = 0
    y_change  = 0 #in the start it will be 0 and then changed

    snake_List = []
    Lenght_of_snake = 1
    #making the food 
    foodx = round(random.randrange(0,width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0,width - snake_block) / 10.0) * 10.0
    #the game loop anything you put in here makes the game
    while not game_over:
        #this then you lose and want to start again menu
        while game_close == True:
            screen.fill(black)
            message("You Lost! Prees C-Play Again or Q-Quit",red)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #for movement
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -snake_block
                    y_change = 0
                elif event.key == pygame.K_RIGHT:
                    x_change = snake_block
                    y_change = 0
                elif event.key == pygame.K_UP:
                    y_change = -snake_block
                    x_change = 0
                elif event.key == pygame.K_DOWN:
                    y_change = snake_block
                    x_change = 0
        #if the snake goes over the boundies the game should be over
        if x >= width or x < 0 or y >= height or y < 0:
            game_close= True
        #change the values to move the snake
        x += x_change
        y += y_change
        screen.fill(black)
        #Draw the food 
        pygame.draw.rect(screen, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_List.append(snake_Head)
        if len(snake_List) > Lenght_of_snake:
            del snake_List[0]
        for i in snake_List[:-1]:
            if i == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)

        pygame.display.update()

        if x == foodx and y == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            eatSound.play()
            Lenght_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()    
gameLoop()