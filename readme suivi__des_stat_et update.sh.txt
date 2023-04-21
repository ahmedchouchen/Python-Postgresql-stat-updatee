exercice : Python/git/GitHub/Postgresql
un program en python  cappable de :

1- se connecter  au serveur Postgresql
2- connecter a une base de donées "test"
3- voir l'etat de mise a jour des statistiques sur une table exemple :[(2023-04-18 21:31:37.574995+01),] ==>etape1: lire element de list ==>etape2: convert to string  ==>etape3: convert to integer
   ==>etape4: faire la comparaison entre last_autoanalyze and current_time

4- il vous informe si les statistique sont à jour ou non [conditions]
5- si les statistiques ne sont pas à jour il donne le choix à l'utilisateur de faire ou non  les mise a jour (y/n)
6- en cas ou l'utilisateur accepte de mettre à jour les statistique (y) alors ==> une ANALYZE sera lancer automatiquement

7- enfin les statistiques sont à jour   et les dates des mise  àjour sont last_autoanalyze et last_analyze sont afficher 



exercice suivant (en cours : utilisation de Jenkins + Webhook pour automatiser  toutes les etapes de l'exercice suivant )