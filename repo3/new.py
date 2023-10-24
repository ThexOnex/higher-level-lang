original_array = [1, 'apple', 2, 'banana', 3, 'cherry', 4, 'date']
int_array = []
str_array = []

for element in original_array:
    if isinstance(element, int):
        int_array.append(element)
    elif isinstance(element, str):
        str_array.append(element)

print("Integer Array:", int_array)
print("String Array:", str_array)
