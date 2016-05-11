#!/usr/bin/env python

import argparse
import json
import os
import sys

import requests


VERSION = ('0', '2', '3')


def get_version():
    return '.'.join(VERSION)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('text', nargs='?', help='message you want to get delivered. wrap in quotes if it contains spaces. Use "-" to read from stdin.')
    parser.add_argument('-w', '--webhook-url', help='webhook URL to use. if not given, the SLACK_WEBHOOK_URL environment variable needs to be set.', default=os.getenv('SLACK_WEBHOOK_URL'))
    parser.add_argument('-c', '--channel', help='channel the message should be sent to. can also be set using the SLACK_CHANNEL environment variable. if not given, the channel configured for this webhook URL will be used.', default=os.getenv('SLACK_CHANNEL'))
    parser.add_argument('-u', '--username', help='username that should be used as the sender. can also be set using the SLACK_USERNAME environment variable. if not given, the username configured for this webhook URL will be used.', default=os.getenv('SLACK_USERNAME'))
    parser.add_argument('-i', '--icon-url', help='URL of an icon image to use. can also be set using the SLACK_ICON_URL environment variable.', default=os.getenv('SLACK_ICON_URL'))
    parser.add_argument('-e', '--icon-emoji', help='Slack emoji to use as the icon, e.g. `:ghost:`. can also be set using the SLACK_ICON_EMOJI environment variable.', default=os.getenv('SLACK_ICON_EMOJI'))
    parser.add_argument('-a', '--attachment', help='send message as a rich attachment', action='store_true', default=False)
    parser.add_argument('-C', '--color', help='set the attachment color')
    parser.add_argument('-t', '--title', help='set the attachment title')

    args = parser.parse_args()

    if args.webhook_url is None:
        sys.stderr.write('No webhook URL given.\nEither use the -w/--webhook-url argument or the SLACK_WEBHOOK_URL environment variable.\n')
        return 1

    if args.text == '-' and not sys.stdin.isatty():
        args.text = sys.stdin.read()

    if args.text is None:
        parser.print_help()
        return 0

    if args.attachment is not True:
        payload = {
            'text': args.text
        }
    else:
        payload = {
            'attachments': [
                {
                    'fallback': args.text,
                    'color': args.color,
                    'fields': [
                        {
                            'title': args.title,
                            'value': args.text,
                            'short': False
                        }
                    ]
                }
            ]
        }

    if args.channel is not None:
        if args.channel[0] not in ['#', '@']:
            args.channel = '#' + args.channel
        payload['channel'] = args.channel

    if args.username is not None:
        payload['username'] = args.username

    if args.icon_url is not None:
        payload['icon_url'] = args.icon_url
    elif args.icon_emoji is not None:
        payload['icon_emoji'] = args.icon_emoji

    try:
        res = requests.post(args.webhook_url, data=json.dumps(payload))
    except Exception as e:
        sys.stderr.write('An error occurred when trying to deliver the message:\n  {0}'.format(e.message))
        return 2

    if not res.ok:
        sys.stderr.write('Could not deliver the message. Slack says:\n  {0}'.format(res.text))


if __name__ == '__main__':
    sys.exit(main())
