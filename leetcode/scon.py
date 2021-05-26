inp=input()
 
a=set({})
max=[]


def test(l):
    a.clear()
    for i in l:

        # print(i)
        lenbe=len(a)
        a.add(i)
        lenaf=len(a)
        if lenaf == lenbe:
            max.append(lenbe)
            return 0

 
for ii in range(len(inp)):
    test(inp[ii:])
    # print(v[ii:])


# test('bbbbb')
max.sort()

print(max[-1])
