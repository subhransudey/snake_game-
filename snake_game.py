import  pygame
import  random
import  os

# initialize pygame
pygame.init()
# initialize mixer for sound
pygame.mixer.init()


# creating window
screen_width  = 600
screen_height = 600
game_window = pygame.display.set_mode((screen_width,screen_height))
#  background image
background_image_1 = pygame.image.load("snake1.jpg")
background_image_1 = pygame.transform.scale(background_image_1,(screen_width,screen_height)).convert_alpha()
# create game title
pygame.display.set_caption("SnakesWithSubhransu")
pygame.display.update()

# color
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green  = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
clock = pygame.time.Clock()
font = pygame.font.SysFont(None,50)
def on_screen_text(text,color,x,y):
    on_screen_text = font.render(text,True,color)
    game_window.blit(on_screen_text,[x,y])

# increasing snake length

def plot_snake(game_window,color,snake_list,size):
    for x,y in snake_list :
        pygame.draw.rect(game_window,color,[x,y,size,size])

# welcome screen
def welcome_screen():

    exit_game = False
    while not  exit_game :
        game_window.fill((255,204,255))
        game_window.blit(background_image_1, (0, 0))
        on_screen_text("Welcome to Snakes",white,120,260)
        on_screen_text("Press Space To Continue",yellow,90,300)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)



# game loop
def gameloop():
    pygame.mixer.music.load("background.mp3")
    pygame.mixer.music.play()
    # game specific variable
    exit_game = False
    game_over = False
    snake_x = 50
    snake_y = 50
    snake_size = 10
    velocity_x = 0
    velocity_y = 0
    init_velocity = 2
    """to measure velocity we need to measure time """
    fps = 60
    # creating foods
    food_x = random.randint(10, screen_width * 0.9)
    food_y = random.randint(10, screen_height * 0.9)
    food_size = 10

    # making score
    score = 0
    snake_list = []
    snake_length = 1
    # high score printing
    # check if highscore.txt file exist or not
    if (not os.path.exists("highscore.txt")):
        with open("highscore.txt","w") as f :
            f.write("0")
    with open("highscore.txt", "r") as f:
        highscore = f.read()  # note that here highscore read as in string format

    while not  exit_game:

        if game_over :
            with open("highscore.txt", "w") as f:
                f.write(str(highscore)) # we are writting score as a string
            game_window.fill(yellow)

            on_screen_text("Game Over ! ",red,165 ,250)
            on_screen_text("Press Enter To Continue",red,75,305)
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT: # to close game window using cross  button.
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome_screen()


        else:
            for event in pygame.event.get():
                #print(event)
                if event.type == pygame.QUIT: # to close game window using cross  button.
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y =0
                    if event.key == pygame.K_LEFT:
                        velocity_x =  -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y =  -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                       velocity_y = init_velocity
                       velocity_x = 0
                    if event.key == pygame.K_q: # cheat code for increasing score
                        score += 5
                        highscore += 5

            snake_x += velocity_x
            snake_y += velocity_y

            if abs(snake_x - food_x) < 10 and abs(snake_y- food_y)<10:
                score +=10
                snake_length += 4


                food_x = random.randint(10, screen_width*0.9)
                food_y = random.randint(10, screen_height*0.9)

                if score > int(highscore):
                    highscore = score
                    print(highscore)

            game_window.fill((102,255,255)) # filling color in the game window

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)
            if len(snake_list) > snake_length:
                del  snake_list[0]
            if snake_x <0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over = True
                pygame.mixer.music.load("explosion.mp3")
                pygame.mixer.music.play()
                # print("Game Over")
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("explosion.mp3")
                pygame.mixer.music.play()
            plot_snake(game_window,black,snake_list,snake_size)
            pygame.draw.rect(game_window, red, [food_x, food_y, food_size, food_size]) # plotting foods in game window
            on_screen_text(f"score : {score}    high score : {highscore}", red, 5, 5)# to show on screen score
        pygame.display.update()
        clock.tick(fps)


    pygame.quit()
    quit()
welcome_screen()
