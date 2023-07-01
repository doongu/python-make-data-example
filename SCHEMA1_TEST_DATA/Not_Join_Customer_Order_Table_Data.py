from faker import Faker
import os 

data_length = int(input("Customer_Data와 Order_Data를 합칩니다. 합칠 데이터 갯수를 입력해주세요 : "))

def make_data_file(data_length):
    path = os.path.dirname(os.path.abspath(__file__))

    fd = open(path + '/data_files/Not_Join_Customer_Order_Data_' + str(data_length) + '.txt', 'w')
    Order_Data_Fd = open(path + '/data_files/Order_Data_' + str(data_length) + '.txt', 'r')
    Customer_Data_Fd = open(path + '/data_files/Customer_Data_' + str(data_length) + '.txt', 'r')
    
    for key in range(1, data_length + 1):
        Order_Line = list(map(str, Order_Data_Fd.readline().split()))
        Customer_Line = list(map(str, Customer_Data_Fd.readline().split()))

        input_list = [Customer_Line[0], Order_Line[0], Customer_Line[1], Customer_Line[2], Order_Line[2]]
        fd.write(' '.join(input_list) + '\n')
    else:
        fd.close()

make_data_file(data_length)