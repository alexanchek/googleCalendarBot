from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import datetime
import dateutil.parser


# работа с google calendar API
def upcomingEvents():
    scopes = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file("client_secrets.json", scopes=scopes)

    credentials = pickle.load(open("token.pkl", "rb"))
    print(credentials)

    service = build("calendar", "v3", credentials=credentials)

    now = datetime.datetime.utcnow() - datetime.timedelta(hours=8.5) # вычитаем 8 часов, стартовая граница дня
    now = now.isoformat() + 'Z'
    endDay = datetime.datetime.now() + datetime.timedelta(hours=15.5) # прибавляем до финальной граниы дня
    endDay = endDay.isoformat() + 'Z'

    # показываем события на сегодняшний день
    events_result = service.events().list(calendarId='primary', timeMin=now, timeMax=endDay,
                                          singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])
    msg = '<b>События на ближайшие дни:</b>\n'
    if not events:
        msg = msg + 'На сегодня пока ничего, босс!'
    else:
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))

            # кусок не работает почему-то
            # if not event['description']:
            #     print('нет описания')
            #     ev_desc = 'нет описания'
            # else:
            #     print(event['description'])
            #     ev_desc = event['description']

            ev_title = event['summary']
            cal_link = '<a href="%s">Подробнее...</a>' % event['htmlLink']
            # берем дату
            ev_start = event['start'].get('dateTime')
            # превращаем в удобоваримый формат день-месяц-год и время
            ev_start = dateutil.parser.parse(ev_start).strftime("%d.%m.%Y %H:%M")
            hr_line = '========================================================'
            # собираем все воедино
            msg = msg + '%s\n%s\n%s\n%s\n\n' % (ev_title, ev_start, cal_link, hr_line)
    return msg
