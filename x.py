import collections

import pandas as pd
from pprint import pprint


exel_data_df = pd.read_excel('wine2.xlsx')
types_of_wine = exel_data_df.to_dict(orient="records")
print(collections.defaultdict(exel_data_df))