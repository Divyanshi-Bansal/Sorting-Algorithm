import knapSack

if __name__ == "__main__":
    print("how many value want")
    n= int(input())
    weight=[]
    for i in range(n):
        print("enter weight")
        weight.append(int(input()))
    value=[]
    for i in range(n):
        print("value of each weight")
        value.append(int(input()))
    print("enter capacity ")
    capacity = int(input())

    maxValue = knapSack.fractionalKnapSack.getMaxValue(weight,value,capacity)
    print("Maximum value of knapSack is ",maxValue)
