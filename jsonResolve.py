import os
import json


def load_json(path, default_data):
    if not os.path.exists(path):
        # create file with default data
        with open(path, "w", encoding="utf-8") as f:
            json.dump(default_data, f, indent=4)
        return default_data

    # load existing file
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
def write_json(path, data):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        