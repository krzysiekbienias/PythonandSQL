import mysql.connector
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
from os import listdir
import os
from typing import List

from kb_sql_class import SQLConnector

from excelconnector import ExcelFilesDetails, CreateDataFrame

if __name__ == "__main__":
    dc_check = SQLConnector()

    data_path = '/Users/krzysiekbienias/Documents/ExcelDataStore/EquityPortfolio'

    os.chdir(data_path)
    excel_details = ExcelFilesDetails(input_path=data_path, suffix='.xls')
    print(f'W have the following Excel Files {excel_details.long_excel_filenames()}')

    #In rows we have files and cells are tabs
    print(f'We have following Excel Files and tabs in this location \n{excel_details.dataFrameSumary()}')

    controlPath = '/Users/krzysiekbienias/Downloads/ControlFiles'
    os.chdir(controlPath)

    loadControlFile = CreateDataFrame(file_name='BlackScholes.xlsx')

    dc_check.close_conection()
    print('The end of program')
