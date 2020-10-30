import InsertionSort

if __name__ == "__main__":
    print("how long you want your list is ?")
    number = int(input())

    print("enter numbers...")
    list=[]
    for i in range(number):
        list[i] = input()

    InsertionSort.insertion(list)
