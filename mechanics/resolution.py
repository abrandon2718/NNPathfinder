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
        if attack.defense == 'a':
            roll = attacker.to_hit['spell'] + randint(1, 20)
            if roll >= defender.effective_ac:
                if roll >= defender.ac+10:
                    defender.take_damage(attack.critical_damage())
                    print(f'Crit! Defender HP: {defender.hp}')
                    crit = True
                if not crit:
                    defender.take_damage(attack.damage())
                    print(f'Hit! Defender HP: {defender.hp}')
        elif attack.defense == 'r':
            roll = defender.reflex + randint(1, 20)
            if roll <= attacker.spell_dc:
                if roll <= attacker.spell_dc-10:
                    crit = True
                    defender.take_damage(attack.critical_damage())
                if not crit:
                    defender.take_damage(attack.damage())
            if roll >= attacker.spell_dc:
                if roll >= attacker.spell_dc+10:
                    crit = True
                if not crit:
                    defender.take_damage(int(attack.damage()/2))
                    
        elif attack.defense == 'w':
            roll = defender.will + randint(1, 20)
            if roll <= attacker.spell_dc:
                if roll <= attacker.spell_dc-10:
                    crit = True
                    defender.take_damage(attack.critical_damage())
                if not crit:
                    defender.take_damage(attack.damage())
            if roll >= attacker.spell_dc:
                if roll >= attacker.spell_dc+10:
                    crit = True
                if not crit:
                    defender.take_damage(int(attack.damage()/2))
                    
        elif attack.defense == 'f':
            roll = defender.fortitude + randint(1, 20)
            if roll <= attacker.spell_dc:
                if roll <= attacker.spell_dc-10:
                    crit = True
                    defender.take_damage(attack.critical_damage())
                if not crit:
                    defender.take_damage(attack.damage())
            if roll >= attacker.spell_dc:
                if roll >= attacker.spell_dc+10:
                    crit = True
                if not crit:
                    defender.take_damage(int(attack.damage()/2))

class Turn:
    def __init__(self, creature: Creature, moves = None, attacks = None):
        self.creature = creature
        self.moves = None
        self.attacks = None
        
    def validate_turn(self):
        action_count = 0
        if self.moves:
            if isinstance(self.moves[0], list):
                for m in self.moves:
                    action_count+=1
            else:
                action_count+=1
            assert action_count < 3, 'Only 3 actions allowed per turn'
        if self.attacks:
            pass
            
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        