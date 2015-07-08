def getRight(s):
    row = s[-2]
    column = s[-1]
    newrow = str(int(row) + 1)
    newcolumn = str(int(column) + 1)
    return newrow + newcolumn

def getLeft(s):
    row = s[-2]
    column = s[-1]
    newrow = str(int(row) + 1)
    newcolumn = column 
    return newrow + newcolumn

def buildRouteIndexes(depth): 
    #when i wrote this only god and i knew what it meant
    #now only god knows.
    lst = [] 
    newlst = []
    for i in xrange(depth):
        if i == 0:
            lst.append("00" + getRight("00"))
            lst.append("00" + getLeft("00"))
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
            #indexes.append(int(route[1]))
            route = route[2:]
        _sum = 0
        for index in indexes:
            print index, indexes
            row = index[0]
            col = index[1]
            num = pyramid[row][col]
            _sum += num
        if _sum > maxSum:
            maxSum = _sum

    return maxSum
routes = buildRouteIndexes(14)
triangle =  readTriangle("resources/triangle.txt")
print triangle[0][0]
findMaxRoute(triangle,routes)
