def linearsearch(array,value): # array lenght=9
    for index in range(0,len(array)): #i-0<0
        if array[index] == target:  #7==7
            return index
    return -1

array=[1,2,3,4,5,6,7,8,9] # execution start here
target=7
result=linearsearch(array,target)
if result == -1:
  print("value not found")
else:
    print("value of the index",result)