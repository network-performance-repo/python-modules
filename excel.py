import pandas as pd
from openpyxl import load_workbook

class File:
    def __init__(self, dataframe, filename,  sheetname='sheet1'):
        self.excel_file = filename
        self.data = dataframe
        sheet_name = sheetname
        self.writer = pd.ExcelWriter(self.excel_file, engine='xlsxwriter')
        self.data.to_excel(self.writer, sheet_name=sheet_name, startrow=1, header=self.data.columns)
        self.workbook = self.writer.book
        self.worksheet = self.writer.sheets[sheet_name]
        self.save()

    def save(self):
        self.writer.save()

def append_sheet(df, file_name, sheetname):
        book = load_workbook(file_name)
        writer = pd.ExcelWriter(file_name, engine='openpyxl')
        writer.book = book
        df.to_excel(writer, sheet_name=sheetname, index=False)
        writer.save()
