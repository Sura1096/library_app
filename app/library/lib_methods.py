from ..file_handle.file_handle import FileHandler


class Library:
    def __init__(self, file_name):
        """
        :param file_name: Имя файла для чтения и записи данных
        """
        self.file_name = file_name
        self.file = FileHandler(self.file_name)
        self.file_content = self.file.read_file_content()
        self.current_id = 0

    def update_file_content(self) -> None:
        """
        Обновляет содержимое файла в памяти.

        :return: None
        """
        self.file_content = self.file.read_file_content()

    def add_book(self, data: dict) -> str:
        """
        Добавляет новую книгу в библиотеку.

        :param data: Данные о книге
        :return: Строка потдверждения добавления книги
        """
        self.current_id += 1
        book_id = self.current_id
        data["id"] = book_id
        data["status"] = "В наличии"

        self.file_content["data"].update({book_id: data})
        self.file.add_new_content(data=self.file_content)
        self.update_file_content()
        return "Книга добавлена."

    def delete_book(self, book_id: int) -> str:
        """
        Удаляет книгу из библиотеки по ее id.

        :param book_id: id книги
        :return: Строка потдверждения удаления книги или ошибка
        """
        try:
            del self.file_content["data"][str(book_id)]
            self.file.add_new_content(data=self.file_content)
            self.update_file_content()
            return "Книга удалена."
        except KeyError:
            return "Книга не найдена."

    def search_by_title_author(self, item: str) -> list | str:
        """
        Ищет книги по названию или автору.

        :param item: Название или автор книги
        :return: Список найденных книг или сообщение об отсутствии книг
        """
        books = []
        for book in self.file_content["data"].values():
            if item.capitalize() == book["title"] or item.title() == book["author"] or item == book["year"]:
                books.append(book)
        if books:
            return books
        else:
            return "Нет книг с таким названием/автором."

    def search_by_year(self, year: int) -> list | str:
        """
        Ищет книги по году издания.

        :param year: Год издания книги
        :return: Список найденных книг или сообщение об отсутствии книг
        """
        books = []
        for book in self.file_content["data"].values():
            if year == book["year"]:
                books.append(book)
        if books:
            return books
        else:
            return "Нет книг с таким годом издания."

    def display_all_books(self) -> list | str:
        """
        Отображает все книги в библиотеке.

        :return: Список всех книг или сообщение об отсутствии книг
        """
        all_books = []
        for book in self.file_content["data"].values():
            all_books.append(book)
        if all_books:
            return all_books
        else:
            return "Пока нет ни одной книги."

    def change_status(self, book_id: int, status: str) -> str:
        """
        Изменяет статус книги по ее id.

        :param book_id: id книги
        :param status: Новый статус книги
        :return: Строка подтверждения изменения статуса или ошибка
        """
        try:
            self.file_content["data"][str(book_id)]["status"] = status
            self.file.add_new_content(data=self.file_content)
            self.update_file_content()
            return "Статус изменен."
        except KeyError:
            return "Книга не найдена."
