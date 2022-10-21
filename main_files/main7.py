print_sorted_dictionary = __import__('orddict').print_sorted_dictionary
simple_delete = __import__('deletedict').simple_delete
a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low", 'ids': [1, 2, 3] }
new_dict = simple_delete(a_dictionary, 'track')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
print("--")
print("--")
new_dict = simple_delete(a_dictionary, 'c is fun')
print_sorted_dictionary(a_dictionary)
print("--")
print_sorted_dictionary(new_dict)
#once the original is updated or deleted
#you won't get the same value even if the variable is updated
