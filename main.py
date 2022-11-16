# PyShort
import numpy as np
import os
import sys
os.chdir(sys.path[0]) # Change to current .py file path

def see(arr):
    for i in arr:
        print(i)

def short1(arr):
    piv=arr[len(arr)-1]
    end=len(arr)
    for i in range(0,end):
        if arr[i]>piv:
            print(arr[i])
            arr=np.delete(arr,arr[i])
            i=i-1
            arr=np.append(arr,arr[i])
    see(arr)

with open("values.txt","r") as f:
    f.read

    