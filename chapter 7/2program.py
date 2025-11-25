# writhin file in python 
 
f = open('demo.txt', 'a') # w - overwride the data || a - add the data in next line

f.write('\n After i learn node.js')
f.close()

# create a file 
f = open('data.txt', 'w')  # in case data.txt not present in my folder then its create automaticaly
f.write('.\n user visit on url https://uc2e3dsf12')
f.close()

# with syntax

with open('demo.txt', 'r') as f:
    data = f.read()
    print(data)

with open('demo.txt', 'w') as f:
    f.write('new data')
