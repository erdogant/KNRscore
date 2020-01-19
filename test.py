#%% Tests regarding flameplot

import flameplot as flameplot
import numpy as np
from sklearn import (manifold, decomposition)

# %% Load data
X,y=flameplot.import_example()

# %% PCA
X_pca_50 = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
X_pca_2 = decomposition.TruncatedSVD(n_components=2).fit_transform(X)
# tSNE
X_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)
# Random
X_rand=np.c_[np.random.permutation(X_pca_2[:,0]), np.random.permutation(X_pca_2[:,1])]

# %% Scatter
flameplot.scatterd(X_pca_2[:,0], X_pca_2[:,1] ,label=y, title='PCA')
flameplot.scatterd(X_tsne[:,0],  X_tsne[:,1],  label=y, title='tSNE')
flameplot.scatterd(X_rand[:,0],  X_rand[:,1],  label=y, title='Random')

# %% Compare PCA(50) vs. tSNE
scores=flameplot.compare(X_pca_50, X_tsne)
fig=flameplot.plot(scores, xlabel='PCA (50d)', ylabel='tSNE (2d)')
# Compare PCA(2) vs. tSNE
scores=flameplot.compare(X_pca_2, X_tsne)
fig=flameplot.plot(scores, xlabel='PCA (2d)', ylabel='tSNE (2d)')
# Compare random vs. tSNE
scores=flameplot.compare(X_rand, X_tsne)
fig=flameplot.plot(scores, xlabel='Random (2d)', ylabel='tSNE (2d)')
