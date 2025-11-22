# LOOPS IN PYTHON
# lOOPS are userd to repeat instructions 

# while loop

count = 1
while count <= 5:
    print('hello')
    count += 1

i = 5
while i <= 100:
    print('apna collage', i )
    i = i + 1

print('loop end')

# solving questons 

# print number form 1 to 100
i = 1 
while i <= 100:
    print('No :' , i)
    i = i + 1
print('------------------------------')

# print number fomr 100 to 1
i = 100
while i >= 1:
    print("No", i) 
    i = i - 1


# print the multiplaction table of a number n.

n = int(input('enter a numner '))
i = 1
while i <= 10:
    print(n ,'*', i , '=', n * i )
    i = i+1

# print list using while loop
nums =  [10, 25, 30, 45, 50, 65, 70, 85, 90, 100]

ind = 0
while ind < len(nums):
    print('number of list :' , nums[ind])
    ind += 1

# search for a number x in this tuple using loop:

nums = (5, 12, 23, 7, 34, 19)
x = 23
i = 0
print(i < len(nums))
while i < len(nums) :
    if(nums[i] == x):
        print('FOUND at index', i)
    i += 1
    
