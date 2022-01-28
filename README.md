# DVC
DVC ML_Use- Case
### STEPS:STEP 01: Create a empty remote repository
```
Create a empty remote repository
```
### STEP 02: create and activate conda environment
```
conda create -prefix ./env python=3.7 -y
conda activate ./env
```
### STEP 03: create a setup file
```
touch setup.py
from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="TUCchkul",
    description="A small package for dvc ml pipeline demo",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TUCchkul/DVC.git",
    author_email="kirticse.chakma869@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
```
### STEP 04: create requirement file and install dependencies
```
touch requirements.txt
pip install -r requirements.txt
```
### STEP 05: initialize dvc
```
dvc init
```
### STEP 06: create the basic directory structure
```
mkdir -p src/utils config
```
### STEP 07: create the config file
```
touch config/config.yml

data_source: http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

artifacts: 
  artifacts_dir: artifacts
  raw_local_dir: raw_local_dir
  raw_local_file: data.csv

```
### step 08: create the stage 01 python file and all utils file:
```bash
touch src/stage_01_load_save.py src/utils/all_utils.py
```
### step 09: create the dvc.yaml file and add the stage 01:
```bash
touch.dvc.yaml
```
content of dvc.yaml file -
```yaml
stages:
  load_data:
    cmd: python src/stage_01_load_save.py --config=config/config.yaml
    deps:
      - src/stage_01_load_save.py
      - src/utils/all_utils.py
      - config/config.yaml
    outs:
      - artifacts/raw_local_dir/data.csv
```
### Step 10: Run the dvc repro command with
```bash
dvc repro 
```
### step 11: push the changes to remote repository
```bash
git init
git add .
git commit -m "stage_01_added"
git brancg -M main
git remote add origin https://github.com/TUCchkul/DVC.git
git push origin main 
```
```bash
touch .gitignore
```


