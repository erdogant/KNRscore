'''Make a scatter plot based on X,Y coordinates.

 Requirements
 ------------
   numpy
   matplotlib
   colormap
 

 Name        : scatter.py
 Author      : E.Taskesen
 Contact     : erdogant@gmail.com
 Date        : Jan. 2020
 Licence     : MIT

'''

#%% Libraries
import flameplot.colormap as colormap
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#%% Main
def scatter(X, y=None, norm=True, cmap='Set1', xlabel=None, ylabel=None, title=None, figsize=(15,10)):
    '''
    

    Parameters
    ----------
    X : numpy array
        2D Coordinates.
    y : list of labels with same size as X
        label of the samples.
    cmap : String, optional
        Colormap > https://matplotlib.org/examples/color/colormaps_reference.html
        'Set1'       (default)     
        'Set2'       
        'rainbow'
        'bwr'        Blue-white-red
        'binary' or 'binary_r'
        'seismic'    Blue-white-red 
        'Blues'      white-to-blue
        'Reds'       white-to-red
        'Pastel1'    Discrete colors
        'Paired'     Discrete colors
        'Set1'       Discrete colors    xlabel : TYPE, optional
        DESCRIPTION. The default is None.
    xlabel : String, optional
        Xlabel. The default is None.
    ylabel : String, optional
        Ylabel. The default is None.
    title : String, optional
        Title of the figure. The default is None.
    norm : Bool, optional
        Normalize datapoints. The default is True.
    figsize : tuple, optional
        Figure size. The default is (15,10).

    Returns
    -------
    Fig, ax


    '''
    assert X.shape[0]==len(y), print('[SCATTER] Error. X should have same length as y.')
    args=dict()
    args['norm']=norm
    args['cmap']=cmap
    args['xlabel']=xlabel
    args['ylabel']=ylabel
    args['title']=title
    args['figsize']=figsize
    
    axiscolor='#dddddd'

    # Take only the first two dimensions
    X=X[:,0:2]

    # Normalize data
    if args['norm']:
        x_min, x_max = np.min(X, 0), np.max(X, 0)
        X = (X - x_min) / (x_max - x_min)
    
    # Create unqiue colors for y
    if y is not None:
        getcolors,colordict=colormap.fromlist(y, cmap=args['cmap'], method='matplotlib')

    # Boot figure
    fig, ax = plt.subplots(figsize=args['figsize'])
    # Scatter
    ax.scatter(X[:,0],X[:,1], facecolor=getcolors, s=15, edgecolor='None')

    # Plot labels
    if y is not None:
        for uiy in colordict.keys():
            XYmean=np.mean(X[y==uiy,:], axis=0)
            plt.text(XYmean[0],XYmean[1], str(uiy), color=colordict.get(uiy), fontdict={'weight': 'bold', 'size': 16})

    # Labels on axis
    ax.set_xlabel(args['xlabel'])
    ax.set_ylabel(args['ylabel'])
    if args['title'] is not None:
        ax.set_title(args['title'])
        
    # set background to none
    ax.set_facecolor('none')
    # Set grid and axis to grey
    ax.grid(True, color=axiscolor)
    for child in ax.get_children():
        if isinstance(child, matplotlib.spines.Spine):
            child.set_color(axiscolor)

    # Show figure
    fig.show()
    fig.canvas.draw()
    # Return
    return(fig,ax)


