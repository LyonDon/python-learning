#coding=utf-8
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

class Admin(User):
	"""docstring for Admin"""
	def __init__(self,first_name,last_name,age,sex,height):
		super(Admin,self).__init__(first_name,last_name,age,sex,height)
		self.privileges=['can add post','can delete spot','can ban user']

	def show_privileges(self):
		print(self.privileges)
		pass
"""
Admin=Admin('a','b',19,'male',178)
Admin.show_privileges()
"""
class Privileges():  
    def __init__(self):  
        self.privileges = ['can add post','can del post','can ban user']  
    def show_privileges(self): 
  		print(self.privileges)
Admin1 = Admin('Ma','Yun',10,'male',188)  
Admin1.show_privileges() 