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
        rData = None
        try:
            with open(file_path + ext) as data_file:
                rData = json.load(data_file)
        except:
            print("File " + date + " not loaded")
            break
        fData = json_normalize(rData["response"]["docs"])

        if strip:
            fData = fData[cols]
            # fData = base.removeColumns(fData, cols)

        print("Dataframe " + date + " loaded succesfully")
        fData['month'] = date
        df.append(fData)
        # except:
        #     raise Warning("File " + date + ext + " couldn't be loaded")

    if len(df) > 0:
        dfComplete = pd.concat(df, sort=True)
        return dfComplete.reset_index()
    else:
        print("ERROR")
        # raise Warning("No matching files found in dates " + str(dates) + "   " + ext)

def getCompactCompletePath(year):
    return os.path.join(base.getPath('dbC'), str(year) + '.txt')

def compactSave(db: pd.DataFrame, year: int):
    print("saving data in a compactsave")
    filepathComplete = getCompactCompletePath(year)
    db.to_csv(filepathComplete, index=None, sep=';', mode='w', header=True)

def compactLoad(year: int):
    db = pd.read_csv(getCompactCompletePath(year), sep=';', index_col=None)
    return db
