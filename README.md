# flameplot

[![Python](https://img.shields.io/pypi/pyversions/flameplot)](https://img.shields.io/pypi/pyversions/flameplot)
[![PyPI Version](https://img.shields.io/pypi/v/flameplot)](https://pypi.org/project/flameplot/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/erdogant/flameplot/blob/master/LICENSE)
[![Downloads](https://pepy.tech/badge/flameplot/week)](https://pepy.tech/project/flameplot/week)

* Quantification of local similarity across two maps/embeddings. 

### Method
To compare the embedding of samples in two different maps, we propose a scale dependent similarity measure. For a pair of maps X and Y, we compare the sets of the, respectively, kx and ky nearest neighbours of each sample. We first define the variable rxij as the rank of the distance of sample j among all samples with respect to sample i, in map X. The nearest neighbor of sample i will have rank 1, the second nearest neighbor rank 2, etc. Analogously, ryij is the rank of sample j with respect to sample i in map Y. Now we define a score on the interval [0, 1], as (eq. 1)
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/eq1.png" width="400" />
</p>
where the variable n is the total number of samples, and the indicator function is given by (eq. 2)
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/eq2.png" width="200" />
</p>
The score sx,y(kx, ky) will have value 1 if, for each sample, all kx nearest neighbours in map X are also the ky nearest neighbours in map Y, or vice versa. Note that a local neighborhood of samples can be set on the minimum number of samples in the class. Alternatively, kxy can be also set on the average class size.

### Schematic overview
Schematic overview to systematically compare local and global differences between two sample projections. For illustration we compare two input maps (x and y) in which each map contains n samples (step 1). The second step is the ranking of samples based on Euclidean distance. The ranks of map x are subsequently compared to the ranks of map y for kx and ky nearest neighbours (step 3). The overlap between ranks (step 4), is subsequently summarized in Score: Sx,y(kx,ky).
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/schematic_overview.png" width="400" />
</p>


### Functions in flameplot
```python
# data is your numpy array
fig = flameplot(coord1, coord2)
status = flameplot.savefig(fig)
```

## Contents
- [Installation](#-installation)
- [Requirements](#-Requirements)
- [Quick Start](#-quick-start)
- [Contribute](#-contribute)
- [Citation](#-citation)
- [Maintainers](#-maintainers)
- [License](#-copyright)

## Installation
* Install flameplot from PyPI (recommended). flameplot is compatible with Python 3.6+ and runs on Linux, MacOS X and Windows. 
* It is distributed under the MIT license.

## Requirements
```python
pip install numpy matplotlib
or
pip install -r requirements.txt
```

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
```python
# Example here
```
<p align="center">
  <img src="https://github.com/erdogant/flameplot/blob/master/docs/figs/fig.png" width="300" />
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

## Maintainers
* Erdogan Taskesen, github: [erdogant](https://github.com/erdogant)

## References
* https://static-content.springer.com/esm/art%3A10.1038%2Fsrep24949/MediaObjects/41598_2016_BFsrep24949_MOESM12_ESM.pdf

## Licence
See [LICENSE](LICENSE) for details.
