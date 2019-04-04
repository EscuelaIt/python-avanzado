import collections

# Normal dict
data_dict = {}
data_dict['last_name'] = "Doe"
data_dict['first_name'] = "Jhon"
data_dict['email'] = "jdoe@fakeemail.com"
print(data_dict)

# Ordered dict
spam = collections.OrderedDict()
spam['last_name'] = "Doe"
spam['first_name'] = "Jhon"
spam['email'] = "jdoe@fakeemail.com"
print(spam)
print(">>>>>>")
print(spam.get('last_name'))
print(spam.get('d'))
print(spam.get('d', "Does not exist"))


for key, value in spam.items():
    print(key, value)

print("print keys")
for key in spam.keys():
    print(key)

# Creating dict using sorted
eggs = collections.OrderedDict(sorted(spam.items()))
print(eggs)
