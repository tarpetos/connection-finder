import flet as ft
from typing import Callable
from .connection_finder_base import _ConnectionFinder
from ..constants import (
    START_BUTTON_TEXT,
    STOP_BUTTON_TEXT,
    VOICE_MESSAGE,
    APP_TITLE,
    WINDOW_MIN_WIDTH,
    WINDOW_MIN_HEIGHT,
)


class FletApp(ft.UserControl, _ConnectionFinder):
    BUTTON_WIDTH = 400
    BUTTON_HEIGHT = 100

    def __init__(self, voice_message: ft.Audio) -> None:
        super().__init__()
        self.start_button = self.build_button(
            text=START_BUTTON_TEXT, button_callback=self.start_search
        )
        self.stop_button = self.build_button(
            text=STOP_BUTTON_TEXT, button_callback=self.stop_search
        )

        self.search_active = None
        self.sound = voice_message

    def build_button(self, text: str, button_callback: Callable) -> ft.ElevatedButton:
        return ft.ElevatedButton(
            text=text,
            on_click=button_callback,
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
        )

    def start_button_configure(self, disable: bool) -> None:
        self.start_button.disabled = disable

    def play_sound(self) -> None:
        self.sound.play()

    def stop_sound(self) -> None:
        self.sound.release()
        self.app_update()

    def app_update(self) -> None:
        self.update()

    def build_column(self) -> ft.Column:
        return ft.Column(
            [self.start_button, self.stop_button],
            horizontal_alignment=ft.CrossAxisAlignment.STRETCH,
        )

    def build(self) -> ft.Column:
        return self.build_column()


def run_app(page: ft.Page) -> None:
    page.title = APP_TITLE
    page.theme_mode = ft.ThemeMode.DARK
    center_alignment = "center"
    page.horizontal_alignment = center_alignment
    page.vertical_alignment = center_alignment
    page.window_min_width = WINDOW_MIN_WIDTH
    page.window_min_height = WINDOW_MIN_HEIGHT
    sound = ft.Audio(src=VOICE_MESSAGE)
    page.overlay.append(sound)
    page.update()
    flet_app = FletApp(sound)
    page.add(flet_app)


def flet_main() -> None:
    ft.app(target=run_app)
