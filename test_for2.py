# Defining a function to compare two lists and return a formatted output
def compare_lists(list1, list2):
    unique_in_list1 = set(list1) - set(list2)
    common_elements = set(list1) & set(list2)
    output = []
    for element in list1:
        if element in unique_in_list1:
            output.append(f"{element} only in List1")
        elif element in common_elements:
            output.append(f"{element} in List1 and List2")
    return output

# Example lists
list1 = ['aaa', 111, (4, 5), 2.01]
list2 = ['bbb', 333, 111, 3.14, (4, 5)]

# Using the function to compare the lists
formatted_output = compare_lists(list1, list2)
for item in formatted_output:
    print(item)

