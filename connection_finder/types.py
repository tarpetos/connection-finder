from enum import Enum
from typing import Type, Literal, Dict, Callable


class UIOption(Enum):
    FLET = "flet"
    TKINTER = "tkinter"
    KIVY = "kivy"


UIOptionString: Type = Literal[UIOption.FLET, UIOption.TKINTER, UIOption.KIVY]
UIOptions: Type = Dict[UIOptionString, Callable]
