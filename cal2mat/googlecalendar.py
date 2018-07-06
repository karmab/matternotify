from __future__ import print_function
import httplib2
import os
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import datetime


SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
CLIENT_SECRET_FILE = 'secret.json'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


def get_credentials():
    calendarpath = os.environ['CALENDARPATH'] if 'CALENDARPATH' in os.environ else '.'
    credential_path = os.path.join('%s/calendar-python-quickstart.json' % calendarpath)
    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
        flow.user_agent = APPLICATION_NAME
        credentials = tools.run_flow(flow=flow, storage=store)
        print('Storing credentials to ' + credential_path)
    return credentials


def get_events(calendar='primary', count=20, timezone=None, days=1, patterns=[], before=0):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    service = discovery.build('calendar', 'v3', http=http)
    now = datetime.datetime.utcnow()
    today = now + datetime.timedelta(days=days)
    now = now.isoformat() + 'Z'
    today = today.isoformat() + 'Z'
    if calendar == 'primary':
        calendarid = calendar
    else:
        page_token = None
        calendar_list = service.calendarList().list(pageToken=page_token).execute()
        calendarid = [x['id'] for x in calendar_list['items'] if x['summary'] == calendar][0]
    eventsResult = service.events().list(
        calendarId=calendarid, timeZone=timezone, timeMin=now, timeMax=today, maxResults=count, singleEvents=True,
        orderBy='startTime').execute()
    events = eventsResult.get('items', [])

    results = []
    if events:
        for event in events:
            summary = event['summary']
            location = event.get('location', None)
            start = event['start'].get('dateTime', event['start'].get('date'))[:-6]
            try:
                start = datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S")
            except:
                print("Incorrect Date for Event %s.Skipping" % summary)
                continue
            start = start - datetime.timedelta(minutes=before)
            cron = start.strftime("%M %H %d %m *")
            if not patterns:
                results.append([summary, cron, location])
            else:
                for pattern in patterns:
                    if pattern in summary:
                        summary = summary.strip()
                        results.append([summary, cron, location])
    return results


if __name__ == '__main__':
    print(get_events(timezone='America/New_York', days=1, before=0))
