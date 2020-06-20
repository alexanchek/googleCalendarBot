from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import datetime
import dateutil.parser

def upcomingEvents():
    scopes = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", scopes=scopes)

    credentials = pickle.load(open("token.pkl", "rb"))
    print(credentials)

    service = build("calendar", "v3", credentials=credentials)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    msg = '<b>События на ближайшие дни:</b>\n'
    if not events:
        msg = msg + 'тут пока ничего нет, хех'
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            # if not event['description']:
            #     print('нет описания')
            #     ev_desc = 'нет описания'
            # else:
            #     print(event['description'])
            #     ev_desc = event['description']

            ev_title = event['summary']
            cal_link = '<a href="%s">Подробнее...</a>' % event['htmlLink']
            ev_start = event['start'].get('dateTime')
            ev_start = dateutil.parser.parse(ev_start).strftime("%d.%m.%Y %H:%M")
            hr_line = '========================================================'
            msg = msg + '%s\n%s\n%s\n%s\n\n' % (ev_title, ev_start, cal_link, hr_line)
    return msg


