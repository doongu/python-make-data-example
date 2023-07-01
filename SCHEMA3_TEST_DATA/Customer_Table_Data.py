from faker import Faker
import os 

CASE = int(input("Customer_Table의 데이터를 생성합니다 CASE를 입력해주세요"))
file_name = input("파일 이름을 작성해 주세요 : ")


def make_data_file(CASE, file_name):
    CASES = {1 : 1000, 2 : 100, 3 : 10, 4 : 1,
             5 : 1000, 6 : 100, 7 : 10, 8 : 1}


    path = os.path.dirname(os.path.abspath(__file__))

    fake = Faker()    
    fd = open(path + '/data_files/' + file_name + '.txt', 'w')

    for key in range(1, CASES[CASE] + 1):
        name_split = fake.name().split()
        name_sum = ''.join(name_split)

        fd.write(str(key) + ' ' + name_sum + ' ' + fake.email() + '\n')
    else:
        fd.close()

make_data_file(CASE, file_name)