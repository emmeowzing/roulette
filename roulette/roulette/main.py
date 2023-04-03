"""
Slack bot that auto-assigns and pings teams and/or groups channel threads.
"""


import time


def cli() -> None:
    """
    Print hello over and over again.
    """
    while True:
        print('Hello')
        time.sleep(10)


if __name__ == '__main__':
    cli()