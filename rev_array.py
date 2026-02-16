
def reverse_array(arr):
    arr.reverse()
    

if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8]
    reverse_array(arr)
print(" ".join(map(str,arr)))