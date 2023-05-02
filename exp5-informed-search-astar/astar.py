import math
sld = {

    'A':19,
    'B':12.6,
    'C':8.6,
    'D':5.8,
    'E':2.25,
    'F':11,
    'I':14,
    'J':8,
    'G':0
}

coords = {

    'A':[0,18],
    'B':[2,13],
    'C':[1,8],
    'D':[3,6],
    'E':[4,0],
    'F':[5,12],
    'G':[6,1],
    'I':[4,15],
    'J':[6,9]
}

def getEuclideanDist(x1,y1,x2,y2):
    return math.sqrt(math.pow(x2-x1,2) + math.pow(y2-y1, 2))

graph = {

    'A':['B','C'],
    'B':['I','D'],
    'C':['D'],
    'D':['E'],
    'E':['G'],
    'F':['D','J'],
    'G':[''],
    'I':['F'],
    'J':['G']
    
}

def getPathCost(path):
    nodes = path.split("-->")
    cost = 0
    for i in range(1,len(nodes)):
        cost += getEuclideanDist(coords[nodes[i-1]][0] , coords[nodes[i-1]][1] , coords[nodes[i]][0]  , coords[nodes[i]][1])
    cost +=sld[nodes[-1]]
    return cost

open_list = [['A' , getPathCost('A')]]
solutions = []

flag = 0
count = 0
while True:
    if flag == 1 or len(open_list) == 0:
        break
    path = open_list[0][0]
    count += 1
    print('\nIt', count)
    end = path.split('-->')[-1]
    while end == 'G':
        open_list.remove([path, getPathCost(path)])
        solutions.append([path, getPathCost(path)])
        if len(open_list) == 0:
            flag = 1
            break
        path = open_list[0][0]
        end = path.split('-->')[-1]
    if len(open_list) != 0:
        for n in graph[end]:
            new_path = path + '-->' + n
            open_list.append([new_path, getPathCost(new_path)])
        open_list.remove([path, getPathCost(path)])
        open_list.sort(key=lambda x:x[1])
        for x in open_list:
            print('{:<40s} Cost:{:f}'.format(x[0],x[1]))
    else:
        print('\nPossible Solutions are:')
        for sol in solutions:
            print(sol[0])
        print('\nOptimal Solution is ', solutions[0][0])
        print('Optimal Cost is ',solutions[0][1])
        print()
    