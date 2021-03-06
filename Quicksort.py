from fnmatch import fnmatch
import random
from unittest import result
import pandas as pd
import numpy as np
import csv

def Filedata_input():

    #랜덤
    Rn_list = list(range(1,1000000))
    Rn_filename = 'Random_list.csv'
    random.shuffle(Rn_list) # 대입이 이루어지지 않음 수정할 것 
    Rn_file = open(Rn_filename, 'w')
    Rn_file.writelines('\n'.join(map(str,Rn_list))) # 개행을 주어 세로로 입력
    Rn_file.close()
    csv_open(Rn_filename)
    
    # 순방향
    num_list = list(range(1,1000000))
    Fn_filename = 'Foward_list.csv'
    Fn_file = open(Fn_filename, 'w')
    Fn_file.writelines('\n'.join(map(str,num_list)))
    Fn_file.close()
    csv_open(Fn_filename)

    #역방향
    Rn_list = list(range(1,1000000))
    Rn_list.sort(reverse=True)
    Re_filename = 'Reverse_list.csv'
    Re_file = open('Reverse_list.csv', 'w')
    Re_file.writelines('\n'.join(map(str,Rn_list)))
    Re_file.close()
    csv_open(Re_filename)
    
def csv_open(filename):
    csv_list = []
    csv_path = open(filename, 'r')
    read_csv = csv_path.readlines()
    colw_csv = list(map(lambda s: s.strip(), read_csv)) # 문자열 \n 제거 
    for i in colw_csv:
        csv_list.append(int(i))
    quickSort_fun(csv_list, 0, len(csv_list)-1)
    result_csvw(filename, csv_list)

def result_csvw(file_name, result_list):
    result_csv = open(file_name+'_result.csv','w')
    result_csv.writelines('\n'.join(map(str,result_list))) # 개행을 주어 CSV 파일에 입력
    result_csv.close()
    
def slice_fun(num_list,front,end): # quicksort_fun에서 호출

    pivot = num_list[(front+end)//2]

    while front <= end:
        while num_list[front] < pivot:
            front += 1 #앞부터 증가 시키며 
        while num_list[end] > pivot:
            end -= 1 #뒤에서 부터 순차 탐색

        if front <= end :
            num_list[front],num_list[end] = num_list[end],num_list[front] # 자리 바꾸기
            front += 1 # 증가
            end -= 1# 뒤 감소

    return front #다음 인덱스 반환

def quickSort_fun(csv_num_list,front,end):

    slice_list = slice_fun(csv_num_list,front,end) #pivot보다 큰 그룹의 첫 번째 idx 반환

    if front < slice_list-1: #1개 될때까지 반복
        quickSort_fun(csv_num_list,front,slice_list-1)
    if slice_list < end: # 기존 배열 마지막 지점 도달할 때까지 반복
        quickSort_fun(csv_num_list,slice_list,end)













    # return quicksort_action(left_list)+[pivot_num]+quicksort_action(right_list)

#     Number_list = []
#     Random_number = []
#     for i in range(1000000):
#         Random_number.append(np.random.randint(1, 100))
    
#     Number_list.append(Random_number)
#     for end in range(1000000):
#         #순방향 정렬 구현하였으나 시간이 많이 걸려 주석 처리
#         # Random_number.append(np.random.randint(1,100))
#         # for i in range(end, 0, -1):
#         #     if i>=1:
#         #         if Random_number[i] < Random_number[i-1]:
#         #             Random_number[i], Random_number[i-1] = Random_number[i-1], Random_number[i]
#                 # swap(Random_number[i-1], Random_number(i))
    
