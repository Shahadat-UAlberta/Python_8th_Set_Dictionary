"""
# Dictionary

-key : value pairs
-Unordered

[0] : "Python"
[1] : "Python"

key1 : "Python"
key2 : "Python"
"""

# Empty Dictionary

my_dict = {}
print(type(my_dict))  # <class 'dict">

my_dict2 = dict()
print(type(my_dict2))  # <class 'dict'>

# With value

my_dict = {
    "name": "Md Shahadat Hossain",
    "fav_language": "python-01",
    "one": 1,
    "two": 2.5,
    "lst": [1, 2, 3, 4],
        1: "One",
}

print(my_dict)  #{'name': 'Md Shahadat Hossain', 'fav_language': 'python-01', 'one': 1, 'two': 2.5, 'lst': [1, 2, 3, 4], 1: 'One',}


my_dict2 = dict({
    "name": "Shahadat",
    "fav_language": "Python-02",
    "fav_language2": "Java",
    "fav_language3": "C++",
    "fav_language4": "C",
    "one": 1,
    "two": 2.5,
    "lst": [1, 2, 3, 4],
    1: "One"


})

print(my_dict2)  # {'name': 'Shahadat', 'fav_language': 'Python-02'}

# Access

print(my_dict["name"])  # Md Shahadat Hossain
print(my_dict2["name"])  # Shahadat

print(my_dict.get("name"))  # Md Shahadat Hossain
print(my_dict2.get("name"))  # Shahadat



print(my_dict2[1])
print(my_dict2.get(1))
print(my_dict["lst"])

my_dict3 = {
    1 : 1,
    2: 5.5
}
print(my_dict3.get(2))

# Update / add
print("___________")
print(my_dict3)

my_dict3[1] = "One"
print(my_dict3)

my_dict3[3] = "Three"
print(my_dict3)

# Remove
print(my_dict3.pop(1))
print(my_dict3)

my_dict3.clear()
print(my_dict3)
