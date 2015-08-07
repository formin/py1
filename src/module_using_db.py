#coding=utf-8 ~

import sys, csv, sqlite3
import codecs, os

def iteminfoDB(DBName, TSVName):
    con = sqlite3.connect(DBName) # database file input
    #t1 : 영화 컨텐츠 정보, COL1 컨텐츠, COL2 감독, COL3 출연자, COL4 장르
    cur = con.cursor()

    cur.executescript("""
       DROP TABLE IF EXISTS t1;
       CREATE TABLE t1 (COL1 TEXT, COL2 TEXT, COL3 TEXT, COL4 TEXT);
       CREATE INDEX t1_index ON t1 (COL1, COL2, COL3, COL4);
       """) # checks to see if table exists and makes a fresh table.

    with open(TSVName, "rb") as f: # CSV file input
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE) # no header information with delimiter

        for row in reader:
            if row[3] == 'MOV':
                #to_db = [row[0],row[9],row[10],row[11]]
                #print repr(to_db).decode('string-escape')
                to_db = [row[0], unicode(row[9], "utf8"), unicode(row[10], "utf8"), unicode(row[11], "utf8")]
                cur.execute("INSERT INTO t1 (COL1,COL2,COL3,COL4) VALUES (?,?,?,?)", to_db)

    con.commit()
    con.close() # closes connection to database


def purchaseRecordDB(DBName, TSVName):
    con = sqlite3.connect(DBName) # database file input
    #t2 : 영화 구매 정보 COL1 구매자, COL2 컨텐츠
    cur = con.cursor()
    cur.executescript("""
       DROP TABLE IF EXISTS t2;
       CREATE TABLE t2 (COL1 INTEGER, COL2 TEXT);
       CREATE INDEX t2_index ON t2 (COL1, COL2);
       """) # checks to see if table exists and makes a fresh table.

    with open(TSVName, "rb") as f: # CSV file input
        reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE) # no header information with delimiter

        for row in reader:
                to_db = [row[0], row[2]]
                cur.execute("INSERT INTO t2 (COL1, COL2) VALUES (?,?)", to_db)

    con.commit()
    con.close() # closes connection to database

def SortUser(DBName):
    con = sqlite3.connect(DBName) # database file input
    cur = con.cursor()
    #t4 : 전체 사용자 리스트 COL1 구매자
    cur.executescript("""
       DROP TABLE IF EXISTS t4;
       CREATE TABLE t4 (COL1 INTEGER);
       CREATE INDEX t4_index ON t4 (COL1);
       insert into t4 (col1) select COL1 from t2 group by COL1;
       """) # checks to see if table exists and makes a fresh table.

    con.commit()
    con.close() # closes connection to database

def SortPurchaseRecord1(DBName):
    con = sqlite3.connect(DBName) # database file input
    cur = con.cursor()
    #t2: 영화 이외의 구매 이력 삭제
    cur.executescript("""
       delete from t2 where COL2 in (select t2.COL2 from t2 left join t1 on t1.COL1 = t2.COL2 where ifnull(t1.COL1,'') = '');
       """) # checks to see if table exists and makes a fresh table.

    con.commit()
    con.close() # closes connection to database

def SortPurchaseRecord2(DBName):
    con = sqlite3.connect(DBName) # database file input
    cur = con.cursor()
    #t3: 영화 구매이력 많은 순서로 랭킹 COL1 구매자, COL2 컨텐츠
    cur.executescript("""
       DROP TABLE IF EXISTS t3;
       CREATE TABLE t3 (COL1 INTEGER, COL2 TEXT);
       CREATE INDEX t3_index ON t3 (COL1, COL2);
       insert into t3 (col1, col2) select count(COL2), COL2 from t2 group by COL2 order by count(COL2) desc;
       """) # checks to see if table exists and makes a fresh table.

    con.commit()
    con.close() # closes connection to database

def SortPurchaseRecord3(DBName):
    con = sqlite3.connect(DBName) # database file input
    cur = con.cursor()
    #t5: 사용자가 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠
    cur.executescript("""
       DROP TABLE IF EXISTS t5;
       CREATE TABLE t5 (COL1 INTEGER, COL2 TEXT, COL3 INTEGER);
       CREATE INDEX t5_index ON t5 (COL1, COL2, COL3);
       """) # checks to see if table exists and makes a fresh table.

    cur.execute("SELECT col1 As TEXT FROM t4")
    rowst4 = cur.fetchall()

    for rowt4 in rowst4:
      rows4Value = str(rowt4[0])
      cur.execute("insert into t5 (col1, col2, col3) select '"+rows4Value+"', t3.COL2, t3.COL1 from t3 left join t2 on t2.COL2 = t3.COL2 and t2.COL1 = '"+rows4Value+"' where ifnull(t2.COL2,'') = '' order by t3.col1 desc limit 200;")

    con.commit()
    con.close() # closes connection to database

def SortPurchaseRecord4(DBName):
    con = sqlite3.connect(DBName) # database file input
    cur = con.cursor()
    #t6: 사용자가 구매한 컨텐츠 장르에서 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠 COL4 장르
    cur.executescript("""
       DROP TABLE IF EXISTS t6;
       CREATE TABLE t6 (COL1 INTEGER, COL2 TEXT, COL3 INTEGER);
       CREATE INDEX t6_index ON t6 (COL1, COL2, COL3);
       """) # checks to see if table exists and makes a fresh table.

    cur.execute("SELECT col1 As TEXT FROM t4")
    rowst4 = cur.fetchall()

    for rowt4 in rowst4:
      rows4Value = str(rowt4[0])
      cur.execute("insert into t6 (col1, col2, col3) select '"+rows4Value+"', t3.COL2, t3.COL1 from t3 left join t2 on t2.COL2 = t3.COL2 and t2.COL1 = '"+rows4Value+"' where ifnull(t2.COL2,'') = '' and t3.col2 in (select t1.COL1 from t1 where t1.COL4 in (select t1.COL4 from t2 inner join t1 on t1.COL1 = t2.COL2 where t2.COL1 = '"+rows4Value+"' group by t1.COL4 order by count(t1.COL4) desc)) order by t3.col1 desc limit 100;")

    con.commit()
    con.close() # closes connection to database

def SortPurchaseRecord5(DBName):
    con = sqlite3.connect(DBName) # database file input
    cur = con.cursor()
    #t7: 사용자가 구매한 컨텐츠의 출연자에서 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠 COL3 출연자
    cur.executescript("""
       DROP TABLE IF EXISTS t7;
       CREATE TABLE t7 (COL1 INTEGER, COL2 TEXT, COL3 INTEGER);
       CREATE INDEX t7_index ON t7 (COL1, COL2, COL3);
       """) # checks to see if table exists and makes a fresh table.

    cur.execute("SELECT col1 As TEXT FROM t4")
    rowst4 = cur.fetchall()

    for rowt4 in rowst4:
      rows4Value = str(rowt4[0])
      cur.execute("insert into t7 (col1, col2, col3) select '"+rows4Value+"', t3.COL2, t3.COL1 from t3 left join t2 on t2.COL2 = t3.COL2 and t2.COL1 = '"+rows4Value+"' where ifnull(t2.COL2,'') = '' and t3.col2 in (select t1.COL1 from t1 where t1.COL3 in (select t1.COL3 from t2 inner join t1 on t1.COL1 = t2.COL2 where t2.COL1 = '"+rows4Value+"' group by t1.COL3 order by count(t1.COL3) desc)) order by t3.col1 desc limit 100;")

    con.commit()
    con.close() # closes connection to database

def SortPurchaseRecord6(DBName):
    con = sqlite3.connect(DBName) # database file input
    cur = con.cursor()
    #t8: 사용자가 구매한 컨텐츠의 감독에서 구매하지 않은 컨텐츠 중 구매 이력이 많은 상위 100 개를 정리 COL1 사용자, COL2 컨텐츠 COL2 감독
    cur.executescript("""
       DROP TABLE IF EXISTS t8;
       CREATE TABLE t8 (COL1 INTEGER, COL2 TEXT, COL3 INTEGER);
       CREATE INDEX t8_index ON t8 (COL1, COL2, COL3);
       """) # checks to see if table exists and makes a fresh table.

    cur.execute("SELECT col1 As TEXT FROM t4")
    rowst4 = cur.fetchall()

    for rowt4 in rowst4:
      rows4Value = str(rowt4[0])
      cur.execute("insert into t8 (col1, col2, col3) select '"+rows4Value+"', t3.COL2, t3.COL1 from t3 left join t2 on t2.COL2 = t3.COL2 and t2.COL1 = '"+rows4Value+"' where ifnull(t2.COL2,'') = '' and t3.col2 in (select t1.COL1 from t1 where t1.COL2 in (select t1.COL2 from t2 inner join t1 on t1.COL1 = t2.COL2 where t2.COL1 = '"+rows4Value+"' group by t1.COL2 order by count(t1.COL2) desc)) order by t3.col1 desc limit 100;")

    con.commit()
    con.close() # closes connection to database

def ExcuteData(DBName,OutputFile):

    if os.path.isfile(DBName):

        shoplistfile = OutputFile
        f = codecs.open(shoplistfile, 'w', "utf-8")

        con = sqlite3.connect(DBName) # database file input

        #con.commit()
        with con:

         cur = con.cursor()

         cur.execute("SELECT col1, col2 As TEXT FROM t5")
         rowst5 = cur.fetchall()

         for rowt5 in rowst5:
          rows5Value = str(rowt5[0])
          f.write(rows5Value + "," + rowt5[1] + "\n")

        f.close()
        con.close() # closes connection to database

    else:
      print "학습 진행 후 실행해 주세요."


