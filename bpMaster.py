import boxplot
from multiprocessing import Process

if __name__ == '__main__':
    years = (2013,2013)
    a = {}
    for year in range(years[0], years[1]):
        a[year] = Process(target=boxplot.plotYear, args=(year,))
        a[year].start()
        # boxplot.plotYear(year)
