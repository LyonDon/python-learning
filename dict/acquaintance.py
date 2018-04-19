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