# Problem1.py

import numpy as np
from scipy.optimize import fsolve
from types import SimpleNamespace

class ProductionEconomy:
    def __init__(self):
        self.par = SimpleNamespace()
        self.par.A = 1.0
        self.par.gamma = 0.5
        self.par.alpha = 0.3
        self.par.nu = 1.0
        self.par.epsilon = 2.0
        self.par.tau = 0.0
        self.par.T = 0.0

    def optimal_labor(self, w, p, A, gamma):
        return (p * A * gamma / w) ** (1 / (1 - gamma))

    def production(l, A, gamma):
        return A * l**gamma

    def profit(w, p, A, gamma):
        return (1 - gamma) * (p * A * gamma / w)**(gamma / (1 - gamma))

    def consumer_utility(self, p1, p2, w):
        labor = ((w * self.par.alpha + self.par.T + self.profit(w, p1) + self.profit(w, p2)) / (self.par.nu * (1 + self.par.epsilon)))**(1 / (1 + self.par.epsilon))
        c1 = self.par.alpha * (w * labor + self.par.T + self.profit(w, p1) + self.profit(w, p2)) / p1
        c2 = (1 - self.par.alpha) * (w * labor + self.par.T + self.profit(w, p1) + self.profit(w, p2)) / (p2 + self.par.tau)
        return labor, c1, c2

    def labor_market_clearing(labor, l1, l2):
        return labor - (l1 + l2)

    def goods_market_clearing(c, y):
        return c - y

    def equations(self, prices):
        p1, p2 = prices
        w = 1  # Numeraire
        labor, c1, c2 = self.consumer_utility(p1, p2, w)
        l1 = self.optimal_labor(w, p1)
        l2 = self.optimal_labor(w, p2)
        y1 = self.production(l1)
        y2 = self.production(l2)
        
        eq1 = labor - (l1 + l2)
        eq2 = c1 - y1
        eq3 = c2 - y2
        
        # Using Walras' law, we only need two of these conditions
        return [eq1, eq2]

    def find_equilibrium_prices(self, initial_guess=[1.0, 1.0]):
        equilibrium_prices = fsolve(self.equations, initial_guess)
        return equilibrium_prices
