new_list = []


def open_1():
    with open("phon.txt", 'r', encoding="utf-8") as f:
        x = f.read().strip().split("\n")
        return x


def all_in_dict():
    global new_list
    for i in open_1():
        z = i.split(",")
        new_dict = {
            "name": z[1],
            "second_name": z[0],
            "phone": z[2],
            "discription": z[3]
        }
        new_list.append(new_dict)
    return new_list


def all_users():
    for i in all_in_dict():
        users = i
        print(f'\nИмя:', users['name'], '\nФамилия:', users['second_name'], '\nТелефон:', users['phone'], '\nОписание:',
              users['discription'])


def find_user_by_lastname():
    x = input("Введите Фамилию: ")
    for i in all_in_dict():
        if i['second_name'] == x:
            print(
                f"\nИмя: {i['name']}, \nФамилия: {i['second_name']}, \nТелефон: {i['phone']}, \nОписание: {i['discription']}")
            break
    else:
        print("Такого пользователя не существует")


def find_user_by_phone_number():
    phone = input("Введите номер телефона: ")
    for i in all_in_dict():
        if i['phone'] == phone:
            print(
                f"\nИмя: {i['name']}, \nФамилия: {i['second_name']}, \nТелефон: {i['phone']}, \nОписание: {i['discription']}")
            break
    else:
        print("Нет пользователей с таким номером")


def add_new_phone():
    second_name = input("Введите Фамилию: ")
    name = input("Введите Имя: ")
    phone = input("Введите Номер телефона: ")
    discription = input("Описание контакта: ")
    new_dict = {"second_name": second_name,
                "name": name,
                "phone": phone,
                "discription": discription}
    new_list.append(new_dict)
    new_contact = ",".join([new_dict["second_name"], new_dict["name"], new_dict["phone"], new_dict["discription"]])
    return new_contact


def add_to_file():
    with open("phon.txt", "a", encoding="utf-8") as file:
        file.write('\n' + add_new_phone())
    return f"Запись прошла успешно"


def show_menu():
    print("\nВыберите действие: \n"
          "1. Отобразить справочник\n"
          "2. Найти по Фамилии\n"
          "3. Найти по номеру\n"
          "4. Добавить абонента\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу\n"
          "7. Добавить записи из соседнего файла")

    choice = input("")
    return choice


def add_new_file():
    x = input("Введите имя фала для добавления в справочник: ")
    x = x + ".txt"
    with open(x, "r", encoding="utf-8") as file:
        file = file.read()
        with open("phon.txt", "a", encoding="utf-8") as f:
            f.write('\n' + file)
    print("Добавили записи из файла!")


def take_choice():
    while True:
        match show_menu():
            case "1":
                all_users()
            case "2":
                find_user_by_lastname()
            case "3":
                find_user_by_phone_number()
            case "4":
                add_new_phone()
            case "5":
                add_to_file()
            case "6":
                print("Всего хорошего")
            case "7":
                add_new_file()
                break


if __name__ == "__main__":
    take_choice()
