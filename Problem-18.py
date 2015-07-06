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
"""jstart = "00"
lst = []
lst.append(start + getRight("00"))
lst.append(start + getLeft("00"))
print lst

newlst = []
for r in lst:
    newlst.append(r + getRight(r))
    newlst.append(r + getLeft(r))

lst = newlst
newlst = []
print lst,newlst
for r in lst:
    newlst.append(r + getRight(r))
    newlst.append(r + getLeft(r))

lst = newlst
newlst = []
print lst,newlst
for r in lst:
    newlst.append(r + getRight(r))
    newlst.append(r + getLeft(r))

print len(newlst )
"""
def recu(depth): 
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
print recu(14)
