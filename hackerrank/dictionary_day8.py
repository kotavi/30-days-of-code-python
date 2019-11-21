"""
English to Spanish dictionary
"""

from  collections import defaultdict

d1 = defaultdict(str)

english_spanish_dict = dict()
english_spanish_dict["Monday"] = "Lunes"
english_spanish_dict["Tuesday"] = "Martes"
english_spanish_dict["Wednesday"] = "Miercoles"
english_spanish_dict["Thursday"] = "Jueves"
english_spanish_dict["Friday"] = "Viernes"
english_spanish_dict["Saturday"] = "Sabado"
english_spanish_dict["Sunday"] = "Domingo"

print(list(english_spanish_dict.keys()))
print(list(english_spanish_dict.values()))

for key, value in english_spanish_dict.items():
    print(key, ": ", value)

shopping_list = defaultdict(bool)
shopping_list['Ham'] = True
shopping_list['Oreos'] = False
shopping_list['Sugar'] = True
shopping_list['Eggs'] = False

print(shopping_list)
shopping_list.pop('Oreos')
print(shopping_list)
shopping_list['Eggs'] = True
print(shopping_list)
shopping_list.clear()
print(shopping_list)