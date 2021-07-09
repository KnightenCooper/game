""" -- End Menu File --

Class: Instruction_Menu()

Functions:  __init__()
            on_show()
            on_draw()
            on_key_press()
"""

import random
import arcade
from arcade.gui import UIManager
from data import constants

class End_Menu(arcade.View):
    """ This class creates the End menu when an end condition is met or the player ends the game.
    
    Stereotype:
        Information Holder

    Attributes:
        game_view (object): holds the information for the current game view.

    """
    def __init__(self, game_view):
        """ The class constructor.
        
        Args:
            self (End_Menu): an instance of End_Menu.
            game_view (object): an instance of game_view.
        """        
        super().__init__()
        self.game_view = game_view

    def on_show(self):
        """ Sets the background color of the end menu.
        
        Args:
            self (End_Menu): an instance of End_Menu.
        """    
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        """ Creates the view for the end menu.
        
        Args:
            self (End_Menu): an instance of End_Menu.
        """    
        arcade.start_render()

        arcade.draw_text("GAME OVER", constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2+50,
                         arcade.color.WHITE, font_size=50, anchor_x="center")

        # Show tip to return or reset
        arcade.draw_text("Press Esc. to quit",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")
        arcade.draw_text("Press Enter to restart the game",
                         constants.SCREEN_WIDTH/2,
                         constants.SCREEN_HEIGHT/2-30,
                         arcade.color.WHITE,
                         font_size=20,
                         anchor_x="center")

    def on_key_press(self, key, _modifiers):
        """ Allows the user to end or resume the game on key press.
        
        Args:
            self (End_Menu): an instance of End_Menu.
            key (arcade.key): sets the keys to end or resume the game.
        """  
        if key == arcade.key.ESCAPE:   # end game
            self.window.close()
        elif key == arcade.key.ENTER:  # restart game
            self.game_view.start_new_game()
            self.window.show_view(self.game_view)