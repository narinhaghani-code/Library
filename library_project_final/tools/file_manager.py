import json
import os


def save_items(path, items):
    folder = os.path.dirname(path)
    if folder != "":
        os.makedirs(folder, exist_ok=True)
    with open(path, "w") as file:
        json.dump(items, file, indent=2)


def load_items(path):
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        raise ValueError("Data file is damaged")
