update_dictionary = __import__('replace_dict').update_dictionary
print_sorted_dictionary = __import__('orddict').print_sorted_dictionary
a_dictionary = { 'language': "C", 'number': 89, 'track': "Low level" }

new_dict = update_dictionary(a_dictionary, 'language', "Python")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
print("--")
print("--")
new_dict = update_dictionary(a_dictionary, 'city', "San Francisco")
print_sorted_dictionary(new_dict)
print("--")
print_sorted_dictionary(a_dictionary)
#after updated you won't find the original dictionary
