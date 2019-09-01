import mysql.connector
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy
from os import listdir
import os
from typing import List
from six import string_types


class SQLConnector():
    def __init__(self):
        self.m_connection_details = self.set_connection_details()
        self.m_db_cursor = self.m_connection_details.cursor()
        # self.mdf_from_query = self.execute_query()
        self.engine = sqlalchemy.create_engine('mysql+pymysql://root:Numeraire2019@127.0.0.1:3306/sql_store')
        self.df = self.testQuery(date='2014-05-19')

    def set_connection_details(self):
        return mysql.connector.connect(host="127.0.0.1",
                                       user="root",
                                       passwd="Numeraire2019",
                                       database='sql_store')

    def quote_sql_string(self, value):
        '''
        If `value` is a string type, escapes single quotes in the string
        and returns the string enclosed in single quotes.
        '''
        if isinstance(value, string_types):
            new_value = str(value)
            new_value = new_value.replace("'", "''")
            return "'{}'".format(new_value)
        return value

    def testQuery(self, date=None):  # example of dynamic query with fstrings
        query = f'''SELECT * FROM sql_store.usd3mlibor
                where observation_date='{date}' '''
        df = pd.read_sql(query, con=self.m_connection_details)
        return df

    def export_data_frame(self, data_frame: pd.DataFrame, table_name: str) -> pd.DataFrame:
        return data_frame.to_sql(name=table_name, con=self.engine, index=True, if_exists='append')

    def close_conection(self):
        self.m_connection_details.close()


if __name__ == "__main__":
    pass
