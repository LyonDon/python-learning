#coding=utf-8
#城市返回值函数
'''
def city_country(city,country):
	city_country='"'+city+','+country+'"'
#	print(city_country)
	return city_country
	pass

print(city_country('beijing','China'))
print(city_country('Berlin','Germany'))
print(city_country('Sedney','Austrlia'))

#设置一个可选实参，num指向一个空字符串
def make_album(name,album,num=''):
	if num:
		make_album=[name,album,num]
		pass
	else:
		make_album=[name,album]
		pass
	return make_album

print(make_album('a','b',num=10))
print(make_album('c','d'))
print(make_album('e','f',num=8))
'''
#用户自定义
def make_album(name,album,num=''):
	if num:
		make_album=[name,album,num]
		pass
	else:
		make_album=[name,album]
		pass
	return make_album

while True:

	print('enter q when you want to quit:')
	name=raw_input('请输入歌手的名字:')
	if name=='q':
		break
		pass
	album=raw_input('请输入专辑的名字:')
	if album=='q':
		break
		pass
	num=raw_input('请输入歌曲的数量:')
	if num=='q':
		break
		pass

	print(make_album(name,album,num))
