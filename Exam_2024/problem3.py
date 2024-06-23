from types import SimpleNamespace
import numpy as np
import matplotlib.pyplot as plt
import param as par

class Interpolation:
    def barycentric_coords(self, y, A, B, C):
        denom = (B[1] - C[1]) * (A[0] - C[0]) + (C[0] - B[0]) * (A[1] - C[1])
        r1 = ((B[1] - C[1]) * (y[0] - C[0]) + (C[0] - B[0]) * (y[1] - C[1])) / denom
        r2 = ((C[1] - A[1]) * (y[0] - C[0]) + (A[0] - C[0]) * (y[1] - C[1])) / denom
        r3 = 1 - r1 - r2
        return r1, r2, r3

    #Building block 2:
    def find_A(self, X, y):
        candidates = X[(X[:,0] > y[0]) & (X[:,1] > y[1])]
        if len(candidates) == 0:
            return np.nan
        return candidates[np.argmin(np.linalg.norm(candidates - y, axis=1))]

    def find_B(self, X, y):
        candidates = X[(X[:,0] > y[0]) & (X[:,1] < y[1])]
        if len(candidates) == 0:
            return np.nan
        return candidates[np.argmin(np.linalg.norm(candidates - y, axis=1))]

    def find_C(self, X, y):
        candidates = X[(X[:,0] < y[0]) & (X[:,1] < y[1])]
        if len(candidates) == 0:
            return np.nan
        return candidates[np.argmin(np.linalg.norm(candidates - y, axis=1))]

    def find_D(self, X, y):
        candidates = X[(X[:,0] < y[0]) & (X[:,1] > y[1])]
        if len(candidates) == 0:
            return np.nan
        return candidates[np.argmin(np.linalg.norm(candidates - y, axis=1))]
