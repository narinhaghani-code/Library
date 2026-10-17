import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from models.member import Member

# OK
member = Member("M0001", "narin Haghani", "narin@example.com")
print(member.__dict__)

# ERROR
try:
    member = Member("1", "Yekta Jafari", "yekta@example.com")
    print(member.__dict__)
except ValueError as error:
    print("Error:", error)

try:
    member = Member("M0001", "Marjan Mohammadi", "not-an-email")
    print(member.__dict__)
except ValueError as error:
    print("Error:", error)
