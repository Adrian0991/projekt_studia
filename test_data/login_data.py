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

class LogInData:
    def __init__(self, length = 20, special_char: bool = 5, dights: bool = 5):
        fake = Faker("pl_PL")
        self.login = fake.password(length + dights)
        self.password = fake.password(length + special_char + dights)