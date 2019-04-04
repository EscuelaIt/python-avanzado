import collections
import math


counter = collections.Counter('eggs')

for k in 'eggs':
    print('Count for %s: %d' % (k, counter[k]))


words_list = ("Este es un texto de prueba. Donde se busca contar cuantas veces está una palabra en este texto. "
"Si está más de una vez saldra en un diccionario de resultados. de de de un").split(' ')
print("words_list >>>>", words_list)

counter = collections.Counter(words_list)

result_dict = {word: counter[word] for word in tuple(words_list) if counter[word] > 1}
print("result_dict: ", result_dict)

# Most common values
counter_2 = collections.Counter()
for i in range(0, 100000):
    counter_2[math.sqrt(i) // 25] += 1

for key, count in counter_2.most_common(5):
    print('%s: %d' % (key, count))

result_dict = {key: count for key, count in counter.most_common(10)}
print("result_dict: ", result_dict)


# Operations
eggs = collections.Counter('eggs')
spam = collections.Counter('spam')


def print_counter(expression, counter):
    sorted_characters = sorted(counter.elements()) 
    print(expression, ''.join(sorted_characters))


print_counter('eggs:', eggs) 

print_counter('spam:', spam) 

print_counter('eggs & spam:', eggs & spam) 

print_counter('spam & eggs:', spam & eggs) 

print_counter('eggs - spam:', eggs - spam) 

print_counter('spam - eggs:', spam - eggs) 

print_counter('eggs + spam:', eggs + spam) 

print_counter('spam + eggs:', spam + eggs) 

print_counter('eggs | spam:', eggs | spam) 

print_counter('spam | eggs:', spam | eggs) 
