import collections
import json
import pprint

# Without use default dict
nodes = [
    ('a', 'b'),
    ('a', 'c'), 
    ('b', 'a'), 
    ('b', 'd'), 
    ('c', 'a'), 
    ('d', 'a'), 
    ('d', 'b'), 
    ('d', 'c'),
]

graph = dict()

for from_, to in nodes:
    if from_ not in graph: 
        graph[from_] = [] 
    graph[from_].append(to)

pprint.pprint(graph)

# Using default dict
graph = collections.defaultdict(list)

for from_, to in nodes:
    graph[from_].append(to)

pprint.pprint(graph)

print(graph.get('a'))

# Default value operations

counter = collections.defaultdict(int)

counter['spam'] += 10

pprint.pprint(counter)

# Creating trees

def tree():
    return collections.defaultdict(tree)

colours = tree()
colours['other']['black'] = 0x000000
colours['other']['white'] = 0xFFFFFF
colours['primary']['red'] = 0xFF0000
colours['primary']['green'] = 0x00FF00
colours['primary']['blue'] = 0x0000FF
colours['secondary']['yellow'] = 0xFFFF00
colours['secondary']['aqua'] = 0x00FFFF
colours['secondary']['fuchsia'] = 0xFF00FF

print(colours)
print(json.dumps(colours, sort_keys=True, indent=4))
