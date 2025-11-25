# Function in python 
# Block of statements that preform a specific task

def caculate_sum (num1, num2):  
    sum = num1 + num2
    print(sum)

caculate_sum(5,4)         

def print_hello():
    print("Hello world")

print_hello()    

# solving que

names = ["Rahul", "Amit", "Sneha", "Pooja", "Ravi"]

def print_name(list) :
    for el in list:
        print(el)

print_name(names)        

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD = ", inr_val , "INR")

converter(10)   