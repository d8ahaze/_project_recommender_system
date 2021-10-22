import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        ("id_news", "id_user", " tags", "url",)

    )



