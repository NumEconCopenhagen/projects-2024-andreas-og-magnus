from types import SimpleNamespace
import numpy as np
import matplotlib.pyplot as plt
import param as par

class Interpolation:
    def getA(X,y):
        #find x points that is bigger than y1 and y2
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
        # find x points that is bigger than y1 and smaller than y2
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
        # find x points that is smaller than y1 and y2
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
        # find x points that is smaller than y1 and bigger than y2
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
        
