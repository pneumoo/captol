# -*- coding: utf-8 -*-
"""
Created on Fri May 13 19:59:12 2016

@author: Brian
"""

import random as r
from datetime import datetime
import math
r.seed(datetime.now())
import pylab as plt

num_caps = 50
cap_val = 22    #in uF
cap_tol = 0.2   #+/- this value
trials = 100000

# For Normal Distributions:
#+/-3 sigma = 1/370
#+/-4 sigma = 1/15787
#+/-5 sigma = 1/1744278
#+/-6 sigma = 1/506797346
#+/-7 sigma = 1/390682215445

def av(lst):
    return sum(lst)/len(lst)

n=1
minval=[]
maxval=[]
meanval=[]
maxtrend = []
mintrend = []
for i in range(num_caps):
    print(n)
    avg_tolerance = []

    for j in range(trials):

        cap_sample = []
        for k in range(n):
            cap_sample.append(r.uniform(-cap_tol, cap_tol))

        avg_tolerance.append(cap_val * (1+av(cap_sample)))



    cap_max = cap_val * (1 + cap_tol)
    cap_min = cap_val * (1 - cap_tol)
    minval.append(min(avg_tolerance))
    maxval.append(max(avg_tolerance))
    meanval.append(av(avg_tolerance))
#    maxtrend.append(-(0.867) * math.log(i+1) + cap_val*(1+cap_tol))
#    mintrend.append((0.867) * math.log(i+1) + cap_val*(1-cap_tol))

#    plt.hist(avg_tolerance, bins=50)
#    plt.axvline(av(avg_tolerance), color='g', linestyle='dashed', linewidth=2)
#    plt.axvline(max(avg_tolerance), color='g', linestyle='dashed', linewidth=2)
#    plt.axvline(min(avg_tolerance), color='g', linestyle='dashed', linewidth=2)
#    plt.axvline(cap_max, color='r', linestyle='dashed', linewidth=2)
#    plt.axvline(cap_min, color='r', linestyle='dashed', linewidth=2)

    n=n+1

plt.plot(range(num_caps),minval)
plt.plot(range(num_caps),maxval)
plt.plot(range(num_caps),meanval)
#plt.plot(range(num_caps),maxtrend)
#plt.plot(range(num_caps),mintrend)