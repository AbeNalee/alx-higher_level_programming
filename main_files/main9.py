complex_delete = __import__('deletebykey').complex_delete
print_sorted_dictionary = __import__('orddict').print_sorted_dictionary
a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
value = "C"
deleted_dict = complex_delete(a_dictionary, value)
print_sorted_dictionary(deleted_dict)
print("--")
print_sorted_dictionary(a_dictionary)
print("--")
print("--")
deleted_dict = complex_delete(a_dictionary, 'c is fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(deleted_dict)
