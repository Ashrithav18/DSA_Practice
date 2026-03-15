def find_min_max(arr):
    n=len(arr)
    
    if n==0:
        return None
    if n==1:
        return arr[0],arr[0]
    if n%2==1:
        mini=maxi=arr[0]
        i=1
    else:
        if arr[0]<arr[1]:
            mini=arr[0]
            maxi=arr[1]
        else:
            mini=arr[1]
            maxi=arr[0]
            i=2
    while i<n-1:
        if arr[i]<arr[i+1]:
            mini=min(mini,arr[i])
            maxi=max(maxi,arr[i+1])
        else:
            mini=min(mini,arr[i+1])
            maxi=max(maxi,arr[i])
        i+=2
    return mini,maxi
        
if__name__="__main__:"
arr=[0,2,34,67,89,32,48]
minimum,maximum=find_min_max(arr)
print(minimum)
print(maximum)
            