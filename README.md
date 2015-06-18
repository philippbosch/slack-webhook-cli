slack-webhook-cli
=================

The easiest way to send messages to a [Slack](https://slack.com/) channel or
user through an [Incoming Webhook](https://api.slack.com/incoming-webhooks).

## TL;DR

[Watch this video](https://vimeo.com/131061395)

## Installation

Using [pip](https://pip.pypa.io/):

```shell
$ pip install slack-webhook-cli
```

From source:

```shell
$ git clone https://github.com/philippbosch/slack-webhook-cli.git
$ cd slack-webhook-cli
$ python setup.py install
```


## Prerequisites

You need to create and configure an incoming webhook [here](https://my.slack.com/services/new/incoming-webhook/). Grab the URL from
the **Webhook URL** field.


## Usage

I'll let the script speak for itself:

```
$ slack -h

usage: slack [-h] [-w WEBHOOK_URL] [-c CHANNEL] [-u USERNAME] [-i ICON_URL]
             [-e ICON_EMOJI] [-a] [-C COLOR] [-t TITLE]
             text

positional arguments:
  text                  message you want to get delivered. wrap in quotes if
                        it contains spaces.

optional arguments:
  -h, --help            show this help message and exit
  -w WEBHOOK_URL, --webhook-url WEBHOOK_URL
                        webhook URL to use. if not given, the
                        SLACK_WEBHOOK_URL environment variable needs to be set
  -c CHANNEL, --channel CHANNEL
                        channel the message should be sent to. can also be set
                        using the SLACK_CHANNEL environment variable. if not
                        given, the channel configured for this webhook URL
                        will be used.
  -u USERNAME, --username USERNAME
                        username that should be used as the sender. can also
                        be set using the SLACK_USERNAME environment variable.
                        if not given, the username configured for this webhook
                        URL will be used.
  -i ICON_URL, --icon-url ICON_URL
                        URL of an icon image to use. can also be set using the
                        SLACK_ICON_URL environment variable.
  -e ICON_EMOJI, --icon-emoji ICON_EMOJI
                        Slack emoji to use as the icon, e.g. `:ghost:`. can
                        also be set using the SLACK_ICON_EMOJI environment
                        variable.
  -a, --attachment      send message as a rich attachment
  -C COLOR, --color COLOR
                        set the attachment color
  -t TITLE, --title TITLE
                        set the attachment title
```

### Examples

```shell
$ slack "Hello from the command line"
$ slack -c \#random "something totally random"
$ slack -u hamlet "to be or not to be"
$ slack -e :ghost: "boo"
```


## License

[MIT](http://philippbosch.mit-license.org/)
