from ..file_handle.file_handle import FileHandler


class Library:
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = FileHandler(self.file_name)
        self.file_content = self.file.read_file_content()
        self.current_id = 0

    def update_file_content(self) -> None:
        self.file_content = self.file.read_file_content()

    def add_book(self, data: dict) -> str:
        self.current_id += 1
        book_id = self.current_id
        data["id"] = book_id
        data["status"] = "В наличии"

        self.file_content["data"].update({book_id: data})
        self.file.add_new_content(data=self.file_content)
        self.update_file_content()
        return "Книга добавлена."

    def delete_book(self, book_id: int) -> str:
        try:
            del self.file_content["data"][str(book_id)]
            self.file.add_new_content(data=self.file_content)
            self.update_file_content()
            return "Книга удалена."
        except KeyError:
            return "Книга не найдена."

    def search_by_title_author(self, item: str) -> list | str:
        books = []
        for book in self.file_content["data"].values():
            if item.capitalize() == book["title"] or item.title() == book["author"] or item == book["year"]:
                books.append(book)
        if books:
            return books
        else:
            return "Нет книг с таким названием/автором."

    def search_by_year(self, year: int) -> list | str:
        books = []
        for book in self.file_content["data"].values():
            if year == book["year"]:
                books.append(book)
        if books:
            return books
        else:
            return "Нет книг с таким годом издания."

    def display_all_books(self) -> list | str:
        all_books = []
        for book in self.file_content["data"].values():
            all_books.append(book)
        if all_books:
            return all_books
        else:
            return "Пока нет ни одной книги."

    def change_status(self, book_id: int, status: str) -> str:
        try:
            self.file_content["data"][str(book_id)]["status"] = status
            self.file.add_new_content(data=self.file_content)
            self.update_file_content()
            return "Статус изменен."
        except KeyError:
            return "Книга не найдена."
