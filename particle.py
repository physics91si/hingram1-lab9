# Physics 91SI
# Spring 2015
# Lab 7

import numpy as np

class Particle:
    """Stores information about a particle with mass, position, and velocity."""
    
    def __init__(self, Position, M):
        """Create a particle with position (numpy array of len 2) and mass."""
        self.pos = Position   # Sets x position
        self.m = M  # Sets mass
        # Initial velocity and acceleration set to be zero
        self.vel = np.zeros((2,))
        self.acc = np.zeros((2,))
    def get_force(self):
        """ Multiplies particle's mass by it's acceleration! """
        return self.acc * self.M

# class Molecule: 
#     """Stores information about a molecule with mass, position, and velocity."""

#     def __init__(self, particle_1_pos_tuple, particle_2_pos_tuple, SpringConstant, L_Theta):
#         self.p1 = particle_1_pos_tuple
#         self.p2 = particle_2_pos_tuple
#         self.k = SpringConstant
#         self.len = L_Theta

#     def get_disp1(self):
#         return self.p1 - self.p2 


