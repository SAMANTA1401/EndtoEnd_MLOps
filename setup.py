from setuptools import find_packages, setup    ## find automatically  all packages avilable for entire machne learning
## application in the directory we have actually created and setup
from typing import List

HYPEN_E_DOT='-e .' #present in requirement.txt not erequired  getting error
def get_requirements(file_path:str)->List[str]: #it return a list of path ,library .Path objects, not strings
    '''this function will return the list of requirements''' #docstring
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        #remove \n from each line with blank using list comprehension
        requirements=[req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements: #if "-e ." is present then remove  it should not come
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(  ## meta data about the entire project
    name='EndtoEnd_MLOps',
    version='0.0.1',
    author="Shubhankar",
    author_email='psamanta1401@gmail.com',
    packages=find_packages(), ## module that is actully imported
    # install_requires=['pandas','numpy','seaborn']  
    ## as we need large no of library we create a function get_requirement() it should be able to read all this file 
    # for install_requires it try to install all packages one by one from requirement.txt
    install_requires=get_requirements('requirements.txt')


)