from setuptools import setup, find_packages

setup(
    name="stockplot",
    packages=find_packages(exclude=["tests"]),
    email="thomasmcinally@hotmail.com",
    author="Thomas McInally",
    url="https://github.com/Thomas-mcinally/stockplot",
    long_description_content_type="text/markdown",
    install_requires=["yfinance", "mplfinance"],
    version="1.0.5",
    entry_points={"console_scripts": ["stockplot = stockplot.main:main"]},
)
