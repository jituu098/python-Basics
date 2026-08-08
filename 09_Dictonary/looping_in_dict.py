age = { "jitu":22, "Raj":18, "saurab":20, "Digen":16}
print("using key method")
for k in age.keys():
    print(k)

print("using values method")
for v in age.values():
    print(v)

print("using items method")
for k,v in age.items():
    print(k,":",v)

print("Checking whether a keys or values in dict")
print("jitu"in age.keys())
print(20 in age.values())

print("\nconverting it to a list")
print(age.keys())
print(list(age.keys()))
print(list(age.values()))
print(age.values())
print(list(age.values()))

print("\n+using get method")
print("I am", str(age.get("jitesh",0)), "age")
print("I am", str(age.get("jitu",0)), "age")

print("\nusing setdefault method")
age.setdefault("abhes","19")
print(age)
