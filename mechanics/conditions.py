# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:37:45 2024

@author: abran
"""

from dataclasses import dataclass
from random import randint

@dataclass
class PersistentDamage:
    damage_die: int
    damage_die_count: int
    dc: int
    
    def damage_tick(self):
        total = 0
        for i in range(self.damage_die_count):
            total += randint(1, self.damage_die)
        return total
    
    def remove_persistence(self):
        return randint(1, 20) >= self.dc

                
    