import  openpyxl as xl

exf = xl.load_workbook('c:\\dd\\itx.xlsx')

aws = exf.active
## A6에 문자열 avg_sal 추가
aws['A6'] = 'avg_sal'
## 6행 2열에 엑셀 함수 직접 입력
aws.cell(row = 6, column = 2).value = "=AVERAGE(B1:B5)"

for i in aws.rows:
    index = i[0].row
    name = i[0].value
    sal = i[1].value

    print('{} {}'.format(name, sal))

exf.save('c:\\dd\\outitx.xlsx')
exf.close()

'''SQLLITE
SQLite version 3.35.5 2021-04-19 18:32:05
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> .oepn 'c:\\dd\\abd'
Error: unknown command or invalid arguments:  "oepn". Enter ".help" for help
sqlite> .open 'c:\\dd\\adb'
sqlite> .mo co
sqlite> .he on
sqlite> create table mt(mount, alt);
sqlite> .ta
city   mt     score
sqlite> .import 'c:\\dd\\mt.txt' mt
sqlite> select * from mt;
mount  alt
-----  ----
설악산    1900
지로산    2915
덕유산    1300
sqlite> select alt, mount from mt;
alt   mount
----  -----
1900  설악산
2915  지로산
1300  덕유산
sqlite> select mount as'산이름' alt as'해발' from mt;
Error: near "alt": syntax error
sqlite> select mount as'산이름', alt as'해발' from mt;
산이름  해발
---  ----
설악산  1900
지로산  2915
덕유산  1300
sqlite> insert into mt values('한라산',1950);
sqlite> select mount as'산이름', alt as'해발' from mt;
산이름  해발
---  ----
설악산  1900
지로산  2915
덕유산  1300
한라산  1950
sqlite>

'''
