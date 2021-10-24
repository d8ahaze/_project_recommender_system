import os.path
import markdown


def openfile(filename):
    """принимает markdown файл, конвертирует его в html и возвращает"""
    filepath = os.path.join("app/pages", filename)  # "app\\pages\\"
    with open(filepath, 'r', encoding='utf-8') as input_file:
        text = input_file.read()

    html = markdown.markdown(text)
    data = {
        "text": html
    }
    return data
