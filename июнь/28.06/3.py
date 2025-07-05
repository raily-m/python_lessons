dict = {
    "a": 1,
    "b": 2,
    "c": 3, 
}
dict["e"] = 4
keys = list(dict.keys())
value = list(dict.values())


print(f"список ключей: {keys}")
print(f"список значений: {value}")

new_dict = {}

for keys,value in dict.items():
    new_dict[value] = keys

print(new_dict)

