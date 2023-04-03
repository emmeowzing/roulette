"""
Roulette chat bot.
"""


from slackbot import Bot as SlackBot
from roulette.roulette.bot import _Bot


class Slack(_Bot):
    """
    Encapsulate a Slack bot.
    """

    def start(self) -> bool:
        """
        Start the Slack bot.
        """
        self.bot = SlackBot()

        return True

    def stop(self) -> None:
        """
        Stop the Slack bot.
        """