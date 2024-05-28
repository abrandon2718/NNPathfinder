# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:50:23 2024

@author: abran
"""

from mechanics.characters import Zwei, Triceratops, evaluate_condition
from mechanics.conditions import PersistentDamage

from pfnn.pathfinder_environment import BattleGrid
from visuals.drawing import draw_map, draw_grid
from visuals import constants

import pygame as pg
import sys
from time import sleep
from random import randint



def initialize_game():
    pg.init()
    surface = pg.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pg.display.set_caption('PF NN Demo')
    surface.fill(constants.BG_COLOR)
    return surface

def game_loop(surface, grid: BattleGrid):
    z = grid.get_creature('Zwei')
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
        move = [randint(0, 7)]
        sleep(0.3)
        grid.move_creature_movelist(z, move)
        draw_map(surface, grid)
        draw_grid(surface, grid)
        pg.display.update()

def main():
    
    zwei = Zwei()
    zwei.coords = [20,20]
    print(f'Zwei starting HP: {zwei.hp}')
    
    enemy = Triceratops()
    enemy.coords = [5,5]
    print(f'Enemy starting HP: {enemy.hp}')
    
    grid = BattleGrid(25, 25)
    grid.add_creature(zwei)
    grid.add_creature(enemy)
    
    surface = initialize_game()
    game_loop(surface, grid)
    
    
if __name__ == '__main__':
    main()
    