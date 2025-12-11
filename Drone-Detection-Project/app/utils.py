from pathlib import Path

def list_images(folder_path):
    folder = Path(folder_path)
    if not folder.exists():
        return []
    return [f for f in folder.iterdir() if f.suffix.lower() in [".jpg", ".png"]]

def create_folder(folder_path):
    Path(folder_path).mkdir(parents=True, exist_ok=True)
