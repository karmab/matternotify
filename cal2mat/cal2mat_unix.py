#!/usr/bin/env python3

import os
import googlecalendar
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

days = int(os.environ['DAYS']) if 'DAYS' in os.environ else 3
before = int(os.environ['BEFORE']) if 'BEFORE' in os.environ else 3
timezone = os.environ['TZ'] if 'TZ' in os.environ else 'Europe/Madrid'
exe = os.environ['EXE'] if 'EXE' in os.environ else 'notify.sh'

if __name__ == "__main__":
    if 'PATTERNS' not in os.environ:
        print("Missing patterns.Leaving...")
        os._exit(1)
    else:
        patterns = os.environ['PATTERNS'].split(',')
    newentries = googlecalendar.get_events(timezone=timezone, days=days, patterns=patterns, before=before)
    for index, entry in enumerate(newentries):
        info = entry[0].strip().lower()
        schedule = entry[1]
        location = entry[2] if entry[2] is not None else ''
        schedule = schedule
        command = "@here %s %s" % (info, location)
        print("%s %s %s" % (schedule, exe, command))
