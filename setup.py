from setuptools import setup, find_packages

setup(
    dependency_links=[],
    name="stockplot",
    packages=find_packages(exclude=["tests"]),
    author="Thomas McInally",
    url="https://github.com/Thomas-mcinally/stockplot",
    long_description_content_type="text/markdown",
    python_requires=">=3.8",
    install_requires=[
        "appdirs==1.4.4",
        "beautifulsoup4==4.11.2; python_full_version >= '3.6.0'",
        "certifi==2022.12.7; python_version >= '3.6'",
        "cffi==1.15.1",
        "charset-normalizer==3.1.0; python_full_version >= '3.7.0'",
        "contourpy==1.0.7; python_version >= '3.8'",
        "cryptography==39.0.2; python_version >= '3.6'",
        "cycler==0.11.0; python_version >= '3.6'",
        "fonttools==4.39.0; python_version >= '3.8'",
        "frozendict==2.3.5; python_version >= '3.6'",
        "html5lib==1.1; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "idna==3.4; python_version >= '3.5'",
        "importlib-resources==5.12.0; python_version < '3.10'",
        "kiwisolver==1.4.4; python_version >= '3.7'",
        "lxml==4.9.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4'",
        "matplotlib==3.7.1; python_version >= '3.8'",
        "mplfinance==0.12.9b7",
        "multitasking==0.0.11",
        "numpy==1.24.2; python_version >= '3.8'",
        "packaging==23.0; python_version >= '3.7'",
        "pandas==1.5.3; python_version >= '3.8'",
        "pillow==9.4.0; python_version >= '3.7'",
        "pycparser==2.21",
        "pyparsing==3.0.9; python_full_version >= '3.6.8'",
        "python-dateutil==2.8.2; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "pytz==2022.7.1",
        "requests==2.28.2; python_version >= '3.7' and python_version < '4'",
        "six==1.16.0; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3'",
        "soupsieve==2.4; python_version >= '3.7'",
        "urllib3==1.26.14; python_version >= '2.7' and python_version not in '3.0, 3.1, 3.2, 3.3, 3.4, 3.5'",
        "webencodings==0.5.1",
        "yfinance==0.2.12",
        "zipp==3.15.0; python_version < '3.10'",
    ],
    version="1.0.14",
    entry_points={"console_scripts": ["stockplot = stockplot.main:main"]},
)
