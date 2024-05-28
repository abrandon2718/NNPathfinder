# -*- coding: utf-8 -*-
"""
Created on Sun May 19 11:28:41 2024

@author: abran
"""

from . import constants
from pfnn.pathfinder_environment import BattleGrid
import pygame as pg

def get_tile_color(tile_contents):
    if tile_contents == 0:
        tile_color = constants.BG_COLOR
    if tile_contents == 'a':
        tile_color = constants.PC_COLOR
    if tile_contents == 'e':
        tile_color = constants.ENEMY_COLOR
    return tile_color

def draw_map(surface, grid: BattleGrid):
    block_width = round(constants.SCREEN_WIDTH/grid.width)
    block_height = round(constants.SCREEN_HEIGHT/grid.height)
    
    for j, row in enumerate(grid.grid):
        for i, tile in enumerate(row):
            myrect = pg.Rect(i*block_width, j*block_height, block_width, block_height)
            pg.draw.rect(surface, get_tile_color(tile), myrect)

def draw_grid(surface, grid: BattleGrid):
    block_width = round(constants.SCREEN_WIDTH/grid.width)
    block_height = round(constants.SCREEN_HEIGHT/grid.height)
    for i in range(grid.width):
        
        new_height = (i * block_height)
        new_width = (i * block_width)
        pg.draw.line(surface, constants.LINE_COLOR, (0, new_height), (constants.SCREEN_WIDTH, new_height), 2)
        pg.draw.line(surface, constants.LINE_COLOR, (new_width, 0), (new_width, constants.SCREEN_HEIGHT), 2)

