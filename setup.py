from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="metmap",
    version="1.0.4",
    author="Lasse Ebdrup Pedersen",
    author_email="laeb@biosustain.dtu.dk",
    description="A tool for generating DNA MTase motif testing sequences",
    long_description=long_description,
    long_description_content_type="text/markdown",
    scripts=['bin/run_metmap.py', ],
    url="https://github.com/cfblaeb/metmap",
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