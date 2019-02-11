import dbInteraction, base
from multiprocessing import Process

def f(year):
    print("working on year: " + str(year) )
    # , cols = ["word_count","type_of_material"]
    yearData = dbInteraction.dbLoad(base.dates(year), strip = True)
    # print("data from year " + str(year) + " is:\n" + str(yearData))
    print("collected data from database")
    dbInteraction.compactSave(yearData, year)

if __name__ == '__main__':
    years = (2007,2012)
    a = {}
    print("starting program")
    for year in range(years[0], years[1]):
        a[year] = Process(target=f, args=(year,))
        a[year].start()
