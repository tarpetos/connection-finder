import flet as ft

from .connection_finder_base import ConnectionFinder
from ..constants import START_BUTTON_TEXT, STOP_BUTTON_TEXT, VOICE_MESSAGE, APP_TITLE


class FletApp(ft.UserControl, ConnectionFinder):
    BUTTON_WIDTH = 400
    BUTTON_HEIGHT = 100

    def __init__(self, voice_message: ft.Audio) -> None:
        super().__init__()
        self.start_button = ft.ElevatedButton(
            text=START_BUTTON_TEXT,
            on_click=self.start_search,
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
        )

        self.stop_button = ft.ElevatedButton(
            text=STOP_BUTTON_TEXT,
            on_click=self.stop_search,
            width=self.BUTTON_WIDTH,
            height=self.BUTTON_HEIGHT,
        )

        self.search_active = None
        self.sound = voice_message

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
        )

    def build(self) -> ft.Column:
        return self.build_column()


def run_app(page: ft.Page) -> None:
    page.title = APP_TITLE
    page.theme_mode = ft.ThemeMode.DARK
    center_alignment = "center"
    page.horizontal_alignment = center_alignment
    page.vertical_alignment = center_alignment
    sound = ft.Audio(src=VOICE_MESSAGE)
    page.overlay.append(sound)
    page.update()
    flet_app = FletApp(sound)
    page.add(flet_app)


def flet_main() -> None:
    ft.app(target=run_app)
