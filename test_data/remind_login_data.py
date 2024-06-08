import string

from faker import Faker
import random
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

class RemindLoginData:
    def __init__(self):
        fake = Faker("pl_PL")
        self.remind_login_email = fake.email()