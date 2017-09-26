
use the following 

```
oc create secret generic matternotify-secret --from-literal=username=$MATTERMOST_USERNAME --from-literal=password=$MATTERMOST_PASSWORD --from-literal=url=$MATTERMOST_URL --from-literal=port=$MATTERMOST_PORT --from-literal=team=$MATTERMOST_TEAM --from-literal=channel=$MATTERMOST_CHANNEL
oc create -f matternotify.yml
```
