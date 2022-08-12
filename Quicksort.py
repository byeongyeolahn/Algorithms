from fnmatch import fnmatch
import random
from unittest import result
import csv
import os
import psutil
import time
import NumberGen

# 결과 csv 파일 생성
def result_csvw(file_name, result_list):
    result_csv = open(file_name+'_result.csv','w')
    result_csv.writelines('\n'.join(map(str,result_list))) # 개행을 주어 CSV 파일에 입력
    result_csv.close()

#quicksort_fun 자동 호출  
def slice_fun(num_list,front,end):
    pivot = num_list[front]

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
    end = time.time()

def memory_use(messae: str='debug'):
    p=psutil.Process()
    rss = p.memory_info().rss/2**20
    return rss
    
if __name__ =="__main__":
    NumberGen.Filedata_input()

    filename = ['Random_list.csv', 'Foward_list.csv', 'Reverse_list.csv']
    for i in range(len(filename)):
        csv_list = [] # 데이터 탐을 공간 확보
        csv_path = open(filename[i], 'r')
        read_csv = csv_path.readlines()
        colw_csv = list(map(lambda s: s.strip(), read_csv)) # 문자열 \n 제거 
        for r in colw_csv:
            csv_list.append(int(r))

        start = time.time()
        first_memory = memory_use()
        quickSort_fun(csv_list, 0, len(csv_list)-1)
        finish_memory = memory_use()
        print("사용 메모리 :", finish_memory - first_memory,"MB")
        print("시간 성능 측정 : ",time.time()-start)
        result_csvw(filename[i], csv_list)
