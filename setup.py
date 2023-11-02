from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:

    """
    This Function will return the  the list of requirements
    """
    requirement_list=[]
    return requirement_list


setup(

    name="sensor",
    version="0.0.1",
    author="Oscar Tandi",
    author_email="oscartandi171@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(), #[],
)

