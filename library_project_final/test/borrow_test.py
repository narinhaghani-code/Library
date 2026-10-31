from datetime import date
from model.borrow import Borrow

# OK
borrow = Borrow(1, 1, 1, date(2024, 1, 1), date(2024, 1, 15))
print(borrow)

# OK - returned 5 days late, fine = 5 * 0.5 = 2.5
borrow.return_date = date(2024, 1, 20)
print("Returned:", borrow.is_returned(), "| Fine:", borrow.fine())

# ERROR
try:
    borrow = Borrow(1, 1, 1, date(2024, 1, 10), date(2024, 1, 1))
except ValueError as error:
    print("Error:", error)

try:
    borrow = Borrow(0, 1, 1, date(2024, 1, 1), date(2024, 1, 15))
except ValueError as error:
    print("Error:", error)
