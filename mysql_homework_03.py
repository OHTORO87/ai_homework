#mysql과 연동
import pymysql as my

con = my.connect(host ='127.0.0.1', user='root', password='1234', db='mydb')
c = con.cursor()

c.execute('create table Man(name char(20), age int);')

c.execute('insert into Man values("김연아", 32)')
c.execute('insert into Man values("손흥민", 30)')
c.execute('insert into Man values("이강인", 21)')


c.execute('select * from Man;')
res = c.fetchall()

print(' name  age ')
print('***********')
for i in res:
    print(i[0],i[1])
print('***********')

con.commit()
c.close()
con.close()
