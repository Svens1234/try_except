#print('Some code')
#print(my_variable)
#try:
    #print(my_variable)
#except:
    #print('Some error has happen')
#print('Code after after error')


#print('Some code')
#try:
    #print(my_variable)
#except:
    #print('NameError has happen')
#print('Code after after error')


#print('Some code')
#try:
    #print(len(23))
    #print(my_variable)
#except:
    #print('NameError has happen')
#print('Code after error')




#print('Some code')
#try:
    #print(len(23))
    #print(my_variable)
#except NameError:
    #print('NameError has happen')
#except TypeError:
    #print('TypeError has happen')
#print('Code after error')






#user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}

#print(user_dictionary['last_name'])
#print(user_dictionary['name'])


#print(user_dictionary.get('last_name'))
#print(user_dictionary.get('name'))


user_dictionary = {'first_name': 'Jack', 'last_name': 'White', 'age': 24}


def get_dictionary_values(dictionary, key):
    try:
        return dictionary[key]
    except KeyError:
        return None


print(get_dictionary_values(user_dictionary, 'age'))
print(get_dictionary_values(user_dictionary, 'a'))
print(get_dictionary_values(user_dictionary, 'first_name'))











