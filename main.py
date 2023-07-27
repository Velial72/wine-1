from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
import found_age
from collections import defaultdict

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')


def get_wine_catalog():
    exel_data_df = pd.read_excel('wine.xlsx')
    types_of_wine = exel_data_df.to_dict(orient="records")
    grouped_wine_cards = defaultdict(list)
    for wine in types_of_wine:
        grouped_wine_cards[wine['Категория']].append(wine)
    return grouped_wine_cards


rendered_page = template.render(
    winery_age=found_age.get_age_winery(),
    types_of_wine=get_wine_catalog()
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
