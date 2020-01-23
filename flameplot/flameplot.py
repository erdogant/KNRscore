"""Comparing low vs. high dimensions/embeddings.

    import flameplot as flameplot

    scores = flameplot.compare(data1, data2)
    fig    = flameplot.plot(scores)
    X,y    = flameplot.import_example()
    fig    = flameplot.scatterd(X[:,0],X[:,1],label=y)


 Requirements
 ------------
   os
   numpy
   tqdm
   scipy
   imagesc
   scatterd


 Example
 -------

    from sklearn import (manifold, decomposition)
    import flameplot as flameplot

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

"""

# --------------------------------------------------------------------------
# Name        : flameplot.py
# Author      : Erdogan.Taskesen
# Date        : Jan. 2020
# Licence     : MIT
# --------------------------------------------------------------------------

# %% Libraries
import os
import numpy as np
from tqdm import tqdm
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import imagesc as imagesc
from scatterd import scatterd


# %% Scatter
def scatter(Xcoord,Ycoord,**args):
    """Scatterplot.

    Parameters
    ----------
    Xcoord : numpy array
        1D Coordinates.
    Ycoord : numpy array
        1D Coordinates.
    **args : TYPE
        See scatterd for all possible arguments.

    Returns
    -------
    fig.

    """
    # Pass all in scatterd
    fig = scatterd(Xcoord, Ycoord,**args)
    return(fig)


# %%
def compare(data1, data2, nn=250, n_steps=5, verbose=3):
    """

    Parameters
    ----------
    data1 : numpy array
        Mapping of first embedding.

    data2 : numpy array
        Mapping of second embedding.

    nn : integer, optional
        number of neirest neighbor to compare between the two maps. This can be set based on the smalles class size or the aveage class size. The default is 250.

    n_steps : integer
        The number of evaluation steps until reaching nn, optional. If higher, the resolution becomes lower and vice versa. The default is 5.

    verbose : integer, optional
        print messages. The default is 3.

    Returns
    -------
    dict contains numpy array with scorings.

    """
    # DECLARATIONS
    args = {}
    args['verbose'] = verbose
    args['n_steps'] = n_steps
    args['nn'] = nn

    # Compute distances
    data1Dist = squareform(pdist(data1, 'euclidean'))
    data2Dist = squareform(pdist(data2, 'euclidean'))

    # Take NN based for each of the sample
    data1Order = _K_nearestneighbors(data1Dist, args['nn'])
    data2Order = _K_nearestneighbors(data2Dist, args['nn'])

    # Update nn
    args['nn'] = np.minimum(args['nn'], len(data1Order[0]))
    args['nn'] = np.arange(1, args['nn']+1, args['n_steps'])

    # Compute overlap
    scores = np.zeros((len(args['nn']), len(args['nn'])))
    for p in tqdm(range(0, len(args['nn'])), disable=(True if args['verbose'] == 0 else False)):
        scores[p, :] = _overlap_comparison(data1Order, data2Order, args['nn'], data1.shape[0], args['nn'][p])

    # Return
    out = dict()
    out['scores'] = scores
    out['nn'] = args['nn']
    out['n_steps'] = args['n_steps']
    return(out)


# %% Plot
def plot(out, cmap='jet', xlabel=None, ylabel=None, reverse_cmap=False):
    """Make plot.

    Parameters
    ----------
    out : dict
        output of the compare() function.
    cmap : string, optional
        colormap. The default is 'jet'.

    Returns
    -------
    fig.

    """
    if reverse_cmap:
        cmap=cmap+'_r'
        
    fig = imagesc.plot(np.flipud(out['scores']),
                       cmap=cmap,
                       row_labels=np.flipud(out['nn']),
                       col_labels=out['nn'],
                       figsize=(20, 15),
                       grid=True,
                       vmin=0,
                       vmax=1,
                       linecolor='#0f0f0f',
                       linewidth=0.25,
                       xlabel=xlabel,
                       ylabel=ylabel)
    return(fig)


# %% Example data
def import_example():
    """Load digit example dataset.

    Returns
    -------
    TYPE
        No input required.

    Returns
    -------
    X,y
    """
    # Local library
    import pandas as pd

    print('[FLAMEPLOT] Loading digit example..')
    curpath = os.path.dirname(os.path.abspath(__file__))
    PATH_TO_DATA = os.path.join(curpath, 'data', 'digits.zip')
    if os.path.isfile(PATH_TO_DATA):
        df = pd.read_csv(PATH_TO_DATA, sep=',')
        return (df.values[:, 1:], df.values[:, 0])
    else:
        print('[KM] Oops! Example data not found! Try to get it at: www.github.com/erdogant/flameplot/')
        return None


# %% Take NN based on the number of samples availble
def _overlap_comparison(data1Order, data2Order, nn, samples, p):

    out = np.zeros((len(nn), 1), dtype='float').ravel()
    for k in range(0, len(nn)):
        tmpoverlap = np.zeros((samples, 1), dtype='uint32').ravel()

        for i in range(0, samples):
            tmpoverlap[i] = len(np.intersect1d(data1Order[i][0:p], data2Order[i][0:nn[k]]))

        out[k] = sum(tmpoverlap) / (len(tmpoverlap) * np.minimum(p, nn[k]))

    return(out)

# %% Take NN based on the number of samples availble
def _K_nearestneighbors(data1Dist, K):

    outputOrder = []

    # Find neirest neighbors
    for i in range(0, data1Dist.shape[0]):
        I = np.argsort(data1Dist[i, :])
        Dsort = data1Dist[i, I]
        idx = np.where(Dsort != 0)[0]
        Dsort = Dsort[idx]
        I = I[idx]
        I = I[np.arange(0, np.minimum(K, len(I)))]

        # Store data
        outputOrder.append(I[np.arange(0, np.minimum(K, len(I)))])
    return(outputOrder)
