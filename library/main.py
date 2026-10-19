from tools.storage import JsonStorage
from view.console_view import ConsoleView
from controller.library_controller import LibraryController
from tools.exceptions import LibraryError


def main():
    storage = JsonStorage("data/library.json")
    view = ConsoleView()
    try:
        library = storage.load()
    except LibraryError as error:
        view.show_error(str(error))
        return
    LibraryController(library, storage, view).run()


if __name__ == "__main__":
    main()
