#%% Tests regarding flameplot

import flameplot as flameplot
from sklearn import (manifold, decomposition)
import pandas as pd
import numpy as np

# %% Load data
X,y=flameplot.import_example()

# %% Make PCA
X_pca_50 = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
X_pca_2 = decomposition.TruncatedSVD(n_components=2).fit_transform(X)
# Make tSNE
X_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)
# Make random
X_rand=np.append([np.random.permutation(X_tsne[:,0])],  [np.random.permutation(X_tsne[:,1])], axis=0).reshape(-1,2)

# %% Scatter
flameplot.scatter(X_pca_2,y, title='PCA')
flameplot.scatter(X_tsne,y, title='tSNE')
flameplot.scatter(X_rand,y, title='Random')

# %% Compare PCA(50) vs. tSNE
scores=flameplot.compare(X_pca_50, X_tsne, n_steps=5)
# plot
fig=flameplot.plot(scores, xlabel='PCA (50d)', ylabel='tSNE (2d)')

# Compare PCA(2) vs. tSNE
scores=flameplot.compare(X_pca_2, X_tsne, n_steps=5)
# plot
fig=flameplot.plot(scores, xlabel='PCA (2d)', ylabel='tSNE (2d)')

# Compare random vs. tSNE
scores=flameplot.compare(X_rand, X_tsne, n_steps=5)
# plot
fig=flameplot.plot(scores, xlabel='Random (2d)', ylabel='tSNE (2d)')

#%%
from sklearn import (manifold, decomposition)

# digits = datasets.load_digits(n_class=6)
# X = digits.data
# y = digits.target
# n_samples, n_features = X.shape
# n_neighbors = 30

X,y=flameplot.import_example()
# df=pd.DataFrame(data=X, index=y)
# df.to_csv('./flameplot/data/digits.csv')

# %% PCA
print("Computing PCA projection")
X_pca = decomposition.TruncatedSVD(n_components=50).fit_transform(X)

# import pca as pca
# out=pca.fit(X, components=0.95, y=y)
# pca.biplot(out)
# pca.plot(out)

# %% t-SNE embedding of the digits dataset
print("Computing t-SNE embedding")
tsne = manifold.TSNE(n_components=2, init='pca')
X_tsne = tsne.fit_transform(X)

tsne = manifold.TSNE(n_components=2, init='pca')
X_tsne2 = tsne.fit_transform(X)

#%%
scores=flameplot.compare(X_tsne2, X_tsne, n_steps=10)
fig=flameplot.plot(scores)

#%%
scores=flameplot.compare(X_tsne, X_pca, n_steps=10)
fig=flameplot.plot(scores)
