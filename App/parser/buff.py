import csv

from get_url import read_column
from .parser import get_html_code, parse_tags

with open("new_dataset.csv", "w") as file:
    write = csv.writer(file)

    write.writerow(["id_user", "url", "tags"])

    for i in range(1000):
        buff = read_column(i)
        buff.append(parse_tags(buff[1], "a", "news-article-tags__link"))
        write.writerow(buff)
