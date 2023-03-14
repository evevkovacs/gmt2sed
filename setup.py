# setup.py
import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="gmt2sed",
    version="0.1",
    author="Eve Kovacs",
    author_email="kovacs@anl.gov",
    long_description=long_description,
    long_description_content_type="text/markdown",
    description="A Python package to predict SEDs from HACC galaxy merger trees",
    packages=["gmt2sed","gmt2sed/gmt2sed"]
    classifiers=[
        "License :: OSI Approved :: BSD 3-clause License",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Astronomy"]
)
