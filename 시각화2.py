"""
import numpy as np 
import matplotlib.pyplot as plt 
 
n_bins = 30 
x = np.random.randn(1000) 
y = np.random.randn(1000) 
 
plt.hist(x, n_bins, histtype='bar', color='red', alpha=0.5)
plt.hist(y, n_bins, histtype='bar', color='blue', alpha=0.3)
plt.show()

#
import matplotlib.pyplot as plt

n_bins = 5

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

plt.hist(x, n_bins, histtype='bar', color='blue', alpha=0.3)

plt.show()
"""

import matplotlib.pyplot as plt 

fig, ax = plt.subplots(3, 3, figsize=(5, 5)) 
 
ax[0, 0].plot(range(10), 'k') # row=0, col=0 
ax[1, 0].plot(range(10), 'b') # row=1, col=0
ax[2, 0].plot(range(10), 'b') # row=1, col=0
ax[0, 1].plot(range(10), 'g') # row=0, col=1
ax[0, 2].plot(range(10), 'g') # row=0, col=1
ax[1, 1].plot(range(10), 'k') # row=1, col=1
ax[2, 2].plot(range(10), 'k') # row=1, col=1
ax[1, 2].plot(range(10), 'r') # row=1, col=1
ax[2, 1].plot(range(10), 'r') # row=1, col=1

plt.show()
