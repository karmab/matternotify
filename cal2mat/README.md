
# this creates cronjobs of notification to mattermost, reading from a google calendar


# for a simple test on docker 
```
docker run --rm -it -v /Users/kboumedh/.kube/:/root/.kube -v /Users/kboumedh/.credentials/:/root/.credentials karmab/cal2mat /bin/bash
```

# on openshift

```
oc policy add-role-to-user view system:serviceaccount:matternotify:default
oc policy add-role-to-user edit system:serviceaccount:matternotify:default
oc create secret generic gcalendar-secret --from-file=$HOME/.credentials/calendar-python-quickstart.json
oc create -f cronmaster.yml
```
