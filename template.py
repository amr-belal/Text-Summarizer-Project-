# template file for the Text-Summarizer-Project for project structure

import os 
import logging
from pathlib import Path

# creating the logger
logging.basicConfig(level=logging.INFO , format = "[%(asctime)s]: %(message)s")



project_name = "text-summarizer"


list_files = [
    "./github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "test.py"
]

for filepath in list_files:
    filepath = Path(filepath)
    filedir , filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir , exist_ok=True)
        logging.info(f"craeting dir {filedir} for file {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
         with open(filepath , "w") as f :
             pass 
             logging.info(f"creating empty file {filepath}")
             
    else:
        logging.info(f"{filename} already exists")
        
    