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
        self.wid, self.hgt = wid, hgt
        self.cellsize = int(wid/3)-self.linesize, int(hgt/3)-self.linesize
        centercol = wid/3 + self.linesize 
        centerrow = hgt/3 + self.linesize
        bottomrow = 2 * hgt/3 + self.linesize
        bottomcol = 2 * wid/3 + self.linesize
        self.board_coords = [[(self.linesize,self.linesize), (centercol, self.linesize),(bottomcol, self.linesize)],
                          [(self.linesize,centerrow),(centercol,centerrow),(bottomcol,centerrow)],
                          [(self.linesize,bottomrow),(centercol,bottomrow),(bottomcol, bottomcol)]]

    def board_lines(self):    
        pg.Surface.fill(self.window, (0,0,0))
        pg.draw.lines(self.window, pg.Color("grey"), True, [(0,0), (self.wid,0), (self.wid,self.hgt), (0,self.hgt)], self.linesize)
        pg.draw.line(self.window, pg.Color("grey"), (self.wid/3,0),(self.wid/3,self.hgt), self.linesize)
        pg.draw.line(self.window, pg.Color("grey"), (2*self.wid/3,0),(2*self.wid/3,self.hgt), self.linesize)
        pg.draw.line(self.window, pg.Color("grey"), (0,self.hgt/3),(self.wid,self.hgt/3), self.linesize)
        pg.draw.line(self.window, pg.Color("grey"), (0,2*self.hgt/3),(self.wid,2*self.hgt/3), self.linesize)
        pg.display.flip()

    def create_cells(self):
        pass


class Game():
    def __init__(self):
        pass