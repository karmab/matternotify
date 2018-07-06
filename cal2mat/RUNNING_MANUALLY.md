
You can also generate the notification crons on any unix system

- put your calendar json file from google in a *secret* directory
- with this hourly cron

```
#!/usr/bin/bash

export PATTERNS="XXX,YYY,ZZZ"
export SECRETDIR=/root/bin/secret
/usr/bin/crontab -l | /usr/bin/grep -v notify > /tmp/mycron
docker run -it -e PATTERNS="$PATTERNS" -v $SECRETDIR:/secret -e CALENDARPATH=/secret --rm karmab/cal2mat_unix  >> /tmp/mycron
crontab /tmp/mycron
```

the `/root/bin/notify.sh` script contains the following

```
#!/usr/bin/bash

export MATTERMOST_USERNAME=jhendrix
export MATTERMOST_PASSWORD=mysecret
export MATTERMOST_URL=chat.mattermost.io
export MATTERMOST_PORT=443
export MATTERMOST_TEAM=myteam
export MATTERMOST_CHANNEL=mychannel
docker run --rm --name=matternotify -e MATTERMOST_USERNAME=$MATTERMOST_USERNAME -e MATTERMOST_PASSWORD=$MATTERMOST_PASSWORD -e MATTERMOST_URL=$MATTERMOST_URL -e MATTERMOST_PORT=$MATTERMOST_PORT -e MATTERMOST_TEAM=$MATTERMOST_TEAM -e MATTERMOST_CHANNEL=$MATTERMOST_CHANNEL karmab/matternotify $@
```
