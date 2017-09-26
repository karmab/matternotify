#!/bin/bash

echo "Starting the cron thing"
echo -e "export LD_LIBRARY_PATH=/opt/rh/rh-python35/root/usr/lib64\nexport MATTERMOST_USERNAME=$MATTERMOST_USERNAME\nexport MATTERMOST_PASSWORD=$MATTERMOST_PASSWORD\nexport MATTERMOST_URL=$MATTERMOST_URL\nexport MATTERMOST_PORT=$MATTERMOST_PORT\nexport MATTERMOST_TEAM=$MATTERMOST_TEAM\nexport MATTERMOST_CHANNEL=$MATTERMOST_CHANNEL" > /home/matter/env
sudo crond -n -s -p -i -x ext
