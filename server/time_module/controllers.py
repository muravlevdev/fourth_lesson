from datetime import datetime


def get_time():
    date = datetime.now()
    return date.strftime('%d-%m-%yT%H:%M:%S')
