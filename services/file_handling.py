import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    punc = ('.', '!', '?', ',', ';', ':')
    if (start + size) > (len(text)):
        end_loop = len(text) - 1
    else:
        end_loop = size + start - 1

    for i in range(size):
        if text[end_loop] in punc:
            if (start + size) < (len(text)) and text[end_loop + 1] in punc:
                if text[end_loop + 2] in punc:
                    end_loop -= 1
                    continue
                else:
                    end_loop -= 2
                    continue
            if text[end_loop - 1] in punc:
                if text[end_loop - 2] in punc:
                    end_loop -= 3
                    continue
                else:
                    end_loop -= 2
                    continue
            return text[start:(end_loop + 1)], end_loop - start + 1
        end_loop -= 1


def prepare_book(path: str) -> None:
    b = open(path, mode='r', encoding='utf-8')
    booking = b.read()
    b.close()
    booking = str(booking)
    pages = len(booking) / PAGE_SIZE
    if pages - int(pages) != 0:
        pages = int(pages) + 1
    start = 0
    res = 'a'
    i = 1
    while res:
        text, len_p = _get_part_text(booking, start, PAGE_SIZE)
        res = text.lstrip()
        start += len_p
        if res:
            book[i] = res
        i += 1


prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))
