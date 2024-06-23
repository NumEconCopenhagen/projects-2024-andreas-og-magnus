import numpy as np
import pandas as pd
from scipy.optimize import fsolve, minimize
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
        self.par.kappa = 0.1

    def optimal_labor(self, w, p, A, gamma):
        return (p * A * gamma / w) ** (1 / (1 - gamma))

    def production(self, l, A, gamma):
        return A * l**gamma

    def profit(self, w, p, A, gamma):
        return ((1 - gamma)/gamma) * w * ((p * A * gamma / w)**(gamma / (1 - gamma)))

    def consumer_utility(self, p1, p2, w):
        labor = ((w * self.par.alpha + self.par.T + self.profit(w, p1, self.par.A, self.par.gamma) + self.profit(w, p2, self.par.A, self.par.gamma)) / (self.par.nu * (1 + self.par.epsilon)))**(1 / (1 + self.par.epsilon))
        c1 = self.par.alpha * (w * labor + self.par.T + self.profit(w, p1, self.par.A, self.par.gamma) + self.profit(w, p2, self.par.A, self.par.gamma)) / p1
        c2 = (1 - self.par.alpha) * (w * labor + self.par.T + self.profit(w, p1, self.par.A, self.par.gamma) + self.profit(w, p2, self.par.A, self.par.gamma)) / (p2 + self.par.tau)
        return labor, c1, c2

    def equations(self, prices):
        p1, p2 = prices
        w = 1
        labor, c1, c2 = self.consumer_utility(p1, p2, w)
        l1 = self.optimal_labor(w, p1, self.par.A, self.par.gamma)
        l2 = self.optimal_labor(w, p2, self.par.A, self.par.gamma)
        y1 = self.production(l1, self.par.A, self.par.gamma)
        y2 = self.production(l2, self.par.A, self.par.gamma)
        
        eq1 = labor - (l1 + l2)
        eq2 = c1 - y1
        eq3 = c2 - y2
        return [eq1, eq2]

    def find_equilibrium_prices(self, initial_guess=[1.0, 1.0]):
        equilibrium_prices = fsolve(self.equations, initial_guess)
        return equilibrium_prices

    def market_clearing_check(self, p1_values, p2_values):
        results = []
        for p1 in p1_values:
            for p2 in p2_values:
                labor, c1, c2 = self.consumer_utility(p1, p2, 1)
                l1 = self.optimal_labor(1, p1, self.par.A, self.par.gamma)
                l2 = self.optimal_labor(1, p2, self.par.A, self.par.gamma)
                y1 = self.production(l1, self.par.A, self.par.gamma)
                y2 = self.production(l2, self.par.A, self.par.gamma)
                labor_market_clearing = np.isclose(labor, l1 + l2)
                goods_market1_clearing = np.isclose(c1, y1)
                goods_market2_clearing = np.isclose(c2, y2)
                results.append((p1, p2, labor_market_clearing, goods_market1_clearing, goods_market2_clearing))
        results_df = pd.DataFrame(results, columns=['p1', 'p2', 'Labor Market Clearing', 'Goods Market 1 Clearing', 'Goods Market 2 Clearing'])
        return results_df

    def social_welfare_function(self, p1, p2, w):
        labor, c1, c2 = self.consumer_utility(p1, p2, w)
        utility = (self.par.alpha * np.log(c1) + (1 - self.par.alpha) * np.log(c2)) - self.par.nu * (labor**(1 + self.par.epsilon)) / (1 + self.par.epsilon)
        y2 = self.production(self.optimal_labor(w, p2, self.par.A, self.par.gamma), self.par.A, self.par.gamma)
        swf = utility - self.par.kappa * y2
        return swf

    def find_optimal_policy(self):
        def objective(params):
            tau, T = params
            self.par.tau = tau
            self.par.T = T
            p1, p2 = self.find_equilibrium_prices()
            w = 1  # Numeraire
            return self.social_welfare_function(p1, p2, w)

        initial_guess = [0.0, 0.0]
        result = minimize(objective, initial_guess, bounds=[(0, None), (0, None)])
        optimal_tau, optimal_T = result.x
        return optimal_tau, optimal_T
