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
            self.grid[creature.coords[0]][creature.coords[1]] = creature.grid_string
        else:
            assert self.check_inbounds(creature), 'Trying to insert creature out of bounds!'
            
            self.creatures.append(creature)
            self.grid[creature.coords[0]][creature.coords[1]] = creature.grid_string
            
    def move_creature_coords(self, creature: Creature, coords = None):
        temp_coords = creature.coords
        creature.coords = coords
        if not self.check_inbounds(creature):
            print('Creature attempting to move out of bounds. Move failed.')
            creature.coords = temp_coords
        elif self.grid[creature.coords[0]][creature.coords[1]] != 0:
            print('Creature colliding with another creature or object. Move failed.')
            creature.coords = temp_coords
        else:
            self.grid[creature.coords[0]][creature.coords[1]] = creature.grid_string
            self.grid[temp_coords[0]][temp_coords[1]] = 0
        
    def move_creature_movelist(self, creature: Creature, movelist = None):
        temp_coords = creature.coords
        if len(movelist) > creature.speed/5:
            movelist = movelist[:int(creature.speed/5)]
        for move in movelist:
            if move == 0:
                self.move_creature_coords(creature, coords=[creature.coords[0]-1, creature.coords[1]])
            elif move == 1:
                self.move_creature_coords(creature, coords=[creature.coords[0]-1, creature.coords[1]+1])
            elif move == 2:
                self.move_creature_coords(creature, coords=[creature.coords[0], creature.coords[1]+1])
            elif move == 3:
                self.move_creature_coords(creature, coords=[creature.coords[0]+1, creature.coords[1]+1])
            elif move == 4:
                self.move_creature_coords(creature, coords=[creature.coords[0]+1, creature.coords[1]])
            elif move == 5:
                self.move_creature_coords(creature, coords=[creature.coords[0]+1, creature.coords[1]-1])
            elif move == 6:
                self.move_creature_coords(creature, coords=[creature.coords[0], creature.coords[1]-1])
            elif move == 7:
                self.move_creature_coords(creature, coords=[creature.coords[0]-1, creature.coords[1]-1])
    
    def get_creature(self, name: str):
        for c in self.creatures:
            if c.name == name:
                return c
        raise ValueError(f'{name} does not exist in list of creatures!')
        
    def remove_creature(self, name: str):
        for index, c in enumerate(self.creatures):
            if c.name == name:
                self.creatures.pop(index)
                self.grid[c.coords[0]][c.coords[1]] = 0
                return
        raise ValueError(f'{name} does not exist in list of creatures!')
                
    
    def update_creatures(self):
        for c in self.creatures:
            if c.hp == 0:
                print(f'{c.name} is dead!')
                self.remove_creature(c.name)
    
    def check_inbounds(self, creature: Creature):
        
        return (creature.coords[0] >= 0 and creature.coords[0] < self.width) and (creature.coords[1] >= 0 and creature.coords[1] < self.height) 
    