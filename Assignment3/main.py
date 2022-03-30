from Repository.repository import Repository
from Controller.controller import Controller
from UI.ui import UI


def main():
    repository = Repository()
    controller = Controller(repository)
    ui = UI(controller)
    ui.start()


if __name__ == "__main__":
    main()