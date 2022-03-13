import flameplot as flameplot
from sklearn import (manifold, decomposition)
import numpy as np

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
