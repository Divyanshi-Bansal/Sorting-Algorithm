# Constraints for this sorting :
#     0<= array Element <= 100000


def countSort(ar):
    freq = [0]*(max(ar)+1)
    for i in ar:
        freq[i]+=1;
    i = 0;
    for j in range(max(ar)+1):
        while(freq[j]>0):
            ar[i] = j;
            i+=1;
            freq[j]-=1;
    return ar;

n = int(input())
ar = list(map(int, input().split()));
ar = countSort(ar)
print(*ar)
