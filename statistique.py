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
        i = i + 1
        x = '''SELECT age  FROM python_test  WHERE id = '1';'''
        y = '''SELECT age  FROM python_test  WHERE id = '2';'''
        cur1.execute(x)
        reponse_query1 = cur1.fetchall()
        cur2.execute(y)
        reponse_query2 = cur2.fetchall()
        print(reponse_query1)
        print(reponse_query2)
        print(reponse_query1[0][0])
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
