
class fractionalKnapSack:

    def getMaxValue(self,wt,val,capacity):
        ival=[]
        for i in range(len(wt)):
            ival.append(ItemValue(wt[i],val[i],i))

        ival.sort(reverse=True)
        totalValue = 0
        for i in ival:
            curWt = int(i.wt)
            curVal = int(i.val)
            if capacity - curWt >=0:
                capacity -= curWt
                totalValue += curVal
            else:
                fraction = capacity/curWt
                totalValue += curVal * fraction
                capacity = int(capacity -(curWt * fraction))
                break
        return totalValue

class ItemValue:

    def __init__(self,wt,val,ind):
        self.wt = wt;
        self.val = val
        self.ind = ind
        self.cost = val//wt

    def __lt__(self, other):
        return self.cost <other.cost
