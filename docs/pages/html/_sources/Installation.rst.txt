Installation
============

System Requirements
-------------------

KNRscore requires:
- Python 3.7 or higher
- pip (Python package installer)
- Basic scientific computing packages (numpy, scipy)
- Visualization packages (matplotlib)

Installation Methods
--------------------

PyPI Installation
~~~~~~~~~~~~~~~~~~

The recommended way to install KNRscore is through PyPI:

.. code-block:: console

    # Install the latest stable version
    pip install KNRscore

    # Force update to the latest version
    pip install -U KNRscore

    # Install with specific version
    pip install KNRscore==1.0.0

GitHub Installation
~~~~~~~~~~~~~~~~~~~

To install the latest development version directly from GitHub:

.. code-block:: console

    # Install from GitHub
    pip install git+https://github.com/erdogant/KNRscore

    # Install specific branch
    pip install git+https://github.com/erdogant/KNRscore@develop

Development Installation
~~~~~~~~~~~~~~~~~~~~~~~~

For developers who want to modify the source code:

.. code-block:: console

    # Clone the repository
    git clone https://github.com/erdogant/KNRscore.git
    cd KNRscore

    # Install in development mode
    pip install -e .

    # Install development dependencies
    pip install -r requirements-dev.txt

Verification
------------

After installation, verify that KNRscore is properly installed:

.. code-block:: python

    import KNRscore as knrs
    print(knrs.__version__)

Dependencies
------------

KNRscore depends on the following packages:
- numpy >= 1.20.0
- scipy >= 1.7.0
- matplotlib >= 3.4.0
- tqdm >= 4.60.0
- imagesc >= 0.1.0
- scatterd >= 0.1.0

These dependencies are automatically installed when installing KNRscore.

Uninstallation
--------------

To remove KNRscore from your system:

.. code-block:: console

    # Uninstall the package
    pip uninstall KNRscore

    # Remove all dependencies (optional)
    pip uninstall numpy scipy matplotlib tqdm imagesc scatterd

Troubleshooting
---------------

Common installation issues and solutions:

1. **Permission Errors**
   - Use ``pip install --user KNRscore`` for user-level installation
   - Or use ``sudo pip install KNRscore`` (not recommended)

2. **Version Conflicts**
   - Create a virtual environment: ``python -m venv knr_env``
   - Activate it: ``source knr_env/bin/activate`` (Linux/Mac) or ``knr_env\Scripts\activate`` (Windows)
   - Install KNRscore in the virtual environment

3. **Missing Dependencies**
   - Install system-level dependencies first
   - Use ``pip install -r requirements.txt``

4. **Development Issues**
   - Ensure you have the latest pip: ``pip install --upgrade pip``
   - Install build tools: ``pip install wheel setuptools``

.. include:: add_bottom.add