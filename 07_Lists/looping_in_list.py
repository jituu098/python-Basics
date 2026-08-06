# Looping through a list

fruits = ["Apple", "Banana", "Mango", "Orange", "Grapes"]

## display all the items present in the list
print("Using a for loop:")
for fruit in fruits:
    print(fruit)

#  print items with index
print("\nUsing index:")
for index in range(len(fruits)):
    print(f"Index {index}: {fruits[index]}")

print("\nUsing enumerate():")
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")