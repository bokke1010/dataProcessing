import base

import pandas as pd
from pandas.io.json import json_normalize
import matplotlib.pyplot, os.path, json

ext: str = ".json"

def dbLoad(dates: list, strip: bool = False, cols: list = ["source", "document_type", "word_count", "type_of_material"]):

    base_path = base.getPath()

    df = []
    for date in dates:
        # try:
        file_path = os.path.join(base_path, date)
        # Read file
        with open(file_path + ext) as data_file:
            rData = json.load(data_file)

        fData = json_normalize(rData["response"]["docs"])

        if strip:
            fData = removeColumns(fData, cols)

        print("Dataframe " + date + " loaded succesfully")
        df.append(fData)
        # except:
        #     raise Warning("File " + date + ext + " couldn't be loaded")

    if len(df) > 0:
        dfComplete = pd.concat(df, sort=True)
        return dfComplete.reset_index()
    else:
        raise IndexError("No matching files found")

def getCompactCompletePath(year):
    return os.path.join(base.getPath('dbC'), str(year) + '.txt')

def compactSave(db: pd.DataFrame, year: int):
    print("saving data in a compactsave")
    filepathComplete = getCompactCompletePath(year)
    print(filepathComplete)
    file = open(filepathComplete, 'w')
    file.write(db.to_json())
    file.close()


def compactLoad(year: int):
    file = open( os.path.join(base.getPath('dbC'), year + '.txt'), 'r')
    text = file.readlines()
    return pd.read_json(text)
