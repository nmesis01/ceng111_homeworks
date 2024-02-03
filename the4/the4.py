def get_families(T):
    if T == []:
        return []
    if type(T[0]) == str:
        temp = []
        nest = []
        for i in T:
            if type(i) == str:
                temp.append(i)
            elif type(i) == list:
                temp.append(i[0])
                nest.append(i)
        return [temp] + get_families(nest)
    else:
        return get_families(T[0])+get_families(T[1:])
def brothers(T,pname):
    families = get_families(T)
    bros = []
    for i in families:
        if pname in i and pname != i[0]:
            for m in i:
                if m != i[0] and pname != m and m[0] == m[0].lower():
                    bros.append(m)
    return bros
def sisters(T,pname):
    result = get_families(T)
    siss = []
    for i in result:
        if pname in i and pname != i[0]:
            for m in i:
                if m != i[0] and pname != m and m[0] == m[0].upper():
                    siss.append(m)
    return siss
def siblings(T,pname):
    bros = brothers(T,pname)
    siss = sisters(T,pname)
    return bros + siss
def uncles(T,pname):
    parent = find_parent(T,pname)
    uncles = brothers(T,parent)
    return uncles
def aunts(T,pname):
    parent = find_parent(T,pname)
    uncles = sisters(T,parent)
    return uncles
def find_parent(T,pname):
    families = get_families(T)
    for i in families:
        if pname in i and i[0] != pname:
            return i[0]
def cousins(T,pname):
    parent = find_parent(T,pname)
    sibs = siblings(T,parent)
    cousins = []
    for i in sibs:
        cousins += find_childs(T,i)
    return cousins
def find_childs(T,pname):
    families = get_families(T)
    childs = []
    for i in families:
        if i[0] == pname:
            for k in i:
                if k != pname:
                    childs.append(k)
    return childs
