import os
from setuptools import setup, find_packages


PACKAGENAME = "gmt2sed"
__version__ = None
pth = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), "gmt2sed", "_version.py"
)
with open(pth, "r") as fp:
    exec(fp.read())


setup(
    name=PACKAGENAME,
    version=__version__,
    author="Eve Kovacs",
    author_email="kovacs@anl.gov",
    description="Galaxy merger trees to SEDs",
    long_description="Compute galaxy SEDs from HACC hydro galaxy merger trees",
    install_requires=["numpy"],
    packages=find_packages(),
    url="https://github.com/evevkovacs/gmt2sed",
    package_data={"gmt2sed": ("tests/testing_data/*.dat",)},
)
