class Clock(object):
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __repr__(self):
        input_hours = str((self.hour + int(self.minute // 60)) % 24).rjust(2, '0')
        input_minutes = str(self.minute % 60).rjust(2, '0')
        return f"{input_hours}:{input_minutes}"

    def __eq__(self, other):
        input_hours = str((self.hour + int(self.minute // 60)) % 24).rjust(2, '0')
        input_minutes = str(self.minute % 60).rjust(2, '0')
        return other == f"{input_hours}:{input_minutes}"

    def __add__(self, minutes):
        input_hours = str((self.hour + int((self.minute + minutes)//60))%24).rjust(2, '0')
        input_minutes = str((self.minute + minutes) % 60 ).rjust(2, '0')
        return f"{input_hours}:{input_minutes}"

    def __sub__(self, minutes):
        return self.__add__(-minutes)
