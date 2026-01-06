"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""

def user_dictionary(firstname, lastname, age):
    create_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return create_user_dictionary
    
solution_dictionary = user_dictionary("John", "Doe", 30)
print(solution_dictionary)