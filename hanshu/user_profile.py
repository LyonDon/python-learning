def build_profile(first,last,**user_info):
	profile={}
	profile['first_name']=first
	profile['last_name']=last
	for key,value in user_info.items():
		profile[key]=value
	return profile

user_profile=build_profile('albert','einstein',location='princetion',filed='physics')
print(user_profile)

print(build_profile('Dong','Liang',location='Xian',age='21',height="178"))

def make_car(manu,size,**info):
	car={}
	car['manu']=manu
	car['size']=size
	for key,value in info.items():
		car[key]=value
	print(car)
	pass
	pass

car=make_car('subaru','outback',color='blue',two_package=True)