import model
import menu

def start():
    while True:
        pb = model.get_phone_book()
        choice = menu.main_menu()
        match choice:
            case 1:
                model.open_file()
                menu.show_message('Файл успешно открыт.')
            case 2:
                model.save_file()
                menu.show_message('Файл успешно сохранен.')
            case 3:
                menu.show_contacs(pb, 'Телефонная книга пуста или не открыта. ')
            case 4:
                model.add_contact(menu.add_contact())
            case 5:
                if menu.show_contacs(pb, 'Телефонная книга пуста или не открыта. '):
                    index = menu.iput_index('Введите номер изменяемого контакта.')
                    contact = menu.change_contact(pb, index)
                    model.change_contact(contact, index)
                    menu.show_message(f'Контакт {model.get_phone_book()[index-1].get("name")} успешно изменен.')
            case 6:
                search = menu.input_serch('Ведите искомый элемент.')
                result = model.finde_contact(search)
                menu.show_contacs(result, 'Контакт не найден.')
            case 7:
                if menu.show_contacs(pb, 'Телефонная книга пуста или не открыта. '):
                    i = input('Ведите номер контакта который хотите удалить: ')
                    if i:
                        i = int(i)
                        model.del_contact(i-1)
                    else:
                        pass
            case 8:
                return