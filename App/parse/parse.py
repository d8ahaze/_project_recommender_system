from bs4 import BeautifulSoup
import requests


# На вход получает ссылку
# Возвращает response_code
def get_html_code(url):
    response_code = requests.get(url)
    return response_code

#news-article-spheres__link (find_all) сферы деятельности на один на сайте
#news-article-place__name (find)  местность
#news-article-place__name (find)  район


# выполняем парсинг в html_code.
# По всей странице ищем элемент заданный в html_tag с классом переданном в class_name
# вернет либо None, либо список с тегами
def parse_tags(url, html_tag, class_name):
    # html_code.text это html код страницы

    html_code = get_html_code(url)
    soup = BeautifulSoup(html_code.text, "lxml")
    # выполняем поиск по всей странице
    tags = soup.find_all(html_tag, class_name)
    all_tags = []
    # Если количество тегов будет равно 0, то вернем None для создания JSON файла
    if len(tags) == 0:
        return None
    # Записываем название тегов в список all_tags для удобств
    # выполняем перебор в списке tags
    for tag in tags:
        # добавляем в all_tags название тега
        # если бы было просто tag, тогда передался бы целый элемент
        all_tags.append(tag.text)
    return all_tags




