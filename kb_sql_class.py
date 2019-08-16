import mysql.connector
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
from os import listdir
import os
from typing import List

data_path = '/Users/krzysiekbienias/Documents/ExcelDataStore/GenericStore'

os.chdir(data_path)


class SQLConnector():
    def __init__(self,query, as_index=None):
        self._as_index = as_index
        self._query = query
        self.m_connection_details = self.set_connection_details()
        self.m_db_cursor = self.m_connection_details.cursor()
        self.mdf_from_query = self.execute_query()
        self.engine = sqlalchemy.create_engine('mysql+pymysql://root:Numeraire2019@127.0.0.1:3306/sql_store')

    def set_connection_details(self):
        return mysql.connector.connect(host="127.0.0.1",
                                       user="root",
                                       passwd="Numeraire2019",
                                       database='sql_store')

    def execute_query(self) -> pd.DataFrame:
        self.m_db_cursor.execute(self._query)
        self.m_db_cursor.fetchall()
        converted_df = pd.read_sql(self._query, con=self.m_connection_details)
        if self._as_index!=None:
            final_df = converted_df.set_index(self._as_index)
        else:
            final_df=converted_df
        return final_df

    def export_data_frame(self, data_frame: pd.DataFrame, table_name: str) -> pd.DataFrame:
        return data_frame.to_sql(name=table_name, con=self.engine, index=True, if_exists='append')

    def close_conection(self):
        self.m_connection_details.close()


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

    def modify_columns_data_frame(self,columns_name:str,l_fill_in:str)->pd.DataFrame: #TODO expand possibility to remove columns, the same with rows
        base_data_frame=self.mdf
        new_col=[l_fill_in]*len(base_data_frame)
        base_data_frame[columns_name]=new_col
        modified_df=base_data_frame
        return modified_df


if __name__ == "__main__":
    pass

