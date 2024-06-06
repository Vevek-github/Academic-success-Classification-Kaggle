from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n", "") for i in requirements]
    hypen_e_dot = "-e ."
    if hypen_e_dot in requirements:
        requirements.remove(hypen_e_dot)
    return requirements

setup(
    name="Kaggle_acad_vevek_HERE",
    version="0.0.1",
    author="Vevek",
    author_email="vevekkottapally123@gmail.com",
    description="Kaggle competition to predict the academic success rate",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Vevek-github/Academic-success-Classification-Kaggle",
    project_urls={
        'Homepage': "https://github.com/Vevek-github/Academic-success-Classification-Kaggle",
        'Issues': "https://github.com/Vevek-github/Academic-success-Classification-Kaggle/issues",
    },
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)
