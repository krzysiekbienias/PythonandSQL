import mysql.connector
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
from os import listdir
import os
from typing import List



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



if __name__ == "__main__":
    pass

