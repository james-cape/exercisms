class Luhn(object):
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")[::-1]

    def valid(self):
        if len(self.card_num) <= 1 or not self.card_num.isnumeric():
            return False
        else:
            accumulator = 0
            for i in range(len(self.card_num)):
                if i % 2 == 1:
                    doubled = int(self.card_num[i]) * 2
                    if doubled > 9:
                        doubled = doubled - 9
                    accumulator += doubled
                else:
                    accumulator += int(self.card_num[i])
            if accumulator % 10 == 0:
                return True
            else:
                return False
