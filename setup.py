from setuptools import find_packages,setup
from typing import List

def getlib(filepath)->List[str]:
    libs=[]
    with open(filepath) as fileobj:
        libs=fileobj.readlines()
        libs=[req.replace('/n','') for req in libs]
    if '-e.' in libs:
        libs.remove('-e.')
    return libs



setup(
name="Kaggle Problem 1",
author="Sai Jagadeesh Yadavalli",
packages=find_packages(),
requires=getlib('requirements.txt')
)