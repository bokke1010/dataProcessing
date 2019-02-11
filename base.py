import pandas as pd
import os.path

monthStrs = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

def dates(year: int, extended: bool = True, months: int = 12) -> list:
    rt = []
    for month in range(months):
        if extended:
            rt.append(str(year) + "-" + monthStrs[month])
        else:
            rt.append(str(year) + "-" + str(month+1))
    return rt

def getPath(folder: str = 'db'):
    # Get correct path
    current_directory = os.path.dirname(__file__)
    parent_directory = os.path.split(current_directory)[0]
    base_path = os.path.join(parent_directory, 'db', folder)
    # ^ Final argument is file name ^
    return base_path

def intify(dataframe, column: str):
    dataframe[column] = pd.to_numeric(dataframe[column])
    return dataframe

def removeColumns(data, cols):
    return data[cols]
