########################################################################################################################
# test de mise à jour  des statistiques sur une table
# Auteur  : ACH
# Date    : 18/04/2023
# Version : 0.5
# Modication :
#  ACH 15/04/2023 :  lecture des statistiques de la table
#  ACH 16/04/2023 :  lecture des valeur des  tuples
#  ACH 17/04/2023 :  convertir timestamp to string
#  ACH 18/04/2022 :  convertir le string to integer
#  ACH 18/04/2022 :  faire la difference entre les deux nombres  sachant que 86400 en second represent le nb de s/jour
########################################################################################################################

from datetime import datetime
now = now=datetime.now()
import psycopg2
from config import config
from datetime import datetime
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
        print("the time of last_autoanalyze is : ")
        print(last_autoanalyze)
        print("the time of last_analyze is : ")
        print(last_analyze)
        print("the time on the server now  is : ")
        print(now)
        time_last_autoanalyze=last_autoanalyze.strftime("%Y")+last_autoanalyze.strftime("%m")+last_autoanalyze.strftime("%d")+last_autoanalyze.strftime("%H%M%S")
        time_last_analyze=last_analyze.strftime("%Y")+last_analyze.strftime("%m")+last_analyze.strftime("%d")+last_analyze.strftime("%H%M%S")
        time_now=now.strftime("%Y")+now.strftime("%m")+now.strftime("%d")+now.strftime("%H%M%S")
        print(time_last_autoanalyze)
        print(time_last_analyze)
        print(time_now)
        diff_time=(int(time_now))-(int(time_last_autoanalyze))
        print(diff_time)

        if diff_time < 8640 :
            print("the statistic on your table is updated  ")
        else:
            print("the statistic on your table is not updated  ")
            reponse=input("do you want to update  the statistic on the table y/n  \n")
            print("1 reponse est : " + str(reponse))

            while  reponse !='y' and  reponse !='n' :
                    reponse = input("choix invalide : please taper  y or n ")
                    print("reposnse est : "+str(reponse))
            if reponse == 'y':
                           cur3 = conn.cursor()
                           update_stat='''analyze test3;'''
                           print("your stat on  table  test3 is updating now ..... please wait ")
                           cur3.execute(update_stat)
            else :
                           print(" attention :you choose to not update the statistic on your table test3  ")

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