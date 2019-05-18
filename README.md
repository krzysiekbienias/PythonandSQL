# PythonandSQL

Here I present how to create data frame from SQl table and also how to insert data to SQL server. The project contains following class 

### class SQLConnector():

__atributes__: 
* _as_index (str)
* _query (str)

__methods__:
* def set_connection_details(self):
* def execute_query(self) -> pd.DataFrame:
* def export_data_frame(self, data_frame: pd.DataFrame, table_name: str)->pd.DataFrame:
* def close_conection(self):

