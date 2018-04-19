#coding:utf-8
friend={'first_name':'Wang','last_name':'Chen','age':25,'City':'BeiJing'}
print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['City'])

#编程词汇
import json
alp={'title':'以首字母大写的方式显示每一个单词',
	'upper':'将字符串全部大写',
	'lower':'将字符串全部小写',
	'rstrip':'消除字符串末尾的空白',
	'append':'在列表末尾添加元素',
	}
print(json.dumps(alp, ensure_ascii=False, encoding='UTF-8'))
print(' ')

alp['pop']='弹出.列表就相当于一个栈，删除列表末尾的元素相当于弹出栈顶的元素'
alp['remove']='根据值删除元素，用于不知道元素位置，但是知道元素指的情况',
alp['sort']='对列表进行（永久）排序'
alp['sort(reverse=True)']='对列表进行反向排序'
alp['sorted']='对列表进行（临时）排序'

#遍历字典
for alpha in alp.items():
	print(json.dumps(alpha, ensure_ascii=False, encoding='UTF-8'))
	pass

#存储河流字典
rivers={'nile':'egypt','Changjiang':'China','Huanghe':'China'}
for river,country in rivers.items():
	print('The '+river+'runs through '+country)
	pass
print(' ')
for river in rivers.keys():
	print(river)
	pass
print(' ')
for country in rivers.values():
	print(country)
	pass
