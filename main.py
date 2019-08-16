import mysql.connector
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
from os import listdir
import os
from typing import List

from kb_sql_class import SQLConnector,ExcelFilesDetails,CreateDataFrame


if __name__ == "__main__":
    dc_check = SQLConnector(as_index='order_id',
                            query='''select  order_id,
                              order_date,
                              first_name,
                              last_name,
                              name as status
                              from customers c
                              join orders o 
                              on o.customer_id=c.customer_id 
                              join order_statuses os
                              on o.status=os.order_status_id''')

    df_order = dc_check.execute_query()

    efd = ExcelFilesDetails(input_path=data_path, suffix='.xls')
    print(efd.mdic_files_and_tabs)

#####################################################################################################
    cdf = CreateDataFrame(file_name='to_paste.xls', sheet_name='murders')
    b_modify_before_insert=False #check value
    if b_modify_before_insert==True:
        dftoinsert = cdf.modify_columns_data_frame(columns_name='Company Name', l_fill_in='GOOG')
    else:
        dftoinsert=cdf.mdf
#####################################################################################################
    b_insert_ornor = True #check value
    if b_insert_ornor == True:
        dc_check.export_data_frame(dftoinsert, table_name='murders')

    dc_check.close_conection()
    print('The end of program')

