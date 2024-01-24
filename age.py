import sys  # used to import the sys module
# user input
year = input("Enter your birth year: ") 
print(type(year))
 # function to determine size of user input
age = 2024 - float(year)
size_year = sys.getsizeof(year) 
print("your age=", age)
print(type(age))
 # user input
height = input("Enter your height in meters:") 
print(type(height))
 # function to determine size of user input
size = sys.getsizeof(height) 
print(" size of height", size, "bytes....." " Size of year", size_year, "bytes")