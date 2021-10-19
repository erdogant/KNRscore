# Flameplot - Quantification of local similarity across two maps/embeddings.

[![Python](https://img.shields.io/pypi/pyversions/flameplot)](https://img.shields.io/pypi/pyversions/flameplot)
[![PyPI Version](https://img.shields.io/pypi/v/flameplot)](https://pypi.org/project/flameplot/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/flameplot/blob/master/LICENSE)
[![Github Forks](https://img.shields.io/github/forks/erdogant/flameplot.svg)](https://github.com/erdogant/flameplot/network)
[![GitHub Open Issues](https://img.shields.io/github/issues/erdogant/flameplot.svg)](https://github.com/erdogant/flameplot/issues)
[![Project Status](http://www.repostatus.org/badges/latest/active.svg)](http://www.repostatus.org/#active)
[![Downloads](https://pepy.tech/badge/flameplot/month)](https://pepy.tech/project/flameplot/)
[![Downloads](https://pepy.tech/badge/flameplot)](https://pepy.tech/project/flameplot)
[![BuyMeCoffee](https://img.shields.io/badge/buymea-coffee-yellow.svg)](https://www.buymeacoffee.com/erdogant)
<!---[![Coffee](https://img.shields.io/badge/coffee-black-grey.svg)](https://erdogant.github.io/donate/?currency=USD&amount=5)-->

### Method
To compare the embedding of samples in two different maps, we propose a scale dependent similarity measure. For a pair of maps X and Y, we compare the sets of the, respectively, kx and ky nearest neighbours of each sample. We first define the variable rxij as the rank of the distance of sample j among all samples with respect to sample i, in map X. The nearest neighbor of sample i will have rank 1, the second nearest neighbor rank 2, etc. Analogously, ryij is the rank of sample j with respect to sample i in map Y. Now we define a score on the interval [0, 1], as (eq. 1)
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/eq1.png" width="450" />
</p>
where the variable n is the total number of samples, and the indicator function is given by (eq. 2)
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/eq2.png" width="250" />
</p>
The score sx,y(kx, ky) will have value 1 if, for each sample, all kx nearest neighbours in map X are also the ky nearest neighbours in map Y, or vice versa. Note that a local neighborhood of samples can be set on the minimum number of samples in the class. Alternatively, kxy can be also set on the average class size.

### Schematic overview
Schematic overview to systematically compare local and global differences between two sample projections. For illustration we compare two input maps (x and y) in which each map contains n samples (step 1). The second step is the ranking of samples based on Euclidean distance. The ranks of map x are subsequently compared to the ranks of map y for kx and ky nearest neighbours (step 3). The overlap between ranks (step 4), is subsequently summarized in Score: Sx,y(kx,ky).
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/schematic_overview.png" width="350" />
</p>


### Functions in flameplot
```python
scores = flameplot.compare(map1,map2)
fig    = flameplot.plot(scores)
X,y    = flameplot.import_example()
fig    = flameplot.scatter(Xcoord,Ycoord)

```
## Installation
* Install flameplot from PyPI (recommended). flameplot is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

## Quick Start
```
pip install flameplot
```

* Alternatively, install flameplot from the GitHub source:
```bash
git clone https://github.com/erdogant/flameplot.git
cd flameplot
python setup.py install
```  

### Import flameplot package
```python
import flameplot as flameplot
```

#### flameplot
Comparison between two maps follow the quantification of local similarity approach.
```python
# Load libraries
from sklearn import (manifold, decomposition)
import pandas as pd
import numpy as np

# Load example data
X,y=flameplot.import_example()

# PCA top 50 PCs
X_pca_50 = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
# PCA top 2 PCs
X_pca_2 = decomposition.TruncatedSVD(n_components=2).fit_transform(X)
# tSNE
X_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)
# Random
X_rand=np.c_[np.random.permutation(X_tsne[:,0]), np.random.permutation(X_tsne[:,1])]
```

Scatter for illustrations purposes
```python
import flameplot as flameplot
flameplot.scatter(X_pca_2[:,0], X_pca_2[:,1], label=y, title='PCA')
flameplot.scatter(X_tsne[:,0],  X_tsne[:,1],  label=y, title='tSNE')
flameplot.scatter(X_rand[:,0],  X_rand[:,1],  label=y, title='Random')
```
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/scatter_pca.png" width="600" />
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/scatter_tsne.png" width="600" />
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/scatter_random.png" width="600" />
</p>

Now we have the coordinates and can make the comparison and plot!
```python
# Compare PCA(50) vs. tSNE
scores1=flameplot.compare(X_pca_50, X_tsne, n_steps=5)
# Compare PCA(2) vs. tSNE
scores2=flameplot.compare(X_pca_2, X_tsne, n_steps=5)
# Compare random vs. tSNE
scores=flameplot.compare(X_rand, X_tsne, n_steps=5)
# plot
fig=flameplot.plot(scores1, xlabel='PCA (50d)', ylabel='tSNE (2d)')
fig=flameplot.plot(scores, xlabel='PCA (2d)', ylabel='tSNE (2d)')
fig=flameplot.plot(scores, xlabel='Random (2d)', ylabel='tSNE (2d)')
```
The comparison between the top 50D of PCA vs. 2D tSNE resulted in high similarities on local and global scales. The axis are the number of "neirest neighbors" (nn). What we see is that on local scales (low nn) high similarity is seen between the maps but also in higher scales.
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/pca50_tsne.png" width="400" />
</p>

The comparison between the top 2D of PCA vs. 2D tSNE resulted in much lower similarities compared to the 50D on local and global scales. What we see is that on local scales (low nn) there is low similarity which depicts that samples have different neighbors. On larger scale it becomes a bit more greenish and slightly more similarities are seen on average between the neighbors. This would basically suggest that the same digits are detected globally but are differently ordered on local scales.
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/pca2_tsne.png" width="400" />
</p>

The comparison between the Random data points vs. 2D tSNE resulted in low similarities on both local and global scales. This what we expect to see as we permuted the data.
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/random_tsne.png" width="400" />
</p>

## Citation
Please cite flameplot in your publications if this is useful for your research. Here is an example BibTeX entry:
```BibTeX
@misc{erdogant2019flameplot,
  title={flameplot},
  author={Erdogan Taskesen},
  year={2019},
  howpublished={\url{https://github.com/erdogant/flameplot}},
}
```
* Taskesen, E. et al. Pan-cancer subtyping in a 2D-map shows substructures that are driven by specific combinations of molecular characteristics. Sci. Rep. 6, 24949

## References
* https://static-content.springer.com/esm/art%3A10.1038%2Fsrep24949/MediaObjects/41598_2016_BFsrep24949_MOESM12_ESM.pdf
* https://www.nature.com/articles/srep24949

### Maintainer
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)
* Contributions are welcome.
* If you wish to buy me a <a href="https://www.buymeacoffee.com/erdogant">Coffee</a> for this work, it is very appreciated :)
