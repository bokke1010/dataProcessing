import base

import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot, os.path, json

months = 12

def plotYear(year):
    dates = base.dates(year,months)
    df = base.readFiles(dates, True)
    df = base.intify(df, "word_count")
    df.boxplot(column=["word_count"], by="type_of_material", rot=-90, figsize=(12,9), fontsize=9)
    matplotlib.pyplot.show()
