# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:50:23 2024

@author: abran
"""

from mechanics.characters import Zwei, Triceratops, evaluate_condition
from mechanics.conditions import PersistentDamage

from pfnn.pathfinder_environment import BattleGrid

def main():
    
    zwei = Zwei()
    zwei.coords = [20,20]
    print(f'Zwei starting HP: {zwei.hp}')
    
    enemy = Triceratops()
    enemy.coords = [5,5]
    print(f'Enemy starting HP: {enemy.hp}')
    
    grid = BattleGrid(30, 30)
    grid.add_creature(zwei)
    grid.add_creature(enemy)
    
    
if __name__ == '__main__':
    main()
    