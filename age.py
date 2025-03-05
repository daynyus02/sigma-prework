# in the examples provided the answers were 31 and 48 but that would have been the case if we were in 2021 not 2025
# Hence why my answers differ as I'm using the current date which is 05/03/2025

from datetime import datetime


def calc_age(dob):
    current = datetime.today().date()
    dob = datetime.strptime(dob, "%d-%m-%Y").date()
    return current.year - dob.year


age = "01-01-1990"
age = "04-12-1972"
print(calc_age(age))
