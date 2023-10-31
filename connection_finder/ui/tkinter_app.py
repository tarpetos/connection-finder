import os
import pygame
import tkinter as tk
from typing import Callable

from .colors import (
    MAIN_BG,
    BUTTON_BG,
    ACTIVE_BUTTON_BG,
    DISABLED_BUTTON_FONT,
    BUTTON_FONT,
    ACTIVE_BUTTON_FONT,
    DISABLED_BUTTON_BG,
)
from .connection_finder_base import _ConnectionFinder
from ..constants import (
    START_BUTTON_TEXT,
    STOP_BUTTON_TEXT,
    APP_TITLE,
    ASSETS_FOLDER,
    VOICE_MESSAGE,
    WINDOW_MIN_WIDTH,
    WINDOW_MIN_HEIGHT,
)


class TkinterApp(tk.Tk, _ConnectionFinder):
    def __init__(self) -> None:
        super().__init__()

        self.configure(bg=MAIN_BG)
        self.main_frame = tk.Frame(self, bg=MAIN_BG)

        self.start_button = self.build_button(
            text=START_BUTTON_TEXT, button_callback=self.start_search
        )
        self.stop_button = self.build_button(
            text=STOP_BUTTON_TEXT, button_callback=self.stop_search
        )

        self.place_elements()

        self.search_active = None
        pygame.mixer.init()
        self.sound = os.path.join(ASSETS_FOLDER, VOICE_MESSAGE)

    def build_button(self, text: str, button_callback: Callable) -> tk.Button:
        return tk.Button(
            master=self.main_frame,
            text=text,
            command=button_callback,
            relief=tk.FLAT,
            background=BUTTON_BG,
            highlightbackground=BUTTON_BG,
            activebackground=ACTIVE_BUTTON_BG,
            disabledforeground=DISABLED_BUTTON_FONT,
            foreground=BUTTON_FONT,
            activeforeground=ACTIVE_BUTTON_FONT,
        )

    def start_button_configure(self, disable: bool) -> None:
        if disable:
            self.start_button.configure(state=tk.DISABLED, bg=DISABLED_BUTTON_BG)
        else:
            self.start_button.configure(state=tk.NORMAL, bg=BUTTON_BG)

    def play_sound(self) -> None:
        pygame.mixer.music.load(self.sound)
        pygame.mixer.music.play(loops=0)

    def stop_sound(self) -> None:
        pygame.mixer.music.stop()

    def app_update(self) -> None:
        self.update()

    def place_elements(self) -> None:
        self.start_button.pack(expand=True, fill=tk.BOTH, padx=100, pady=75)
        self.stop_button.pack(expand=True, fill=tk.BOTH, padx=100, pady=75)
        self.main_frame.pack(expand=True, fill=tk.BOTH)


def tkinter_main() -> None:
    tkinter_app = TkinterApp()
    tkinter_app.wm_title(APP_TITLE)
    tkinter_app.minsize(width=WINDOW_MIN_WIDTH, height=WINDOW_MIN_HEIGHT)
    tkinter_app.mainloop()
