def test(mylist,i):
    return sum (mylist[:i]) == i

mylist = [1,1,1,1,1]

i = 2

print (test(mylist,i))