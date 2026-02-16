# -*- coding: utf-8 -*-
"""
Created on Mon Feb 16 15:23:25 2026

@author: tatas
"""

import numpy as np
import time
#==========================================
#Task 1: Create an Array and Basic Math
#==========================================
temps_celsius=np.array([22,25,28,24,26])

temps_fahrenheit=temps_celsius*1.8+32

average=np.mean(temps_fahrenheit)

print(f"Celsius: {temps_celsius}")
print(f"Fahrenheit: {temps_fahrenheit}")
print(f"Average Fahrentheit: {average}")

#==========================================
#Task 2: Array Shape and Statistics
#==========================================
test_scores=np.array([85, 90, 78, 92, 88, 76, 95, 82, 89, 91, 87, 84])

print(f"Shape: {test_scores.shape}")
print(f"Total elements: {len(test_scores)}")
print(f"Highest score: {test_scores.max()}")
print(f"Lowest score: {test_scores.min()}")
print(f"Range: {test_scores.max()-test_scores.min()}")

#==========================================
#Task 3: Performance Comparison
#==========================================
nparray=np.arange(1,50001)
pylist=list(range(1,50001))

npstarttime=time.time()
npsum=nparray.sum()
npendtime=time.time()
nptime=npendtime-npstarttime

pystarttime=time.time()
pysum=sum(pylist)
pyendtime=time.time()
pytime=pyendtime-pystarttime


print(f"NumPy sum: {npsum}")
print(f"Python sum: {pysum}")
print(f"NumPy time: {nptime:.4f} seconds")
print(f"Python time: {pytime:.4f} seconds")
print(f"NumPy is {pytime/nptime:.1f}x faster")


