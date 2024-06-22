from types import SimpleNamespace
import numpy as np
import matplotlib.pyplot as plt
import param as par

class Interpolation:
    def getA(X,y):
        xlist= []
        for x in X:
            if x[0]>y[0] and x[1]>y[1]:
                xlist.append(x)
        if len(xlist)==0:
            return "NaN"
        else:
            eDistance = []
            for x in xlist:
                eDistance.append(np.linalg.norm(x-y))
            return xlist[np.argmin(eDistance)]
    def getB(X, y):
        xlist = []
        for x in X:
            if x[0] > y[0] and x[1] < y[1]:
                xlist.append(x)
        if len(xlist) == 0:
            return "NaN"
        else:
            eDistance = []
            for x in xlist:
                eDistance.append(np.linalg.norm(x - y))
            return xlist[np.argmin(eDistance)]
    def getC(X, y):
        xlist = []
        for x in X:
            if x[0] < y[0] and x[1] < y[1]:
                xlist.append(x)
        if len(xlist) == 0:
            return "NaN"
        else:
            eDistance = []
            for x in xlist:
                eDistance.append(np.linalg.norm(x - y))
            return xlist[np.argmin(eDistance)]
    def getD(X, y):
        xlist = []
        for x in X:
            if x[0] < y[0] and x[1] > y[1]:
                xlist.append(x)
        if len(xlist) == 0:
            return "NaN"
        else:
            eDistance = []
            for x in xlist:
                eDistance.append(np.linalg.norm(x - y))
            return xlist[np.argmin(eDistance)]
        
