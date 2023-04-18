#!/usr/bin/python
import datetime
import psycopg2
from config import config
def connect():
 conn = None
 try:
    for i in range(1):
        params = config()
        conn = psycopg2.connect(**params)
        cur1 = conn.cursor()
        cur2 = conn.cursor()

        x = '''SELECT last_autoanalyze FROM pg_stat_all_tables WHERE relname = 'test3';   '''
        y = '''SELECT  last_analyze FROM pg_stat_all_tables WHERE relname = 'test3';   '''
        cur1.execute(x)
        reponse_query1 = cur1.fetchall()
        cur2.execute(y)
        reponse_query2 = cur2.fetchall()
        last_autoanalyze=reponse_query1[0][0]
        last_analyze=reponse_query2[0][0]
        print(last_autoanalyze)
        print(last_analyze)
        cur1.close()
        cur2.close()
 except (Exception, psycopg2.DatabaseError) as error:
  print(error)
 finally:

    if conn is not None:
       conn.close()
       print('Database connection closed.')
if __name__ == '__main__':
 connect()