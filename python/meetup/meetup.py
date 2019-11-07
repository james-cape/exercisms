from datetime import date, timedelta
import calendar

def meetup(year, month, week, day_of_week):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    if week == 'teenth':
        for i in range(13, 20):
            if days[calendar.weekday(year, month, i)] == day_of_week:
                return date(year, month, i)
    if week == '1st':
        for i in range(1, 8):
            if days[calendar.weekday(year, month, i)] == day_of_week:
                return date(year, month, i)
    if week == '2nd':
        for i in range(8, 15):
            if days[calendar.weekday(year, month, i)] == day_of_week:
                return date(year, month, i)
    if week == '3rd':
        for i in range(15, 22):
            if days[calendar.weekday(year, month, i)] == day_of_week:
                return date(year, month, i)
    if week == '4th':
        for i in range(22, 29):
            if days[calendar.weekday(year, month, i)] == day_of_week:
                return date(year, month, i)
    if week == 'last':
        # breakpoint()
        days_in_month = calendar.monthrange(year, month)[1]
        for i in range(days_in_month - 6, days_in_month + 1):
            if days[calendar.weekday(year, month, i)] == day_of_week:
                return date(year, month, i)
    if week == '5th':
        if month == 2:
            breakpoint()
            raise MeetupDayException
        else:
            for i in range(29, calendar.monthrange(year, month)[1] + 1):
                if days[calendar.weekday(year, month, i)] == day_of_week:
                    return date(year, month, i)


class MeetupDayException(Exception):
    pass
