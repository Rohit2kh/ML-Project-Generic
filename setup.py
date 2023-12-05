from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file:str) -> List[str]:
    '''
    this function will return requiremnets (libraries used)
    '''
    requirements = []
    with open(file) as file_object:
        requirements = file_object.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name = "ML_project",
    version = '0.0.1',
    author = "Rohit Khandal",
    author_email="rohitkhandal1811@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)
