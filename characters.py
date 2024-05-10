# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:39:31 2024

@author: abran
"""

from attacks import Fireball, RayOfFrost, ProduceFlame

class Zwei:
    def __init__(self):
        self.spells = ['fireball', 'ray_of_frost', 'produce_flame']
        self.attacks = [
                        (Fireball(rank=4), 3),
                        (RayOfFrost(rank=4), -1),
                        (ProduceFlame(rank=4),-1)
                        ]
        self.modifier = 4
        
        for a in self.attacks:
            a[0].modifier *= self.modifier
        
        self.speed = 30
        self.hp = 72
        self.ac = 23
        self.spell_dc = 26
        self.to_hit = {
            'spell': 16,
            'melee': 13
            }
        

class Triceratops:
    def __init__(self):
        self.spells = ['fireball', 'ray_of_frost', 'produce_flame']
        self.attacks = [
                        
                        ]
        self.speed = 30
        self.hp = 140
        self.ac = 26
        self.fortitude = 18
        self.reflex = 12
        self.will = 14
        self.ability_dc = 26
        self.to_hit = {
            'melee': 19
            }
        self.modifier = 4
        
        