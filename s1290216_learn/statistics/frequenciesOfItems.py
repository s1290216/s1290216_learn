import PAMI.extras.dbStats.transactionalDatabaseStats as tds

class frequenciesOfItems:
    def __init__(self, filename, separator = '\t'):
        obj = tds.transactionalDatabaseStats(filename, separator)
        obj.run()
        obj.printStats()
        obj.plotGraphs()
        itemsFrequenciesDictionary = None
        return itemsFrequenciesDictionary

if __name__ == '__main__':
    filename = input("Please input the file name: ")
    separator = input("Please input the separator: ")
    print(frequenciesOfItems(filename, separator))