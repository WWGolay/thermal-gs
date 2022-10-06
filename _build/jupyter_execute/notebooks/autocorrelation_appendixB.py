#!/usr/bin/env python
# coding: utf-8

# # B1. Autocorrelation

# ## B1.1. Notebook setup

# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


# ## B1.2. <a href="https://www.dropbox.com/s/821u22nl4avqf67/autocorrelation_appendixB.zip?dl=1">Download data</a>

# Unzip the contents into a folder named <font color='green'>data</font> in the same level as the notebooks folder. The directory structure should end up looking like the following: 
# ```
# thermal-gs
# ├── data
# │   ├── thermal-gs.mplstyle
# │   ├── UXArietis_auto.txt
# │   ├── ...
# ├── figures
# │   ├── ux-arietis_auto.pdf
# │   ├── ux-arietis_auto.png
# │   ├── ...
# ├── notebooks
# │   ├── autocorelation_appendixB.ipynb
# │   ├── ...
# .
# .
# .

# ## B1.3. Load

# In[2]:


autocorr = np.loadtxt('../data/UXArietis_auto.txt')
plt.style.use('../data/thermal-gs.mplstyle')


# ## B1.4. Plot

# In[3]:


fig, ax = plt.subplots(1, 1, figsize=(4, 3))
ax.grid()

n = np.linspace(1, 20000, autocorr.shape[0])
ax.plot(n, n / 50, '--k', label='50x steps')
ax.plot(n, autocorr, 'o-', label='autocorrelation')
ax.set_xlim(0, n.max())
ax.set_ylim(0, autocorr.max() + 0.1 * (autocorr.max() - autocorr.min()))
ax.set_xlabel('number of steps')
ax.set_ylabel(r'mean $\hat{\tau}$')
ax.xaxis.set_major_locator(mpl.ticker.MultipleLocator(n[-1]/4))
ax.xaxis.set_minor_locator(mpl.ticker.MultipleLocator(n[-1]/20))
ax.yaxis.set_major_locator(mpl.ticker.MultipleLocator(50))
ax.yaxis.set_minor_locator(mpl.ticker.MultipleLocator(10))

fig.set_facecolor('white')
plt.savefig('../figures/ux-arietis_auto.png', bbox_inches='tight')
plt.savefig('../figures/ux-arietis_auto.pdf', bbox_inches='tight')
plt.show()

