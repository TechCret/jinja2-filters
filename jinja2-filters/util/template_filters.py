import datetime

from dateutil.relativedelta import relativedelta


def calculate_date_date(date_str, format_str):
    start_date = datetime.datetime.strptime(date_str, format_str)
    print('date', start_date)
    return relativedelta(datetime.datetime.now(), start_date).years
