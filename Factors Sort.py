def findFactors(n):
    i,count=1,0
    while(i*i<=n):
        if n%i==0:
            count+= 2 if i*i!=n else 1
        i+=1
    return count

def factorsSort(arr):
    arr.sort()
    dic={}
    for i in arr:
        dic[i]=findFactors(i)
    dic=[key  for key, value in sorted(dic.items(), key=lambda item: item[1])]
    return dic

print(factorsSort(list(map(int,input().split()))))