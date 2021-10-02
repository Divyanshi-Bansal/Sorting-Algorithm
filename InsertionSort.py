

class insertionSort:

    def __init__(self,list):
        self.list = list

    def insertion(list):
        for i in range(1,len(list)):
            j=i-1
            key = list[i]
            while key<list[j] and j>=0:
                list[j+1] = list[j]
                j=j-1
            list[j+1] = key
        for ele in list:
            print(ele,end=" ")
