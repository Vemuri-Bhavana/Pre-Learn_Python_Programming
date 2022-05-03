num_list=['a','c','b']
for position,val in enumerate(num_list):
    print (position, val)
print(sorted(num_list))
print(list(reversed(num_list)))
list_2=['h','i','j']
zipped_list=zip(num_list,list_2)
print(list(zipped_list))
