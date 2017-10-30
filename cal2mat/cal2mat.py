import yaml
from kubernetes import client, config
import os
import googlecalendar
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


namespace = 'matternotify'
mastercron = 'cal2mat'
timezone = 'America/New_York'
days = 1
patterns = ['Application Integration Engineering', 'AOS Group 3/4']
before = 5
template = "crontemplate.yml"

if __name__ == "__main__":
    if 'KUBERNETES_PORT' in os.environ:
        config.load_incluster_config()
    else:
        config.load_kube_config()
    cli = client.BatchV2alpha1Api()
    # clean old crons
    old_crons = [item.metadata.name for item in cli.list_namespaced_cron_job(namespace=namespace).items]
    for old in cli.list_namespaced_cron_job(namespace=namespace).items:
        if old.metadata.name == mastercron:
            continue
        print("Removing old cronjob %s" % old.metadata.name)
        cli.delete_namespaced_cron_job(old.metadata.name, namespace, {})
    with open(template) as data:
        oribody = yaml.load(data)
    newentries = googlecalendar.get_events(timezone=timezone, days=days, patterns=patterns, before=before)
    for entry in newentries:
        name = entry[0].strip().lower()
        schedule = entry[1]
        location = entry[2]
        body = oribody
        body['metadata']['name'] = name
        body['spec']['schedule'] = schedule
        body['spec']['jobTemplate']['spec']['template']['spec']['containers'][0]['command'][1] = "@all %s %s" % (name, location)
        print("Creating cronjob %s" % name)
        cli.create_namespaced_scheduled_job(namespace, body)
