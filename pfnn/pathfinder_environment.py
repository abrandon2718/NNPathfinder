# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:40:06 2024

@author: abran
"""
from dataclasses import dataclass
from mechanics.characters import Creature

class BattleGrid:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.grid = []
        
        for h in range(self.height):
            temp = []
            for w in range(self.width):
                temp.append(0)
            self.grid.append(temp)
        
        self.creatures = []
        
    def add_creature(self, creature: Creature):
        if self.creatures:
            for c in self.creatures:
                assert creature.coords != c.coords, 'Cannot add a creature to a location where a creature exists!'
            
            assert self.check_inbounds(creature), 'Trying to insert creature out of bounds!'
            
            self.creatures.append(creature)
            self.grid[creature.coords[0]][creature.coords[1]] = creature
        else:
            assert self.check_inbounds(creature), 'Trying to insert creature out of bounds!'
            
            self.creatures.append(creature)
            self.grid[creature.coords[0]][creature.coords[1]] = creature
    
    def update(self):
        pass
    
    def check_inbounds(self, creature: Creature):
        
        return (creature.coords[0] >= 0 and creature.coords[0] < self.width) and (creature.coords[1] >= 0 and creature.coords[1] < self.height) 
    
    def execute_move(self, creature: Creature, move_list):
        pass