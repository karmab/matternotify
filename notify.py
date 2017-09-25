#!/usr/bin/env python3

from mattermostdriver import Driver
import os
import sys

if len(sys.argv) == 1:
    print("No message provided. Leaving")
    sys.exit(1)
else:
    message = ' '.join(sys.argv[1:])

if 'MATTERMOST_USERNAME' not in os.environ:
    print("missing USERNAME.Leaving...")
    os._exit(1)
username = os.environ.get('MATTERMOST_USERNAME')

if 'MATTERMOST_PASSWORD' not in os.environ:
    print("missing MATTERMOST_PASSWORD.Leaving...")
    os._exit(1)
password = os.environ.get('MATTERMOST_PASSWORD')

if 'MATTERMOST_URL' not in os.environ:
    print("missing MATTERMOST_URL.Leaving...")
    os._exit(1)
url = os.environ.get('MATTERMOST_URL')

if 'MATTERMOST_PORT' not in os.environ:
    print("missing MATTERMOST_PORT.Leaving...")
    os._exit(1)
port = int(os.environ.get('MATTERMOST_PORT'))

if 'MATTERMOST_TEAM' not in os.environ:
    print("missing MATTERMOST_TEAM.Leaving...")
    os._exit(1)
team = os.environ.get('MATTERMOST_TEAM')

if 'MATTERMOST_CHANNEL' not in os.environ:
    print("missing MATTERMOST_CHANNEL.Leaving...")
    os._exit(1)
channel = os.environ.get('MATTERMOST_CHANNEL')

foo = Driver({
    'url': url,
    'login_id': username,
    'password': password,
    'scheme': 'https',
    'port': port,
    'basepath': '/api/v4',
    'verify': False,
})

foo.login()
channel = foo.api['channels'].get_channel_by_name_and_team_name(channel_name=channel, team_name=team)
channel_id = channel['id']

print("Sending message to channel %s: %s %s" % (channel, message))
foo.api['posts'].create_post(options={
                             'channel_id': channel_id,
                             'message': message,
                             })

foo.logout()
