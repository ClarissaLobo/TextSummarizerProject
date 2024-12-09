import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name="textSummarizer"

list_of_files=[
    ".github/workflows/.gitkeep",  #CI/CD FOR DEPLOYMENT(yaml FILE WILL BE WRITTEN HERE)WHENERVER WE DO COMMIT IT WILL TAKE MY CODE FROM GITHUB AND DEPLOY TO CLOUD
    f"src/{project_name}/__init__.py",#constructr file to import from folders as local pacakage so construdtor is important
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",#build an image of source code and then deploy it to AWS
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath) #this will take the PATH library and make it appropriate according to OS and give path
    filedir, filename= os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0): #checking file size if its 0 then create file
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} is already exists")