import csv



def get(n):
    num = int(n)
    result = []

    with open('/Users/hong-in-yeong/WEB/hiy-django/costaurant/csv/Food_info_test.csv.csv',mode='r')as f_i:
        reader = csv.reader(f_i)

        for i in reader:
            result.append(i)
    print(num)
    return result

print(get(6))