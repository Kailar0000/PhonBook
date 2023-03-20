import tex_fail

def main_menu() -> int:
    print(tex_fail.main_menu)
    length_menu = len(tex_fail.main_menu.split('\n'))-1
    while True:
        choise =input("Выберите пункт меню: ")
        if choise.isdigit() and 0 < int(choise) <= length_menu:
            return int(choise)
        else:
            print(f"Ведите число от 1 до {length_menu}")

def show_contacs(book: list[dict], error_massag: str):
    if not book:
        print(error_massag)
        return False
    else:
        for i, contact in enumerate(book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
        return True

def add_contact() -> dict:
    name = input('Ведите имя:')
    phone = input('Ведите номер:')
    comment = input('Ведите комментарий:')
    return {'name' : name, 'phone' : phone, 'comment' : comment}

def iput_index(massage: str):
    return  int(input(massage))

def input_serch(massage: str):
    return input(massage)

def change_contact(book: list[dict], index: int):
    print('')
    contact = add_contact()
    return {'name': contact.get('name') if contact.get('name') else book[index-1].get('name'),
            'phone': contact.get('phone') if contact.get('phone') else book[index-1].get('phone'),
            'comment': contact.get('comment') if contact.get('comment') else book[index-1].get('comment')}

def show_message(message: str):
    print('-' * len(message))
    print(message)
    print('-' * len(message))