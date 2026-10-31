# Library Management System

Install streamlit once, then run the program from inside this folder (a page opens in the browser):

    pip install streamlit
    streamlit run main.py

Run the tests from inside this folder:

    python3 -m test.book_test
    python3 -m test.member_test
    python3 -m test.storage_test
    python3 -m test.borrow_test
    python3 -m test.controller_test

Structure:

    main.py       starts the app
    model/        book.py, member.py, borrow.py, storage.py
    controller/   book_controller.py, member_controller.py, borrow_controller.py
    view/         menu.py, book_view.py, member_view.py, borrow_view.py
    tools/        validation.py, file_manager.py
    test/         book_test.py, member_test.py, storage_test.py, borrow_test.py, controller_test.py
