from model.member import Member

# OK
member = Member(1, "Narin Haghani", "narin@example.com")
print(member)

# ERROR
try:
    member = Member("abc", "Yekta Jafari", "yekta@example.com")
except ValueError as error:
    print("Error:", error)

try:
    member = Member(2, "Marjan Mohammadi", "not-an-email")
except ValueError as error:
    print("Error:", error)

try:
    member = Member(3, "12", "ali@example.com")
except ValueError as error:
    print("Error:", error)
