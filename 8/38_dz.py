"""
Дополнить телефонный справочник возможностью изменения и удаления данных.
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
для изменения и удаления данных.
"""




# Функция для чтения данных из файла с кодировкой UTF-8
def read_phonebook(filename):
    phonebook = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                phonebook.append(data)
    except FileNotFoundError:
        print("Файл не найден.")
    return phonebook

# Функция для вывода данных из справочника
def print_phonebook(phonebook):
    for contact in phonebook:
        print(f"Фамилия: {contact[0]}, Имя: {contact[1]}, Отчество: {contact[2]}, Телефон: {contact[3]}")

# Функция для сохранения данных в файле с кодировкой UTF-8
def save_phonebook(filename, phonebook):
    with open(filename, 'w', encoding='utf-8') as file:
        for contact in phonebook:
            file.write(','.join(contact) + '\n')

# Функция для поиска контакта по характеристике
def search_contact(phonebook, attribute, value):
    results = []
    for contact in phonebook:
        if value.lower() in contact[attribute].lower():
            results.append(contact)
    return results

# Функция для изменения данных контакта
def update_contact(phonebook, attribute, old_value, new_value):
    updated = False
    for contact in phonebook:
        if old_value.lower() in contact[attribute].lower():
            contact[attribute] = new_value
            updated = True
    return updated

# Функция для удаления контакта
def delete_contact(phonebook, attribute, value):
    deleted = False
    phonebook_copy = phonebook[:]
    for contact in phonebook_copy:
        if value.lower() in contact[attribute].lower():
            phonebook.remove(contact)
            deleted = True
    return deleted

def main():
    phonebook_file = "phonebook.txt"
    phonebook = read_phonebook(phonebook_file)

    while True:
        print("\nМеню:")
        print("1. Вывести все контакты")
        print("2. Добавить новый контакт")
        print("3. Поиск по характеристике")
        print("4. Изменить данные контакта")
        print("5. Удалить контакт")
        print("6. Выход")

        choice = input("Выберите опцию (1/2/3/4/5/6): ")

        if choice == '1':
            print_phonebook(phonebook)
        elif choice == '2':
            last_name = input("Введите фамилию: ")
            first_name = input("Введите имя: ")
            middle_name = input("Введите отчество: ")
            phone_number = input("Введите номер телефона: ")
            new_contact = [last_name, first_name, middle_name, phone_number]
            phonebook.append(new_contact)
            save_phonebook(phonebook_file, phonebook)
            print("Контакт успешно добавлен.")
        elif choice == '3':
            search_attribute = input("Введите характеристику для поиска (Фамилия/Имя/Отчество/Телефон): ")
            search_value = input(f"Введите {search_attribute} для поиска: ")
            attribute_mapping = {"Фамилия": 0, "Имя": 1, "Отчество": 2, "Телефон": 3}
            if search_attribute in attribute_mapping:
                search_results = search_contact(phonebook, attribute_mapping[search_attribute], search_value)
                if search_results:
                    print_phonebook(search_results)
                else:
                    print("Нет результатов для заданных параметров.")
            else:
                print("Неверная характеристика для поиска.")
        elif choice == '4':
            search_attribute = input("Введите характеристику для изменения (Фамилия/Имя/Отчество/Телефон): ")
            search_value = input(f"Введите {search_attribute} для поиска: ")
            new_value = input(f"Введите новое значение для {search_attribute}: ")
            attribute_mapping = {"Фамилия": 0, "Имя": 1, "Отчество": 2, "Телефон": 3}
            if search_attribute in attribute_mapping:
                updated = update_contact(phonebook, attribute_mapping[search_attribute], search_value, new_value)
                if updated:
                    save_phonebook(phonebook_file, phonebook)
                    print("Данные успешно изменены.")
                else:
                    print("Нет результатов для заданных параметров.")
            else:
                print("Неверная характеристика для изменения.")
        elif choice == '5':
            search_attribute = input("Введите характеристику для удаления (Фамилия/Имя/Отчество/Телефон): ")
            search_value = input(f"Введите {search_attribute} для поиска: ")
            attribute_mapping = {"Фамилия": 0, "Имя": 1, "Отчество": 2, "Телефон": 3}
            if search_attribute in attribute_mapping:
                deleted = delete_contact(phonebook, attribute_mapping[search_attribute], search_value)
                if deleted:
                    save_phonebook(phonebook_file, phonebook)
                    print("Данные успешно удалены.")
                else:
                    print("Нет результатов для заданных параметров.")
            else:
                print("Неверная характеристика для удаления.")
        elif choice == '6':
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
