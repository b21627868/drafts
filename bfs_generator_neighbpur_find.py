graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

#def bfs(graph, forefront, end):
    # assumes no cycles
   # next_forefront = []
  #  for i, path in forefront:
   #     if i in graph:
    #        for node in graph[i]:
     #           next_forefront.append((node, path + ',' + node))

#    for node,path in next_forefront:
 #       if node==end:
  #          return path
    #else:
   #     return bfs(graph,next_forefront,end)

#print (bfs(graph,[('A','A')],'F'))
commands = {}
nodes = {}
with open("Commands_12", "r") as c:
    for cmd in c.read().splitlines():
        commands.setdefault(int(cmd.split("\t")[0]), []).append(cmd.split("\t")[1:])

print(commands)
print(commands[0])
def create_node(name, pos, range, battery_level):
    nodes[name] = [
        int(pos.split(";")[0]), #posX
        int(pos.split(";")[1]), #posY
        int(range.split(";")[0]), #rangeX1
        int(range.split(";")[1]), #rangeX2
        int(range.split(";")[2]), #rangeY1
        int(range.split(";")[3]), #rangeY2
        int(battery_level)
    ]

    print("\tCOMMAND *CRNODE*: New node " + name + " is created")
time=0
for k in commands.get(time):
    print(k)
   # if t[0] == "CRNODE":
    #    create_node(t)

#import collections
#neighbours=collections.OrderedDict([('x1', ['x2', 'x3']), ('x2', ['x4', 'x5']), ('x3', ['x6', 'x8']), ('x4', ['x5', 'x7']), ('x5', ['x7']), ('x6', ['x7', 'x8']), ('x7', ['x9']), ('x8', []), ('x9', [])])
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
pathh = []
def bfs(graph, forefront, end):
    global pathh
    # assumes no cycles
    next_forefront = []
    for i, path in forefront:
        if i in graph:
            for node in graph[i]:
                if node not in path and end not in path:
                    next_forefront.append((node, path + ',' + node))

    for node,path in next_forefront:
        if node==end:
            pathh.append(path)
    else:
        print(pathh)
        return bfs(graph,next_forefront,end)

print (bfs(graph,[('A','A')],'F'))