# matternotify repository

[![Build Status](https://travis-ci.org/karmab/matternotify.svg?branch=master)](https://travis-ci.org/karmab/matternotify)
[![](https://images.microbadger.com/badges/image/karmab/matternotify.svg)](https://microbadger.com/images/karmab/matternotify "Get your own image badge on microbadger.com")

MatterNotify allows you to send messages to members of a given mattermost team in a specific channel periodically ( for instance when it's time for a meeting ).

you can either use the provided script notify.py, or run on docker or openshift

## Requisites

the following environment variables need to be set for the script to work

- MATTERMOST_USERNAME
- MATTERMOST_PASSWORD
- MATTERMOST_URL
- MATTERMOST_PORT
- MATTERMOST_TEAM
- MATTERMOST_CHANNEL

To send a single message using the container version, 

```
docker run --rm -it --name=matternotify -e MATTERMOST_USERNAME=$MATTERMOST_USERNAME -e MATTERMOST_PASSWORD=$MATTERMOST_PASSWORD -e MATTERMOST_URL=$MATTERMOST_URL -e MATTERMOST_PORT=$MATTERMOST_PORT -e MATTERMOST_TEAM=$MATTERMOST_TEAM -e MATTERMOST_CHANNEL=$MATTERMOST_CHANNEL karmab/matternotify YOUR_MESSAGE
```

to use on openshift, we leverage cronjobs

```
oc run matternotify --image=karmab/matternotify --schedule='*/1 * * * *' --restart=OnFailure --labels parent="matter" --env MATTERMOST_USERNAME=$MATTERMOST_USERNAME --env MATTERMOST_PASSWORD=$MATTERMOST_PASSWORD --env MATTERMOST_URL=$MATTERMOST_URL --env MATTERMOST_PORT=$MATTERMOST_PORT --env MATTERMOST_TEAM=$MATTERMOST_TEAM --env MATTERMOST_CHANNEL=$MATTERMOST_CHANNEL -- YOUR_MESSAGE
```

for more security, you can also use [secrets](secrets.md)


## Using with cal2mat

```
oc new-project matternotify
oc create secret generic matternotify-secret --from-literal=username=$MATTERMOST_USERNAME --from-literal=password=$MATTERMOST_PASSWORD --from-literal=url=$MATTERMOST_URL --from-literal=port=$MATTERMOST_PORT --from-literal=team=$MATTERMOST_TEAM --from-literal=channel=$MATTERMOST_CHANNEL
oc create secret generic gcalendar-secret --from-file=$HOME/.credentials/calendar-python-quickstart.json
# edit cronmaster PATTERNS env and optionally DAYS and BEFORE( for time before alert to be sent)
oc create -f cronmaster.yml
```

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

Mc Fly!!!

karmab
