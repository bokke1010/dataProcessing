import base, dbInteraction

import pandas as pd
import matplotlib.pyplot

def plotYear(year, byCol: str):
    df = dbInteraction.compactLoad(year)
    # print("Dataframe loaded from cpSave:\n" + str(df))
    df.boxplot(column=["word_count"], by=byCol, rot=-90, figsize=(12,9), fontsize=9, showfliers = False)
    matplotlib.pyplot.show()

def plotYears(yearS, yearE, byCol: str):
    a = []
    for year in range(yearS, yearE+1):
        a.append(dbInteraction.compactLoad(year))
    df = pd.concat(a)
    # print("Dataframe loaded from cpSave:\n" + str(df))
    df.boxplot(column=["word_count"], by=byCol, rot=-90, figsize=(12,9), fontsize=9, showfliers = False)
    matplotlib.pyplot.show()
