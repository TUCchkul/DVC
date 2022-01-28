# DVC
DVC ML-DL-CV-NLP-Use- Case
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