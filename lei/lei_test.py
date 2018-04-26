#coding=utf-8
class Restaurant(object):
	"""docstring for Restaurant"""
	def __init__(self,restaurant_name,cuisine_type):
		self.restaurant_name=restaurant_name
		self.cuisine_type=cuisine_type

	def describe_restaurant(self):
		print('restaurant_name is '+self.restaurant_name.title())
		print('cuisine_type is '+self.cuisine_type.title())

	def open_restaurant(self):
		print('The restaurant is open')

restaurant=Restaurant("Yao","noddles")

restaurant.describe_restaurant()
restaurant.open_restaurant()

a_restaurant=Restaurant('a','aoddles')
a_restaurant.describe_restaurant()
b_restaurant=Restaurant('b','boddles')
b_restaurant.describe_restaurant()
c_restaurant=Restaurant('c','coddles')
c_restaurant.describe_restaurant()
print(" ")

class User(object):
	"""docstring for User"""
	def __init__(self,first_name,last_name,age,sex,height):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.sex=sex
		self.height=height

	def describe_user(self):
		print("the user's message is "+
			"\nfirst_name:"+self.first_name.title()+
			"\nlast_name:"+self.last_name.title()+
			"\nage:"+self.age.title()+
			"\nsex:"+self.sex.title()+
			"\nheight:"+self.height.title()
			)
		pass

	def greet_user(self):
		print("hello "+self.first_name.title()+self.last_name.title())
		pass
		
user1=User("zhang","hang",'25','female','170')
user2=User("zhao","xiang","24","male","180")
user3=User("li","chen","29","male","180")
user1.describe_user()
user2.describe_user()
user3.describe_user()