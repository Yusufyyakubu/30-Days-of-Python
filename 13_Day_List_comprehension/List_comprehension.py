# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
filtered = [n for n in numbers if(n<=0)]
print(filtered)


# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
one_dimensional = [x for lst in list_of_lists for l in lst for x in l]
print(one_dimensional)

#Using list comprehension create the following list of tuples

lst = [(a,b,a,a**2,a**3,a**4,a**5) 
        for a in range(0,11)
        for b in [1]
      ]

print(lst)



# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output Required
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]

new_list = [[item[0].upper(),item[0].upper()[:3],item[1].upper()]  for country in countries for item in country ]
print(new_list)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [
            {'country' : item[0].upper(), 'city' : item[1].upper()}
            for country in countries
            for item in country
]

print(new_list)


# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output required
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']

new_list = ["{} {}".format(item[0], item[1]) 
            for tuples in names for item in tuples 
           ]

print(new_list)





