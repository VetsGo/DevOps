import json
from data_saver import DataSaver

class JsonSaver(DataSaver):
    def save(self, data: dict, filename: str):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)