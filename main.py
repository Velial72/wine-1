import datetime
import pandas as pd
import argparse

from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict

import found_age


def get_wine_catalog():
    exel_data_df = pd.read_excel('wine.xlsx')
    types_of_wine = exel_data_df.to_dict(orient="records")
    grouped_wine_cards = defaultdict(list)
    for wine in types_of_wine:
        grouped_wine_cards[wine['Категория']].append(wine)
    return grouped_wine_cards

def get_dir_path():
    parser = argparse.ArgumentParser(description='Запуск Сайта-магазина')
    parser.add_argument('-d', '--dir', help='Укажите путь к файлу с продукцией, по умолчанию wine_catalog.xlsx',
                        default='wine_catalog.xlsx')
    args = parser.parse_args()
    return args.dir
    

if __name__ == '__main__':

    year_of_opening = 1920
    winery_age = found_age.get_age_winery(),
    correct_year_name = found_age.get_age_winery()
    wines_catalog = get_wine_catalog(get_dir_path())
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    rendered_page = template.render(
        wines_catalog=wines_catalog,
        winery_age=winery_age,
        correct_year_name=correct_year_name,
    )
    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
