def MinimumCostRemove(arr):
    arr.sort(reverse=True)
    s=0
    for i in range(len(arr)):
        s+=arr[i]*(i+1)
    return s
print(MinimumCostRemove(list(map(int,input().split()))))
