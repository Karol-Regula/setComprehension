def union(a, b):#performs union operation
  out = [x for x in a]
  out2 = [x for x in b if x not in out]
  out += out2
  out.sort()
  return out

def intersection(a, b):#performs intersection operation
  out = [x for x in a if x in b]
  return out

def setDifference(a, b):#returns set difference of a and b, (members of a that are not in b)
  out = [x for x in a if x not in b]
  return out

def symmetricDifference(a, b):#returns the symmetric differnce of a and b, (member in exactly one of a and b)
  out = setDifference(a, b)
  out2 = setDifference(b, a)
  out += out2
  out.sort()
  return out

def cartesianProduct(a, b):#returns the cartesian product of a and b, (all possible ordered pairs of elements from a and b)
  out = [(x, y) for x in a for y in b]
  return out

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [2, 5, 8, 9]
l3 = [2, 4, 7]

print "l1: " + str(l1)
print "l2: " + str(l2)
print "l3: " + str(l3)
print ''

print "union (l2, l3): " + str(union(l2, l3))
print "intersection (l1, l2): " + str(intersection(l1, l2))
print "setDifference (l1, l2): " + str(setDifference(l1, l2))
print "symmetricDifference (l2, l3): " + str(symmetricDifference(l2, l3))
print "cartesianProduct (l2, l3): " + str(cartesianProduct(l2, l3))
