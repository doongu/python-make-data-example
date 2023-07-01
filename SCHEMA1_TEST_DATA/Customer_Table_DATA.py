from faker import Faker
import os 

tuple_length = int(input("튜플의 갯수를 입력해주세요 : "))
file_name = input("파일 이름을 작성해 주세요 : ")

def make_data_file(tuple_length, file_name):
    path = os.path.dirname(os.path.abspath(__file__))

    fake = Faker()    
    fd = open(path + '/data_files/' + file_name + '.txt', 'w')
    # fd = open(file_name, 'w')

    for key in range(1, tuple_length + 1):
        fd.write(str(key) + ' ' + fake.name() + ' ' + fake.email() + '\n')
    else:
        fd.close()

make_data_file(tuple_length, file_name)