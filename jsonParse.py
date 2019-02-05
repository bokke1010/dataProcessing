import dbInteraction, base
from multiprocessing import Process

def f(year):
    print("working on year: " + str(year) )
    yearData = dbInteraction.dbLoad(base.dates(year))
    print("collected data from database")
    # print("database is:\n" + str(yearData))
    dbInteraction.compactSave(yearData, year)

if __name__ == '__main__':
    years = (1905,1910)
    a = {}
    print("starting program")
    for year in range(years[0], years[1]):
        a[year] = Process(target=f, args=(year,))
        a[year].start()
