import os

# Folders to create
folders = [
    "ml_project/data",
    "ml_project/src",
    "ml_project/config",
    "ml_project/notebooks"
]

# Files to create
files = [
    "ml_project/data/raw_data.csv",
    "ml_project/src/__init__.py",
    "ml_project/src/data_loader.py",
    "ml_project/src/preprocessing.py",
    "ml_project/src/model.py",
    "ml_project/src/train.py",
    "ml_project/src/evaluate.py",
    "ml_project/src/predict.py",
    "ml_project/config/config.yaml",
    "ml_project/notebooks/eda.ipynb",
    "ml_project/main.py",
    "ml_project/requirements.txt",
    "ml_project/setup.py",
    "ml_project/README.md",
    "ml_project/.gitignore"
]

def create_structure():
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

    for file in files:
        with open(file, "w") as f:
            f.write("")  # Empty file
        print(f"Created file: {file}")

if __name__ == "__main__":
    print("Creating ML project structure...")
    create_structure()
    print("\nDone!")
