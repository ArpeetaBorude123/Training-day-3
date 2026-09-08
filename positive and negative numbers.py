# i/p =[1,4,7,-1,0,6,-4]
# o/p=[positive=4,negative=3]
arr = [3, -2, 7, -1, 8, 6, -4]

positive = 0
negative = 0

for i in arr:
    if i > 0:
        positive += 1
    elif i < 0:
        negative += 1

print("positive =", positive)
print("negative =", negative)