import re
from datetime import date


def title_validator(title):
    if not isinstance(title, str) or not re.match(r"^[a-zA-Z0-9 ,.:'-]{2,100}$", title):
        raise ValueError("Invalid Title")
    return title


def author_validator(author):
    if not isinstance(author, str) or not re.match(r"^[a-zA-Z .'-]{3,50}$", author):
        raise ValueError("Invalid Author")
    return author


def isbn_validator(isbn):
    if not isinstance(isbn, str) or not re.match(r'^\d{10}(\d{3})?$', isbn):
        raise ValueError("Invalid ISBN (use 10 or 13 digits)")
    return isbn


def year_validator(year):
    if not isinstance(year, int) or not 1000 <= year <= date.today().year:
        raise ValueError("Invalid Year")
    return year


def count_validator(count, minimum=0):
    if not isinstance(count, int) or count < minimum:
        raise ValueError("Invalid Count")
    return count


def name_validator(name):
    if not isinstance(name, str) or not re.match(r'^[a-zA-Z ]{3,50}$', name):
        raise ValueError("Invalid Name")
    return name


def member_id_validator(member_id):
    if not isinstance(member_id, str) or not re.match(r'^M\d{4}$', member_id):
        raise ValueError("Invalid Member ID (example: M0001)")
    return member_id


def email_validator(email):
    if not isinstance(email, str) or not re.match(r'^[\w.+-]+@[\w-]+(\.[\w-]+)+$', email):
        raise ValueError("Invalid Email")
    return email


def borrow_id_validator(borrow_id):
    if not isinstance(borrow_id, int) or borrow_id < 1:
        raise ValueError("Invalid Borrow ID")
    return borrow_id


def date_validator(value):
    if not isinstance(value, date):
        raise ValueError("Invalid Date")
    return value
