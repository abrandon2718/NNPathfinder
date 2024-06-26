# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 20:39:31 2024

@author: abran
"""

from .attacks import Fireball, RayOfFrost, ProduceFlame, KnockdownAttack
from .conditions import PersistentDamage

class Creature:
    def __init__(self, hp: int = 0, speed: int = 0, ac: int = 0, conditions: list = []):
        self.hp = hp
        self.speed = speed
        self.ac = ac
        self.effective_ac = self.ac
        self.conditions = conditions
        self.coords = [0,0]
        
    def take_damage(self, damage):
        if isinstance(damage, dict):
            self.conditions.append(damage['effect'])
            dam = damage['damage']
            if dam >= self.hp:
                self.hp = 0
            else:
                self.hp -= dam
        else:
            if damage >= self.hp:
                self.hp = 0
            else:
                self.hp -= damage
        

class Zwei(Creature):
    def __init__(self):
        super().__init__()
        self.name = 'Zwei'
        self.grid_string = 'a'
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
        self.fortitude = 11
        self.reflex = 13
        self.will = 16
        self.effective_ac = self.ac
        self.spell_dc = 26
        self.to_hit = {
            'spell': 16,
            'melee': 13
            }
        self.conditions = []
        
        

class Triceratops(Creature):
    def __init__(self):
        super().__init__()
        self.name = 'Triceratops'
        self.grid_string = 'e'
        self.spells = []
        self.modifier = 9
        self.attacks = [
                        (KnockdownAttack('horns', damage_die=8, damage_die_count=2, area=0, reach=15, modifier=self.modifier))
                        ]
        self.speed = 30
        self.hp = 140
        self.ac = 26
        self.effective_ac = self.ac
        self.fortitude = 18
        self.reflex = 12
        self.will = 14
        self.ability_dc = 26
        self.to_hit = {
            'melee': 19
            }
        self.conditions = []
        
def evaluate_condition(creature: Creature):
    if not creature.conditions:
        return
    for con in creature.conditions:
        if isinstance(con, PersistentDamage):
            creature.take_damage(con.damage_tick())
            
            if con.remove_persistence():
                creature.conditions.remove(con)
                
            continue
        if isinstance(con, str):
            if con == 'prone':
                creature.effective_ac = creature.ac - 2