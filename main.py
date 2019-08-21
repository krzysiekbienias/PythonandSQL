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

    data_path = '/Users/krzysiekbienias/Documents/ExcelDataStore/GenericStore'

    os.chdir(data_path)
    excel_details = ExcelFilesDetails(input_path=data_path, suffix='.xls')

    dc_check.close_conection()
    print('The end of program')
