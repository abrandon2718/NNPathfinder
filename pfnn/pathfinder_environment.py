# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 18:40:06 2024

@author: abran
"""
from dataclasses import dataclass
# import gymnasium as gym
# from gymnasium import Env
# from gymnasium.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete 
# import numpy as np
# import random
# import os
# from stable_baselines3 import PPO
# from stable_baselines3.common.vec_env import VecFrameStack
# from stable_baselines3.common.evaluation import evaluate_policy

# class CustomEnv(gym.Env):
#     def __init__(self):
#         super(CustomEnv, self).__init__()
        
#         # Define action and observation space
#         self.action_space = Discrete(2)  # Example: Two possible actions
#         self.observation_space = Box(low=0, high=1, shape=(3,))  # Example: 3-dimensional observation space
        
#         # Define other attributes if needed
        
#     def step(self, action):
#         pass
#         # Implement how the environment changes in response to the action
#         # Return observation, reward, done, info
        
#     def reset(self):
#         pass
#         # Reset the environment to its initial state
#         # Return initial observation
        
#     def render(self, mode='human'):
#         pass
#         # Implement visualization of the environment (optional)

@dataclass
class BattleGrid:
    width: int
    height: int
    grid: [list]
    
    def __repr__(self):
        for row in self.height:
            
            print('|')
            
            for col in self.width:
                if self.grid[row][col]:
                    pass