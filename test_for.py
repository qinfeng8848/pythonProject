
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# Identify unique and common elements
unique_in_list1 = set(list1) - set(list2)
common_elements = set(list1) & set(list2)

# Generate formatted output
output = []
for element in list1:
    if element in unique_in_list1:
        output.append(f"{element} only in List1")
    elif element in common_elements:
        output.append(f"{element} in List1 and List2")

for item in output:
    print(item)





