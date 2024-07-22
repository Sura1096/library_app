from .lib_methods import Library


class UserOperation:
    @staticmethod
    def insert_new_book(lib: Library) -> str:
        print("Введите следующие данные для добавления книги:")
        title = input("1. Название книги: ")
        author = input("2. Автор книги: ")
        year = input("3. Год издания книги: ")
        try:
            title = title.split(':')[-1].capitalize()
            author = author.split(':')[-1].title()
            year = int(year.split(':')[-1])
        except ValueError:
            return "Некорректные данные."

        data = {"title": title, "author": author, "year": year}
        return lib.add_book(data)

    @staticmethod
    def remove_book(lib: Library) -> str:
        book_id = input("Введите id книги, которую нужно удалить: ").split(":")[-1]
        try:
            book_id = int(book_id)
        except ValueError:
            return "Некорректный id книги."
        if book_id:
            return lib.delete_book(book_id)
        else:
            return "Некорректный id книги."

    @staticmethod
    def find_book(lib: Library) -> list | str:
        book_item = input("Введите название/автора/год издания книги, которую нужно найти: ").split(":")[-1]
        if book_item:
            if book_item.isdigit():
                book_item = int(book_item)
                return lib.search_by_year(book_item)
            else:
                return lib.search_by_title_author(book_item)
        else:
            return "Некорректные данные."

    @staticmethod
    def all_books(lib: Library) -> list | str:
        return lib.display_all_books()

    @staticmethod
    def update_status(lib: Library) -> str:
        book_id = input("Введите id книги, у которой хотите поменять статус: ").split(":")[-1]
        try:
            book_id = int(book_id)
        except ValueError:
            return "Некорректный id книги."
        status = input("Введите новый статус (в наличии/выдана): ").split(":")[-1].lower()
        if book_id and status:
            if status not in ("в наличии", "выдана"):
                return "Некорректный статус. Необходимо ввести либо 'в наличии' либо 'выдана'."
            else:
                return lib.change_status(book_id, status)
        else:
            return "Некорректные данные."
