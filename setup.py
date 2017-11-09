from setuptools import setup

setup(
    name="metmap",
    version="1.0.1",
    author="Lasse Ebdrup Pedersen",
    author_email="laeb@biosustain.dtu.dk",
    description="A tool for generating DNA MTase motif testing sequences",
    scripts=['bin/run_metmap.py', ],
    url="https://github.com/biosustain/metmap",
    packages=['metmap'],
    install_requires=['biopython'],
    python_requires='>=3.6',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "License :: Free for non-commercial use",
    ],
)