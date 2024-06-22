from types import SimpleNamespace
import numpy as np

import param as par
class careermodelclass:
    def __init__(self):
        par = self.par = SimpleNamespace()
        par.J = 3
        par.N = 10
        par.K = 10000
        par.F = np.arange(1,par.N+1)
        par.sigma = 2
        par.v = np.array([1,2,3])
        par.c = 1
    
    def epsilon(self):
        return np.random.normal(0, par.sigma, par.N)
    def utility(self, x):
        return par.v + epsilon
    def realized_utility (self):
        return par.v[:, np.newaxis] + epsilon
    def average_realized_utility(self):
        return np.mean(realized_utility)
