#-*- coding: utf-8 -*-
import urllib
import re
import sys
import datetime
import time
import sqlite3 as lite

def bggBaza():
 con=lite.connect('bgg.db')
 cur=con.cursor()
 cur.execute('select sqlite_version()')
 data=cur.fetchone()
 print str(data) 

def bggTop100():
 plik=open('bggTop100.html','w')
 strona = urllib.urlopen('http://boardgamegeek.com/browse/boardgame')
 plik.write(strona.read())
 plik.close()
 aaa=0
 miejsce=0
 print "BGG Top 100"
 f=open('bggTop100.html','r')
 for line in f.readlines():
  if aaa==2:
   d=re.search('>[a-zA-Z0-9(): ]*',line)
   print str(miejsce)+" " + d.group()[1:]
   aaa=0 
  if aaa==1:
   aaa=2
  b=re.search('results_objectname[1234567890]*',line)
  if b:
   aaa=1
   miejsce=miejsce+1
 f.close()



bggTop100()
bggBaza()

