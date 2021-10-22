import csv

name_1 = "da"
name_2 = "ta"

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(
        [name_1, name_2]
    )
