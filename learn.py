def calculate_free_fall_height():
    # This code calculates the height of an object in free fall after a certain time.
    v = 25 # Initial velocity in m/s
    g = 9.8 # Acceleration due to gravity in m/s^2
    t = 3 # Time in seconds
    h = v * t - 0.5 * g * t**2
# 结合这三个数据和一个公式，我们就可以得出物体在自由落体是的高度。

    print (f"该物体的下落高度为{h}米")

    #我们来看看运行的结果

calculate_free_fall_height()


F = 117.8 # 华氏度
C = (F - 32) * 5 / 9 # 摄氏度转换为华氏度的公式

print (f"华氏度{F}对应的摄氏度为{C}")

# 那么我们就发现了一个问题，华氏度转换为摄氏度时，结果给出的小数点后有很多位，这样会让人觉得不太美观。
# 那么我们换一种思路来看看怎么处理

F = 117.8 # 华氏度
C = (F - 32) * 5 / 9 # 摄氏度转换为华氏度的公式

print ("华氏%.2f对应的摄氏度为%.2f" % (F, C))

# 那么我们就可以看到，%.2f表示保留两位小数，这样就让结果看起来更美观了。

# 接下来我们来看看math模块如何使用

from math import *

# math模块提供了许多数学函数和常量，我们可以使用它来进行更复杂的数学计算。
# 例如，我们可以使用math模块来解决小球阻力落体运动

g = 9.8   # 单位：米/秒平方，重力加速度
m = 0.25  # 单位：千克
u = 0.5
t = 2 # 单位：秒

v = sqrt(m*g/u) * tanh(sqrt(u*g/m) * t)
# 计算小球的速度
print("小球在%.2f秒后的速度为%.2f米/秒" % (t, v))      

# 这里我们使用了math模块中的sqrt和tanh函数来计算小球的速度。
# 同理，我们还可以计算小球的位移

x = m/u * log(cosh(sqrt(u*g/m)*t))

# 计算小球的位移
print("小球在%.2f秒后的位移为%.2f米" % (t, x))