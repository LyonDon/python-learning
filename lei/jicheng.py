#coding=utf-8
class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type
		self.number_served=0

	def describe_restaurant(self):
		print('restaurant_name is '+self.restaurant_name.title())
		print('cuisine_type is '+self.cuisine_type.title())

	def open_restaurant(self):
		print('The restaurant is open')

	def number_served_people(self):
		print('there are '+str(self.number_served)+' people in the restaurant')
		pass

	def set_number_served(self):
		self.number_served=int(input('请输入就餐人数:'))
		print(self.number_served)
		pass

	def increment_number_served(self,people):
		self.number_served+=people
		pass

class IceCreamStand(Restaurant):
	"""docstring for IceCreamStand"""
	def __init__(self,restaurant_name,cuisine_type):
		super(IceCreamStand,self).__init__(restaurant_name,cuisine_type)
		self.flavors=['sweet','spicy','cold']

	def IceCream(self):
		print(self.flavors)

IceCreamStand=IceCreamStand('a','b')
IceCreamStand.IceCream()