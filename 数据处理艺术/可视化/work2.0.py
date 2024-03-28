# 二、Matplotlib
# 1、自定义数据场景，自定义合适的数据，
# 分别应用饼图、柱状图、直方图、折线图、散点图、气泡图、雷达图、箱线图做分析说明；

# import matplotlib.pylab as plt
#
# # 饼图
# # 处理中文乱码
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
#
# # 构造数据
# data = [255, 455, 638, 565, 784, 948]
# labels = ['汉堡', '薯条', '可乐', '黄金鸡块', '蛋挞', '其它']
#
# # 绘制饼图
# plt.pie(x=data,  # 数据
#         labels=labels,  # 标签
#         autopct='%.2f%%'  # 格式
#         )
# plt.show()
#
#
# # 柱状图
# import numpy as np
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
#
# xdata = ["北京", "上海", "广州", "深圳", "南京", "重庆", "长沙"]
# ydata = [2300, 1900, 1500, 1300, 1100, 2500, 800]
#
# plt.bar(xdata, ydata, alpha=0.5, width=0.3, color='yellow', edgecolor='red',
#         label='人口数', lw=3)
# plt.legend(loc='upper left')
#
# plt.xlabel('This Is X Axis', fontsize=15)
# plt.ylabel('万人', fontsize=15)
# plt.title('各个城市人口柱状图', fontsize=15)
# # 如果想自己给 x 轴的 bar 加上标签,rotation 控制倾斜角度
# plt.xticks(rotation=30)
# plt.yticks(np.arange(0, 2500, 300))
# plt.show()


# # 直方图
# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import random
#
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# data = pd.DataFrame({'age': [random.randint(0, 100) for i in range(100)]})
# plt.hist(x=data['age'],  # 数据
# bins=20,  # 列数
# range=(0, 100),  # 范围
# color='steelblue',  # 颜色
# edgecolor='black')  # 边界颜色
# plt.xlabel('年龄段（每 5 岁一小段）')
# plt.ylabel('人数')
# plt.title('各年龄段人数分布直方图')
# plt.show()






# # 折线图
#
# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import random
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# data = pd.Series([random.randint(0, 100) for i in range(100)])
# data.plot(kind='kde',
#           color='red',
#           label='核密度图')
# plt.xlabel('年龄段（每 5 岁一小段）')
# plt.ylabel('人数')
# plt.title('各年龄段人数分布核密度图')
# plt.show()



# # 散点图
#
# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import random
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# data = pd.DataFrame({'销售额': [2000, 2300, 2600, 2900, 3000,
#                              3300, 3500, 3900, 4000, 4300, 4500, 4700],
#                     '利润': [250, 280, 290, 310, 340, 360,
#                            370, 380, 410, 420, 430, 450]},
#                     index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# # print(data)
# plt.scatter(x=data['销售额'],
#             y=data['利润'],
#             label='办公用品',
#             color='red',
#             alpha=0.8)
# plt.xlabel('销售额（万元）')
# plt.ylabel('利润（万元）')
# plt.title("销售额利润散点图")
# plt.legend()
# plt.show()





# # 气泡图

# import pandas as pd
# import matplotlib as mpl
# import matplotlib.pyplot as plt
# import random
# # 设置中文字体
# mpl.rcParams['font.sans-serif'] = ['SimHei']
# data = pd.DataFrame({'销售额':[random.randint(7000, 9000) for i in range(12)],
#                     '利润': [random.randint(500, 2000) for i in range(12)],
#                      '利润率': [random.randint(1, 100)*5 for i in range(12)]},
#                     index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
# print(data)
# plt.scatter(x=data['销售额'],
#             y=data['利润'],
#             s=data['利润率'],
#             label='办公用品',
#             color='red',
#             alpha=0.8)
# plt.xlabel('销售额（万元）')
# plt.ylabel('利润（万元）')
# plt.title("销售额利润利润率气泡表")
# plt.legend()
# plt.show()



# # 雷达图
#
# import numpy as np
# import matplotlib.pyplot as plt
# # 显示中文
# plt.rcParams['font.sans-serif'] = ['KaiTi']
# # 标签
# labels = np.array(['身份', '历史', '行为', '人脉', '履约能力', ])
# data = np.array([90, 88, 85, 89, 90])
# dataLenth = 5  # 数据长度
# # 分割圆周长
# angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
# # 闭合
# data = np.concatenate((data, [data[0]]))
# angles = np.concatenate((angles, [angles[0]]))
# # 做极坐标系
# plt.polar(angles, data, 'bo-', linewidth=1)
# # 做标签
# plt.thetagrids(angles * 180/np.pi, labels)
# # 填充
# plt.fill(angles, data, facecolor='yellow', alpha=0.5)
# plt.ylim(0, 100)
# plt.title("芝麻分解读雷达图")
# plt.show()





# 箱线图

# import matplotlib.pyplot as plt
# # 处理中文乱码
# plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
# data = [[1, 3, 6, 8, 9, 23, 24, 26, 28, 27, 39, 35, 32, 21, 15, 17],
#         [0, 4, 5, 6, 7, 21, 25, 26, 27, 26, 59, 65, 42, 41, 45, 57]]
# labels = ['label1', 'label2']
# plt.boxplot(data, notch=True, labels=labels, meanline=True)
# plt.title("我是箱线图")
# plt.show()

