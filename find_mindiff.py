def find_mindiff(arr,m):
    n=len(arr)
    arr.sort()
    mindiff=float('inf')
    
    for i in range(n-m+1):
        diff=arr[i+m-1]-arr[i]
        if diff<mindiff:
            mindiff=diff
    return mindiff

arr=[2,3,4,7,9,12,56]
m=3
res=find_mindiff(arr,m)
print(res)