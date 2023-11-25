import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()
    

__version__ = '0.0.0'

REPO_NAME = 'kidney-Disease-Classification-Mlflow-DVC'
AUTHOR_USER_NAME = 'Mahesh Kumar'
SRC_REPO = 'Kidney_Disease_CNN_classifier'
AUTHOR_EMAIL = 'maheshkumar201095@gmail.com'


setuptools.setup(
    
    name = SRC_REPO,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email = AUTHOR_EMAIL_USER,
    description = "A small python package for CNN app",
    long_description = long_description,
    url = f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_url = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
        
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where="src")
)