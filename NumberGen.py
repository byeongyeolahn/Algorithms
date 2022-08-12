import random
import csv

def Filedata_input():
    #랜덤
    Rn_list = list(range(1,1000001))
    Rn_filename = 'Random_list.csv'
    random.shuffle(Rn_list)
    Rn_file = open(Rn_filename, 'w')
    Rn_file.writelines('\n'.join(map(str,Rn_list))) # 개행을 주어 세로로 입력
    Rn_file.close()
    
    # 순방향
    num_list = list(range(1,1000001))
    Fn_filename = 'Foward_list.csv'
    Fn_file = open(Fn_filename, 'w')
    Fn_file.writelines('\n'.join(map(str,num_list)))
    Fn_file.close()

    #역방향
    Rn_list = list(range(1,1000001))
    Rn_list.sort(reverse=True)
    Re_filename = 'Reverse_list.csv'
    Re_file = open('Reverse_list.csv', 'w')
    Re_file.writelines('\n'.join(map(str,Rn_list)))
    Re_file.close()