import InsertionSort

def __init__(self,number,list):
    self.number = number
    self.array = list

number = int(input())
list=[]
for i in range(number):
    list[i] = int(input())

InsertionSort(list)
