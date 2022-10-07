from flameplot.flameplot import(
    compare,
    plot,
    import_example,
    scatter,
    wget)

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.1.0'

# module level doc-string
__doc__ = """
flameplot - Python package for the comparison of high dimensional embeddings using a scale dependent similarity measure.
=================================================================================================================================

Decription
-----------
Quantification of local similarity across two maps or embeddings, such as PCA and t-SNE.
To compare the embedding of samples in two different maps using a scale dependent similarity measure.
For a pair of maps X and Y, we compare the sets of the, respectively, kx and ky nearest neighbours of each sample.

Examples
--------
>>> # Load data
>>> X, y = flameplot.import_example()
>>>
>>> # Compute embeddings
>>> embed_pca = decomposition.TruncatedSVD(n_components=50).fit_transform(X)
>>> embed_tsne = manifold.TSNE(n_components=2, init='pca').fit_transform(X)
>>>
>>> # Compare PCA vs. tSNE
>>> scores = flameplot.compare(embed_pca, embed_tsne, n_steps=25)
>>>
>>> # plot PCA vs. tSNE
>>> fig = flameplot.plot(scores, xlabel='PCA', ylabel='tSNE')
>>>

References
----------
* Blog: https://towardsdatascience.com/the-similarity-between-t-sne-umap-pca-and-other-mappings-c6453b80f303
* Github: https://github.com/erdogant/flameplot
* Documentation: https://erdogant.github.io/flameplot/

"""
