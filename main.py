from app.library.lib_methods import Library
from app.library.lib_user_operations import UserOperation


lib = Library("db.json")
user = UserOperation()


def main():
    print("Добро пожаловать в систему управления библиотекой!\n"
          "Выберете (напишите номер пункта), что бы вы хотели сделать:\n"
          "1. Добавить книгу;\n"
          "2. Удалить книгу;\n"
          "3. Найти книгу;\n"
          "4. Показать все книги;\n"
          "5. Изменить статус книги.")
    user_input = input("Введите номер пункта: ")
    try:
        user_input = int(user_input)
    except ValueError as er:
        print("Необходимо ввести номер пункта.")
    if user_input == 1:
        print(user.insert_new_book(lib))
    elif user_input == 2:
        print(user.remove_book(lib))
    elif user_input == 3:
        print(user.find_book(lib))
    elif user_input == 4:
        print(user.all_books(lib))
    elif user_input == 5:
        print(user.update_status(lib))


if __name__ == '__main__':
    continue_user_choice = "да"
    while continue_user_choice == "да":
        main()
        continue_user_choice = input("Хотите продолжить? [да/нет]: ").split(":")[-1].lower()
        if continue_user_choice == "нет":
            print("До свидания!")
            break
        elif continue_user_choice not in ("да", "нет"):
            continue_user_choice = input("Пожалуйста, введите 'да' или 'нет': ").split(":")[-1].lower()
