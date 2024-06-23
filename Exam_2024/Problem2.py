from types import SimpleNamespace
import numpy as np
from numpy.random import normal
class careermodelclass:
    def __init__(self):
        self.par = SimpleNamespace()
        self.par.J = 3
        self.par.N = 10
        self.par.K = 10000
        self.par.F = np.arange(1, self.par.N + 1)
        self.par.sigma = 2
        self.par.v = np.array([1, 2, 3])
        self.par.c = 1
    def epsilon(self):
        return normal(0, self.par.sigma, (self.par.K, self.par.J))
    def realized_utility(self):
        epsilon_samples = self.epsilon()
        return self.par.v + epsilon_samples
    def average_realized_utility(self):
        realized_utilities = self.realized_utility()
        return np.mean(realized_utilities, axis=0)
    def expected_utility(self):
        epsilon_samples = self.epsilon()
        expected_utility = self.par.v + np.mean(epsilon_samples, axis=0)
        return expected_utility
