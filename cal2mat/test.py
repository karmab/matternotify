#!/bin/bash

import yaml
from kubernetes import client, config
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

namespace = 'matternotify'
cronmaster = 'cal2mat'
timezone = 'America/New_York'

if __name__ == "__main__":
    config.load_kube_config()
    template = "crontemplate.yml"
    cli = client.BatchV2alpha1Api()
    # cli = client.BatchV1beta1Api()
    with open(template) as data:
        oribody = yaml.load(data)
    cli.create_namespaced_cron_job(namespace, oribody)
