[![Python](https://img.shields.io/pypi/pyversions/KNRscore)](https://img.shields.io/pypi/pyversions/KNRscore)
[![PyPI Version](https://img.shields.io/pypi/v/KNRscore)](https://pypi.org/project/KNRscore/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/KNRscore/blob/master/LICENSE)
[![Github Forks](https://img.shields.io/github/forks/erdogant/KNRscore.svg)](https://github.com/erdogant/KNRscore/network)
[![GitHub Open Issues](https://img.shields.io/github/issues/erdogant/KNRscore.svg)](https://github.com/erdogant/KNRscore/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Downloads](https://pepy.tech/badge/flameplot/month)](https://pepy.tech/project/KNRscore/)
[![Downloads](https://pepy.tech/badge/flameplot)](https://pepy.tech/project/KNRscore)
[![DOI](https://zenodo.org/badge/234703853.svg)](https://zenodo.org/badge/latestdoi/234703853)
[![Sphinx](https://img.shields.io/badge/Sphinx-Docs-Green)](https://erdogant.github.io/KNRscore/)
[![Medium](https://img.shields.io/badge/Medium-Blog-green)](https://erdogant.github.io/KNRscore/pages/html/Documentation.html#medium-blog)

## KNRscore - K-Nearest-Rank Similarity to quantify local structural similarity between two maps or embeddings.

**⭐️ Star this repo if you like it ⭐️**


### Medium Blog

Also checkout [The Similarity between t-SNE, UMAP, PCA, and Other Mappings](https://erdogant.github.io/KNRscore/pages/html/Documentation.html#medium-blog) to get a structured overview and usage of ``KNRscore``.


#

### Method
To compare the embedding of samples in two different maps, we propose a scale dependent similarity measure. For a pair of maps X and Y, we compare the sets of the, respectively, kx and ky nearest neighbours of each sample. We first define the variable rxij as the rank of the distance of sample j among all samples with respect to sample i, in map X. The nearest neighbor of sample i will have rank 1, the second nearest neighbor rank 2, etc. Analogously, ryij is the rank of sample j with respect to sample i in map Y. Now we define a score on the interval [0, 1], as (eq. 1)
<p align="left">
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/eq1.png" width="450" />
</p>
where the variable n is the total number of samples, and the indicator function is given by (eq. 2)
<p align="left">
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/eq2.png" width="250" />
</p>
The score sx,y(kx, ky) will have value 1 if, for each sample, all kx nearest neighbours in map X are also the ky nearest neighbours in map Y, or vice versa. Note that a local neighborhood of samples can be set on the minimum number of samples in the class. Alternatively, kxy can be also set on the average class size.

### Schematic overview
Schematic overview to systematically compare local and global differences between two sample projections. For illustration we compare two input maps (x and y) in which each map contains n samples (step 1). The second step is the ranking of samples based on Euclidean distance. The ranks of map x are subsequently compared to the ranks of map y for kx and ky nearest neighbours (step 3). The overlap between ranks (step 4), is subsequently summarized in Score: Sx,y(kx,ky).
<p align="left">
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/schematic_overview.png" width="350" />
</p>


<hr> 

### [Documentation pages](https://erdogant.github.io/KNRscore/)

On the [documentation pages](https://erdogant.github.io/KNRscore/) you can find detailed information about the working of the ``KNRscore`` with examples. 

<hr> 


#### Install KNRscore from PyPI

```bash
pip install KNRscore
```

#### Import KNRscore package

```python
import KNRscore as knrs
```

### Functions in KNRscore

```python
import KNRscore as knrs
scores = knrs.compare(map1, map2)
fig    = knrs.plot(scores)
fig    = knrs.scatter(Xcoord,Ycoord)

```
### Example
```python
    # Imort library
    import KNRscore as knrs

    # Load data
    X, y = KNRscore.import_example()
    
    # Compute embeddings
    embed_pca = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
    embed_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)
    
    # Compare PCA vs. tSNE
    scores = knrs.compare(embed_pca, embed_tsne, n_steps=25)
    
    # plot PCA vs. tSNE
    fig, ax = knrs.plot(scores, xlabel='PCA', ylabel='tSNE')
    fig, ax = knrs.scatter(embed_tsne[:, 0], embed_tsne[:, 1], labels=y, cmap='Set1', title='tSNE Scatter Plot')
    fig, ax = knrs.scatter(embed_pca[:, 0], embed_pca[:, 1], labels=y, cmap='Set1', title='PCA Scatter Plot')
```

### Examples

* [Example: Comparison between two maps follow the quantification of local similarity approach.](https://erdogant.github.io/KNRscore/pages/html/Examples.html)

<p align="left">
  <a href="https://erdogant.github.io/KNRscore/pages/html/Examples.html">
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/pca50_tsne.png" width="400" />
  </a>
</p>

# 

* [Example: Comparison 2D embeddings: PCA vs tSNE](https://erdogant.github.io/KNRscore/pages/html/Examples.html#comparison-2d-embeddings-pca-vs-tsne)

<p align="left">
  <a href="https://erdogant.github.io/KNRscore/pages/html/Examples.html#comparison-2d-embeddings-pca-vs-tsne">
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/pca2_tsne.png" width="400" />
  </a>
</p>

# 

* [Example: Comparison Random data vs. t-SNE](https://erdogant.github.io/KNRscore/pages/html/Examples.html#comparison-random-data-vs-t-sne)

<p align="left">
  <a href="https://erdogant.github.io/KNRscore/pages/html/Examples.html#comparison-random-data-vs-t-sne">
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/random_tsne.png" width="400" />
  </a>
</p>


# 

* [Example: Scatterplots](https://erdogant.github.io/KNRscore/pages/html/Examples.html#scatterplots)

<p align="left">
  <a href="https://erdogant.github.io/KNRscore/pages/html/Examples.html#scatterplots">
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/scatter_pca.png" width="600" />
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/scatter_tsne.png" width="600" />
  <img src="https://github.com/erdogant/KNRscore/blob/master/docs/figs/scatter_random.png" width="600" />
  </a>
</p>

<hr>

<hr>



## References
* Taskesen, E. et al. Pan-cancer subtyping in a 2D-map shows substructures that are driven by specific combinations of molecular characteristics. Sci. Rep. 6, 24949
* https://static-content.springer.com/esm/art%3A10.1038%2Fsrep24949/MediaObjects/41598_2016_BFsrep24949_MOESM12_ESM.pdf
* https://www.nature.com/articles/srep24949


<a href="https://www.buymeacoffee.com/erdogant"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=erdogant&button_colour=FFDD00&font_colour=000000&font_family=Cookie&outline_colour=000000&coffee_colour=ffffff" /></a>
