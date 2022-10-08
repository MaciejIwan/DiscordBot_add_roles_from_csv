import pandas.core.frame
from pandas import read_csv


class CSV:

    def __init__(self, filename):
        self.filename = filename
        self.data = None

    def load_data_from_file(self):
        data: pandas.DataFrame = read_csv(
            '../lista.csv',
            header=0,
            dtype={"discordID": "string", "spec": "string", "index": "string", "name": "string", "surname": "string"}
        )
        self.data = data.values[1:]

    def print_all(self):
        for row in self.data:
            print(', '.join(row))


if __name__ == "__main__":
    CSV = CSV("../lista.csv")
    CSV.load_data_from_file()
    for row in CSV.data:
        print(row)
