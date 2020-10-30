import InsertionSort

if __name__ == "__main__":
    n = int(input("enter length"))
    list=list()
    for i in range(n):
        m = int(input("enter number "))
        list.append(m)

    InsertionSort.insertionSort.insertion(list)
