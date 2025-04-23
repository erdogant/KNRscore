import KNRscore as KNRscore
from sklearn import (manifold, decomposition)
import numpy as np

#%%
import KNRscore as knrs

knrs.check_logger(verbose='debug')
knrs.check_logger(verbose='info')
knrs.check_logger(verbose='warning')
knrs.check_logger(verbose='error')

# %%
# Load libraries
from sklearn import (manifold, decomposition)
import pandas as pd
import numpy as np

# Import library
import KNRscore as KNRscore

# Load mnist example data
X, y = KNRscore.import_example()

# PCA: 50 PCs
X_pca_50 = decomposition.TruncatedSVD(n_components=50).fit_transform(X)

# tSNE: 2D
X_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)

# Compare PCA(50) vs. tSNE
scores = KNRscore.compare(X_pca_50, X_tsne, n_steps=25)

# Plot
fig, ax = KNRscore.plot(scores, xlabel='PCA (50d)', ylabel='tSNE (2d)')

fig, ax = KNRscore.scatter(X_pca_50[:,0], X_pca_50[:,1])

# %%
# Load data
X, y = KNRscore.import_example()

# Compute embeddings
embed_pca = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
embed_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)

# Compare PCA vs. tSNE
scores = KNRscore.compare(embed_pca, embed_tsne, n_steps=25)
# plot PCA vs. tSNE
fig, ax = KNRscore.plot(scores, xlabel='PCA', ylabel='tSNE')


# %%
# Make random data
X_rand=np.append([np.random.permutation(embed_tsne[:,0])],  [np.random.permutation(embed_tsne[:,1])], axis=0).reshape(-1,2)

# Compare random vs. tSNE
scores = KNRscore.compare(X_rand, embed_tsne, n_steps=25)
fig, ax = KNRscore.plot(scores, xlabel='Random', ylabel='tSNE')

scores = KNRscore.compare(X_rand, embed_pca, n_steps=25)
fig, ax = KNRscore.plot(scores, xlabel='Random', ylabel='PCA')

# Scatter
fig, ax = KNRscore.scatter(embed_pca[:,0], embed_pca[:,1] , labels=y, title='PCA', density=False)
fig, ax = KNRscore.scatter(embed_tsne[:,0], embed_tsne[:,1], labels=y, title='tSNE')
fig, ax = KNRscore.scatter(X_rand[:,0], X_rand[:,1], labels=y, title='Random')


#%% Tests regarding KNRscore
import KNRscore as KNRscore
import numpy as np
from sklearn import (manifold, decomposition)

# %% Load data
X,y=KNRscore.import_example()

# %% PCA
X_pca_50 = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
X_pca_2 = decomposition.TruncatedSVD(n_components=2).fit_transform(X)
# tSNE
X_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)
# Random
X_rand=np.c_[np.random.permutation(X_pca_2[:,0]), np.random.permutation(X_pca_2[:,1])]

# %% Scatter
KNRscore.scatter(X_pca_2[:,0], X_pca_2[:,1] ,label=y, title='PCA')
KNRscore.scatter(X_tsne[:,0],  X_tsne[:,1],  label=y, title='tSNE')
KNRscore.scatter(X_rand[:,0],  X_rand[:,1],  label=y, title='Random')

# %% Compare PCA(50) vs. tSNE
scores=KNRscore.compare(X_pca_50, X_tsne, n_steps=25)
fig=KNRscore.plot(scores, xlabel='PCA (50d)', ylabel='tSNE (2d)')
# Compare PCA(2) vs. tSNE
scores=KNRscore.compare(X_pca_2, X_tsne, n_steps=25)
fig=KNRscore.plot(scores, xlabel='PCA (2d)', ylabel='tSNE (2d)')
# Compare random vs. tSNE
scores=KNRscore.compare(X_rand, X_tsne, n_steps=25)
fig=KNRscore.plot(scores, xlabel='Random (2d)', ylabel='tSNE (2d)')

# %%