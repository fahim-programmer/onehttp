from setuptools import setup

# Build a Wheel Using this python setup.py bdist_wheel

LONG_DESCRIPTION = 'A simple module that extends functionality of core modules and makes it easier to work with non-dynamic html based websites with cookies and other features'

setup(
    name='onehttp',
    version='1.0.0',
    packages=['oneHTTP'],
    url='https://github.com/fahim-programmer/onehttp',
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    author='Fahim Chohan',
    platforms=['Windows', 'MacOS', 'Linux'],
    description='Simple HTTP request management / browsing',
    install_requires=[
        "beautifulsoup4==4.12.2",
        "bs4==0.0.1",
        "certifi==2023.7.22",
        "charset-normalizer==3.0.0",
        "idna==3.4",
        "pdfkit==1.0.0",
        "requests==2.31.0",
        "soupsieve==2.4.1",
        "urllib3==1.26.0"
    ],
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)