from functools import reduce
slist=[1,2,3,4,5,6,7,8,9,10]
mlist=[1,4,5,6,8,9,10,11,13,15,16,17,19]
def sum_ele(a):
    m=0
    for i in range(len(a)):
        m=m+a[i]
    return m
print(sum_ele(slist))
print(sum_ele(mlist))
print(list(map(lambda x:x*x,slist)))
print(list(map(lambda y:y*y,mlist)))
print(list(filter(lambda val: val%2!=0, slist)))
print(list(filter(lambda val: val%2==0, slist)))
print(list(filter(lambda val: val%2!=0, mlist)))
print(list(filter(lambda val: val%2==0, mlist)))
#sum of all the number in the list
print(reduce(lambda x,y:x+y,slist))
print(reduce(lambda x,y:x+y,mlist))
#product of all the elements in list
print(reduce(lambda x,y:x*y,slist))
print(reduce(lambda x,y:x*y,mlist))
xlist=[['abc',1],['xyz',3],['pqr',2],['klm',4]]
print(list(sorted(xlist,key=lambda x:x[1])))