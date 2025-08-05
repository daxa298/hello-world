# Python基础训练.py
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
