import os
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO,format="%(asctime)s %(levelname)s %(message)s")

project="cnnClassifier"

list_of_file=[
    ".github/workflows/.gitkeep",
    f"src/{project}/__init__.py",
    f"src/{project}/components/__init__.py",
    f"src/{project}/utils/__init__.py",
    f"src/{project}/config/__init__.py",
    f"src/{project}/config/configuration.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/entity/__init__.py",
    f"src/{project}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for file_path in list_of_file:
    file_path=Path(file_path)
    file_dir, file_name = os.path.split(file_path)
    
    if file_dir !="":
        os.makedirs(file_dir, exist_ok=True)
        logging.info(f"Created directory: {file_dir} and filename created: {file_name}")
        
    if (not os.path.exists(file_path))or (os.path.getsize(file_path)==0):
        with open(file_path, "w") as f:
            pass
            logging.info(f"Created file: {file_path}")
            
    else:
        logging.info(f"File {file_name} already exists.")