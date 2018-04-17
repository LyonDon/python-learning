#coding:utf-8
animals=['lion','tiger','cat',]
for animal in animals:
	print(animal)
	print('The '+animal+' is a feline.\n')
	pass
print('They have something in common\n')

#其他的一些尝试
squares=[]
for value in range(1,11):
	squares.append(value**2)	
	pass
#print('\n')
print(squares)

squares=[value**2 for value in xrange(1,11)]
print(squares)

print('The first three items in the list are '+str(squares[:3]))
print('Three items from the middle of the lists are '+str(squares[4:7]))
print('The last three items in the lists are '+str(squares[-3:]))

pizzas=['KFC','Mac','PizzaHut']
friend_pizza=pizzas[:]
print(friend_pizza)

friend_pizza.append('mkc')
for pizza in pizzas:
	print('my favorite pizzas are '+pizza)
	pass
print('my fried''s favorite pizzas are:'+str(friend_pizza))

my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]
for food in my_foods:
	print(food)
	pass
for food in friend_foods:
	print(food)
	pass