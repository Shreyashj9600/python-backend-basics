# fist program 
print('hello world!')

# variables 
name = "shreyash" 
email = "shreyash@gmail.com"

print('my name is' , name)
print('my email is' , email)

# type chake in python
print(type(name))
print(type(email))

# Data types in python
# 1) Integers : +ve, -ve (5, -5, 0)
# 2) String : 'shreyash' , "shreyash" , '''shreyash'''  (' ', " ", ''' ''', )
# 3)Float : 2.99, 5.87
#  4) Boolean : True, false
#  5) None : a = None   

old = True
a = None
print(type(old))
print(type(a))

# Keywords
# keyword are reserved word in python

# False      await      else       import     pass
# None       break      except     in         raise
# True       class      finally    is         return
# and        continue   for        lambda     try
# as         def        from       nonlocal   while
# assert     del        global     not        with
# async      elif       if         or         yield

# sum print
a = 5
b = 10
sum = a + b 
print(sum)


# type of tokens
# punctuators
# punctuators are symbol to organize sentence structure in programming.
# (), {}, @, [], # etc.

# Experession Execution 

# String and numeric values can operate together with *
A,B = 2,3
Txt = "@"
print(2*Txt*3) 

# String and String can operate with +  (concatenation)
A,B = "2",3
Txt = "@"
print((A+Txt)*B)

# Numeric values can operate with all arithmetic operators (+,-,*,/,%,**)
A,B = 2,3
C = 4
print(A+B*C)

# ✅ Python Operator Precedence Table (High → Low)
# Brackets → Orders(**) → Division → Multiplication → Addition → Subtraction

#comments in pyton 
# single line comments
""" This is 
    a multiline 
    comments"""

#