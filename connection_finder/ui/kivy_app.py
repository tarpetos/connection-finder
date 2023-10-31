import os
from typing import Callable

from .connection_finder_base import _ConnectionFinder
from .colors import (
    MAIN_BG,
    BUTTON_BG,
    ACTIVE_BUTTON_BG,
    DISABLED_BUTTON_BG,
    BUTTON_FONT,
)
from ..constants import (
    START_BUTTON_TEXT,
    STOP_BUTTON_TEXT,
    APP_TITLE,
    WINDOW_MIN_WIDTH,
    WINDOW_MIN_HEIGHT,
    ASSETS_FOLDER,
    VOICE_MESSAGE,
)


def kivy_main() -> None:
    from kivy.app import App
    from kivy.core.window import Window
    from kivy.uix.gridlayout import GridLayout
    from kivy.uix.button import Button
    from kivy.core.audio import SoundLoader
    from kivy.clock import Clock

    class KivyApp(App, _ConnectionFinder):
        def __init__(self, **kwargs) -> None:
            super().__init__(**kwargs)
            self.start_button = self.build_button(
                text=START_BUTTON_TEXT, button_callback=self.start_search
            )
            self.stop_button = self.build_button(
                text=STOP_BUTTON_TEXT, button_callback=self.stop_search
            )

            self.search_active = None
            sound_path = os.path.join(ASSETS_FOLDER, VOICE_MESSAGE)
            self.sound = SoundLoader().load(sound_path)
            self.request_event = None

        def build_button(self, text: str, button_callback: Callable) -> Button:
            return Button(
                text=text,
                on_press=button_callback,
                background_color=BUTTON_BG,
                background_normal=ACTIVE_BUTTON_BG,
                background_disabled_down=DISABLED_BUTTON_BG,
                color=BUTTON_FONT,
            )

        def start_search(self, *args) -> None:
            self.search_active = True
            self.start_button_configure(disable=True)
            Clock.schedule_interval(self._check_connection, 1)
            if not self.search_active:
                Clock.unschedule(self._check_connection)

        def start_button_configure(self, disable: bool) -> None:
            self.start_button.disabled = disable

        def play_sound(self) -> None:
            self.sound.play()

        def stop_sound(self) -> None:
            Clock.unschedule(self._check_connection)
            self.sound.stop()

        def app_update(self) -> None:
            pass

        def build(self) -> GridLayout:
            parent = GridLayout(cols=1, spacing=125, padding=100)
            parent.add_widget(self.start_button)
            parent.add_widget(self.stop_button)
            return parent

    kivy_app = KivyApp()
    kivy_app.title = APP_TITLE
    Window.size = (WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
    Window.minimum_width, Window.minimum_height = Window.size
    Window.clearcolor = MAIN_BG
    kivy_app.run()
