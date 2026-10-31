import re
from datetime import date


def name_validator(name):
    if not isinstance(name, str) or not re.match(r"^[a-zA-Z\s]{3,50}$", name):
        raise ValueError("Invalid Name")
    return name


def title_validator(title):
    if not isinstance(title, str) or not re.match(r"^[a-zA-Z0-9\s,.:'-]{2,100}$", title):
        raise ValueError("Invalid Title")
    return title


def location_validator(location):
    if not isinstance(location, str) or location.strip() == "":
        raise ValueError("Location must be a string")
    return location


def isbn_validator(isbn):
    if not isinstance(isbn, str) or not re.match(r"^\d{10}(\d{3})?$", isbn):
        raise ValueError("Invalid ISBN (10 or 13 digits)")
    return isbn


def email_validator(email):
    if not isinstance(email, str) or not re.match(r"^[\w.+-]+@[\w-]+(\.[\w-]+)+$", email):
        raise ValueError("Invalid Email")
    return email


def id_validator(value, label):
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid {label}")
    if value <= 0:
        raise ValueError(f"{label} must be positive")
    return value


def count_validator(value, label, minimum=0):
    try:
        value = int(value)
    except (ValueError, TypeError):
        raise ValueError(f"Invalid {label}")
    if value < minimum:
        raise ValueError(f"{label} must be at least {minimum}")
    return value


def year_validator(year):
    try:
        year = int(year)
    except (ValueError, TypeError):
        raise ValueError("Invalid Year")
    if not 1000 <= year <= date.today().year:
        raise ValueError("Invalid Year")
    return year


def date_validator(value):
    if not isinstance(value, date):
        raise ValueError("Invalid Date")
    return value
