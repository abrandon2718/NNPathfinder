# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 12:37:45 2024

@author: abran
"""

from dataclasses import dataclass
from random import randint
from characters import Creature

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
    
    def check_persistence(self):
        return randint(1, 20) > self.dc
    
def evaluate_condition(creature: Creature):
    if creature.conditions.length == 0:
        return
    for con in creature.conditions:
        if isinstance(con, PersistentDamage):
            creature.take_damage(con.damage_tick())
            
            if not con.check_persistence():
                creature.conditions.remove(con)
                
            continue
        if isinstance(con, str):
            if con == 'prone':
                creature.effective_ac = creature.ac - 2
                
    