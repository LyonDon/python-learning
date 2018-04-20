#coding=utf-8
def make_shirt(size,word):
	print('大小是'+str(size))
	print('字样是'+word)

make_shirt(19,'woe')

def make_shirt(size='big',word='I love Python'):
	print('a '+size+' size'+' with '+word)
	pass

make_shirt()
make_shirt(size='medium')
make_shirt(word='coding')

def describe_city(city,country='China'):
	print(city+' is in '+country)
	pass

describe_city('BeiJing')
describe_city('Sedney','Austrlia')
describe_city('Berlin','Germany')