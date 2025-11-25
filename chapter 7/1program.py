# File I/O in python

# Python can be used to perform operations on a file. (read & write data)

# type of all files 
# 1) Text file : txt, docx, .log, etc
# 2) binary file : mp4, mov, .png, .jpeg etc.

# Character — Meaning
# 'r' — open for reading (default)
# 'w' — open for writing, truncating the file first
# 'x' — create a new file and open it for writing
# 'a' — open for writing, appending to the end of the file if it exists
# 'b' — binary mode
# 't' — text mode (default)
# '+' — open a disk file for updating (reading and writing)

f = open("demo.txt", "r")   
data = f.read()
print(data)
print(type(data))
f.close()   

# data = f.read()     reads entire file
# data = f.readline() reads one line at time  