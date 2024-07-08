##l1 = [1, 2, 3]
##l2 = l1
##
##print('l1: ',id(l1))
##print('l2: ',id(l2))
##print('l1: ',l1)
##print('l2: ',l2)
##l2[0] = 0
##print('****************')
##print('l1: ',id(l1))
##print('l2: ',id(l2))
##print('****************')
##print('l1: ',l1)
##print('l2: ',l2)
##print('****************')
##l1 = [1, 2, 3]
####l2 = l1[:]
##l2 = l1.copy()
##print('l1: ',id(l1))
##print('l2: ',id(l2))
##print('l1: ',l1)
##print('l2: ',l2)
##l2[0] = 0
##print('****************')
##print('l1: ',id(l1))
##print('l2: ',id(l2))
##print('****************')
##print('l1: ',l1)
##print('l2: ',l2)
##print('****************')
##x1 = 5
##x2 = x1
##
##print('x1: ',id(x1))
##print('x2: ',id(x2))
##x2 =+ 1
##
##print('x1: ',id(x1))
##print('x2: ',id(x2))

##x = [1,2,['a','b'],3]
##print(x)
##print(x[2])
##print(x[2][1])
##x = [1,2,['a',[1.1,2.2],'b'],3]
##print(x)
##print(x[2][1][1])
##x = [1,2,['Nasir', 'Khani']]
##print(x)
##print(x[2][0][2])


##l1 = [1, 2, ['a', 'b']]
##l2 = l1.copy()
##print('l1: ',id(l1))
##print('l2: ',id(l2))
##print('l1: ',l1)
##print('l2: ',l2)
##print('****************')
##l2[2][1] = 0
##print('l1: ',l1)
##print('l2: ',l2)
import copy
l1 = [1, 2, ['a', 'b']]
l2 = copy.deepcopy(l1)
print('l1: ',id(l1))
print('l2: ',id(l2))
print('l1: ',l1)
print('l2: ',l2)
print('****************')
l2[2][1] = 0
print('l1: ',l1)
print('l2: ',l2)

































