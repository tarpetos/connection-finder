from connection_finder import AppStarter
from connection_finder.types import AppOptionString, AppOption


def main(option: AppOptionString) -> None:
    starter = AppStarter()
    starter.start(option)


if __name__ == "__main__":
    main(option=AppOption.FLET)
