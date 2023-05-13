from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import pandas as pd
from pprint import pprint
import found_age

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

exel_data_df = pd.read_excel('wine2.xlsx')
types_of_wine = exel_data_df.to_dict(orient="records")
pprint(types_of_wine)

rendered_page = template.render(
    age_of_winery=found_age.age_winery(),
    types_of_wine=types_of_wine
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
