import pygame


class Menu():
    # reference game to reuse the code we have written in those functions
    def __init__(self, game):
        self.game = game  # gives us access to the code
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        # tells the menu to keep running
        self.run_display = True
        # ( x, y, width, height)
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        # to make sure the cursor is not on top of text and to its left, that's why it is a negatice number
        self.offset = - 100

    # helper function
    def draw_cursor(self):
        self.game.draw_text('>', 15, self.cursor_rect.x, self.cursor_rect.y)

    # helper function, makes us more efficient so we don't have to rewrite everytime
    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


# put Menu in brackets to inherit those values
class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        # tto know which one is highlighted
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.instructionsx, self.instructionsy = self.mid_w, self.mid_h + 50
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 70
        # aligns our > with text
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        # already set to true but just to make sure
        self.run_display = True
        while self.run_display:
            # sets the flags we made in the game class for us
            self.game.check_events()
            self.check_input()
            # again resetting screen
            self.game.display.fill(self.game.GOLD)
            # creating headlines and centering them
            self.game.draw_text('Escape Room!', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 100)
            self.game.draw_text('Main Menu', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Instructions", 20, self.instructionsx, self.instructionsy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.game.draw_text('Click the "x" key to quit', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 180)
            self.draw_cursor()
            # to update and make sure all cursor info is put onto screen
            self.blit_screen()

    def move_cursor(self):
        # to be able to move down words during the main menu.
        # During main menu, be able to use down key to move ot the other options
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.instructionsx + self.offset, self.instructionsy)
                self.state = 'Instructions'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Instructions':
                self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.instructionsx + self.offset, self.instructionsy)
                self.state = 'Instructions'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Instructions':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False


class InstructionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            # if key is clicked
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            # colour stays gold
            self.game.display.fill(self.game.GOLD)
            # text on screen
            self.game.draw_text('INSTRUCTIONS', 30, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 60)
            self.game.draw_text('Turn volume up for full experience', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 15)
            self.game.draw_text('To view a clue, click and hold on an object.', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 0)
            self.game.draw_text('If it is a clue, a larger picture will appear', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 15)
            self.game.draw_text('Once you have figured out the answer click the lock', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 30)
            self.game.draw_text('Type the answer in the console', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 45)
            self.game.draw_text('If you are correct, instructions will be given to you', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 60)
            self.game.draw_text('If you are incorrect, keep thinking', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 75)
            self.game.draw_text('Once you figure it out, click the lock again to try your luck', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 90)
            self.game.draw_text('You have 3 tries per room', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 105)
            self.game.draw_text('If you fail in any room, the bomb will detonate ', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 120)
            self.game.draw_text('Click the ENTER key to go back to the main menu', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 180)
            self.blit_screen()

class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            # if key is clicked
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            # background colour stays gold
            self.game.display.fill(self.game.GOLD)
            # text on screen
            # doing /2 to make sure it is centered, and adding to y value to bring text down
            self.game.draw_text('CREDITS', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Varak Mesropian', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.game.draw_text('Megheti Bekmezian', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 25)
            self.game.draw_text('Karnie Karshafian', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 40)
            self.game.draw_text('Click the ENTER key to go back to the main menu', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 180)
            self.blit_screen()
