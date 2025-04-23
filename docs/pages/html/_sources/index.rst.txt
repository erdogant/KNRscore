KNRscore Documentation
======================

|python| |pypi| |docs| |stars| |LOC| |downloads_month| |downloads_total| |license| |forks| |open issues| |project status| |medium| |DOI| |repo-size| |donate|

.. image:: ../figs/pca2_tsne.png
   :width: 400
   :align: center
   :alt: PCA vs t-SNE Comparison

-----------------------------------

Overview
--------

``KNRscore`` is a powerful Python package for quantitative comparison of high-dimensional embeddings using a scale-dependent similarity measure. It enables researchers and data scientists to:

- Compare different dimensionality reduction techniques (PCA, t-SNE, UMAP, etc.)
- Quantify local similarities between embeddings
- Evaluate the preservation of neighborhood structures
- Visualize comparison results with intuitive plots

Key Features
------------

- **Scale-dependent Analysis**: Compare embeddings at different neighborhood scales
- **Flexible Input**: Works with any embedding or high-dimensional data
- **Intuitive Visualization**: Generate clear comparison plots
- **Easy Integration**: Simple usage with comprehensive documentation

.. tip::
    For a detailed explanation of the methodology, check out our `Medium blog post <https://towardsdatascience.com/the-similarity-between-t-sne-umap-pca-and-other-mappings-c6453b80f303>`_ on quantitative comparisons between dimensionality reduction techniques.

-----------------------------------

.. note::
    **Your ❤️ is important to keep maintaining this package.** You can `support <https://erdogant.github.io/KNRscore/pages/html/Documentation.html>`_ in various ways, have a look at the `sponser page <https://erdogant.github.io/KNRscore/pages/html/Documentation.html>`_.
    Report bugs, issues and feature extensions at `github <https://github.com/erdogant/KNRscore/>`_ page.


Quick Start
-----------

.. code-block:: console

   pip install KNRscore

.. code-block:: python

   import KNRscore as knrs
   from sklearn.decomposition import PCA
   from sklearn.manifold import TSNE
   
   # Load example data
   X, y = knrs.import_example(data='digits')
   
   # Create embeddings
   pca = PCA(n_components=2).fit_transform(X)
   tsne = TSNE(n_components=2).fit_transform(X)
   
   # Compare embeddings
   scores = knrs.compare(pca, tsne)
   
   # Visualize results
   fig, ax = knrs.plot(scores, xlabel='PCA', ylabel='tSNE')

.. note::
    **Support the Project**: Your support helps maintain and improve this package. Consider:
    
    - Starring the repository on GitHub
    - Reporting issues and suggesting features
    - Contributing code or documentation
    - Supporting through GitHub Sponsors
    
    Visit our `sponsor page <https://erdogant.github.io/KNRscore/pages/html/Documentation.html>`_ for more ways to contribute.

Documentation Contents
======================

.. toctree::
   :maxdepth: 2
   :caption: Getting Started
   
   Background
   Installation
   Tutorials

.. toctree::
   :maxdepth: 2
   :caption: Examples
   
   Examples

.. toctree::
   :maxdepth: 2
   :caption: Usage
   
   Documentation
   Coding quality
   KNRscore.KNRscore

.. toctree::
   :maxdepth: 2
   :caption: Reference
   
   genindex
   modindex
   search

.. |python| image:: https://img.shields.io/pypi/pyversions/KNRscore.svg
    :alt: Python Version
    :target: https://erdogant.github.io/KNRscore/

.. |pypi| image:: https://img.shields.io/pypi/v/KNRscore.svg
    :alt: PyPI Version
    :target: https://pypi.org/project/KNRscore/

.. |docs| image:: https://img.shields.io/badge/Sphinx-Docs-blue.svg
    :alt: Documentation
    :target: https://erdogant.github.io/KNRscore/

.. |stars| image:: https://img.shields.io/github/stars/erdogant/KNRscore
    :alt: GitHub Stars
    :target: https://github.com/erdogant/KNRscore

.. |LOC| image:: https://sloc.xyz/github/erdogant/KNRscore/?category=code
    :alt: Lines of Code
    :target: https://github.com/erdogant/KNRscore

.. |downloads_month| image:: https://static.pepy.tech/personalized-badge/flameplot?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=PyPI%20downloads/month
    :alt: Monthly Downloads
    :target: https://pepy.tech/project/KNRscore

.. |downloads_total| image:: https://static.pepy.tech/personalized-badge/flameplot?period=total&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads
    :alt: Total Downloads
    :target: https://pepy.tech/project/KNRscore

.. |license| image:: https://img.shields.io/badge/license-MIT-green.svg
    :alt: MIT License
    :target: https://github.com/erdogant/KNRscore/blob/master/LICENSE

.. |forks| image:: https://img.shields.io/github/forks/erdogant/KNRscore.svg
    :alt: GitHub Forks
    :target: https://github.com/erdogant/KNRscore/network

.. |open issues| image:: https://img.shields.io/github/issues/erdogant/KNRscore.svg
    :alt: Open Issues
    :target: https://github.com/erdogant/KNRscore/issues

.. |project status| image:: http://www.repostatus.org/badges/latest/active.svg
    :alt: Project Status
    :target: http://www.repostatus.org/#active

.. |medium| image:: https://img.shields.io/badge/Medium-Blog-green.svg
    :alt: Medium Blog
    :target: https://erdogant.github.io/KNRscore/pages/html/Documentation.html#medium-blog

.. |donate| image:: https://img.shields.io/badge/Support%20this%20project-grey.svg?logo=github%20sponsors
    :alt: Support
    :target: https://erdogant.github.io/KNRscore/pages/html/Documentation.html#

.. |DOI| image:: https://zenodo.org/badge/234703853.svg
    :alt: DOI
    :target: https://zenodo.org/badge/latestdoi/234703853

.. |repo-size| image:: https://img.shields.io/github/repo-size/erdogant/KNRscore
    :alt: repo-size
    :target: https://img.shields.io/github/repo-size/erdogant/KNRscore

.. include:: add_bottom.add
