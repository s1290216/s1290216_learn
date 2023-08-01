import PAMI.extras.dbStats.transactionalDatabaseStats as tds

class frequenciesOfItems:
    def __init__(self, filename, separator = '\t'):
        self.filename = filename
        self.separator = separator
    
    def frequency(self):
        obj = tds.transactionalDatabaseStats(self.filename, self.separator)
        obj.run()
        return obj.getSortedListOfItemFrequencies()

if __name__ == '__main__':
    filename = input("Please input the file name: ")
    separator = input("Please input the separator: ")
    print(frequenciesOfItems(filename, separator).frequency())