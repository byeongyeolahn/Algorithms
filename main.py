import Quicksort
import time
import sys
import psutil
import os

if __name__ =="__main__":
    start = time.time()
    process = psutil.Process(os.getpid())
    Quicksort.Filedata_input()
    print(process.memory_percent())
    end = time.time()
    # Quicksort.pandas_csv()
    print("시간 성능 측정 : ",time.time()-start)