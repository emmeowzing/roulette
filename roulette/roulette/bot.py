"""
Template discourse class.
"""


from typing import Any


class _Bot:
    """
    Base bot class with default methods every Bot instance should have.
    """
    def __init__(self, token: str, url: str) -> None:
        self.token = token
        self.url = url

    def start(self) -> Any:
        raise NotImplemented

    def stop(self) -> Any:
        raise NotImplemented

    def __enter__(self) -> _Bot:
        self.start()
        return self

    def __exit__(self, *args: Any) -> None:
        self.stop()