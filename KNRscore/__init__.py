import logging

from KNRscore.KNRscore import(
    compare,
    plot,
    import_example,
    scatter,
    wget,
    check_logger,
    )

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '2.0.0'

# Setup root logger
_logger = logging.getLogger('KNRscore')
_log_handler = logging.StreamHandler()
_fmt = '[{asctime}] [{name}] {msg}'
_formatter = logging.Formatter(fmt=_fmt, style='{', datefmt='%d-%m-%Y %H:%M:%S')
_log_handler.setFormatter(_formatter)
_log_handler.setLevel(logging.INFO)
_logger.addHandler(_log_handler)
_logger.propagate = False


# module level doc-string
__doc__ = """
KNRscore - A Python package for computing K-Nearest-Rank Similarity, a metric that quantifies local structural similarity between two maps or embeddings.


=================================================================================================================================

Decription
-----------
Quantification of local similarity across two maps or embeddings, such as PCA and t-SNE.
To compare the embedding of samples in two different maps using a scale dependent similarity measure.
For a pair of maps X and Y, we compare the sets of the, respectively, kx and ky nearest neighbours of each sample.

Examples
--------
>>> # Load data
>>> X, y = KNRscore.import_example()
>>>
>>> # Compute embeddings
>>> embed_pca = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
>>> embed_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)
>>>
>>> # Compare PCA vs. tSNE
>>> scores = KNRscore.compare(embed_pca, embed_tsne, n_steps=25)
>>>
>>> # plot PCA vs. tSNE
>>> fig = KNRscore.plot(scores, xlabel='PCA', ylabel='tSNE')
>>>

References
----------
* Blog: https://towardsdatascience.com/the-similarity-between-t-sne-umap-pca-and-other-mappings-c6453b80f303
* Github: https://github.com/erdogant/KNRscore
* Documentation: https://erdogant.github.io/KNRscore/

"""
