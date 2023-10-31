from .ui import flet_main, tkinter_main, kivy_main
from .types import UIOption, UIOptionString, UIOptions


class ConnectionFinder:
    def start(self, app_selector: UIOptionString) -> None:
        app_options: UIOptions = {
            UIOption.FLET: flet_main,
            UIOption.TKINTER: tkinter_main,
            UIOption.KIVY: kivy_main,
        }

        select_ui = app_options.get(app_selector, None)
        if select_ui is None:
            raise ValueError(
                f"Invalid app option! Should be one of the {UIOptionString}"
            )
        select_ui()
