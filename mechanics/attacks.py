# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:42:23 2024

@author: abran
"""

from dataclasses import dataclass
from random import randint
from .conditions import PersistentDamage

@dataclass
class Attack:
    name: str
    damage_die: int
    damage_die_count: int
    area: int
    reach: int
    modifier: int
    kind: str
    defense: str
    
    
    def damage(self):
        total = 0
        for i in range(self.damage_die_count):
            total += randint(1, self.damage_die)
        return total + self.modifier
    
    def critical_damage(self):
        return self.damage()*2
    
@dataclass    
class Fireball(Attack):
    name: str = 'fireball'
    kind: str = 'spell'
    rank: int = 3
    damage_die: int = 6
    damage_die_count: int = rank * 2
    area: int = 20
    reach: int = 500
    modifier: int = 0
    defense: str = 'r'

@dataclass    
class RayOfFrost(Attack):
    name: str = 'ray_of_frost'
    kind: str = 'spell'
    rank: int = 1
    damage_die: int = 4
    damage_die_count: int = rank
    area: int = 20
    reach: int = 500
    modifier: int = 1
    defense: str = 'a'
    
@dataclass    
class ProduceFlame(Attack):
    name: str = 'produce_flame'
    kind: str = 'spell'
    rank: int = 1
    damage_die: int = 4
    damage_die_count: int = rank
    area: int = 20
    reach: int = 500
    modifier: int = 1
    defense: str = 'a'
    
    def critical_damage(self):
        return {'damage': self.damage()*2, 'effect': PersistentDamage(10,self.rank)}
    
@dataclass
class KnockdownAttack(Attack):
    kind: str = 'melee'
    defense: str = 'a'

    def damage(self):
        total = 0
        for i in range(self.damage_die_count):
            total += randint(1, self.damage_die)
        
        return {'damage': total+self.modifier, 'effect': 'prone'}
    
    
