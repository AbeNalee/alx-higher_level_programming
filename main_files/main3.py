multiply_by_2 = __import__('mul2dict').multiply_by_2
print_sorted_dictionary = __import__('orddict').print_sorted_dictionary
a_dictionary = {'John': 12, 'Alex': 8, 'Bob': 14, 'Mike': 14, 'Molly': 16}
multiply = multiply_by_2(a_dictionary)
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(multiply)
