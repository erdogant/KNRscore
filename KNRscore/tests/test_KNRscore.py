import pytest
import numpy as np
import KNRscore as knrs
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.datasets import make_blobs

# Generate synthetic data for testing
def sample_data():
	"""Generate sample data for testing.
	
	Example:
		>>> X, y, pca, tsne = sample_data()
		>>> print(X.shape)  # (100, 10)
		>>> print(pca.shape)  # (100, 2)
	"""
	X, y = make_blobs(n_samples=100, n_features=10, centers=3, random_state=42)
	pca = PCA(n_components=2).fit_transform(X)
	tsne = TSNE(n_components=2, random_state=42).fit_transform(X)
	return X, y, pca, tsne

def test_compare():
	"""Test the compare function with different embeddings.
	
	Example:
		>>> from sklearn.decomposition import PCA
		>>> from sklearn.manifold import TSNE
		>>> X, y = knrs.import_example(data='digits')
		>>> pca = PCA(n_components=2).fit_transform(X)
		>>> tsne = TSNE(n_components=2).fit_transform(X)
		>>> scores = knrs.compare(pca, tsne, nn=50, n_steps=5)
		>>> print(scores['scores'].shape)  # (10, 10)
	"""
	_, _, pca, tsne = sample_data()
	
	# Test with PCA and t-SNE embeddings
	scores = knrs.compare(pca, tsne, nn=50, n_steps=5)
	
	# Check if output is a dictionary
	assert isinstance(scores, dict)
	
	# Check if required keys are present
	assert 'scores' in scores
	assert 'nn' in scores
	assert 'n_steps' in scores
	
	# Check if scores array has correct shape
	assert scores['scores'].shape[0] == len(scores['nn'])
	assert scores['scores'].shape[1] == len(scores['nn'])
	
	# Check if scores are between 0 and 1
	assert np.all(scores['scores'] >= 0)
	assert np.all(scores['scores'] <= 1)

def test_plot():
	"""Test the plot function.
	
	Example:
		>>> X, y = knrs.import_example(data='digits')
		>>> pca = PCA(n_components=2).fit_transform(X)
		>>> tsne = TSNE(n_components=2).fit_transform(X)
		>>> scores = knrs.compare(pca, tsne)
		>>> fig, ax = knrs.plot(scores, cmap='viridis', xlabel='PCA', ylabel='tSNE')
		>>> fig.savefig('comparison_plot.png')
	"""
	_, _, pca, tsne = sample_data()
	
	# First get comparison scores
	scores = knrs.compare(pca, tsne, nn=50, n_steps=5)
	
	# Test plotting with different parameters
	fig, ax = knrs.plot(scores, cmap='viridis', xlabel='PCA', ylabel='tSNE')
	
	# Check if figure and axes are created
	assert fig is not None
	assert ax is not None
	
	# Test with reversed colormap
	fig, ax = knrs.plot(scores, cmap='viridis', reverse_cmap=True)
	assert fig is not None
	assert ax is not None

def test_scatter():
	"""Test the scatter function.
	
	Example:
		>>> X, y = knrs.import_example(data='digits')
		>>> pca = PCA(n_components=2).fit_transform(X)
		>>> fig, ax = knrs.scatter(pca[:, 0], pca[:, 1], 
		...                       labels=y, 
		...                       cmap='Set1',
		...                       title='PCA Scatter Plot')
		>>> fig.savefig('scatter_plot.png')
	"""
	_, y, pca, _ = sample_data()
	
	# Test with different parameters
	fig, ax = knrs.scatter(pca[:, 0], pca[:, 1], 
						  labels=y, 
						  cmap='Set1',
						  title='PCA Scatter Plot')
	
	# Check if figure and axes are created
	assert fig is not None
	assert ax is not None

def test_import_example():
	"""Test the import_example function.
	
	Example:
		>>> # Load the digits dataset
		>>> X, y = knrs.import_example(data='digits')
		>>> print(X.shape)  # (1797, 64)
		>>> print(y.shape)  # (1797,)
		>>> 
		>>> # Load custom dataset from URL
		>>> url = 'https://example.com/data.csv'
		>>> X, y = knrs.import_example(url=url)
	"""
	# Test with digits dataset
	X, y = knrs.import_example(data='digits')
	
	# Check if data is loaded correctly
	assert isinstance(X, np.ndarray)
	assert isinstance(y, np.ndarray)
	assert X.shape[0] == y.shape[0]

def test_edge_cases():
	"""Test edge cases and error handling.
	
	Example:
		>>> # Test with empty arrays
		>>> with pytest.raises(Exception):
		...     knrs.compare(np.array([]), np.array([]))
		>>> 
		>>> # Test with different sized arrays
		>>> X, y = knrs.import_example(data='digits')
		>>> pca = PCA(n_components=2).fit_transform(X)
		>>> tsne = TSNE(n_components=2).fit_transform(X)
		>>> with pytest.raises(Exception):
		...     knrs.compare(pca, tsne[:50])  # Different number of samples
	"""
	_, _, pca, tsne = sample_data()
	
	# Test with empty arrays
	with pytest.raises(Exception):
		knrs.compare(np.array([]), np.array([]))
	
	# Test with different sized arrays
	with pytest.raises(Exception):
		knrs.compare(pca, tsne[:50])
