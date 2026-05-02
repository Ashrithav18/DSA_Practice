def intersection(arr1,arr2):
    set1=set(arr1)
    result=[]
    for num in arr2:
        if num in set1:
            result.append(num)
            set1.remove(num)
    return result

arr1=[1,2,2,3,4]
arr2=[5,2,3,6]  
print(intersection(arr1,arr2))  