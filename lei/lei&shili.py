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

restaurant=Restaurant('yao','noddles')
restaurant.number_served_people()
restaurant.number_served=17
restaurant.number_served_people()
restaurant.set_number_served()
restaurant.increment_number_served(10)
restaurant.number_served_people()
#第二个实例
class User(object):
	"""docstring for User"""
	def __init__(self,first_name,last_name,age,sex,height):
		self.first_name=first_name
		self.last_name=last_name
		self.age=age
		self.sex=sex
		self.height=height
		self.login_attempts=0

	def describe_user(self):
		print("the user's message is"+
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
		
	def increment_login_attempts(self):
		self.login_attempts+=1
		pass
	def reset_login_attempts(self):
		self.login_attempts=0
		pass

user1=User("zhang","hang",'25','female','170')
user2=User("zhao","xiang","24","male","180")
user3=User("li","chen","29","male","180")
user1.describe_user()
user2.describe_user()
user3.describe_user()
user3.increment_login_attempts()
user3.increment_login_attempts()
print(user3.login_attempts)
user3.reset_login_attempts()
print(user3.login_attempts)