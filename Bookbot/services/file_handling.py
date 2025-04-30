import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text, start, page_size):
    textik = text
    textik = textik[start:min(start+page_size, len(text))]
    if textik[-1] in [',', '.', '!', ':', ';', '?'] and min(start+page_size, len(text)) != len(text) and text[start+page_size] in [',', '.', '!', ':', ';', '?']:
        flag = False
        while True:
            if textik[-1] in [',', '.', '!', ':', ';', '?'] and flag:
                return [textik, len(textik)]
            if not (textik[-1] in [',', '.', '!', ':', ';', '?']):
                flag = True
            textik = textik[:-1]
    while True:
        if textik[-1] in [',', '.', '!', ':', ';', '?']:
            print(textik)
            return [textik, len(textik)]
        print(1)
        textik = textik[:-1]


# Функция, формирующая словарь книги
# Не удаляйте эти объекты - просто используйте
book: dict[int, str] = {}
PAGE_SIZE = 1050


# Дополните эту функцию, согласно условию задачи
def prepare_book(path: str) -> None:
    global book
    i = 1
    z = 0
    file = open(path,'r', encoding='utf-8')
    text = file.read()
    while True:
        u = _get_part_text(text, z, PAGE_SIZE)
        z += u[1]
        book[i] = u[0].strip()
        i += 1
        if z == len(text):
            return None
# Вызов функции prepare_book для подготовки книги из текстового файла
print(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))