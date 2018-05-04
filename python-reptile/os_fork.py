#coding=utf-8
import os
from multiprocessing  import Process
#子进程要执行的代码
def run_proc(name):
	print('Child process %s (%s) Runing...'% (name,os.getpid()))
if __name__ == '__main__':
	print('Parnet process %s.' % os.getpid())
	for i in xrange(5):
		p=Process(target=run_proc,args=(str(i),))
		print('process will start')
		p.start()
		pass
	p.join()
	print('process end')
pass