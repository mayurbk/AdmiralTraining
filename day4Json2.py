a = {4:1,6:2,7:{8:3,9:4,5:{10:5},2:6,6:{3:7,1:8}}}
print(type(a))

def nD(d):
    for v in d.values():
        if isinstance(v,dict):
            yield from nD(v)
        else:
            yield v
print(list(nD(a)))

