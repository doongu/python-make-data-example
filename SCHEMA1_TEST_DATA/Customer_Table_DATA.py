from faker import Faker
import os 

tuple_length = int(input("Customer_Table의 데이터를 생성합니다. \n\n 튜플의 갯수를 입력해주세요 : "))
file_name = input("파일 이름을 작성해 주세요 : ")

def make_data_file(tuple_length, file_name):
    path = os.path.dirname(os.path.abspath(__file__))

    fake = Faker()    
    fd = open(path + '/data_files/' + file_name + '.txt', 'w')

    for key in range(1, tuple_length + 1):
        name_split = fake.name().split()
        name_sum = ''.join(name_split)

        fd.write(str(key) + ' ' + name_sum + ' ' + fake.email() + '\n')
    else:
        fd.close()

make_data_file(tuple_length, file_name)