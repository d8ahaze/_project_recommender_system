from typing import List, Any

from fastapi import APIRouter

from App.method.constuction_for_json import JSON
from App.parse.get_url import range_news_for_user
from App.parse.parse import get_html_code, parse_tags

router = APIRouter(
    prefix="/parse",
    tags=["moscow"]
)

# создаем массив
json_list: List[Any] = []


# json = JSON(
#     id_news:
#     is_user:
#     tags:
#     url:
# )

@router.get("/parse")
async def get_parse():
    return json_list


id_user = 1
user = range_news_for_user(id_user)

# Делаем проход по массиву и сохраняем в себе саму ссылку
json_list = []
for url in user["url_clean"]:
    html_code = get_html_code(url)
    # записываем все в список tags
    tags = parse_tags(html_code, "a", "news-article-tags__link")
    # Сие страшное выражение означает, что мы ищем
    # в DataFrame со столбцом url_clean строчки, где url совпадает с нашми
    # в резульате чего, мы получаем номер строки
    number_column = user.loc[user["url_clean"] == url].index[0]
    buff = JSON(
        id_news=number_column,
        id_user=id_user,
        tags=tags,
        url=url
    )
    json_list.append(buff)


@router.get("/res")
async def get_json():
    return json_list


@router.post("/parse")
async def get_create_json():
    pass
