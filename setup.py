from setuptools import setup, find_packages

setup(
    name = 'stockplot',
    packages = find_packages(),
    email='thomasmcinally@hotmail.com',
    author='Thomas Mcinally',
    install_requires=[
        'matplotlib',
        'pandas',
        'yfinance',
        'mplfinance'
    ],  
    version = '1.0.0',
    entry_points = {
        'console_scripts': [
            'stockplot = stockplot.main:main'
        ]
    })
