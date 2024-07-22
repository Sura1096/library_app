import json


class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file_content(self) -> dict:
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                books = json.load(file)
        except json.decoder.JSONDecodeError:
            books = {"data": {}}
        return books

    def add_new_content(self, data: dict) -> None:
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
