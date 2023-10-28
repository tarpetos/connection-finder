from enum import Enum
from typing import Type, Literal


class AppOption(Enum):
    FLET = "flet"
    TKINTER = "tkinter"


AppOptionString: Type = Literal[AppOption.FLET, AppOption.TKINTER]
