from distutils.core import setup

PACKAGE = "pyhocon-fix"
NAME = "pyhocon-fix"
DESCRIPTION = "This package can download funds data from http://huobijijin.com and then analyze the data for giving valuable funds."
AUTHOR = "Lin Deng"
AUTHOR_EMAIL = "ptreesptrees@gmail.com"
URL = "https://github.com/FinixLei/FundsData"
VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    # long_description=read("README.md"),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    license="Apache License, Version 2.0",
    url=URL,
    packages=["FundsData"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    zip_safe=False,
)