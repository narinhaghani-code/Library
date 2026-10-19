import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import date
from models.borrow import Borrow

# OK
borrow = Borrow(1, "1234567890", "M0001", date(2024, 1, 1), date(2024, 1, 15))
print(borrow.__dict__)

# OK - returned 5 days late, fine = 5 * 0.5 = 2.5
borrow.mark_returned(date(2024, 1, 20))
print("Returned:", borrow.is_returned(), "| Fine:", borrow.fine())

# ERROR
try:
    borrow = Borrow(1, "1234567890", "M0001", date(2024, 1, 10), date(2024, 1, 1))
    print(borrow.__dict__)
except ValueError as error:
    print("Error:", error)
