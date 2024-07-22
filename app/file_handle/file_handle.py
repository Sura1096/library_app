import json


class FileHandler:
    def __init__(self, file_name):
        """
        Инициализирует обрабработчик файла.

        :param file_name: Имя файла
        """
        self.file_name = file_name

    def read_file_content(self) -> dict:
        """
        Читает содержимое файла и возвращает данные в виде словаря.

        :return: Данные из файла в виде словаря
        """
        try:
            with open(self.file_name, 'r', encoding='utf-8') as file:
                books = json.load(file)
        except json.decoder.JSONDecodeError:
            books = {"data": {}}
        return books

    def add_new_content(self, data: dict) -> None:
        """
        Записывает новые данные в файл.

        :param data: Данные для записи в файл
        :return: None
        """
        with open(self.file_name, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
