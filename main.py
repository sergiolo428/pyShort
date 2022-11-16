# PyShort
import numpy as np
import os
import sys
os.chdir(sys.path[0]) # Change to current .py file path

# See data
def see(arr):
    for i in arr:
        print(i)

# Shorting (Not working rn)
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

# Get values from files
def extract():
    data=[]
    with open("values.txt","r") as f:
        for line in f:
            data.append(line.split())
    return data

def flatten(info):
    final_list=[]
    for  i in info:
        for j in i:
            final_list.append(j)
    return final_list

info=flatten(extract())
see(info)
