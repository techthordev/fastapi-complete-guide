"""
Dictionaries
"""

user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Roby',
    'age': 32
}

user_dictionary["married"] = True
# print(user_dictionary.get('name'))
# print(len(user_dictionary))
# user_dictionary.pop("age")
# user_dictionary.clear()
# del user_dictionary
# print(user_dictionary)

# for x, y in user_dictionary.items():
#     print(x, y)

user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age")
print(user_dictionary2)