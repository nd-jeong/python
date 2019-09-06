# Imports argv from sys module
from sys import argv

script, filename = argv
# Sets txt varible to open filename argument
txt = open(filename)
# Prints file name
print(f"Here's your file {filename}:")
# Prints text inside file
print(txt.read())
txt.close()

print("Type the filename again:")
# Sets variable as user input
file_again = input("> ")
# Sets txt_again varible as opening user input file name
txt_again = open(file_again)
# Prints text inside file
print(txt_again.read())
txt_again.close()