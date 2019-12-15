import sys

arguments = sys.argv
print(arguments)

"""
$ python3 python3_standard_library/command_line_arguments.py 1 2 3
['python3_standart_library/command_line_arguments.py', '1', '2', '3']
"""

sys.argv.remove(arguments[0])
arguments = sys.argv
print(arguments)
"""
$ python3 python3_standard_library/command_line_arguments.py 1 2 3
['python3_standard_library/command_line_arguments.py', '1', '2', '3']
['1', '2', '3']
"""
res = 0
for value in arguments:
    res += int(value)
print("Sum of arguments:", res)
"""
Sum of arguments: 6
"""