import pandas as pd

XML_FILE = pd.read_excel("./dataset/dataset_news_1.xlsx")


def read_column(str_nude: int):
    """Функция чтения строки из датасета"""
    if 0 >= str_nude >= len(XML_FILE["url_clean"]):
        return "Error range"
    return [XML_FILE["user_id"][str_nude], "http://" + XML_FILE["url_clean"][str_nude]]


# Входные данные номер строки из xlsx (NOTICE: с 1)
# Возвращает либо ошибку, либо ссылку
def get_url(id_news: int):
    # Проводим проверку на допустимость id_news
    if 1 <= id_news <= len(XML_FILE["url_clean"]):
        return "http://" + XML_FILE["url_clean"][id_news]
    return f"ERROR! The requested {id_news} not find!\n"


# входные данные: id-пользователя(int)
def range_news_for_user(user_id: int):
    """Вернет список новостей для пользователя"""
    if XML_FILE["user_id"].find(user_id) == -1:
        return f"ERROR! The requested {user_id} not find!\n"

    range_user = XML_FILE[XML_FILE["user_id"] == user_id]
    urls = []
    for url in range_user:
        urls.append("http://" + url)
    return urls
