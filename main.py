#!/usr/bin/env python3
""" Gets a list of events for a specified user from github """

import json
from argparse import ArgumentParser
import requests


def main(argv=None):
    """ Githubber main function """
    args = parse_cmd_arguments(argv)
    response = requests.get(f"https://api.github.com/users/{args.user}/events")
    events = json.loads(response.content)

    for event in events:
        print("Event ID:{} created at {} by {}".format(
            event['id'],
            event['created_at'],
            event['actor']['display_login'],
        ))

    # Included because it was specifically asked for.
    # print(events[0]['created_at'])


def parse_cmd_arguments(args):
    """ Parses the command line arguments

    Arguments:
        args {list} -- argument list from command line

    Returns:
        ArgumentParser.parse_args
    """
    parser = ArgumentParser(description="githubber")
    parser.add_argument(
        "--user",
        help="Get stuff about specified user",
        action="store",
        required=True,
    )
    return parser.parse_args(args)


if __name__ == "__main__":
    main()
