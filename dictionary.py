my_dict = {"a":"alpha", "o": "omega", "g": "gamma"}
print(my_dict)
print(my_dict.get("a","Nothing found for key a"))
print(my_dict.get("z", "nothing found for key z"))


my_dict = {"a":"alpha", "o": "omega", "g": "gamma"}
print("Retrieving a value from  the dictionary using it's key:")
print(my_dict["a"])
print(my_dict["z"])

my_dict["d"] = "delta"
print(my_dict)