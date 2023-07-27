import datetime


current_date = datetime.datetime.now()
winery_age = str(current_date.year - 1920)


def get_winery_age():
    if winery_age[-1] == '1':
        age = f'{winery_age} год'
    elif winery_age[-1] in '234':
        age = f'{winery_age} года'
    else:
        age = f'{winery_age} лет'
    return age
