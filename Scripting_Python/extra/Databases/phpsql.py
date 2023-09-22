'''import mysql.connector
cnx = mysql.connector.connect(user='boris', password='howest2022',database='biodb2')
cursor = cnx.cursor()
query = ("SELECT * FROM modorg")
cursor.execute(query)
cursor.close()
cnx.close()
'''

import MySQLdb
db = MySQLdb.connect(host="localhost",user="boris",passwd="howest2022",db="biodb2")
cur = db.cursor()
cur.execute("SELECT * FROM modorg")
db.close()
