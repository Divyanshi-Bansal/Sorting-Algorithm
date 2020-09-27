import InsertionSort

def __init__(self,number,list):
    self.number = number
    self.array = list

print("how long yo want your list is ?")
number = int(input())
print("enter numbers...")
list=[]
for i in range(number):
    list[i] = int(input())

InsertionSort.insertion(list)
