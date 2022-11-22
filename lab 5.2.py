sample_dict = {
    "name":"Kelly",
    "Surname":"Jones",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

for key, value in sample_dict.items():
    print(f'{key:<10}:{value:>10}')
for key in sample_dict.keys():
    print(key,sample_dict[key])
l1=["age","salary","name", "jik"]
newdict = {}
for key in l1:
    if key in sample_dict.keys():
        newdict[key]=sample_dict[key]
print(newdict)

for key in l1:
    print(sample_dict.pop(key,"x"))
if "Jones" in sample_dict.values():
    print("mhm")
else:
    print("wagh")

sample_dict["location"] = sample_dict.pop("city")
print(sample_dict)

g = {}
key = 1
for key in range(1,16):
    g[key] = key*key
print(g)



