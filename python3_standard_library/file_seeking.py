my_file = open('command_line_arguments.py', 'r')

print("Reading first 20 symbols....\n")
print(my_file.read(20))
print("-" * 50)
print("Reading another 20 symbols....\n")
print(my_file.read(20))
print("-" * 50)
print("Reading from the beginning again....\n")
my_file.seek(0)
print(my_file.read(20))

