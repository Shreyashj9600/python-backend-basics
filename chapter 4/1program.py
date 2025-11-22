# Dictionaries
# Dictionaries are used to store data values in key:value pairs They are unordered,
# mutable(Changeabal) & don't allow duplicate keys

dict = {
    "name":"shradha",
    "cgpa": 9.6,
    "marks":[98,97,95]
}
print(dict)
print(dict['name'])
dict["cgpa"] = 5.55
print(dict["cgpa"])

# Nested Dictionary

student = {
    "name":"rahul kumar",
    "subjects":{
        "phy":97,
        "chem":98,
        "math":97
    }
}

print(student["subjects"]["chem"])

# Dictionary Methods
print(student.keys())
print(student.values())