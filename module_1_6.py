my_dict = {'Dmitry': 1990, 'Grigori': 1985, 'Alisa': 2005}
print(my_dict)
my_dict['Alisa'] = 2005
my_dict['Alex'] = 1993
print(my_dict['Alisa'])
print(my_dict.get('Alex'))
print(my_dict)
my_dict.update({'Maria': 1999, 'Kirill': 2000})
print(my_dict)
print(my_dict.pop('Dmitry'))
print(my_dict)



my_set = {2, 'Python',  9, 0, 2, 0, 9}
print(my_set)
my_set.update({'Java', 8})
print(my_set)
my_set.remove(2)
print(my_set)
