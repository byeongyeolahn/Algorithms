from fnmatch import fnmatch
import random
from unittest import result
import pandas as pd
import numpy as np
import csv
import os
import psutil
import time

def Filedata_input():

    #랜덤
    Rn_list = list(range(1,1000000))
    Rn_filename = 'Random_list.csv'
    random.shuffle(Rn_list)
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

#파일 오픈 및 데이터 read    
def csv_open(filename):
    csv_list = []
    csv_path = open(filename, 'r')
    read_csv = csv_path.readlines()
    colw_csv = list(map(lambda s: s.strip(), read_csv)) # 문자열 \n 제거 
    for i in colw_csv:
        csv_list.append(int(i))
    quickSort_fun(csv_list, 0, len(csv_list)-1)
    result_csvw(filename, csv_list)

# 결과 csv 파일 생성
def result_csvw(file_name, result_list):
    result_csv = open(file_name+'_result.csv','w')
    result_csv.writelines('\n'.join(map(str,result_list))) # 개행을 주어 CSV 파일에 입력
    result_csv.close()

#quicksort_fun 자동 호출  
def slice_fun(num_list,front,end):

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

def memory_use(messae: str='debug'):
    p=psutil.Process()
    rss = p.memory_info().rss/2**20
    return rss
    
if __name__ =="__main__":
    start = time.time()
    first_memory = memory_use()
    Filedata_input()
    end = time.time()
    finish_memory = memory_use()
    print("사용 메모리 :", finish_memory - first_memory,"MB")
    print("시간 성능 측정 : ",time.time()-start)