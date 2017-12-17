import sys
import math

commands = dict()
nodes = dict()
relations = dict()

routes = []

data_size = 0
packet_size = float(sys.argv[1])
remaining_data_size = 0.0
number_of_packets = 0

node_source = None
node_target = None

# calculate relations for given node


def calculate_relations(node_name):

    global relations

    c = nodes[node_name]
    neighbors = []
    for n, p in nodes.items():

        if n != node_name:
            if c[0]-c[3] <= p[0] <= c[0]+c[2] and c[1]-c[5] <= p[1] <= c[1]+c[4]:
                neighbors.append(n)

        relations[node_name] = neighbors


# calculates possible routes with existing nodes
def calculate_routes():
    for n in nodes.keys():
        calculate_relations(n)

    if len(routes) > 0:
        routes.clear()

    out = "\tNODES & THEIR NEIGHBORS:"

    for n, p in relations.items():
        out += "%s -> %s |" % (n, ", ".join(p))

    print(out)

    get_next_node(node_source, node_target)

    if len(routes) > 0 :
        print("\t%d ROUTE(S) FOUND:" % (len(routes)))
        for i in range(0, len(routes)):
            print("\tROUTE %d:%s\tCOST: %0.4f"% (i + 1, " -> ".join(routes[i]), get_route_cost(routes[i])))

        select_best_route()
    else:
        print("\tNO ROUTE FROM %s TO %s FOUND" % (node_source, node_target))
        exit_program()

# the recursive next node calculator


def get_next_node(node_name, node_target, path=None, level=0):

    if path is None:
        path = dict()

    path[level] = node_name

    if path[level] == node_target:

        valid_path = []
        for i in range(level + 1):
            valid_path.append(path[i])

        routes.append(valid_path)

    elif len(relations[node_name]) > 0:
        for n in relations[node_name]:
            found = False
            for x in range(level):
                if path[x] == n:
                    found = True
                    break
            if found:
                continue
            get_next_node(n, node_target, path, level + 1)

# get cost between two given nodes


def get_cost(source, target):
    dist = math.hypot(target[0] - source[0], target[1] - source[1])
    bat = target[6]
    return dist / bat

# get total cost for given specific route nodes


def get_route_cost(route_nodes):

    cost = 0.0

    for i in range(0, len(route_nodes) - 1):
        cost += get_cost(nodes.get(route_nodes[i]), nodes.get(route_nodes[i + 1]))
    return cost

# route cost comparator and prints the best cost route


def select_best_route():

    opt_cost = get_route_cost(routes[0])
    r = 0
    for i in range(1, len(routes)):
        cost = get_route_cost(routes[i])
        if cost < opt_cost:
            r = i
            opt_cost = cost
    print("\tSELECTED ROUTE (ROUTE %d):%s" % (r + 1, " -> ".join(routes[r])))
    return r

# prepare *SEND* data
def prepare_data(source, target, size):

    global number_of_packets, remaining_data_size, data_size, node_source, node_target

    print("\tCOMMAND *SEND*: Data is ready to send from %s to %s" % (source, target))
    data_size = float(size)
    number_of_packets = abs(float(data_size) / packet_size)
    remaining_data_size = data_size
    node_source = source
    node_target = target

# the function called during simulation time until there is no available packet to send
def send_data(time):

    global remaining_data_size

    print("\tPACKET %d HAS BEEN SENT"% (time + 1))
    remaining_data_size -= min(remaining_data_size, packet_size)
    print("\tREMAINING DATA SIZE: %0.1f BYTE" % remaining_data_size)


# create node
def create_node(name, pos, range, battery_level):
    nodes[name] = [
        float(pos.split(";")[0]), #posX
        float(pos.split(";")[1]), #posY
        float(range.split(";")[0]), #rangeX1
        float(range.split(";")[1]), #rangeX2
        float(range.split(";")[2]), #rangeY1
        float(range.split(";")[3]), #rangeY2
        float(battery_level)
    ]

    print("\tCOMMAND *CRNODE*: New node " + name + " is created")


# remove given node
def remove_node(name):

    global nodes,relations

    try:
        del nodes[name]
        del relations[name]

        print("\tCOMMAND *RMNODE*: Node " + name + " is removed")

        #calculate_routes()

    except KeyError:
        pass

# move given node
def move_node(name, pos):
    if nodes[name] != None:
        nodes[name][0] = int(pos.split(";")[0]) #posX
        nodes[name][1] = int(pos.split(";")[1]) #posY

        print("\tCOMMAND *MOVE*: The location of node " + name + " is changed")

        #calculate_routes()

# change battery for given node
def change_battery(name, bat):
    if nodes[name] != None:
        nodes[name][6] = int(bat)

        print("\tCOMMAND *CHBTTRY*: Battery level of node %s is changed to %d" % (name, int(bat)))

        #calculate_routes()


# exit program - used if there is no available route
def exit_program():
    print("********************************")
    print("AD-HOC NETWORK SIMULATOR - END")
    print("********************************")
    exit(0)


# program start here
print("********************************")
print("AD-HOC NETWORK SIMULATOR - BEGIN")
print("********************************")

# read the command file and store them for later evaluation
with open("commands", "r") as c:
    for cmd in c.read().splitlines():
        commands.setdefault(int(cmd.split("\t")[0]), []).append(cmd.split("\t")[1:])
time = 0
init = True
# process the commands here
while number_of_packets > 0 or init:

    print("SIMULATION TIME: %02d:%02d:%02d" % (time / 3600, (time / 60) % 60, time % 60))
    if commands.get(time) is not None:
        for params in commands.get(time):
            if params[0] == "CRNODE":
                create_node(params[1], params[2], params[3], params[4])
                #if not init:
                    #calculate_routes()
            if params[0] == "RMNODE":
                remove_node(params[1])
            if params[0] == "SEND":
                prepare_data(params[1], params[2], params[3])
            if params[0] == "MOVE":
                move_node(params[1], params[2])
            if params[0] == "CHBTTRY":
                change_battery(params[1], params[2])
        if params[0] == "RMNODE" or params[0] == "MOVE" or params[0] == "CHBTTRY" or params[0] == "CRNODE":
            calculate_routes()
    if init:
        calculate_routes()

    send_data(time)
    number_of_packets -= 1
    time += 1

    init = False
exit_program()
