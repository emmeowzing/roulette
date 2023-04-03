"""
Slack bot that auto-assigns and pings teams and/or groups channel threads.
"""


from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
from importlib import metadata as meta

import logging
import sys
import os


__version__ = meta.version('slack-roulette')

log = logging.getLogger(__name__)


def cli() -> None:
    """
    Print hello over and over again.
    """
    parser = ArgumentParser(
        formatter_class=ArgumentDefaultsHelpFormatter,
        description=__doc__
    )

    parser.add_argument(
        '--version', action='store_true', default=False,
        help='Show premiscale version.'
    )

    parser.add_argument(
        '--debug', action='store_true', default=False,
        help='Turn on logging debug mode.'
    )

    parser.add_argument(
        '--token', default='$SLACK_TOKEN', type=str,
        help='Specify a Slack token with the CLI. Can be set to environment variable names as well.'
    )

    args = parser.parse_args()

        # Configure logger.
    if args.log_stdout:
        logging.basicConfig(
            stream=sys.stdout,
            format='%(asctime)s | %(levelname)s | %(message)s',
            level=(logging.DEBUG if args.debug else logging.INFO)
        )
    else:
        logging.basicConfig(
        stream=sys.stdout,
        format='%(message)s',
        level=(logging.DEBUG if args.debug else logging.INFO)
    )

    if len(args.token) and args.token[0] == '$':
        token = os.path.expandvars(args.token)

    if not len(args.token) or not token:
        log.error('Must set Slack token.')
        sys.exit(1)