from datetime import date, timedelta
import calendar

def meetup(year, month, week, day_of_week):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    days_in_month = calendar.monthrange(year, month)[1]
    ranges = {
        'teenth': range(13, 20),
        '1st': range(1, 8),
        '2nd': range(8, 15),
        '3rd': range(15, 22),
        '4th': range(22, 29),
        '5th': range(29, calendar.monthrange(year, month)[1] + 1),
        'last': range(days_in_month - 6, days_in_month + 1)
    }
    if month == 2 and week == '5th': 
        raise MeetupDayException('Only four weeks in Feb')
    for day in ranges[week]:
        if days[calendar.weekday(year, month, day)] == day_of_week:
            return date(year, month, day)
    
class MeetupDayException(Exception):
    def __init__(self, error_message):
        self.error_message = error_message



