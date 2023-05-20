from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.2'
DESCRIPTION = 'An easy to use web scrapping library via JS scripts'
LONG_DESCRIPTION = 'A package that allows to scrapp data from Web pages by running JS scripts from python.'

# Setting up
setup(
    name="ScrapPyJS",
    version=VERSION,
    author="Hind Sagar Biswas",
    author_email="<hindsbhk@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['selenium'],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2"],
    },
    keywords=['python', 'web scrapping', 'scrap'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)