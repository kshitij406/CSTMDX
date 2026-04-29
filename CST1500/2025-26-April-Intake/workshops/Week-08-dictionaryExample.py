sample_dict = {"name": "Kelly", "age": 25, "salary": 8000, "city": "New york"}

print("\nOriginal Dictionary: \n" + str(sample_dict))

# keys to extract
keys = ["name", "salary"]

# new dict
res = dict()

for k in keys:
    # add current key with its value from sample_dict
    res.update({k: sample_dict[k]})

print("\nNew Dictionary:")
print(res)
print("\n")
