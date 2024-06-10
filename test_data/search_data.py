from faker import Faker
import csv

def get_csv_data(filename):
    rows = []
    data_file = open(filename, "r")
    reader = csv.reader(data_file)
    # Pomiń pierwszy wiersz
    next(reader, None)
    for row in reader:
        rows.append(row)
    return rows

class SearchData:
    def __init__(self, length = 20, dights: bool = 5):
        fake = Faker("pl_PL")
        self.word = fake.password(length + dights)