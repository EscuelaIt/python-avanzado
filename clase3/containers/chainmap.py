import builtins
import collections


# No use of Chainmap
def get_builtin_key(key):
    builtin_vars = vars(builtins)
    if key in locals():
        value = locals()[key] 
    elif key in globals():
        value = globals()[key] 
    elif key in builtin_vars:
        value = builtin_vars[key] 
    else:
        raise NameError('name %r is not defined' % key) 
    return value

value = get_builtin_key('dict')
print(type(value))
dict_data = value({'test': "Without use Chainmap"})
print(type(dict_data))
print(dict_data)

# Using Chainmap
mappings = collections.ChainMap(globals(), locals(), vars(builtins))
value = mappings['dict']
print(type(value))

dict_data = value({'test': "Using Chainmap"})
print(type(dict_data))
print(dict_data)


dict_1 = {
    'first_name': "Carlos",
    'last_name': "Martinez"
}

dict_2 = {
    'home_city': "Medellín"
}

combined = collections.ChainMap(dict_1, dict_2)
print(combined.get('first_name'))
print(combined.get('last_name'))
print(combined.get('home_city'))

# Access to mappings
for map_ in combined.maps:
    print(map_)
