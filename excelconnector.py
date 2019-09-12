import mysql.connector
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
from os import listdir
import os
from typing import List


class ExcelFilesDetails():
    def __init__(self, input_path, suffix):
        self._input_path = input_path
        self._suffix = suffix
        self.mls_whole_name = self.long_excel_filenames()
        self.mls_short_names = self.short_excel_filenames()
        self.mls_tab_names = self.get_tab_excel_list()
        self.mdic_files_and_tabs = self.create_dictionary()

    def long_excel_filenames(self):
        return list(filter(lambda x: self._suffix in x, os.listdir(self._input_path)))

    def short_excel_filenames(self):
        ls_whole_names = list(filter(lambda x: self._suffix in x, os.listdir(self._input_path)))
        ls_short_names = []
        for i in range(len(ls_whole_names)):
            s_temp = ls_whole_names[i]
            s_ticker = s_temp[:-4]
            ls_short_names.append(s_ticker)
        return ls_short_names

    def get_tab_excel_list(self):
        tab_list = []
        for i in range(len(self.mls_whole_name)):
            xlsx = pd.ExcelFile(self.mls_whole_name[i])
            ls_file_sheets = xlsx.sheet_names
            tab_list.append(ls_file_sheets)
        return tab_list

    def create_dictionary(self):
        files_names_and_tabs = dict(zip(self.mls_short_names, self.mls_tab_names))
        return files_names_and_tabs


class CreateDataFrame:
    def __init__(self, file_name: str, sheet_name: str, set_index=None):
        self._file_name = file_name
        self._sheet_name = sheet_name
        self._set_index = set_index
        self.mdf = self.create_data_frame_from_excel()

    def create_data_frame_from_excel(self):
        df_from_excel = pd.read_excel(self._file_name, sheet_name=self._sheet_name)
        if self._set_index != None:
            df_from_excel = pd.read_excel(self._file_name, sheet_name=self._sheet_name)
            return df_from_excel.set_index(self._set_index)
        else:
            return df_from_excel

    def get_columns(self):
        return self.mdf.columns

    def get_dimension(self):
        return self.mdf.shape

    def modify_columns_data_frame(self, columns_name: str,
                                  l_fill_in: str) -> pd.DataFrame:  # TODO expand possibility to remove columns, the same with rows
        base_data_frame = self.mdf
        new_col = [l_fill_in] * len(base_data_frame)
        base_data_frame[columns_name] = new_col
        modified_df = base_data_frame
        return modified_df

class OutputInExcel:
    def __init__(self,sFileName,sSheetName,sPath):
        self._sFileName=sFileName
        self._sSheetName=sSheetName
        self._sPath=sPath

    def createResultsToPresent(self,dfToSave,formatStyle,colRange=None)->None:
        oDataToExcel=pd.ExcelWriter(self._sFileName,self._sSheetName,engine='xlsxwriter')
        dfToSave.to_excel(oDataToExcel,sheet_name=self._sSheetName)
        workbook=oDataToExcel.book
        worksheet=oDataToExcel.sheets[self._sSheetName]
        if(formatStyle=='percentage'):
            fixedFormat=workbook.add_format({'num_format':'0%'})
            worksheet.set_column(colRange,None,fixedFormat)
        oDataToExcel.save()
        if (formatStyle == 'CommaFormat'):
            fixedFormat = workbook.add_format({'num_format': '#,##0.00%'})
            worksheet.set_column(colRange, None, fixedFormat)
        oDataToExcel.save()



if __name__ == "__main__":
    pass
