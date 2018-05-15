##线程和进程

###创建多线程
*	用threading模块创建多线程
*	从threading.Thread继承创建线程类

###协程
用户级轻量级线程（单线程，省去了cpu的调度开销）
spawn():形成协程
joinall()：添加协程，并启动运行
Pool对象：可对协程的并发数量进行管理

###分布式进程
将Process进程分布到多台机器上

**PS：**
CPU密集型操作：推荐多进程，因为多线程只能调用一个cpu内核
IO密集型操作：推荐多线程，可提高效率
***

##网络编程

###socket（套接字）
一个socket表示“打开了一个网络链接”
打开一个socket需要知道目标计算机的IP地址和端口号，再指定协议类型
Python提供两个基本的Socket模块
>Socket：提供标准API
>SocketServer：提供服务器中心类，简化网络服务器开发

###html
###CSS
###javascript
>严格区分大小写，忽略空格，制表符和换行符
####数据类型
Number整型
字符串类型
布尔值类型
数组类型
对象类型

function关键字：用来定义函数
*允许传入任意个参数而不影响调用*
当结果错误时返回NaN

###XPath
在XML中查找信息的语言，也可在html文档中工作
>xml:lang="en":
>>这是一个W3C的标准；
lang代表语言，这儿是英语；改成zh-cn指简体中文
xml:lang就是xml的语言，这儿的xml是一种html扩展语言，功能很强大；因为各浏览器的兼容不一样，所以就有这么一个机构，想做出一个统一标准的兼容方案；在html代码中加入这样一个代码，可使所有浏览器都按标准的排版去设计；如果去掉，可能部分浏览器不兼容，最好都加上，因为是标准。
XPath进行属性选取的时候可以使用通配符*匹配未知元素

###JSON
JSON是JavaScript对象表示法，用于存储和交换文本信息
JSON语法
>JSON名称/值对。类似python中的字典
>JSON值
>JSON对象：可包含多个名称/值对
>JSON数组：在方括号中书写，可包含多个对象

##HTTP标准
###HTTP请求过程
1.	首先客户端与服务器建立连接
2.	建立链接后，客户端发送一个请求给服务器
3.	服务器接到请求，给予相应的响应信息，格式为一个状态行
4.	客户端接收服务器所返回的信息，通过浏览器将信息显示在用户的显示屏上

这些过程由HTTP协议自己完成

###HTTP状态码含义
1\*\*信息，服务器收到请求，需进一步操作
2\*\*成功
3\*\*重定向
4\*\*客户端错误
5\*\*服务器错误

###HTTP头部信息
HTTP头部信息由众多头域组成，每个头域有一个域名，冒号和域值
GET
Host头域
User-Agent头域
Accept请求报头域
Accept-Language请求报头域
......
***
#初识网络爬虫
###网络爬虫结构
![网络爬虫结构](https://github.com/LyonDon/python-learning/raw/master/python-reptile/photo/%E5%9B%BE%E5%83%8F%201.png)
##HTTP的python实现
###urllib2/urllib实现
urllib2和urllib是python中的两个内置模块，要实现HTTP功能，实现方式以urllib2为主，urllib为辅
###httplib/urllib实现
###更人性化的Requests

***
#HTML解析大法
##初识Firebug
一个用于web前端开发的工具，是FireFox浏览器的一个扩展插件。可以用于调试JavaScript、查看DOM、分析CSS、监控网络流量以及进行Ajax交互等。几乎提供了前端开发需要的全部功能

##正则表达式
是由普通字符以及特殊字符组成的文字模式
\b是正则表达式规定的一个特殊代码，被称为元字符，代表单词的开头或结尾，也就是单词的分解处
*常用元字符*
元字符主要有四种作用

*	匹配字符
*	匹配位置
*	匹配数量
*	匹配模式

![正则表达式常用元字符](https://github.com/LyonDon/python-learning/raw/master/python-reptile/photo/%E5%9B%BE%E5%83%8F%203.png)

*字符转义*
*重复*
*字符集合*
*分支条件*
*字符集合*
*分支条件*
*分组*
*反义*
*后向引用*
