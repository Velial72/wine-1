import datetime


current_year = datetime.datetime.now()
age_of_winery = str(current_year.year - 1920)


def age_winery():
    if age_of_winery[-1] == '1':
        age = f'{age_of_winery} год'
    elif age_of_winery[-1] in '234':
        age = f'{age_of_winery} года'
    else:
        age = f'{age_of_winery} лет'
    return age