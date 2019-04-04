def most_significant(value): 
    while value >= 10:
        value //= 10 
    return value

# 1
print(most_significant(12345))

# 9
print(most_significant(99))

# 0
print(most_significant(0))


def add(collection, key, value):
    index = most_significant(key) 
    collection[index].append((key, value))

def contains(collection, key):
    index = most_significant(key) 
    for k, v in collection[index]:
        if k == key:
            return True 
    return False

# Create the collection of 10 lists 
collection = [[], [], [], [], [], [], [], [], [], []]

# Add some items, using key/value pairs
add(collection, 123, 'a')
add(collection, 456, 'b')
add(collection, 789, 'c')
add(collection, 101, 'c')

# Look at the collection 
# [[], [(123, 'a'), (101, 'c')], [], [], [(456, 'b')], [], [], [(789, 'c')], [], []]
print(collection)

# Check if the contains works correctly
# True
print(contains(collection, 123)) 
# False
print(contains(collection, 1))

user_dict = {
    'username': "carlosmart",
    'email': "carlosmart626@gmail.com",
    'twitter': "@carlosmart626",
    'web_page': "https://carlosmart.dev"
}
print(user_dict)
print(user_dict.keys())

class User:

    def __init__(self, username, email, twitter, web_page):
        self.username = username
        self.email = email
        self.twitter = twitter
        self.web_page = web_page

    def __str__(self):
        return f"{self.username}"

user = User(**user_dict)
print("user: ", user)

print(user.__dict__)
print(dir(user))
print(user.__class__(username='Mario', email='1231', twitter="123", web_page="asda"))
