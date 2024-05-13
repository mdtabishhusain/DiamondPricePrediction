from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:     #this line means we are creating a function named get_requirements in which a file path is given in form of string and it will return a list in form of string.
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()           #This will read each line in the file whose path is provided but when we go to next line \n is appended. This will disturb our function and will interrupt in installing the packages so we will replace \n with blank space using list comprehension
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

        return requirements


setup(
    name='DiamondPricePrediction',
    version='0.0.1',
    author='Tabish',
    author_email='mdtabishhusain@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()

)