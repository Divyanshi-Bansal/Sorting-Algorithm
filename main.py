import InsertionSort

def __init__main(self,number,list):
    self.number = number
    self.list = list

print("how long yo want your list is ?")
number = int(input())

print("enter numbers...")
list=[]
for i in range(number):
    list[i] = input()

InsertionSort.insertion(list)
