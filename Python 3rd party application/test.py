import matplotlib.pyplot as plt
xt, yt = 1, 2
plt.plot(xt,yt,'ro')
plt.grid('on')      #显示网格线
plt.axis([0,2,1,3]) #设置坐标轴范围
plt.show()