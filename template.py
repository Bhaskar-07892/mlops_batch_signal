import os
from pathlib import Path

project_files = [
    "data/data.csv",

    "src/__init__.py",
    "src/data_loader.py",
    "src/analyzer.py",
    "src/logger.py",
    "src/exception.py",
    "src/config.py",

    "run.py",
    "config.yaml",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "README.md",
    "metrics.json",
    "run.log"
] 

for file_path in project_files:
    
    file = Path(file_path)

    file.parent.mkdir(parents=True, exist_ok=True)

    file.touch(exist_ok = True)

print("Project structure completed ! .")

