import sys
print(sys.version)

import numpy as np
import scipy.linalg as la
import matplotlib.pyplot as plt
%matplotlib inline

def plot_2d(vecs):
    """
    To plot vectors when their points are given
    Only for 2D graphs
    """
    for i in vecs:
        ax.annotate('', xy=i, xytext=(0, 0),
                arrowprops=dict(facecolor='black',
                shrink=0,
                alpha=0.8,
                width=0.6))
        ax.text(1.2*i[0],1.2*i[1],str(i))

fig, ax = plt.subplots(figsize = (14,8))
for spine in ['left', 'bottom']:
    ax.spines[spine].set_position('zero')
for spine in ['right', 'top']:
    ax.spines[spine].set_color('none')
#Removing upper and right spines. Movinng left and bottom spines to the middle
ax.set(xlim = (-10,10), ylim = (-10,10))
vectors = [[1,2],[3,4],[-2,-6]]
plot_2d(vectors)
