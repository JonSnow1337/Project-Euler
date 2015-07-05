r = [[[0,0]]]
def getLeft(route):
    lastPoint = route[-1]
    #up row by one, column same
    #print lastPoint[0] + 1, lastPoint[1]
    return [lastPoint[0] + 1, lastPoint[1]]

def appendLeft(route):
    #print route
    lastPoint = route[-1]
    #up row by one, column same
    #print lastPoint[0] + 1, lastPoint[1]
    route.append([lastPoint[0] + 1, lastPoint[1]])
    #print route
    return route

def getRight(route):
    lastPoint = route[-1]
    #up row by one, column by one 
    #print lastPoint[0] + 1, lastPoint[1]  + 1 
    return [lastPoint[0] + 1, lastPoint[1]  + 1 ]

def appendRight(route):
    #print route
    lastPoint = route[-1]
    #up row by one, column by one 
    #print lastPoint[0] + 1, lastPoint[1]  + 1 
    route.append([lastPoint[0] + 1, lastPoint[1]  + 1 ])
    #print route
    return route


x = [] 
def buildRoutes(depth):
    if depth == 0:
        return [[0,0]]
    else:
        for i in range(depth):
            r1 = appendRight(buildRoutes(depth -1))
            r2 = appendLeft(buildRoutes(depth - 1))
            print "r1"
            print r1
            print "r2"
            print r2
            print "r2 r1"
            print r1 + r2
            return r1 + r2

x = buildRoutes(0)
print x

x = buildRoutes(3)
print x
