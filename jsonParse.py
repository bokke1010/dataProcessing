import dbInteraction, base, multiprocessing
from multiprocessing import Process, Pool


def f(year):
    print("working on year: " + str(year) )
    yearData = dbInteraction.dbLoad(base.dates(year), strip = True)
    print("collected data from database")
    # print(yearData)
    # if not yearData == None:
    dbInteraction.compactSave(yearData, year)
    # else:
    #     print("Year " + str(year) + " not read succesfully")

if __name__ == '__main__':
    years = (1851,2018)
    a = {}
    print("starting program")
    pool = Pool(processes=14)
    print(pool.map(f, range(years[0], years[1]+1)))
