#!/usr/bin/python
import psycopg2
from config import config
def connect():
 conn = None
 try:
    for i in range(3):
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        i = i + 1
        x = 'select * from python_test where id ='+str(i)
        cur.execute(x)
        reponse_query = cur.fetchall()

        print(type(reponse_query))
        print(reponse_query)
        cur.close()
 except (Exception, psycopg2.DatabaseError) as error:
  print(error)
 finally:

    if conn is not None:
       conn.close()
       print('Database connection closed.')
if __name__ == '__main__':
 connect()
