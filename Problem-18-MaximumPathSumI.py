"""
By starting at the top of the triangle below and moving to adjacent numbers on
 the row below, the maximum total from top to bottom is 23.

Find the maximum total from top to bottom of the triangle below:

How it works:
 -First i build all the possible routes from top to bottom
 -they are build by going left(adding 1 to row index,
 and going right(1 to col and 1 to row)
 -For each route i go once left, once right and that made 2 new routes
 -The old route is deleted.
 -in the end i have 2 to the power 10 routes
 -Routes are stored as [0,0 ,1,0 , 2,0] etc
 -Hardest part done, i just go through the pyramid using routes,
 adding all the numbers pyramid has at those indexes
 -And then i return the largest.

Optimization Posibility:
 -instead of calculating sum of routes for each and every route,
  we can store previous sums and use those while calculating new ones.
"""
def getRight(s):
    row = s[-2] 
    column = s[-1]
    newrow = row + 1
    newcolumn = column + 1
    return [newrow , newcolumn]

def getLeft(s):
    row = s[-2]
    column = s[-1]
    newrow = row + 1
    newcolumn = column 
    return [newrow,newcolumn]

def buildRouteIndexes(depth): 
    #when i wrote this only god and i knew what it meant
    #now only god knows.
    lst = [] 
    newlst = []
    for i in xrange(depth):
        if i == 0:
            lst.append([0,0] + getRight([0,0]))
            lst.append([0,0] + getLeft([0,0]))
        else:
            newlst = []
            for r in lst:
                newlst.append(r + getRight(r))
                newlst.append(r + getLeft(r))
            lst = newlst

    return lst

def readTriangle(txtFile):
    with open(txtFile) as triangle:
        lines = triangle.read().splitlines()
        pyramid = []
        for line in lines:
            pyramid.append(line.split(" "))

    return pyramid

def findMaxRoute(triangle, routes):
    maxSum = 0
    for route in routes:
        #split every route by two nums
        #first num is route row, second column
        indexes = []
        for i in xrange(len(route) / 2):
            indexes.append([int(route[0]), int(route[1])])
            route = route[2:]
        _sum = 0
        for index in indexes:
            row = index[0]
            col = index[1]
            num = int(triangle[row][col])
            _sum += num
        if _sum > maxSum:
            maxSum = _sum

    return maxSum

if __name__ == "__main__":
    routes = buildRouteIndexes(14)
    triangle =  readTriangle("resources/triangle.txt")
    print findMaxRoute(triangle,routes)
