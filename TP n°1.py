# Exercice 1:

def croiss1(l):
    drap, prec = True, min(l)
    for ele in l:
        drap = ele >= prec and drap
        if not(drap):
            return False
        prec = ele
    return True

def croiss2(l):
    return l == sorted(l)

l = [1, 4, 5, 2, 6]
print(croiss1(l))
print(croiss2(l))

l = [1, 2, 4, 5, 6]
print(croiss1(l))
print(croiss2(l))


# Exercice 3 :

l = [0, 1, 2, 1, 2]
a = id(l)

# 1) l[:] = l[:] + [10]
# 2) l[:] = [l[0]] + [10] + l[1:]
# 3) l[:] = l[::-1]
# 4) l[:] = [l[0]] + l[2:]
# 5) l[:] = l[1:4]
# 6) l[:] = l[1:4] * 3
# 7) l[:] = []

print(l)
print(a == id(l))


# Exercice 4 :

# 1)
def g(l):
    for x in l[:]:
        l.append(x)
        
l = [1, 2, 3]
g(l)
print(l)

# 2)
def h(l):
    l[:] = l * 2
    
l = [1, 2, 3]
h(l)
print(l)


# Exercice 5 :

def tousDistincts(L):
    tousDiff = True
    for i in range(len(L)):
        if L[i] in L[i + 1:]:
            tousDiff = False
            break
        else:
            tousDiff = True
    return tousDiff
    
l =  [1, 5, 2, 5, 3, 4, 2]
print(tousDistincts(l))

