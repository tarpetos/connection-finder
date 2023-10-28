from .ui import flet_main, tkinter_main
from .types import AppOption, AppOptionString


class AppStarter:
    def start(self, app_selector: AppOptionString) -> None:
        if app_selector == AppOption.FLET:
            flet_main()
        elif app_selector == AppOption.TKINTER:
            tkinter_main()
        else:
            raise ValueError(f"Invalid app option! Should be on of the {AppOptionString}")
