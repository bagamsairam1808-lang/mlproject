from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(filename: str) -> List[str]:
    requirements = []
    with open(filename, "r") as f:
        requirements = f.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements 

setup(
    name="mlproject",
    version="0.0.1",
    author="Sairam",
    author_email="bagamsairam1808@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)