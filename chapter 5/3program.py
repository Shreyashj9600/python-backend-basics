# Loops in Python 
# Loops are used for sequential traversal,  for traversing list string tuples etc.

nums = [1,2,3,4,5]

for num in nums :
    print("printing numbers ", num)


str = "ApnaCollage"
for ch in str:
    print(ch)
else:
    print("END")    

nums = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
ind = 0
for el in nums:
    if(el == x):
        print("Index Foun" , ind)
    ind += 1


# Range
for i in range(5): # range(stop)
    print(i)

print('----------------')

for i in range(2,10): # range(start,stop)
    print(i)

print('----------------')

for i in range(2,10,2) : # range(start,stop, step)
    print(i)


# pass Statement
# pass is a null statement that dose nothing. it is used as placeholder for futher code.

for i in range(5):
    pass

print('some use full work')


