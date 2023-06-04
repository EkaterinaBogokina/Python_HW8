def add_contact(f):
    input_name = input('Enter name: ')
    input_last_name = input('Enter surname: ')
    input_phone = input('Enter phone number: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'{data}\n')
    print(f'Recording {data} added')


def read_all(f):
    with open(f, 'r',encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list
        

def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace(';', '')
        line = line.replace('\n', '')
        print(line)
        

def search_contact(f):
    last_name = input('Enter surname ')
    adr_book = read_all(f)
    for line in adr_book:
        if last_name in line:
            print(line)


def delete_contact(f):
    surname_to_delete = input('Enter surname: ')
    name_to_delete = input('Enter name: ')
    data = read_all(f)
    new_data = []
    for item in data:
        if surname_to_delete in item and name_to_delete in item:
            continue
        new_data.append(item)
    with open(f, 'w', encoding='utf-8') as fd: 
        fd.write(''.join(new_data))




def main():
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - добавить запись;\n2 - прочитать всю тел. книгу;\n'
                            '3 - найти запись;\nd - удалить запись;\nz - выход;  ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
           print_all(file)
        elif user_choice == '3':
           search_contact(file)
        elif user_choice == 'd':
           delete_contact(file)
        elif user_choice == 'z':
            break
           


if __name__ == '__main__':
    main()
