from faker import Faker
import os 

CASE = int(input("Customer_Data와 Order_Data를 합칩니다. 합칠 CASE를 입력해주세요 : "))

def make_data_file(CASE):

    Customer_Table_Len = [-1, 1, 10, 100, 1, 10, 100, 1000]

    CASES = {1 : 100000, 2 : 100000, 3 : 100000, 4 : 1000000,
            5 : 1000000, 6 : 1000000,  7 : 1000000 }
    path = os.path.dirname(os.path.abspath(__file__))

    fd = open(path + '/data_files/CASE' + str(CASE) + '_Not_Join_Customer_Order_Data' + '.txt', 'w')
    Order_Data_Fd = open(path + '/data_files/CASE' + str(CASE) + '_Order_Data' '.txt', 'r')
    
    for i in range(1, CASES[CASE] // Customer_Table_Len[CASE] + 1):
        
        Customer_Data_Fd = open(path + '/data_files/CASE' + str(CASE) + '_Customer_Data' + '.txt', 'r')
    
        for j in range(1, Customer_Table_Len[CASE] + 1):
            Order_Line = list(map(str, Order_Data_Fd.readline().split()))
            Customer_Line = list(map(str, Customer_Data_Fd.readline().split()))

            input_list = [ Customer_Line[0], Order_Line[0], Customer_Line[1], Customer_Line[2],  Order_Line[2]]
            
            
            fd.write(' '.join(input_list) + '\n')
    else:
        fd.close()

make_data_file(CASE)