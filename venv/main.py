import csv

name_1 = "da"
name_2 = "ta"
data_names = ["ma", "in"]

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        #[name_1, name_2]
        #чтобы открыть в виде таблицы можно использовать LibreOffice
        #data_names
        ("user_name", "user_rename")
    )
user_data = [
    ["user1", "rename1"],
    ["user1", "rename1"],
    ["user1", "rename1"],
]

for user in user_data:
    with open("data.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow(
            user
        )


#объединение данных в одну коллекцию
# with open("data.csv", "a") as file:
#        writer = csv.writer(file)
#        writer.writerows(
#            user_data
#        )