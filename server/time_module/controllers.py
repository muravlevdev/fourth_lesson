from datetime import datetime


def get_time(data):
    date = datetime.now()
    return date.strftime('%d-%m-%yT%H:%M:%S')
