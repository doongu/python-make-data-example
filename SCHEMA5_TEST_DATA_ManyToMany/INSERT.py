import pymysql
import os 

host = input("host를 입력해주세요 : ")
user = input("user를 입력해주세요 : ")
password = input("password를 입력해주세요 : ")
database = input("데이터 베이스 명을 입력해주세요 : ")
table = input("테이블 명을 입력해주세요 : ")
data_file = input("입력하실 파일 명을 입력해주세요 : ")

mydb = pymysql.connect(
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
    file_line_list = list(map(str, fd.readline().split()))
    for i in range(len(file_line_list)):
        if i != len(file_line_list) - 1:
            sql += '%s,'
        else:
            sql += '%s)'
            
    # int 형 처리
    for i in range(len(file_line_list)):
        if str.isdigit(file_line_list[i]):
            file_line_list[i] = int(file_line_list[i])
    else:
        file_line_tuple = tuple(file_line_list)

    if not file_line_tuple:
        break
    
    mc.execute(sql, file_line_tuple)

mydb.commit()
mydb.close()
print(mc.rowcount, "개의 레코드가 입력되었습니다.")