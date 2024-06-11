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

class RemindPasswordData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.remind_password_email = fake.email()