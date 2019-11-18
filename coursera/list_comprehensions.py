"""
[<transformer_expression> for <var_name> in <sequence> if <condition>]
"""

"""
Write code to assign to the variable compri all the values of the key name 
in any of the sub-dictionaries in the dictionary tester. 
Do this using a list comprehension.
"""
tester = {'info': [{"name": "Lauren", 'class standing': 'Junior', 'major': "Information Science"},{'name': 'Ayo', 'class standing': "Bachelor's", 'major': 'Information Science'}, {'name': 'Kathryn', 'class standing': 'Senior', 'major': 'Sociology'}, {'name': 'Nick', 'class standing': 'Junior', 'major': 'Computer Science'}, {'name': 'Gladys', 'class standing': 'Sophomore', 'major': 'History'}, {'name': 'Adam', 'major': 'Violin Performance', 'class standing': 'Senior'}]}
compri = [dict_['name'] for dict_ in tester['info']]

"""
Write code to assign to the variable compri all the values of the key name 
in any of the sub-dictionaries in the dictionary tester. 
Do this using a list comprehension.
"""
list_of_words = ["Lauren", 'class standing', 'Junior', 'major', "Information Science", 'name', 'Ayo', "Bachelor's", 'Information Science', 'Kathryn', 'Senior', 'Sociology', 'Junior', 'Computer Science', 'Sophomore', 'History', 'Violin Performance']
result = [len(word) for word in list_of_words if len(word) < 4]
print(result)
result = [word for word in list_of_words if len(word) < 4]
print(result)

print("List comprehension VS. map and filter\n")

lst = [4, 5, 6, 7, 8, 9]
print("Task: value ** 2")
print("List comprehension: ", [value ** 2 for value in lst])
print("Map               : ", list(map(lambda value: value ** 2, lst)))

print("\nTask: value % 2 == 0")
print("List comprehension: ", [value for value in lst if value % 2 == 0])
print("Filter            : ", list(filter(lambda value: value % 2 == 0, lst)))

print("\nTask: value ** 2 if value % 2 == 0")
print("List comprehension: ", [value ** 2 for value in lst if value % 2 == 0])
print("Map and Filter    : ", list(map(lambda value: value ** 2, filter(lambda value: value % 2 == 0, lst))))