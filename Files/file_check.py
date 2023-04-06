import os

def create_file_if_not_exists(path):
    if not os.path.exists(path):
        # Create directory structure if it doesn't exist
        os.makedirs(os.path.dirname(path), exist_ok=True)
        # Create empty file
        open(path, 'a').close()



from pathlib import Path

def create_file_if_not_exists(path):
    file_path = Path(path)
    if not file_path.exists():
        # Create directory structure if it doesn't exist
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # Create empty file
        file_path.touch()
