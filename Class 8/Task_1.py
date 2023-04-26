class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def extract_date(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        return cls(day, month, year)

    @staticmethod
    def validate_date(date_string):
        day, month, year = map(int, date_string.split('-'))
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 1900:
            return True
        else:
            return False
date_string = '10-12-2021'
if Date.validate_date(date_string):
    date = Date.extract_date(date_string)
    print(date.day, date.month, date.year)
else:
    print('Invalid date format!')