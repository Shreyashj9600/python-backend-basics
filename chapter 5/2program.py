# Break and continue
# Break : used to terminate the loop when encountered

# continue : terminates execution in the currect iteration and continue execution of the 
#            loop with the next iteration .        

nums = (5, 12, 23, 7, 34, 19)
x = 23
i = 0
print(i < len(nums))
while i < len(nums) :
    if(nums[i] == x):
        print('FOUND at index', i)
        break # stop
    else:
        print('finding')
    i += 1


i = 1
while i <= 10:
    if(i%2 == 0):
        i += 1
        continue # skip
    print(i)
    i += 1    
    