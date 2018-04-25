#coding=utf-8
#定义魔术师列表

#自己编写
#第一个函数负责打印魔术师的名字
magician_names=['A','B','C','D']
def show_magician():
	for name in magician_names:
		print(name)
		pass
show_magician()

#第二个函数负责在每个魔术师的名字前面加上“the gret”
magician_names=['A','B','C','D']
print_names=[]
def make_great(magician_names,print_names):
	while magician_names:
		current_name=magician_names.pop()
		current_name='the great '+current_name
		print_names.append(current_name)
		pass
	pass
def show_magician(print_names):
	for name in print_names:
		print(name)
		pass
	pass

make_great(magician_names,print_names)
show_magician(print_names)

#网上答案
#创建一个包含魔术师名字的列表，并将其传递给一个名为show_magicians() 的函数， 这个函数打印列表中每个魔术师的名字。  
name_list = ['mag1','mag2','mag3']  
def show_magicians():  
    for name in name_list:  
        print(name)  
show_magicians()  
  
# 编写一个名为make_great() 的函数,对魔术师列表进行修改， 
#在每个魔术师的名字中都加入字样“theGreat”。 调用函数show_magicians() ， 确认魔术师列表确实变了。  
name_list = ['mag1','mag2','mag3']  
name_change = []  
def make_great(name_list,name_change):  
    while name_list:  
        cur = name_list.pop()  
        cur = 'the great ' + cur  
        name_change.append(cur)  
      
def show_magicians(name_change):  
    for name in name_change:  
        print(name)  
          
make_great(name_list,name_change)  
show_magicians(name_change) 

# 8-11 不变的魔术师 ： 修改你为完成练习8-10而编写的程序， 在调用函数make_great() 时， 向它传递魔术师列表的副本。   
# 由于不想修改原始列表， 请返回修改后的列表， 并将其存储到另一个列表中。 分别使用这两个列表来调用show_magicians() ，   
# 确认一个列表包含的是原来的魔术师名字， 而另一个列表包含的是添加了字样“the Great”的魔术师名字。  
name_list = ['mag1','mag2','mag3']  
name_change = []  
  
def make_great(name_list,name_change):  
    while name_list:  
        cur = name_list.pop()  
        cur = 'great' + cur  
        name_change.append(cur)  
def show_magicians(name_change):   
    for name in name_change:  
        print(name)  
  
make_great(name_list[:],name_change)  
show_magicians(name_list)  
show_magicians(name_change)  