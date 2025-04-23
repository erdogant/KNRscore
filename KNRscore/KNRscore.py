"""Comparing low vs. high dimensions/embeddings."""

# -------------------------------
# Name        : KNRscore.py
# Author      : Erdogan.Taskesen
# Licence     : See licences
# -------------------------------

# %% Libraries
import os
import numpy as np
from tqdm import tqdm
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import imagesc as imagesc
from scatterd import scatterd

from urllib.parse import urlparse
import pandas as pd
import requests
import logging

logger = logging.getLogger(__name__)


# %%
def compare(mapX, mapY, nn=250, n_steps=5, verbose='info'):
    """Comparison of two embeddings.

    Decription
    -----------
    Quantification of local similarity across two maps or embeddings, such as PCA and t-SNE.
    To compare the embedding of samples in two different maps using a scale dependent similarity measure.
    For a pair of maps X and Y, we compare the sets of the, respectively, kx and ky nearest neighbours of each sample.

    Parameters
    ----------
    mapX : numpy array
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
    dict()
        * scores : array with the scores across various nearest neighbors (nn).
        * nn : nearest neighbors
        * n_steps : The number of evaluation steps until reaching nn.

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
    >>> fig, ax = KNRscore.plot(scores, xlabel='PCA', ylabel='tSNE')
    >>>

    References
    ----------
    * Blog: https://towardsdatascience.com/the-similarity-between-t-sne-umap-pca-and-other-mappings-c6453b80f303
    * Github: https://github.com/erdogant/KNRscore
    * Documentation: https://erdogant.github.io/KNRscore/

    """
    # Set logger
    set_logger(verbose=verbose)

    # DECLARATIONS
    args = {}
    args['verbose'] = verbose
    args['n_steps'] = n_steps
    args['nn'] = nn

    # Compute distances
    data1Dist = squareform(pdist(mapX, 'euclidean'))
    data2Dist = squareform(pdist(mapY, 'euclidean'))

    # Take NN based for each of the sample
    data1Order = _K_nearestneighbors(data1Dist, args['nn'])
    data2Order = _K_nearestneighbors(data2Dist, args['nn'])

    # Update nn
    args['nn'] = np.minimum(args['nn'], len(data1Order[0]))
    args['nn'] = np.arange(1, args['nn'] + 1, args['n_steps'])

    # Compute overlap
    scores = np.zeros((len(args['nn']), len(args['nn'])))
    for p in tqdm(range(0, len(args['nn'])), disable=(True if args['verbose'] == 0 else False)):
        scores[p, :] = _overlap_comparison(data1Order, data2Order, args['nn'], mapX.shape[0], args['nn'][p])

    # Return
    results = {}
    results['scores'] = scores
    results['nn'] = args['nn']
    results['n_steps'] = args['n_steps']
    return(results)


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
        cmap=cmap + '_r'

    fig, ax = imagesc.plot(np.flipud(out['scores']),
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
    return fig, ax


# %% Scatter
def scatter(Xcoord, Ycoord, **args):
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
    fig, ax = scatterd(Xcoord, Ycoord, **args)
    return fig, ax


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
        Iloc = np.argsort(data1Dist[i, :])
        Dsort = data1Dist[i, Iloc]
        idx = np.where(Dsort != 0)[0]
        Dsort = Dsort[idx]
        Iloc = Iloc[idx]
        Iloc = Iloc[np.arange(0, np.minimum(K, len(Iloc)))]

        # Store data
        outputOrder.append(Iloc[np.arange(0, np.minimum(K, len(Iloc)))])
    return(outputOrder)


# %% Import example dataset from github.
def import_example(data='digits', url=None, sep=','):
    """Import example dataset from github source.

    Import one of the few datasets from github source or specify your own download url link.

    Parameters
    ----------
    data : str
        Name of datasets: 'digits'
    url : str
        url link to to dataset.
    verbose : int, optional
        Print progress to screen. The default is 3.
        0: None, 1: ERROR, 2: WARN, 3: INFO (default), 4: DEBUG, 5: TRACE

    Returns
    -------
    pd.DataFrame()
        Dataset containing mixed features.

    """
    if url is None:
        if data=='digits':
            url='https://erdogant.github.io/datasets/digits.zip'
        else:
            print('Not a valid name.')
            return None
    else:
        data = wget.filename_from_url(url)

    if url is None:
        print('Nothing to download.')
        return None

    curpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    filename = os.path.basename(urlparse(url).path)
    PATH_TO_DATA = os.path.join(curpath, filename)
    if not os.path.isdir(curpath):
        os.makedirs(curpath, exist_ok=True)

    # Check file exists.
    if not os.path.isfile(PATH_TO_DATA):
        print('Downloading [%s] dataset from github source..' %(data))
        wget(url, PATH_TO_DATA)

    # Import local dataset
    print('Import dataset [%s]' %(data))
    df = pd.read_csv(PATH_TO_DATA, sep=',')
    # Return
    return (df.values[:, 1:], df.values[:, 0])


# %% Download files from github source
def wget(url, writepath):
    """Download files from a URL.

    Parameters
    ----------
    url : str
        URL to download from.
    writepath : str
        Path to save the downloaded file.

    Examples
    --------
    >>> # Download a file
    >>> url = 'https://example.com/data.csv'
    >>> writepath = 'data.csv'
    >>> KNRscore.wget(url, writepath)
    """
    r = requests.get(url, stream=True)
    with open(writepath, "wb") as fd:
        for chunk in r.iter_content(chunk_size=1024):
            fd.write(chunk)

# %%
def convert_verbose_to_new(verbose):
    """Convert old verbosity to the new.

    Parameters
    ----------
    verbose : int or str
        Verbosity level to convert.

    Returns
    -------
    str
        New verbosity level.

    Examples
    --------
    >>> # Convert numeric verbosity to string
    >>> verbose = KNRscore.convert_verbose_to_new(3)
    >>> print(verbose)  # 'info'
    """
    # In case the new verbosity is used, convert to the old one.
    if verbose is None: verbose=0
    if not isinstance(verbose, str) and verbose<10:
        status_map = {
            'None': 'silent',
            0: 'silent',
            6: 'silent',
            1: 'critical',
            2: 'warning',
            3: 'info',
            4: 'debug',
            5: 'debug'}
        if verbose>=2: print('[KNRscore] WARNING use the standardized verbose status. The status [1-6] will be deprecated in future versions.')
        return status_map.get(verbose, 0)
    else:
        return verbose


def convert_verbose_to_old(verbose):
    """Convert new verbosity to the old ones.

    Parameters
    ----------
    verbose : int or str
        Verbosity level to convert.

    Returns
    -------
    int
        Old verbosity level.

    Examples
    --------
    >>> # Convert string verbosity to numeric
    >>> verbose = KNRscore.convert_verbose_to_old('info')
    >>> print(verbose)  # 3
    """
    # In case the new verbosity is used, convert to the old one.
    if verbose is None: verbose=0
    if isinstance(verbose, str) or verbose>=10:
        status_map = {
            60: 0, 'silent': 0, 'off': 0, 'no': 0, None: 0,
            40: 1, 'error': 1, 'critical': 1,
            30: 2, 'warning': 2,
            20: 3, 'info': 3,
            10: 4, 'debug': 4}
        return status_map.get(verbose, 0)
    else:
        return verbose


# %%
def get_logger():
    """Get the current logger level.

    Returns
    -------
    int
        Current logger level.

    Examples
    --------
    >>> # Get current logger level
    >>> level = KNRscore.get_logger()
    >>> print(level)  # 20 (for info level)
    """
    return logger.getEffectiveLevel()


# %%
def set_logger(verbose: [str, int] = 'info'):
    """Set the logger for verbosity messages.

    Parameters
    ----------
    verbose : [str, int], default is 'info' or 20
        Set the verbose messages using string or integer values.
        * [0, 60, None, 'silent', 'off', 'no']: No message.
        * [10, 'debug']: Messages from debug level and higher.
        * [20, 'info']: Messages from info level and higher.
        * [30, 'warning']: Messages from warning level and higher.
        * [50, 'critical']: Messages from critical level and higher.

    Examples
    --------
    >>> # Set logger to warning level
    >>> KNRscore.set_logger('warning')
    >>> 
    >>> # Set logger to debug level
    >>> KNRscore.set_logger(10)
    """
    # Convert verbose to new
    verbose = convert_verbose_to_new(verbose)
    # Set 0 and None as no messages.
    if (verbose==0) or (verbose is None):
        verbose=60
    # Convert str to levels
    if isinstance(verbose, str):
        levels = {'silent': 60,
                  'off': 60,
                  'no': 60,
                  'debug': 10,
                  'info': 20,
                  'warning': 30,
                  'error': 50,
                  'critical': 50}
        verbose = levels[verbose]

    # Show examples
    logger.setLevel(verbose)


# %%
def disable_tqdm():
    """Disable tqdm progress bars based on logger level.

    Returns
    -------
    bool
        True if tqdm should be disabled, False otherwise.

    Examples
    --------
    >>> # Check if tqdm should be disabled
    >>> disable = KNRscore.disable_tqdm()
    >>> print(disable)  # True if logger level is warning or higher
    """
    return (True if (logger.getEffectiveLevel()>=30) else False)


# %%
def check_logger(verbose: [str, int] = 'info'):
    """Check the logger by printing messages at different levels.

    Parameters
    ----------
    verbose : [str, int], default is 'info'
        Verbosity level to test.

    Examples
    --------
    >>> # Test all logger levels
    >>> KNRscore.check_logger('debug')
    DEBUG
    INFO
    WARNING
    CRITICAL
    """
    set_logger(verbose)
    logger.debug('DEBUG')
    logger.info('INFO')
    logger.warning('WARNING')
    logger.critical('CRITICAL')
