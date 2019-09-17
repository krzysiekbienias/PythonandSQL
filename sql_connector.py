import mysql.connector
import numpy as np
import pandas as pd
import pymysql
import sqlalchemy



def create_df_from_query(data_base_name,as_index):
    db_connection=mysql.connector.connect(host="127.0.0.1",
                 user="root",
                 passwd="Numeraire2019",
                 database=data_base_name)

    s_query='''select  order_id,
                order_date,
                
                first_name,
                last_name,
                name as status
                
                
                from customers c
                join orders o 
                on o.customer_id=c.customer_id 
                join order_statuses os
                on o.status=os.order_status_id'''

    db_cursor=db_connection.cursor()
    db_cursor.execute(s_query)

    db_cursor.fetchall()
    converted_df=pd.read_sql(s_query,con=db_connection)


    db_connection.close()
    return final_df

df_custom=create_df_from_query(data_base_name='sql_store',
                               as_index='order_id')
np.random.seed(0)
df_toimport=pd.DataFrame({'x1':np.random.random(10),'x2':np.random.random(10)})



data_base_name='sql_store'
db_connection=mysql.connector.connect(host="127.0.0.1",
                 user="root",
                 passwd="Numeraire2019",
                 database=data_base_name)


engine = sqlalchemy.create_engine('mysql+pymysql://root:Numeraire2019@127.0.0.1:3306/sql_store')#at the end we put name of db
df_toimport.to_sql(name='test3',con=engine,index=True,if_exists='append')
print('aa')