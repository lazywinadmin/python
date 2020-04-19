p = True
q = True
print not (p or not q)

p = True
q = False
print not (p or not q)


p = False
q = True
print not (p or not q)

p = False
q = False
print not (p or not q)
