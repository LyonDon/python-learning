#coding:utf-8
Wang_Chen={
		'last_name':'Chen',
		'first_name':'Wang',
		'age':25,
		'City':'BeiJing'},
Zhang_hang={
		'last_name':'hang',
		'first_name':'Zhang',
		'age':25,
		'City':'BeiJing'
	}
people=[Wang_Chen,Zhang_hang]
for person in people:
	print(person)
	pass

'''
print(friend['first_name'])
print(friend['last_name'])
print(friend['age'])
print(friend['City'])
'''

#宠物字典
dog={
	'type':'small',
	'owner':'dell',
}
cat={
	'type':'small',
	'owner':'lucy',
}

pets=[dog,cat]
for pet in pets:
	for name,value in pet.items():
		print(name,value.title())
	pass

#地方字典
favorite_places={
	'Lucy':['BeiJing','Xian','Tronto'],
	'Robe':['Nanjing','Berlin'],
	'Tei':['Hawell'],
}
for place in favorite_places.items():
	print(place)
	pass