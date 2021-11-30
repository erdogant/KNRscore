import flameplot as flameplot
from sklearn import (manifold, decomposition)
import numpy as np

# fig    = flameplot.plot(scores)
# X,y    = flameplot.import_example()
# fig    = flameplot.scatterd(X[:,0],X[:,1],label=y)


# Load data
X,y=flameplot.import_example()

# Make PCA
X_pca = decomposition.TruncatedSVD(n_components=50).fit_transform(X)

# Make tSNE
X_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)

# Make random
X_rand=np.append([np.random.permutation(X_tsne[:,0])],  [np.random.permutation(X_tsne[:,1])], axis=0).reshape(-1,2)

# Compare PCA vs. tSNE
scores=flameplot.compare(X_pca, X_tsne, n_steps=25)
# plot PCA vs. tSNE
fig=flameplot.plot(scores, xlabel='PCA', ylabel='tSNE', reverse_cmap=True)

# Compare random vs. tSNE
scores=flameplot.compare(X_rand, X_tsne, n_steps=25)
# plot Random vs. tSNE
fig=flameplot.plot(scores, xlabel='Random', ylabel='tSNE')

# Scatter
flameplot.scatter(X_pca[:,0], X_pca[:,1] ,y, title='PCA')
flameplot.scatter(X_tsne[:,0], X_tsne[:,1], y, title='tSNE')
flameplot.scatter(X_rand[:,0], X_rand[:,1], y, title='Random')