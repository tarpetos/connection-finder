from connection_finder import ConnectionFinder
from connection_finder.types import UIOptionString, UIOption


def main(option: UIOptionString) -> None:
    starter = ConnectionFinder()
    starter.start(option)


if __name__ == "__main__":
    main(option=UIOption.FLET)
