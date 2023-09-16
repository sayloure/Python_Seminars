"""
Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной
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

def main():
    phonebook_file = "phonebook.txt"
    phonebook = read_phonebook(phonebook_file)

    while True:
        print("\nМеню:")
        print("1. Вывести все контакты")
        print("2. Добавить новый контакт")
        print("3. Поиск по характеристике")
        print("4. Выход")

        choice = input("Выберите опцию (1/2/3/4): ")

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
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()
