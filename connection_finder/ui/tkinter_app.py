import os
import pygame
import tkinter as tk
from typing import Callable
from .connection_finder_base import ConnectionFinder
from ..constants import START_BUTTON_TEXT, STOP_BUTTON_TEXT, APP_TITLE, ASSETS_FOLDER, VOICE_MESSAGE


class TkinterApp(tk.Tk, ConnectionFinder):
    BG_COLOR = "#1A1C1E"
    BUTTON_BG_COLOR = "#202429"
    ACTIVE_BUTTON_BG_COLOR = "#2D363F"
    DISABLED_BUTTON_BG_COLOR = "#323436"
    BUTTON_FONT_COLOR = "#9DC9FD"
    ACTIVE_FONT_COLOR = "#9ECAFF"
    DISABLED_FONT_COLOR = "#757678"

    def __init__(self):
        super().__init__()

        self.configure(bg=self.BG_COLOR)
        self.main_frame = tk.Frame(self, bg=self.BG_COLOR)

        self.start_button = self.build_button(text=START_BUTTON_TEXT, button_callback=self.start_search)
        self.stop_button = self.build_button(text=STOP_BUTTON_TEXT, button_callback=self.stop_search)

        self.place_elements()

        self.search_active = None
        pygame.mixer.init()
        self.sound = os.path.join(ASSETS_FOLDER, VOICE_MESSAGE)

    def build_button(self, text: str, button_callback: Callable) -> tk.Button:
        return tk.Button(
            master=self.main_frame,
            text=text,
            command=button_callback,
            background=self.BUTTON_BG_COLOR,
            foreground=self.BUTTON_FONT_COLOR,
            relief=tk.FLAT,
            highlightbackground=self.BUTTON_BG_COLOR,
            activebackground=self.ACTIVE_BUTTON_BG_COLOR,
            activeforeground=self.ACTIVE_FONT_COLOR,
            disabledforeground=self.DISABLED_FONT_COLOR,
        )

    def start_button_configure(self, disable: bool) -> None:
        if disable:
            self.start_button.configure(state=tk.DISABLED, bg=self.DISABLED_BUTTON_BG_COLOR)
        else:
            self.start_button.configure(state=tk.NORMAL, bg=self.BUTTON_BG_COLOR)

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
    tkinter_app.minsize(width=480, height=480)
    tkinter_app.mainloop()
