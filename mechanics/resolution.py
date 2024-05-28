# -*- coding: utf-8 -*-
"""
Created on Mon May 27 21:21:40 2024

@author: abran
"""

from mechanics.characters import Creature
from mechanics.attacks import Attack

from pfnn.pathfinder_environment import BattleGrid

from random import randint


def resolve_attack(attacker: Creature, defender: Creature, attack: Attack):
    crit = False
    if attack.kind == 'melee':
        roll = attacker.to_hit['melee'] + randint(1, 20)
        if roll >= defender.effective_ac:
            if roll >= defender.ac+10:
                defender.take_damage(attack.critical_damage())
                crit = True
            if not crit:
                defender.take_damage(attack.damage())
    
    if attack.kind == 'spell':
        crit = False
        