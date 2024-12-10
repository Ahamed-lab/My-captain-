
def print_positive_numbers(input_list):
    # Filter positive numbers using list comprehension
    positive_numbers = [num for num in input_list if num > 0]
    return positive_numbers


list1 = [12, -7, 5, 64, -14]
print("Input: list1 =", list1)
print("Output:", ', '.join(map(str, print_positive_numbers(list1))))


list2 = [12, 14, -95, 3]
print("\nInput: list2 =", list2)
print("Output:", print_positive_numbers(list2))


