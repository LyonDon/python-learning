#coding:utf-8
for x in xrange(1,21):
	print(x)
	pass

#下面如果实xrange（）的话，则返回的是一个一个生成器“xrange（1，1000001）”
list=range(1,1000001)
#print(list)

print(max(list))
print(min(list))
print(sum(list))

for x in xrange(1,21,2):
	print(x)
	pass

for x in xrange(1,31,3):
	print(x)
	pass

for x in xrange(1,11):
	print(x**3)
	pass

sum=[x**3 for x in xrange(1,11)]
print(sum)