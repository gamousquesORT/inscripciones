# create a class to read an excel file
import pandas as pd


class ExcelReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_and_display(self):
        data = pd.read_excel(self.file_path)
        for index, row in data.iterrows():
            print(row[index])
            #for cell in row:
            #    print(cell)

reader = ExcelReader('./inscripciones.xlsx')
reader.read_and_display()

