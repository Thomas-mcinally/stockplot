from setuptools import setup, find_packages

setup(
    name = 'stockplot',
    version = '1.0.0',
    packages = find_packages(),
    install_requires=[
        'matplotlib',
        'pandas',
        'yfinance',
        'mplfinance'
    ],  
    entry_points = {
        'console_scripts': [
            'stockplot = stockplot.main:main'
        ]
    })

