# Python基础训练.py
from math import *
"注意：本文已加入数学模组，请在后续的代码中排除掉from math import！！！"
# 1.字符串格式化输出
# 在Python中，我们可以使用字符串格式化输出的方式来控制输出的精度和格式。
#首先，我们来看一个简单的Python程序，它会输出一段话。
#coding=utf-8
# 这是一个Python程序，要求用户输入姓名，并根据输入的姓名输出不同的问候语。
# 下面是代码的实现：
###### Begin ######
name=input("输入姓名：")
print("{}同学，学好Python，前途无量！".format(name))
print("{}大侠，学好Python，大展拳脚！".format(name[0]))	
print("{}哥哥，学好Python，人见人爱！".format(name[1:]))
###### End ######
# 运行结果：
# 输入姓名：张三
# 张同学，学好Python，前途无量！
# 张大侠，学好Python，大展拳脚！
# 三哥哥，学好Python，人见人爱！

# 这个程序中运用了字符串的格式化功能，可以根据用户输入的姓名动态生成不同的问候语。

#中字符串Hello world长度为11（注意，空格也是一个字符），正向递增以最左侧字符H序号为0，向右侧依次递增，最右侧字符d序号为11-1=10；反向递减序号以最右侧字符d序号为-1，向左依次递减，最左侧字符H序号为-11。这两种索引字符的方法可以同时使用。

#Python 字符串也提供区间访问方式，采用[N:M]格式，表示字符串中从N到M（不包含M）的子字符串，其中，N和M为字符串的索引序号，可以混合使用正向递增序号和反向递减序号。如果表示中N或者M索引缺失，则表示字符串把开始或结束索引值设为默认值。

#注意：字符串中的英文字符和中文字符都算作1个字符。

# 下面是一个字符串的索引和切片示例：
###### Begin ######
str = "Ciallo～(∠・ω< )⌒★"
print(str[0])    # 输出第一个字符'C'
print(str[1:5])  # 输出从索引1到4的子字符串 'iall'
print(str[-1])   # 输出最后一个字符'★'
print(str[-5:-1])# 输出倒数第五个到倒数第二个的子字符串 '(∠・ω< )⌒'
###### End ######
# 运行结果：
# C
# iall
# ★
# (∠・ω< )⌒

# 2.数学运算
# 在Python中，我们可以使用运算符进行基本的数学运算，如加法
# ********** Begin ********** #
a = 10
b = 5
c = a + b
d = a - b
e = a * b
f = a / b
print("{} + {} = {}".format(a,b,c)) 
print("{} - {} = {}".format(a,b,d)) 
print("{} * {} = {}".format(a,b,e)) 
print("{} / {} = {}".format(a,b,f)) 
# ********** End ********** #
# 3.字符串处理
# 在字符串处理中，经常需要统计字符串的长度、进行大小写转换以及去除字符串前后空格等操作。例如，在基于关键词的搜索引擎中，要查询关键词是否在文档或者网页中出现，搜索引擎并不需要区分关键词中字符的大小写以及关键词前后的空格等。这时就需要对字符串进行处理，将其中的大写字符都转换为小写，并剔除字符串开头和结尾处的空格，然后再统一进行字符串匹配。
# 下面是一个字符串处理的示例：
# coding=utf-8

# 获取待处理的源字符串
source_string = "Where there is a will,there is a way"
# 处理字符串：将字符串转换为标题格式，去除前后空格，并输出处理后的字符串和长度
########## Begin ##########
title_string = source_string.title()
strip_string = title_string.strip()
print(strip_string)
length = len(strip_string)
print(length)
########## End ##########
# 运行结果：
# Where There Is A Will,There Is A Way 
# 36
# 在这个示例中，我们首先将源字符串转换为标题格式，然后去除前后空格，最后输出处理后的字符串和其长度。

# 那么在此期间，我们用的title()和strip()分别代表什么意思？
# title()方法将字符串中的每个单词的首字母转换为大写，其余字母转换为小写。
# strip()方法用于去除字符串开头和结尾的空格。
# 这两个方法在字符串处理中非常常用，可以帮助我们更好地处理和格式化字符串。

# 此外，strip()还可以去除特定的字符，例如：
# coding = utf-8
# 创建一个字符串hello_world
hello_world = '  **The world ** is big!*    '
# 利用strip()方法处理hello_world字符串
blank_hello_world = hello_world.strip()
char_hello_world = hello_world.strip('TH *')
# 打印输出转换后的字符串
print(blank_hello_world)
print(char_hello_world)

# 这里我们使用了strip('TH *')，那么在运行结果中，将会去除掉T H * 这三个字符

#输出结果：
#**The world ** is big!*
# #he world ** is big!

# 4.字符串查找与替换
# 在字符串处理中，查找和替换是非常常见的操作。Python提供了多种方法来实现这些功能。
# 下面是一个字符串查找和替换的示例：

# 查找子字符串
source_string = "Where there is a will,there is a way"
index = source_string.find("will")
print("子字符串'will'的起始索引为：{}".format(index))
# 替换子字符串
new_string = source_string.replace("will", "power")
print("替换后的字符串为：{}".format(new_string))
# 在这个示例中，我们使用了find()方法来查找子字符串"will"在源字符串中的起始索引，并使用replace()方法将"will"替换为"power"。

# 接下来我们来看看字符串的分割与连接操作。

# 5.字符串分割与连接
# 在字符串处理中，分割和连接是非常常见的操作。Python提供了split()和join()方法来实现这些功能。
# 下面是一个字符串分割和连接的示例：
# 分割字符串
source_string = "apple,banana,cherry"
fruit_list = source_string.split(",")
print("分割后的字符串列表为：{}".format(fruit_list))
# 连接字符串
new_source_string = "-".join(fruit_list)
print("连接后的字符串为：{}".format(new_source_string))
# 在这个示例中，我们使用了split()方法将源字符串按照逗号分割成一个字符串列表，并使用join()方法将字符串列表连接成一个新的字符串。

# 6.列表元素增删改

# 在Python中，列表是一种非常常用的数据结构，可以存储多个元素。我们可以对列表进行增、删、改等操作。

# 我们在使用这类功能时，往往会用到这么几个函数，它们分别是append()、insert()、remove()和pop()等。

# 6.1 列表元素添加
 # 6.1.1 使用append()方法添加元素
# append()方法用于在列表的末尾添加一个元素。其语法如下：
# list.append(element)
# 其中，list是要添加元素的列表，element是要添加的元素。

 # 下面是一个示例：
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print("添加元素后的列表为：{}".format(fruits))

# 运行结果：
# 添加元素后的列表为：['apple', 'banana', 'cherry', 'orange']

 # 6.1.2 使用insert()方法添加元素
# insert()方法用于在列表的指定位置插入一个元素。其语法如下:
# list.insert(index, element)
# 其中，list是要添加元素的列表，index是要插入元素的位置，element是要插入的元素。
# 下面是一个示例：
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "orange")
print("添加元素后的列表为：{}".format(fruits))
# 运行结果：
# 添加元素后的列表为：['apple', 'orange', 'banana', 'cherry']

# 6.2 修改列表元素
# 修改列表中的元素可以通过索引直接访问并赋值。其语法如下：
# list[index] = new_value
# 其中，list是要修改元素的列表，index是要修改元素的位置，new_value是新的值。
# 下面是一个示例：
fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print("修改元素后的列表为：{}".format(fruits))
# 运行结果：
# 修改元素后的列表为：['apple', 'orange', 'cherry']

# 6.3 删除列表元素
 #6.3.1 使用del函数删除元素 
#在 Python 中，调用del函数能够删除指定索引位置的元素，其基本语法如下：
# del list[index]
# 其中，list是要删除元素的列表，index是要删除元素的位置。
# 下面是一个示例：
fruits = ["apple", "banana", "cherry"]
del fruits[1]
print("删除元素后的列表为：{}".format(fruits))
# 运行结果：
# 删除元素后的列表为：['apple', 'cherry']
# 6.3.2 使用remove()方法删除元素
# remove()方法用于删除列表中第一个匹配的元素。其语法如下:
# list.remove(element)
# 其中，list是要删除元素的列表，element是要删除的元素。
# 下面是一个示例：
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print("删除元素后的列表为：{}".format(fruits))
# 运行结果：
# 删除元素后的列表为：['apple', 'cherry']
# 6.3.3 使用pop()方法删除元素
# pop()方法用于删除列表中指定位置的元素，并返回该元素。其语法如下:
# list.pop(index)
# 其中，list是要删除元素的列表，index是要删除元素的位置。
# 下面是一个示例：
fruits = ["apple", "banana", "cherry"]
removed_fruit = fruits.pop(1)
print("删除的元素为：{}".format(removed_fruit))
print("删除元素后的列表为：{}".format(fruits))
# 运行结果：
# 删除的元素为：banana
# 删除元素后的列表为：['apple', 'cherry']

# 7.列表元素的排序
 #Python还可以对列表中的元素进行排序
"""
例如，我们想将参加会议的专家名单guests列表中的五个名字元素['zhang san','li si','wang wu','sun qi','qian ba']，分别按照首字母从小到大的顺序和从大到小的顺序分别排序。排序后的输出分别为：

['li si','qian ba','sun qi','wang wu','zhang san']
['zhang san','wang wu','sun qi','qian ba','li si']

"""
#那么我们该怎么实现呢？
"使用sort()函数来实现排序"
#Python 针对列表数据结构内置提供了sort()方法，实现对列表元素的排序功能。其基本语法如下：
# source_list.sort(reverse=True)
"""
其中：
source_list：待排序的列表；
sort：列表排序函数的语法关键词；
reverse：sort函数的可选参数。如果设置其值为True，则进行反向从大到小排序，如果设置为False或者不填写该参数，则默认进行正向从小到大排序。
"""

# 8.数值列表的简单统计运算
# 在本知识点中，我们将会从range()、list()、sum()等函数来入手

# 8.1 range()函数

#Python 提供了range()函数，能够用来生成一系列连续增加的数字。其基本使用语法有如下三种：
# (1)使用range函数来进行数字的生成
#range(lower_limit,upper_limit,step)
"""
其中：

lower_limit: 生成系列整数的下限整数，不填该参数则默认为从0开始，生成的整数从此数开始，包括该数；

upper_limit：生成系列整数的上限整数，必填参数，生成的整数要小于该上限；

step：在下限和上限之间生成系列整数之间的间隔步长，不填该参数则默认步长为1。

注意：range()函数的三个参数都只能为整数。如果range()函数中仅一个参数，则该参数表示upper_limit，如果仅两个参数，则分别表示lower_limit和upper_limit。
"""

# 下面是一个示例：
for i in range(1, 10, 2):
    print(i)
    print("当前数字是：{}".format(i))
# 以上代码将会输出：
# 1
# 当前数字是：1
# 3
# 当前数字是：3
# 5
# 当前数字是：5
# 7
# 当前数字是：7
# 9
# 当前数字是：9

# (2) 基于range()函数创建数字列表
#我们可以通过range()函数，利用 Python 列表提供的append()插入功能创建一个列表

#例如，我们要创建一个包含10个0~9整数的平方的列表：
squares = []
for i in range(10):
    squares.append(i ** 2)
print("0~9整数的平方列表为：{}".format(squares))

# 运行结果：
# 0~9整数的平方列表为：[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 9.列表切片
#我们在前三个知识点 中学习了如何处理单个列表元素和所有列表元素，在这一知识点中我们还将学习如何处理部分列表元素（Python 中称为切片）。
#Python 切片是对一个列表取其部分元素获得一个子序列的常见操作，切片操作的返回结果类型与被切片的对象一致。要创建一个已有列表的切片，通过指定切片的第一个列表元素和最后一个列表元素的索引号即可。其基本语法如下：
#list_slice = source_list[start:end:step]
"""
其中：

source_list：被切片的源列表；

list_slice：切片后生成的子序列列表；

start：切片起始索引位置，省略则从头开始；

end：切片结束索引位置，省略则切至列表末尾；

step：切片步长，可选参数，表示每N个元素取一个，默认为1。

注意：切片和range()函数一样，Python 会自动到达所指定切片结束索引位置的前面一个元素停止。
"""
#例如，下面是我已经点好的菜名列表，现在朋友点的菜单中包含我的前三个菜名，输出朋友的菜单：
my_menu = ['fish','pork','pizza','carrot']
print(my_menu[1:4:2])
print(my_menu[:3])
print(my_menu[2:])
"""
输出结果：

['pork','carrot']
['fish','pork','pizza']
['pizza','carrot']
"""
#负数索引返回的是离列表末尾相应间隔的元素，列表末尾元素的索引是从-1开始的。例如，朋友的菜单是包含我的菜单最后3个菜名：

my_menu=['fish','pork','pizza','carrot']
print(my_menu[-3:])

#输出结果
['pork','pizza','carrot']

#Tip：当列表中的元素个数未知时，可以使用以下个例：
# coding=utf-8

# 创建并初始化my_menu列表
my_menu = []
while True:
	try:
		food = input()
		my_menu.append(food)
	except:
		break

# 请在此添加代码，对my_menu列表进行切片操作
########## Begin ##########
print(my_menu[::3])
print(my_menu[-3:])

########## End ##########

# 9.元组与字典
# 元组看起来犹如列表，但元组使用圆括号（）而不是[]来标识，而且列表的元素可以修改，但元组的元素不能修改。本关介绍元组的常见使用方法以及元组和列表的使用区别。

"""
元组与列表很相似，两者之间的差别在于：

列表在初始化后其中的元素还可以进行增删改等操作，但是元组在初始化后其中的元素不能进行更改；
列表在赋值时使用方括号[]，而元组在赋值时使用小括号()。
"""
"""
创建元组
元组创建很简单，只需要在括号()中添加元素，元素之间用逗号隔开。元组中只包含单个元素时，需要在该元素后面添加逗号。例如：

menu1 = ('meat','fish','chicken')
menu2 = ('meat',)
"""

"""
访问元组
元组和列表一样，可以使用下标索引来访问元组中的值。例如:

menu = ('meat','fish','chicken','carrot')
print(menu[0])
print(menu[1:3])
输出结果：

meat
('fish', 'chicken')
修改元组
元组中的元素值是不可以修改的，如果强行修改会报错。例如我们想修改元组menu中的某个值：

menu = ('meat','fish','chicken','carrot')
menu[0] = 'pizza'
print(menu[0])
输出结果：

TypeError: 'tuple' object does not support item assignment
系统会自动报错，元组中的元素值不支持修改。

元组内置函数
元组和列表一样，都有一些内置函数方便编程。例如：

len(tuple)：计算元组中元素个数；

max(tuple)：返回元组中元素的最大值；

min(tuple)：返回元组中元素的最小值；

tuple(seq)：将列表转换为元组。

元组中的元素是不能改变的，它也没有append()、insert()这样的方法，但其他获取元素的方法和列表是一样的。
"""

# 接下来我们来看一个示例

# coding=utf-8

# 创建并初始化menu_list列表
menu_list = []
while True:
    try:
        food = input()
        menu_list.append(food)
    except:
        break

# 请在此添加代码，对menu_list进行元组转换以及元组计算等操作，并打印输出元组及元组最大的元素
###### Begin ######
menu = tuple(menu_list)
print(menu)
BIG = max (tuple(menu_list))
print(BIG)
#######  End #######


# I/O 运行结果：（input输入为'meat', 'fish', 'chicken', 'carrot'）
# ('meat', 'fish', 'chicken', 'carrot')
# chicken

