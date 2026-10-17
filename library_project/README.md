# Library Management System

Run the program (from inside this folder):

    python3 main.py

Run the tests (each one prints OK / ERROR results):

    python3 models/book_test.py
    python3 models/member_test.py
    python3 models/borrow_test.py
    python3 models/library_test.py

Structure:

    main.py          starts the program
    models/          book.py, member.py, borrow.py, library.py + *_test.py files
    tools/           validation.py, exceptions.py, storage.py
    view/            console_view.py
    controller/      library_controller.py
