from flameplot.flameplot import(
    compare,
    plot,
    import_example,
    scatter,
    wget)

__author__ = 'Erdogan Tasksen'
__email__ = 'erdogant@gmail.com'
__version__ = '1.0.1'

# module level doc-string
__doc__ = """
flameplot - Python package for the comparison of high dimensional embeddings using a scale dependent similarity measure.
=================================================================================================================================

Decription
-----------
Quantification of local similarity across two maps or embeddings, such as PCA and t-SNE.
To compare the embedding of samples in two different maps using a scale dependent similarity measure.
For a pair of maps X and Y, we compare the sets of the, respectively, kx and ky nearest neighbours of each sample.

"""
