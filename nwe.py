'''arr=[6,-2,4,-3,3,-7]

arr.sort()
min=arr[0]
for i in range(len(arr)):
    
    
    if min>arr[i]:
            
        min=arr[i]
        

print(min)
        
start=0
end=len(arr)-1


for i in arr:
    if start<end:
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
print(arr)'''
st='aabb'
