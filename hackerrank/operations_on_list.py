def list_commands():
    input_data = ["insert 0 5", "insert 1 10", "insert 0 6", "print", "remove 6", "append 9", "append 1",
                  "sort", "print", "pop", "reverse", "print", "insert 2 19", "insert 0 -2", "print", "sort", "print"]
    lst = []
    switcher = {
        "insert": "lst.insert(index, value)",
        "print": "print(lst)",
        "remove": "lst.remove(value)",
        "append": "lst.append(value)",
        "sort": "lst.sort()",
        "pop": "lst.pop()",
        "reverse": "lst.reverse()"
    }
    for i in range(len(input_data)):
        inp = input_data[i].split()
        command = inp[0]
        if len(inp) == 3:
            index = int(inp[1])
            value = int(inp[2])
        if len(inp) == 2:
            value = int(inp[1])
        exec(switcher[command])


# execute different commands on a list
print("*" * 50)
list_commands()
