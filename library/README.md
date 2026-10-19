# Library Management System

Run the program (from inside this folder):

    python3 main.py

Run the tests (each one prints OK / ERROR results):

    python3 tests/book_test.py
    python3 tests/member_test.py
    python3 tests/borrow_test.py
    python3 tests/library_test.py

Structure:

    main.py          starts the program
    models/          book.py, member.py, borrow.py, library.py
    tools/           validation.py, exceptions.py, storage.py
    view/            console_view.py
    controller/      library_controller.py
    tests/           book_test.py, member_test.py, borrow_test.py, library_test.py
