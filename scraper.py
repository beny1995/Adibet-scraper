# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib
import sys
import MySQLdb

reload(sys)
sys.setdefaultencoding('utf-8')
db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="",
                     db="adibet", use_unicode=True, charset='utf8')
cur = db.cursor()

r = urllib.urlopen('http://www.adibet.com/').read()
soup = BeautifulSoup(r,"html.parser")

data = []
cols=""
cols1=""
cols2=""
table = soup.find('table', attrs={'width':'620'})


#table_body = table.find('tbody')


rows = table.find_all('tr')
for row in rows:
    cols = row.find_all('td')

    for ele1 in cols:
     zz=ele1.text
     cols1+=zz+"|"
    for ele in cols:
      tt=ele.get("bgcolor")
      cols2+=tt+"|"
    insert_stmt = (
    "INSERT INTO stave(p1,p2) "
    "VALUES (%s, %s)"
    )
    data = (cols1, cols2)
    cur.execute(insert_stmt, data)
    print (cols1)
    print (cols2)
    cols1=""
    cols2=""
    print ("----------------------")

db.commit()

