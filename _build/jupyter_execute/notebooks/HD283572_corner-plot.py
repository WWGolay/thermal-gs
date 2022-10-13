#!/usr/bin/env python
# coding: utf-8

# # 8. HD 283572 Corner Plot

# ## 8.1. Notebook setup

# In[1]:


import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import emcee
import corner
import warnings
warnings.filterwarnings('ignore')


# ## 8.2. <a href="https://www.dropbox.com/s/6lfj9z74tphpekj/hd283572_corner-plot.zip?dl=1">Download data</a>

# Unzip the contents into a folder named <font color='green'>data</font> in the same level as the notebooks folder. The directory structure should end up looking like the following: 
# ```
# thermal-gs
# ├── data
# │   ├── HD283572_chain.h5
# │   ├── HD283572_lmfit_params.txt
# │   ├── thermal-gs.mplstyle
# │   ├── ...
# ├── figures
# │   ├── HD283572_corner.pdf
# │   ├── HD283572_corner.png
# │   ├── ...
# ├── notebooks
# │   ├── HD283572_corner-plot.ipynb
# │   ├── ...
# .
# .
# .

# ## 8.3. Load

# In[2]:


sampler = emcee.backends.HDFBackend('../data/HD283572_chain.h5')
samples = sampler.get_chain(flat=True)
samples /= np.array([1, 1, 1, 1, np.pi/180, 1, 1, 1, 1, np.pi/180])
lmfit_params = np.loadtxt('../data/HD283572_lmfit_params.txt')
lmfit_params /= np.array([1, 1, 1, 1, np.pi/180, 1, 1, 1, 1, np.pi/180])

plt.style.use('../data/thermal-gs.mplstyle')


# ## 8.4. Plot

# In[3]:


thin = 10000
plt_labels = ['$L_{pwr}$', '$\delta$', '$n_{e,pwr}$', '$B_{pwr}$', '$\phi_{pwr}$', '$L_{th}$', '$T_e$', '$n_{e,th}$', '$B_{th}$', '$\phi_{th}$']
median_values = np.median(samples[::thin, :], axis=0)
winnerWalker = np.argmax(sampler.get_log_prob(flat=True))
mostParams = samples[winnerWalker]
cmap = mpl.cm.get_cmap('Reds')
cmap.set_under(color='w')

cornerFig = corner.corner(samples[::thin, :],color='black',top_ticks=True,quiet=True, show_titles=True,use_math_text=True,
labels=plt_labels,plot_datapoints=False,quantiles=[0.16, 0.84], title_quantiles=[0.16, 0.5, 0.84], label_kwargs={"fontsize":16}, 
title_kwargs={"fontsize":16}, max_n_ticks=4, bins=25, title_fmt='3.3g', plot_density=False, fill_contours=True,
levels=(0.393, 0.865, 0.989), hist_kwargs={'color':cmap(0.75)}, 
contourf_kwargs={'colors':(cmap(-1), cmap(0.25), cmap(0.75), cmap(0.999)), 'alpha':0.75})

corner.overplot_lines(cornerFig, lmfit_params, color='C1', label='Least squares')
corner.overplot_points(cornerFig, np.array([lmfit_params]), color='C1', marker='s', ms=3)
corner.overplot_lines(cornerFig, mostParams, color='C0', label='Most probable')
corner.overplot_points(cornerFig, np.array([mostParams]), color='C0', marker='s', ms=5)
corner.overplot_lines(cornerFig, median_values, color='black', label='Median')
corner.overplot_points(cornerFig, np.array([median_values]), color='black', marker='s', ms=5)

handles,labels = cornerFig.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
cornerFig.legend(by_label.values(), by_label.keys(), fontsize=24)
cornerFig.set_facecolor('white')
plt.savefig('../figures/HD283572_corner.png', bbox_inches='tight')
plt.savefig('../figures/HD283572_corner.pdf', bbox_inches='tight')
cornerFig.show()

