import pygame as pg
from pygame.locals import *
import random

class Player():
    def __init__(self, size):
       self.playerwid, self.playerhgt = size
       self.player = pg.Surface(size)
       
    def player_display(self, window, coords):
        pg.Surface.blit(window, self.player, coords)
        pg.display.flip()     
       

class PlayerX(Player):
    def __init__(self, size):
        Player.__init__(size)
        pg.draw.line(self.player, (0,255,0), (0,0), size, 5)
        pg.draw.line(self.player, (0,255,0), (self.playerwid,0), (0, self.playerhgt), 5)


class PlayerO(Player):
    def __init__(self, size):
        Player.__init__(size)  
        pg.draw.circle(self.player, (255,0,0),(self.playerwid/2,self.playerhgt/2), self.playerwid/2, 5)


class Button():
    def __init__(self):
        pass


class Board():
    
    
    def __init__(self, wid = 640, hgt = 640):
       pass
    def board_lines(self):    
        pass

    def create_cells(self):
        pass


class Game():
    def __init__(self):
        pass