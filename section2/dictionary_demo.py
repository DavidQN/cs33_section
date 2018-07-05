

# STEP 1:
# Create dictionary
dict_1 = {"item1": 1, "item2": 2}
print(dict_1)
# prints: {'item1': 1, 'item2': 2}


# STEP 2:
# Retrieve a value from the dictionary given the key
print(dict_1["item1"])
# prints: 1


# STEP 3:
# Allocate a new key and value and insert into the dictionary
dict_1["item3"] = 3
print(dict_1)
# prints: {'item1': 1, 'item2': 2, 'item3': 3}


# STEP 4
# Allocate multiple key and value pairs into the dictionary
dict_1.update({"item4": 4, "item5": 5})
print(dict_1)
# prints: {'item1': 1, 'item2': 2, 'item3': 3, 'item4': 4, 'item5': 5}


# Are Dicts hashmaps? In a sense, there is a form of hashing that allows us
# to hash our keys which allows us to retrieve our values efficiently. Don't take my word for it.

a = {}
b = ["some", "list"]
# hash(b)
## should give us an error: list objects are unhashable

a[b] = "some"
# should give us an error: list objects are unhashable
