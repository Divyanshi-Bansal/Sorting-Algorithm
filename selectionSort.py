class selectionSort:
    def __init__(self,list) -> None:
        self.list=list

    def selection(list):
        print("Array before sort -->",list)
        for i in range(len(list)):
            minimum = i
            for j in range(i, len(list)):
                if list[j] < list[minimum]:
                    minimum = j
            if i != minimum:
                list[minimum], list[i] = list[i], list[minimum] 
        print("Array after sort -->",list)