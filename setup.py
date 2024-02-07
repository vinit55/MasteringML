from setuptools import find_packages, setup
from typing_1 import List
def get_requirements(file_path:str)->List[str]:
    '''
    Will return requirements list
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n","") for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
name='masteringml',
version='0.0.1',
author='Vinit',
author_email='vinitvaichole55@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)