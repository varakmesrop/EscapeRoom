from Menu.menu import *
import pygame
import os
import Escape_Room
import time

n = 1

pygame.display.set_caption("Escape Room!")

class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        # FOR CONTROLS- WHEN THEY CLICK KEY, TURNS TRUE
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        # canvas size by pixels
        self.DISPLAY_W, self.DISPLAY_H = 900, 500
        # creates canvas
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        # so the player can see what is happening
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        #self.font_name = 'fancy_writing.zip'
        # font for writing on screen
        self.font_name = pygame.font.get_default_font()
        # black and white in RGB(red, green, blue)
        self.BLACK, self.WHITE, self.GOLD = (0, 0, 0), (255, 255, 255), (238, 232, 170)
        self.main_menu = MainMenu(self)
        self.options = InstructionsMenu(self)
        self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        Escape_Room.the_main_game()


    def check_events(self):
        # goes through a list of everything the player can do
        for event in pygame.event.get():
            # when the player clicks "X" and wants to close the window
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                # stops anything else that could be running
                self.curr_menu.run_display = False
            # when the player clicks something on keyboard it checks if it was enter, the down or up key
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True


    # this resets it to make sure that when the for example the up key isn't pressed, it should be false and not stay as true
    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    # choosing the sizw of text and where we want it relative to the screen
    def draw_text(self, text, size, x, y ):
        # loading font
        font = pygame.font.Font(self.font_name,size)
        # local variable
        text_surface = font.render(text, True, self.BLACK)
        # getting dimensions of rectangle
        text_rect = text_surface.get_rect()
        # takes x and y and centers your text depending on that specific dimension
        text_rect.center = (x,y)
        # instead of passing x and y, pass variables we just made
        self.display.blit(text_surface,text_rect)