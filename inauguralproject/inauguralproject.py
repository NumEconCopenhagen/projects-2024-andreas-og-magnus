from types import SimpleNamespace

import param
class ExchangeEconomyClass:
    def __init__(self):
        par = self.par = SimpleNamespace()
        par.alpha = 1/3
        par.beta = 2/3
        par.w1A = 0.8
        par.w2A = 0.3
        par.w1B = 1 - par.w1A
        par.w2B = 1 - par.w2A
        par.p2 = 1

    def utility_A(self, x1A, x2A):
        return x1A**self.par.alpha * x2A**(1-self.par.alpha)

    def utility_B(self, x1B, x2B):
        return x1B**self.par.beta * x2B**(1-self.par.beta)

    def demand_A(self, p1):
        return (self.par.alpha * (p1 * self.par.w1A + self.par.p2 * self.par.w2A)) / p1, ((1 - self.par.alpha) * (p1 * self.par.w1A + self.par.p2 * self.par.w2A)) / self.par.p2

    def demand_B(self, p1):
        return (self.par.beta * (p1 * self.par.w1B + self.par.p2 * self.par.w2B)) / p1, ((1 - self.par.beta) * (p1 * self.par.w1B + self.par.p2 * self.par.w2B)) / self.par.p2

    def check_market_clearing(self, p1):
        par = self.par
        x1A, x2A = self.demand_A(p1)
        x1B, x2B = self.demand_B(p1)
        eps1 = x1A - par.w1A + x1B - par.w1B
        eps2 = x2A - par.w2A + x2B - par.w2B
        return eps1, eps2
    
    def negative_utility_A(self, p1):
        # Utility function but returns negative for optimization
        x1A, x2A = self.demand_A(p1)
        return -self.utility_A(x1A, x2A)
    
    def max_u_a(self,x):
        return -self.utility_A(x[0], x[1])

    def max_u_ab(self,x):
        utility_A = self.utility_A(x[0], x[1])
        utility_B = self.utility_B(1-x[0], 1-x[1])
        return -(utility_A + utility_B)