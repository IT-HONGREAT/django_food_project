import csv


def get(file_path):

    result = []

    with open(file_path, mode="r") as f_i:
        reader = csv.reader(f_i)

        for i in reader:
            result.append(i)

    return result


print(get("/Users/hong-in-yeong/WEB/hiy-django/costaurant/csv/Food_info_test.csv.csv"))
