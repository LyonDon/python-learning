#coding:utf-8
#版本一
alien_color='red'
if alien_color=='green':
	print("gamer has won five points")
	pass
#版本二
alien_color='green'
if alien_color=='green':
	print("gamer has won 5 points")
	pass

alien_color='green'
#版本一
if alien_color=='green':
	print("gamer has won 10 points")
	pass
if alien_color!='green':
	print("gamer has won 5 points")
	pass
#版本二
if alien_color=='green':
	print('gamer has won 10 points')
else:
	print("gamer has won 5 points")
	pass

#列表if else练习
favorite_fruits=['apple','orange','grapes']
if 'apple' in favorite_fruits:
	print("you really like apple")
	pass
if 'watermelon' in favorite_fruits:
	print('you really like watermelon')
	pass

#以特殊方式跟管理员打招呼
users_name=['Adam','Alex','Bob','Admin','King']
for user_name in users_name:
	print('hello '+user_name)
	pass
	if user_name=='Admin':
		print('hello Admin,would you like to see a status report?')
	else:
		print('hello,Eric,thank you for logging in again')
		pass
users_name=[]
if users_name==[]:
	print('\nWe need to find some users')

#模拟网站
current_users=['Ann','Lucy','Tina','Hani','Jackie']
new_users=['Ann','Tina','Bin','HANI','Nancy']

Current_users=[string.upper() for string in current_users]
New_users=[string.upper() for string in new_users]

for New_user in New_users:
	if New_user in Current_users:
		print(New_user+' has been used.Need another one')
	else:
		print(New_user+' has never been used')
		pass
	pass

#数字列表
nums=[1,2,3,4,5,6,7,8,9]
for num in nums:
	if num==1:
		print('1st')
	elif num==2:
		print('2nd')
	else:
		print(str(num)+'th')
		pass
	pass