# need to run "pip install cx_Oracle"
import cx_Oracle
import logging
import pandas as pd

class DbSession:
    def __init__(self, host, username, password, port='1521', service='stat4p'):
        logging.basicConfig(filename='logger.log', level=logging.DEBUG, format='%(asctime)s %(message)s')
        dsn_tns = cx_Oracle.makedsn(host, port, service)
        self.host = host
        try:
            self.connection = cx_Oracle.connect(username, password, dsn_tns)
            self.cur = self.connection.cursor()
            logging.error("Connection to "+host+" Created successfully")
        except cx_Oracle.DatabaseError as e:
            logging.error("There is a problem with Oracle", e)

    def launch_query(self,query):
        self.cur.execute(query)
        return self.cur.fetchall()

    def export_from_query(self, query,export_name):
        df_ora = pd.read_sql(query, con=self.connection)
        print(df_ora)
        df_ora.to_csv(export_name)

    def df_from_query(self, query):
        df = pd.read_sql(query, con=self.connection)
        return df

    def close(self):
        self.connection.close()
        logging.error("Connection to "+self.host+" closed successfully")
