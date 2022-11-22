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
def extract(filename):
    data=[]
    file=filename + ".txt"
    with open(file,"r") as f:
        for line in f:
            data.append(line.split())
    return data

#Flatten lines into a single array
def flatten(info):
    final_list=[]
    for  i in info:
        for j in i:
            final_list.append(j)
    return final_list

# Short one array by the info in other one
def short(nums,words):
    zip_list=zip(words,nums)
    sorted_pair=sorted(zip_list)
    tuples=zip(*sorted_pair)
    list1, list2 = [ list(tuple) for tuple in tuples]
    print(list1)
    print(list2)

#short(extract("values"),extract("words"))