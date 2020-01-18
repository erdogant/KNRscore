#%% Tests regarding flameplot
import flameplot as flameplot
import pandas as pd

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
