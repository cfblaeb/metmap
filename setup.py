from setuptools import setup

setup(
    name="metmap",
    version="1.0.0",
    author="Lasse Ebdrup Pedersen",
    author_email="laeb@biosustain.dtu.dk",
    description=("A tool for generating DNA MTase motif testing sequences"),
    scripts=['bin/metmap', ],
    #url = "http://packages.python.org/an_example_pypi_project",
    packages=['metmap'],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: Free for non-commercial use",
    ],
)