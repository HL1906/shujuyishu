import numpy as np

# 1、学生成绩数组操作
# （1）创建学生成绩数组，第一行为平时成绩，第二行为期末成绩，第三行为总分；
# （2）查看创建的学生成绩数组；
# （3）查看数组相关属性；
# （4）单独查看学生期末成绩；
# （5）所有成绩（平时与期末）加10分；
# （6）计算学生最终成绩（平时成绩：40%；期末成绩60%）；
# （7）描述性统计分析学生成绩（平均成绩、中位数、分位数、方差、标准差）；



# （1）创建学生成绩数组，第一行为平时成绩，第二行为期末成绩，第三行为总分；
arrjhl = np.array([[99, 98, 97, 100], [100, 97, 98, 99], [199, 195, 195, 199]])
print("\n")


# （2）查看创建的学生成绩数组；
print(arrjhl)
print("\n")


# （3）查看数组相关属性；
# 秩，即轴的数量或维度的数量
print("学生成绩数组的秩:", arrjhl.ndim)

# 数组的维度，对于矩阵，n行m列
print("数组的维度:", arrjhl.shape)

# 数组元素的总个数，相当于.shape中n*m的值
print("数组元素的总个数:", arrjhl.size)

# ndarray对象的元素类型
print("ndarray对象的元素类型:", arrjhl.dtype)

# ndarray对象中每个元素的大小，以字节为单位
print("ndarray对象中每个元素的大小，以字节为单位:", arrjhl.itemsize)
print("\n")


# （4）单独查看学生期末成绩；
# 第一行为平时成绩，第二行为期末成绩，第三行为总分；
print("学生期末成绩:", arrjhl[1])
print("\n")


# （5）所有成绩（平时与期末）加10分；
print("原总分:",arrjhl[2])
arrjhl2 = arrjhl[2] + 10
print("加分后成绩：", arrjhl2)
print("\n")


# （6）计算学生最终成绩（平时成绩：40%；期末成绩60%）；
print("折分前平时成绩：", arrjhl[0])
print("折分前期末成绩：", arrjhl[1])
print("折分前总成绩：", arrjhl2)
arrjhl3 = arrjhl[0] * 0.4
arrjhl4 = arrjhl[1] * 0.6
arrjhl5 = arrjhl3 + arrjhl4
print("最终成绩：", arrjhl5)
print("\n")


# （7）描述性统计分析学生成绩（平均成绩、中位数、分位数、方差、标准差）；
# 取学生的最终成绩来计算

# 平均成绩 average()、mean()
print("平均成绩:", np.average(arrjhl5))

# 中位数
print("中位数:", np.median(arrjhl5))

# 分位数  百分位函数percentile()
print("分位数:", np.percentile(arrjhl5, 98))

# 方差 var()
print("方差:", np.var(arrjhl5))

# 标准差
print("标准差:", np.std(arrjhl5))

