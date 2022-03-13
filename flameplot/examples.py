import flameplot as flameplot
from sklearn import (manifold, decomposition)
import numpy as np

# %%
# Load libraries
from sklearn import (manifold, decomposition)
import pandas as pd
import numpy as np

# Import library
import flameplot as flameplot

# Load mnist example data
X,y = flameplot.import_example()

# PCA: 50 PCs
X_pca_50 = decomposition.TruncatedSVD(n_components=50).fit_transform(X)

# tSNE: 2D
X_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)

# Compare PCA(50) vs. tSNE
scores = flameplot.compare(X_pca_50, X_tsne, n_steps=5)

# Plot
fig = flameplot.plot(scores, xlabel='PCA (50d)', ylabel='tSNE (2d)')

# %%
# Load data
X, y = flameplot.import_example()

# Compute embeddings
embed_pca = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
embed_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)

# Compare PCA vs. tSNE
scores = flameplot.compare(embed_pca, embed_tsne, n_steps=25)
# plot PCA vs. tSNE
fig = flameplot.plot(scores, xlabel='PCA', ylabel='tSNE')


# %%
# Make random data
X_rand=np.append([np.random.permutation(embed_tsne[:,0])],  [np.random.permutation(embed_tsne[:,1])], axis=0).reshape(-1,2)

# Compare random vs. tSNE
scores = flameplot.compare(X_rand, embed_tsne, n_steps=25)
fig = flameplot.plot(scores, xlabel='Random', ylabel='tSNE')

scores = flameplot.compare(X_rand, embed_pca, n_steps=25)
fig = flameplot.plot(scores, xlabel='Random', ylabel='PCA')

# Scatter
flameplot.scatter(embed_pca[:,0], embed_pca[:,1] , label=y, title='PCA')
flameplot.scatter(embed_tsne[:,0], embed_tsne[:,1], label=y, title='tSNE')
flameplot.scatter(X_rand[:,0], X_rand[:,1], label=y, title='Random')
