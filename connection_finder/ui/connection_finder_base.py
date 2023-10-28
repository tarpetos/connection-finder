import requests
from abc import ABC, abstractmethod

from ..constants import REQUEST_URL, SUCCESSFUL_REQUEST_CODE


def is_connected() -> bool:
    try:
        send_request = requests.get(REQUEST_URL)
        if send_request.status_code == SUCCESSFUL_REQUEST_CODE:
            return True
    except requests.exceptions.ConnectionError:
        return False


class ConnectionFinder(ABC):
    def __init__(self):
        self.search_active = None

    def start_search(self, *args) -> None:
        self.search_active = True
        self.start_button_configure(disable=True)

        while True:
            self._check_connection()
            if not self.search_active:
                break

    def stop_search(self, *args) -> None:
        self.search_active = False
        self.start_button_configure(disable=False)
        self.stop_sound()

    def _check_connection(self) -> None:
        if not self.search_active:
            return

        if is_connected():
            self.play_sound()
            self.search_active = False
            self.start_button_configure(disable=False)

        self.app_update()

    @abstractmethod
    def start_button_configure(self, disable: bool) -> None:
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def play_sound(self) -> None:
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def stop_sound(self) -> None:
        raise NotImplementedError("Subclasses must implement this method.")

    @abstractmethod
    def app_update(self) -> None:
        raise NotImplementedError("Subclasses must implement this method.")
