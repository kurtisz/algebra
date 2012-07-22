def isGroup(S, fxy):
    return isClosed(S, fxy) and isAssociative(S, fxy) and hasIdentity(S, fxy) and haveInverses(S, fxy)

def isClosed(S, fxy):
    for a in S:
        for b in S:
            if not fxy(a,b) in S:
                return False
    return True

def isAssociative(S, fxy):
    for a in S:
        for b in S:
            for c in S:
                if not (fxy(fxy(a,b),c) == fxy(a,fxy(b,c))):
                    return False
    return True

def hasIdentity(S, fxy):
    for a in S:
        isIdentity = True
        for b in S:
            if not ((fxy(a,b) == b) and (fxy(b,a) == b)):
                isIdentity = False
                break
        if isIdentity:
            return True
    return False

def getIdentity(S, fxy):
    for a in S:
        isIdentity = True
        for b in S:
            if not ((fxy(a,b) == b) and (fxy(b,a) == b)):
                isIdentity = False
                break
        if isIdentity:
            return a
    return None

def haveInverses(S, fxy):
    e = getIdentity(S, fxy)
    for a in S:
        if not hasInverse(a, S, fxy, e):
            return False
    return True

def hasInverse(a, S, fxy, e):
    for b in S:
        if (fxy(a,b) == e) and (fxy(b,a) == e):
            return True
    return False

def getInverse(a, S, fxy, e):
    for b in S:
        if (fxy(a,b) == e) and (fxy(b,a) == e):
            return b
    return False

def getOrder(a, fxy, e, groupOrder):
    order = 1
    cum = a
    while (cum != e) and order <= groupOrder:
        cum = fxy(cum,a)
        order += 1
    return order

def isSubgroup(S, G):
    # using the finite subgroup test
    # currently assuming they use the same operation
    for a in S:
        if not a in G:
            return False
        for b in S:
            if not a + b in S:
                return False

def commutes(a, G):
    for b in G:
        if not (a + b == b + a):
            return False
    return True