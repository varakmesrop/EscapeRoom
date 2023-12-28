import pygame
import os


# to use sound and writing
pygame.mixer.init()
pygame.font.init()

# for different loops, (understand later)
n = 1

# for the tries
t = 0
r = 0

# making the window
WIDTH, HEIGHT = 900, 500  # width and height of window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # making the window
pygame.display.set_caption("Escape Room!")  # the name of the window

# defining the colours (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GOLD = (238, 232, 170)
RED = (255, 0, 0)

# the different fonts, which we will use for the writings
myfont = pygame.font.SysFont('Comic Sans MS', 30)  # font name and the size
letter_font = pygame.font.SysFont('Courier', 30)  # font name and the size


FPS = 60  # how many frames per second

# the width and the height of the people
people_width, people_height = 100, 260

# making the audios
# Background music
background_music = pygame.mixer.Sound("images_mvk/backgroundmusic.mp3")  # in the folder, the music file
pygame.mixer.Sound.set_volume(background_music, 0.1)
background_music.play(-1)


# screaming sound effects
girl_scream = pygame.mixer.Sound("images_mvk/womanscream.mp3")  # in the folder, the music file
boy_scream = pygame.mixer.Sound("images_mvk/manscream.mp3")  # in the folder, the music file

# explosion sound effects
The_explosion = pygame.mixer.Sound("images_mvk/explosion sound short.mp3")  # in the folder, the music file

# notes sound effects
The_Notes_sound = pygame.mixer.Sound("images_mvk/The_Notes.mp3")  # in the folder, the music file

# pictures
# making characters
woman = pygame.image.load(os.path.join("images_mvk", "woman.png"))  # in the folder, the image file
woman = pygame.transform.scale(woman, (people_width, people_height))  # the size of it, making it the size we defined above for the humans

man = pygame.image.load(os.path.join("images_mvk", "man.png"))  # in the folder, the image file
man = pygame.transform.scale(man, (people_width, people_height))  # the size of it, making it the size we defined above for the humans


# making the backgrounds that are images
# in the folder, the image file
# the size of it, making it the size we defined above for the window
Scene1 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "scene1.jpg")), (WIDTH, HEIGHT))
Letter_back = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "letter.png")), (WIDTH, HEIGHT))
First_room = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "Room1.jpeg")), (WIDTH, HEIGHT))
Last_room = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "background 3.png")), (WIDTH, HEIGHT))
Second_room = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "library background .png")), (WIDTH, HEIGHT))

# making the objects
# in the folder, the image file
# with the size (the last set of numbers)
# we used trial and error to find the size of each picture

# room 1, normal pics
red_wine = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "spilled_wine.png")), (114, 62))
roses = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "roses.png")), (150, 165))
vegetables = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "vegetables.png")), (45, 30))
telescope_comp_project = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "telescope comp project.png")), (127, 104))
lock1 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "lock .png")), (118, 116))
flag_1 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "flag 1.png")), (65, 57))
flag_2 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "flag 2.png")), (65, 57))
flag_3 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "flag 3.png")), (65, 57))
flag_4_correct = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "winner flag.png")), (65, 57))
charlie_1 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "charlie chaplin. pic 2 comp project.png")), (170, 172))
charlie_2 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "charlie chaplin pic 3 comp project.png")), (140, 172))

# room 1, close up pics
red_wine2 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "spilled_wine2.png")), (514, 432))
close_up_roses = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "close up rose.png")), (225, 250))
close_up_vegetables = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "leaf.png")), (340, 220))
close_up_telescope = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "space.png")), (350, 270))

# the hole for last room
The_hole = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "hole.png")), (500, 300))

# room 2, normal pics
spider = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "spider on web.png")), (100, 80))
book = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "closed book.png")), (65, 58))
candles = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "candles (1).png")), (83, 87))
radio = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "radio .png")), (200, 94))
lock_2 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "lock .png")), (118, 116))
charlie_3 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "pic of charlie chaplin.png")), (192, 172))


# room 2, close up pics
close_up_spider = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "spider.png")), (300, 225))
close_up_book = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "book.png")), (700, 450))
close_up_candles = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "candles close up.png")), (300, 225))
close_up_radio = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "notes.png")), (300, 225))
close_up_charlie_3 = pygame.transform.scale(pygame.image.load(os.path.join("images_mvk", "close up charlie chaplin.png")), (384, 344))



def draw_window():  # the first scene

    WIN.blit(Scene1, (0, 0))  # putting the background, with the location
    # the writings, with the colour
    opening_writing = myfont.render("It is a beautiful night in Paris, France.The city of love.", 1, WHITE)
    opening_writing2 = myfont.render("You have a date with your significant other,", 1, WHITE)
    opening_writing3 = myfont.render("who you have been seeing for a while.", 1, WHITE)
    opening_writing4 = myfont.render("They told you that they are a spy", 1, WHITE)

    # positioning the writings
    WIN.blit(opening_writing,(100,0))
    WIN.blit(opening_writing2, (150, 40))
    WIN.blit(opening_writing3, (225, 80))
    WIN.blit(opening_writing4, (225, 120))

    # positioning the humans
    WIN.blit(woman, (200, 240))
    WIN.blit(man, (600, 240))

    pygame.time.delay(10000)  # delaying the screen, to make it longer
    pygame.display.update()  # updating the window






def black_window(): # the second scene
    WIN.fill(BLACK)  # filling the background to black

    # the writings, with the colour
    black_writing = myfont.render("All of a sudden, everything goes black and you hear screaming.", 1, WHITE)
    black_writing2 = myfont.render("You have been kidnapped.", 1, WHITE)
    black_writing3 = myfont.render("You wake up in a room of a Parisian mansion.", 1, WHITE)
    black_writing4 = myfont.render("There is a scroll on the table:", 1, WHITE)

    # positioning the writings
    WIN.blit(black_writing, (7,100))
    WIN.blit(black_writing2, (250, 140))
    WIN.blit(black_writing3, (150, 180))
    WIN.blit(black_writing4, (225, 220))

    pygame.time.delay(10000)  # delaying the screen, to make it longer
    pygame.display.update()  # updating the display


def letterScene():  # the third scene
    WIN.blit(Letter_back, (0, 0))  # putting the background, with the location

    # the writings, with the colour
    letter_writing = letter_font.render("(The Scroll)", 1, BLACK)
    letter_writing1 = letter_font.render("You have 3 tries per room to escape the", 1, BLACK)
    letter_writing2 = letter_font.render("mansion before the hidden bomb detonates", 1, BLACK)
    letter_writing3 = letter_font.render("Good luck and don’t have too much fun.", 1, BLACK)
    letter_writing4 = letter_font.render("Your time has begun.", 1, BLACK)

    # positioning the writings
    WIN.blit(letter_writing, (0, 0))
    WIN.blit(letter_writing1, (100, 140))
    WIN.blit(letter_writing2, (100, 180))
    WIN.blit(letter_writing3, (100, 220))
    WIN.blit(letter_writing4, (100, 260))
    pygame.time.delay(10000)

    pygame.display.update() # updating the display






def the_game1():  # the first room
    global n  # bringing the variable n in the function (know why later)
    global event  # bringing event in the function
    global t  # bringing the variable t in the function (for the lock trials)


    WIN.blit(First_room, (0, 0))  # setting the background, and location

    # putting images on screen using coordinates
    WIN.blit(red_wine, (210, 430))
    WIN.blit(roses, (750, 300))
    WIN.blit(vegetables, (325, 325))
    WIN.blit(telescope_comp_project, (450, 250))
    WIN.blit(lock1, (0, 300))

    WIN.blit(flag_1, (40, 30))
    WIN.blit(flag_2, (40, 150))
    WIN.blit(flag_3, (250, 30))
    WIN.blit(flag_4_correct, (250, 150))

    WIN.blit(charlie_1, (675, 75))
    WIN.blit(charlie_2, (525, 75))


    if t < 3:  # if the amount of the lock trials is less than 3
        if event.type == pygame.MOUSEBUTTONDOWN:  # mouse event
            mx, my = pygame.mouse.get_pos()  # getting the coordinates of where the mouse clicks
            # picking a range, on the screen with the coordinates, so when pressed the zoomed in picture appears
            if (210 <= mx <= 324) and (430 <= my <= 492):
                WIN.blit(red_wine2, (280, 80))
            if (750 <= mx <= 900) and (300 <= my <= 465):
                WIN.blit(close_up_roses, (600, 0))
            if (325 <= mx <= 370) and (325 <= my <= 355):
                WIN.blit(close_up_vegetables, (0, 300))
            if (450 <= mx <= 577) and (250 <= my <= 354):
                WIN.blit(close_up_telescope, (0, 0))
            if (0 <= mx <= 118) and (300 <= my <= 416):  # when click on the lock
                print("Enter the first letter (in all CAPS) of the colours...")
                print("...in the correct order to unlock the lock, and continue to the next room")
                print("EXAMPLE: for purple, yellow, orange, and green.")
                print("You would type: PYOG")
                password = str(input("Enter the password here: "))  # asking for the password
                if password == "WRGB":  # if they are correct
                    print("That's Correct")
                    n = n + 1  # adding 1 to this, so it can go to the other while loop
                    return password  # returning something, in order to leave this function
                else:
                    t = t + 1  # adding 1, to the trial
                    print("incorrect")
                    print("you failed ", str(t)," time(s)")  # printing how many tries they failed
    else:  # if they exceed their tries
        n = 10  # go to this while loop
        return n  # returning something, in order to leave this function



    pygame.display.update()  # updating the display


def the_game15(): # room 2
    global n  # bringing the variable n in the function (know why later)
    global event  # bringing event in the function
    global r  # bringing the variable r in the function (for the lock trials)

    WIN.blit(Second_room, (0, 0)) # setting the background, and location

    # putting images on screen using coordinates
    WIN.blit(spider, (815, 0))
    WIN.blit(book, (250, 300))
    WIN.blit(candles, (410, 15))
    WIN.blit(radio, (650, 400))
    WIN.blit(lock_2, (0, 375))

    WIN.blit(charlie_3, (25, 50))



    if r < 3: # if the amount of the lock trials is less than 3
        if event.type == pygame.MOUSEBUTTONDOWN:  # mouse event
            mx, my = pygame.mouse.get_pos()  # getting the coordinates of where the mouse clicks
            # picking a ratio, on the screen with the coordinates, so when pressed the zoomed in picture appears
            if (815 <= mx <= 915) and (0 <= my <= 80):
                WIN.blit(close_up_spider, (600, 100))
            if (250 <= mx <= 315) and (300 <= my <= 358):
                WIN.blit(close_up_book, (200, 100))
            if (410 <= mx <= 493) and (15 <= my <= 102):
                WIN.blit(close_up_candles, (400, 200))
            if (650 <= mx <= 850) and (400 <= my <= 494):
                WIN.blit(close_up_radio, (300, 300))
                The_Notes_sound.play()  # the notes play
            if (25 <= mx <= 217) and (50 <= my <= 222):
                WIN.blit(close_up_charlie_3, (0, 25))
            if (0 <= mx <= 118) and (375 <= my <= 491):  # when click on the lock
                print("Enter the 4 digit number password ")
                password2 = int(input("Enter the password here: "))  # asking for the password
                if password2 == 1889:  # if they are correct
                    print("That's Correct")
                    n = n + 1  # adding 1 to this, so it can go to the other while loop
                    return password2  # returning something, in order to leave this function
                else:
                    r = r + 1  # adding 1, to the trial
                    print("incorrect")
                    print("you failed ", str(r)," time(s)")  # printing how many tries they failed

    else:  # if they exceed their tries
        n = 10  # go to this while loop
        return n  # returning something, in order to leave this function

    pygame.display.update()  # updating the display

def the_game2(): #the third room
    WIN.blit(Last_room, (0, 0))  # setting the background, and location
    pygame.display.update()  # updating the display

def the_black_hole():
    WIN.blit(The_hole, (200,300))  # adding the hole in the room

    hole_writing = myfont.render("OH NO!!!", 1, BLACK)  # writing on screen, with colour
    WIN.blit(hole_writing, (250, 100))  # location of writing
    pygame.display.update()  # updating the display

def last_black():
    WIN.fill(BLACK)  # making the background black

    # the writings, with the colour
    b_writing = myfont.render("You have escaped and are being taken to the Empire State", 1, WHITE)
    b_writing2 = myfont.render("Building in New York through a black hole.", 1, WHITE)
    b_writing3 = myfont.render("Your significant other is captured", 1, WHITE)
    b_writing4 = myfont.render("and you must save them before they are killed.", 1, WHITE)
    b_writing5 = myfont.render("To continue please purchase the full game for $4.99", 1, WHITE)
    b_writing6 = myfont.render("Click the red square to quit and play again!", 1, WHITE)

    # positioning the writings
    # we used trial and error to find the positions
    WIN.blit(b_writing, (20, 100))
    WIN.blit(b_writing2, (150, 140))
    WIN.blit(b_writing3, (175, 180))
    WIN.blit(b_writing4, (115, 220))
    WIN.blit(b_writing5, (45, 260))
    WIN.blit(b_writing6, (150, 320))

    pygame.display.update()  # updating the display

def game_over(): # when they lose
    WIN.fill(BLACK)  # filling the background black

    # the writings, with the colour
    go_writing = myfont.render("Game Over!", 1, RED)
    go_writing2 = myfont.render("You put in the wrong code 3 times, and the bomb detonated", 1, WHITE)
    go_writing3 = myfont.render("To try again, press the red square to quit and play the game", 1, WHITE)

    # positioning the writings
    WIN.blit(go_writing, (350, 180))
    WIN.blit(go_writing2, (10, 220))
    WIN.blit(go_writing3, (10, 320))

    pygame.display.update()  # updating the display

def the_main_game(): # the main code
    global n # bringing in n variable, which helps with locating each loop
    global event # brining in event

    clock = pygame.time.Clock()  # setting the clock
    while n == 1:  # when n is 1
        clock.tick(FPS)  # how many frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you want to leave, it closes
                False
        # calling the functions
        draw_window()
        black_window()
        girl_scream.play()
        boy_scream.play()
        letterScene()
        pygame.time.delay(10000)  # delaying one of the window
        n = n + 1  # adding 1 to n

    while n == 2:  # when n is 2
        clock.tick(FPS)  # how many frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you want to leave, it closes
                False
        the_game1()  # calling the function

    while n == 3:  # when n is 3
        clock.tick(FPS)  # how many frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you want to leave, it closes
                False
        the_game15()  # calling the function

    while n == 4:  # when n is 4
        clock.tick(FPS)  # how many frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you want to leave, it closes
                False
        # calling the functions
        the_game2()
        pygame.time.delay(5000)  # delaying for 5 seconds
        the_black_hole()
        pygame.time.delay(5000)  # delaying 5 seconds
        n = n + 1  # adding 1 to n

    while n == 5:  # when n is 5
        clock.tick(FPS)  # how many frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you want to leave, it closes
                False
        last_black()  # calling the function

    while n == 10:  # when n is 10
        clock.tick(FPS) # how many frames per second
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you want to leave, it closes
                False
        The_explosion.play()  # playing explosion sound effect
        game_over()  # calling the function


    pygame.display.update() # updating the display
    pygame.quit()  # quitting pycharm





