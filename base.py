import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot, os.path, json

ext: str = ".json"

def dates(year: int, months: int = 12) -> list:
    rt = []
    for month in range(months):
        rt.append(str(year) + "-" + str(month+1))
    return rt

def readFiles(dates: list, strip: bool = False, cols: list = ["source", "document_type", "word_count", "type_of_material"]):

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
                rData = json.load(data_file)

            fData = json_normalize(rData["response"]["docs"])

            if strip:
                fData = removeColumns(fData, cols)

            df.append(fData)
        except:
            raise Warning("File " + date + ext + " does not exist")

    if len(df) > 0:
        return pd.concat(df)
    else:
        raise IndexError("No matching files found")

def intify(dataframe, column: str):
    dataframe[column] = pd.to_numeric(dataframe[column])
    return dataframe

def removeColumns(data, cols):
    return data[cols]
