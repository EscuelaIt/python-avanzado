class Spam(object):
    eggs = 'my eggs'


NewSpam = type('Spam', (object,), dict(eggs='new eggs'))

"""
Type docstring:
type(object_or_name, bases, dict)
type(object) -> the object's type
type(name, bases, dict) -> a new type
# (copied from class doc)
"""

spam = Spam()
print(spam.eggs)

new_spam = NewSpam()
print(new_spam.eggs)
