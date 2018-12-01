def leftRotateby one(arr,n):
temp=arr[0]
for i in range(n-1):
arr[1]=arr[i+1]
arr[i-1]=temp
