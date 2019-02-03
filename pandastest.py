import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot, os.path, json

year = 1950
months = 12
ext = ".json"

dates = []
for month in range(months):
    dates.append(str(year) + "-" + str(month))


# Get correct path
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
base_path = os.path.join(parent_directory, 'db', 'db')
# ^ Final argument is file name ^

df = []

for date in dates:
    try:
        file_path = os.path.join(base_path, date)
        # Read file
        with open(file_path + ext) as data_file:
            data = json.load(data_file)
        df.append(json_normalize(data["response"]["docs"]))

    except:
        pass
    try:
        pass
        # df[date].boxplot(column="word_count",by="pub_date")
    except KeyError:
        pass

tst = pd.concat(df)
tst["word_count"] = pd.to_numeric(tst["word_count"])
tst.boxplot(column=["word_count"], by="type_of_material", rot=-90, figsize=(12,9), fontsize=9)

matplotlib.pyplot.show()
