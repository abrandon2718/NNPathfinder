# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:50:23 2024

@author: abran
"""

from mechanics.characters import Zwei, Triceratops, evaluate_condition
from mechanics.conditions import PersistentDamage

def main():
    
    zwei = Zwei()
    print(f'Zwei starting HP: {zwei.hp}')
    
    enemy = Triceratops()
    print(f'Enemy starting HP: {enemy.hp}')
    
    
if __name__ == '__main__':
    main()
    