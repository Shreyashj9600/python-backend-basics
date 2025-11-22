# Strings
# string is a data type that store a sequence of charactor

# Basic operation 
# concatenation
    # "hello" + "world" --> "helloworld"

str1 = 'hello'
str2 = 'world'

final_string = str1 + str2
print(final_string)

# length of str
len1 = "shreyash"
result = len(len1)
print(result)

# Indexing
# h e l l o _ w o r  l  d
# 1 2 3 4 5 6 7 8 9 10 11

str = "Apna collage"
ch = str[2]
print(ch)

# Slicing 
# Accesing part of string
# str[starting_ind : ending_ind] # ending idx is not included

str2 = 'Apna Collage'
print(str2[1:4])
print(str2[:4]) #[0:4]
print(str2[5:]) #[5:len(str2)]

# str = "i am coder"
# str.endswith('er')
# str.capitalize()
# str.replace(old,new)
# str.find(word)
# str.count('am') # how many time char present in string

# problem solving 

name = input("enter a name : ")

print('Name is ', name + ' and length of char is present :' , len(name) )

