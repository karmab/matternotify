# matternotify repository

[![Build Status](https://travis-ci.org/karmab/matternotify.svg?branch=master)](https://travis-ci.org/karmab/matternotify)
[![](https://images.microbadger.com/badges/image/karmab/matternotify.svg)](https://microbadger.com/images/karmab/matternotify "Get your own image badge on microbadger.com")

MatterNotify allows you to send messages to members of a given mattermost team in a specific channel periodically ( for instance when it's time for a meeting ).

You ll have to provide the cron to use, for instance

```
00 15 * * * /notify.py @all time for a daily meeting
```

## Requisites

the following environment variables need to be set for the called script to work

- MATTERMOST_USERNAME
- MATTERMOST_PASSWORD
- MATTERMOST_URL
- MATTERMOST_PORT
- MATTERMOST_TEAM
- MATTERMOST_CHANNEL

Then i use

```
docker run --name=matternotify -v $PWD/cron:/var/spool/cron -e MATTERMOST_USERNAME=$MATTERMOST_USERNAME -e MATTERMOST_PASSWORD=$MATTERMOST_PASSWORD -e MATTERMOST_URL=$MATTERMOST_URL -e MATTERMOST_PORT=$MATTERMOST_PORT -e MATTERMOST_TEAM=$MATTERMOST_TEAM -e MATTERMOST_CHANNEL=$MATTERMOST_CHANNEL --restart unless-stopped -d karmab/matternotify
```

Also note that i explicitely set the timezone to Europe/Madrid (CEST)

## TODO

- Run on openshift
- Not run as root?
- Use centos image

## Copyright

Copyright 2017 Karim Boumedhel

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Problems?

Send me a mail at [karimboumedhel@gmail.com](mailto:karimboumedhel@gmail.com) !

Mac Fly!!!

karmab
