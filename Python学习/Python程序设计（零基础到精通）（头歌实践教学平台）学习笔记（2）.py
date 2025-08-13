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
menu_list = ['meat', 'fish', 'chicken', 'carrot']
# 请在此添加代码，对menu_list进行元组转换以及元组计算等操作，并打印输出元组及元组最大的元素
###### Begin ######
menu = tuple(menu_list)
print(menu)
if menu:
    BIG = max(menu)
    print(BIG)
#######  End #######


# I/O 运行结果：（input输入为'meat', 'fish', 'chicken', 'carrot'）
# ('meat', 'fish', 'chicken', 'carrot')
# chicken
