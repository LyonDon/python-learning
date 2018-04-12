#!/usr/bin/python
#-*- coding:utf-8 -*-

list=['Bill Gates','Steve Jobs','Kobe']
print(list)
print(list[0]+" can't come because he's too busy\nSo,I need to make a plan B")
list[0]='Yao Ming'
print(list)
list.append('Jay lee')
list.append("周星驰")
list.append('Jackie Chan')
print(str(list).decode('string_escape'))
list.insert(0,'Trump')
print(str(list).decode('string_escape'))
print("I think I've invited "+str(len(list))+" guests")

print("sorry that I can only invite two people")
poped=list.pop(0)
print('sorry'+' '+poped)
poped=list.pop(0)
print('sorry'+' '+poped)
poped=list.pop(0)
print('sorry'+' '+poped)
poped=list.pop(0)
print('sorry'+' '+poped)
poped=list.pop(0)
print('sorry'+' '+poped)

#print(str(list).decode('string_escape'))
print(list[0]+' you are still invited')
print(list[1]+' you are still invited')

del list[0]
del list[0]
print(list)