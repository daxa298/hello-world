# 欢迎回来，让我们回想一下上次在Python Tutorial（Python新手教程）.py中我所讲述的内容。
# 在那篇文章中，我介绍了Python的基本语法和一些简单的操作。
# 今天，我们将继续探索Python的世界，创建一个新的项目文件，并添加一些有趣的代码。
# 在开始之前，我们先来回顾一下上次的内容。

# 首先是一个简单的打印语句，它输出一条问候消息。
print("This is my project file.")

# 下面的这段代码演示了Python的基本语法和字符串格式化。
a = "modest"
b = "ambitious"
print(f"{a} and {b} are two adjectives.")

print(f"He is a variable: {a}, {b}")

def greet(name):
    """Function to greet a person."""
    print(f"Hello, {name}!")

greet("Alice")
# The code above defines a variable and a function.

# 接下来是一个简单的加法操作，它计算两个变量的和并打印结果。

x= 10
y = 20
z = x + y
print(f"The sum of {x} and {y} is {z}.")
# This code performs a simple addition and prints the result.

# This script prints a message and demonstrates basic variable usage.
# It also includes a function to greet a person by name.    

# Python中的数字类型
# 在Python中，数字可以用多种方式表示，包括八进制和十六进制等。
number1 = 0xA0F # 十六进制
print(number1)

number2 = 0o37 # 八进制
print(number2)

#那么，既然我们可以用八进制和十六进制来表示数字，那么Python中还有其他方法来表示数字呢？
#（以下内容来自于runoob.com）

#Python 支持三种不同的数值类型：

 ##整型(int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。布尔(bool)是整型的子类型。

 ##浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）

 ##复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

#那么我们就来看看Python中如何表示这些数字类型吧。（这里假设numberN是一个变量）
# 整型 
numberN = 1000
print(int(numberN))  # 输出整数类型

# 浮点型
numberN = 1000.0
print(float(numberN))  # 输出浮点类型

# 复数
numberN = 1 + 2j
print(complex(numberN))  # 输出复数类型

# 此外，我们在高中数学中也学习过，复数也可以用极坐标的形式表示，Python中也可以使用cmath模块来处理复数的极坐标形式。（该部分内容后面会详解）
import cmath
# 复数的极坐标形式
numberN = 1 + 2j
polar_coords = cmath.polar(numberN)
print(f"复数 {numberN} 的极坐标形式为：{polar_coords}")

# 复数的极坐标形式可以用cmath模块中的polar函数来计算，返回值是一个元组，包含模和辐角。

# 我们在使用complex函数是，也可以这么操作：
numberN = complex(1, 2)  # 实部为1，虚部为2
print(f"复数 {numberN} 的实部为：{numberN.real}, 虚部为：{numberN.imag}")

# 上面的.real和.imag属性可以用来获取复数的实部和虚部。

# 那么有人就会问了：Python中如何进行这三种类型的计算呢？

# Python的计算
# Python中可以直接对这三种类型进行计算，Python会自动处理类型转换。
# 例如：
# 整型和浮点型的计算
int_num = 10
float_num = 20.5
result = int_num + float_num
print(f"整型和浮点型的计算结果为：{result}")
# 复数的计算
complex_num = 1 + 2j
result = int_num + complex_num
print(f"整型和复数的计算结果为：{result}")
# 复数和浮点型的计算
result = complex_num + float_num
print(f"复数和浮点型的计算结果为：{result}")
# 复数和复数的计算
result = complex_num + (3 + 4j)
print(f"复数和复数的计算结果为：{result}")
# 以上代码展示了Python中不同数值类型的表示和计算方式。