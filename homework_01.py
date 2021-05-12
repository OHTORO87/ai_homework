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
