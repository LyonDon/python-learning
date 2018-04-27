#coding=utf-8
print('请输入两个数字，我给你返回它们的和')
print('若要退出请输入q')

while True:
	num1=raw_input("请输入第一个数字：")
	if num1=='q':
		break
	num2=raw_input('请输入第二个数字：')
	if num2=='q':
		break
	try:
		sum0=int(num1)+int(num2)
	except ValueError:
		print('请输入正确的数字')
	else:
		print(sum0)