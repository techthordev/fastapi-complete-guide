"""
String Formatting
"""

first_name = "Thor"
# print("Hi " +first_name)

print(f"Hi {first_name}")

sentence = "Hi {} {}"
last_name = "SonOfOdin"
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")