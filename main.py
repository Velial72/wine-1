import datetime
import pandas as pd
import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict


def get_winery_age(winery_age):
    if winery_age[-1] == '1':
        age = f'{winery_age} год'
    elif winery_age[-1] in '234':
        age = f'{winery_age} года'
    else:
        age = f'{winery_age} лет'
    return age

def get_wine_catalog(wine_cards_filepath):
    excel_data_df = pd.read_excel(wine_cards_filepath, sheet_name='Лист1', na_values='nan', keep_default_na=False)
    wines = excel_data_df.to_dict(orient='records')
    grouped_wine_cards = defaultdict(list)
    for wine in wines:
        grouped_wine_cards[wine['Категория']].append(wine)
    return grouped_wine_cards


def get_dir_path():
    parser = argparse.ArgumentParser(description='Запуск Сайта-магазина')
    parser.add_argument('-d', '--dir', help='Укажите путь к файлу с продукцией, по умолчанию wine.xlsx',
                        default='wine.xlsx')
    args = parser.parse_args()
    return args.dir
    

if __name__ == '__main__':
    year_of_foundation = 1920
    current_date = datetime.datetime.now()
    winery_age = str(current_date.year - year_of_foundation)
    correct_winery_age = get_winery_age(winery_age),
    wines_catalog = get_wine_catalog(get_dir_path())
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        wines_catalog=wines_catalog,
        winery_age=correct_winery_age,
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
