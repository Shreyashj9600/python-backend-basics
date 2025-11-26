# create a file "practice.txt" using python. Add the following data in it:
# Hi everyone
# we are learning file I/O
# using java
# l like programming in java

with open("practice.txt" , 'r') as f:
    data = f.read()

new_data =  data.replace('java' , 'python')    

with open('practice.txt', 'w') as f:
    f.write(new_data)