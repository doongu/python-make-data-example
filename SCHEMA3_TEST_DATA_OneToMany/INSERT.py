import mysql.connector
import os 

host = input("host를 입력해주세요 : ")
user = input("user를 입력해주세요 : ")
password = input("password를 입력해주세요 : ")
database = input("데이터 베이스 명을 입력해주세요 : ")
table = input("테이블 명을 입력해주세요 : ")
data_file = input("입력하실 파일 명을 입력해주세요 : ")

mydb = mysql.connector.connect(
    host = host,
    user = user,
    passwd = password,
    database = database
)

mc = mydb.cursor()

path = os.path.dirname(os.path.abspath(__file__))
fd = open(path + '/data_files/' + data_file + '.txt', 'r')

while True:

    sql = "INSERT INTO " + table + " VALUES ("
    file_line_tuple = tuple(map(str, fd.readline().split()))
    for i in range(len(file_line_tuple)):
        if i != len(file_line_tuple) - 1:
            sql += '%s,'
        else:
            sql += '%s)'
            
    # int 형 처리
    for i in range(len(file_line_tuple)):
        if str.isdigit(file_line_tuple[i]):
            file_line_tuple[i] = int(file_line_tuple[i])
         
    mc.execute(sql, file_line_tuple)
    if not file_line_tuple:
        break

mydb.commit()
mydb.close()
print(mc.rowcount, "개의 레코드가 입력되었습니다.")