# 分支结构

## 布尔类型及相关运算

### 关系运算符 [有六个]

用于两个值进行比较

`!=`为数学符号 $\neq$

`==`为数学符号 $=$

`<=`为数学符号 $\leq$

注：python中允许 $1<a<10$ 的写法。

### 布尔类型

布尔类型只有True和False两个值

#### 逻辑运算符

and 

or

not

注：数字0，空字符串，表示空值的None会被认为是False.

```python 
a = 'python'
print(a and True)
print(True and a)
print(False and a)
```

第一个结果为`True`

第二个结果为`python`

第三个结果为`False`

#### 运算符应用

## 单分支和双分支

### 单分支结构

#### 语法形式

if 条件表达式：

​			语句块

### 双分支结构

#### 语法形式

if 条件表达式：

​			语句块1

else:

​			语句块2

## 多分支和嵌套 if 

### 多分支结构

#### 语法形式

if 条件表达式1：

​			语句块1

elif 条件表达式2：

​			语句块2

.

.

elif 条件表达式n：

​			语句块n

else:

​			语句块n+1

注：一般情况下，条件表达式先写特殊条件，再写一般条件。

### 嵌套if语句

在if 分支结构的语句中又包含一个或多个if结构语句。

## 字符串的比较与分析

### in和not in运算符

判断一个字符串是否在另一个字符串中

返回布尔值True或者False

### 比较字符串

比较运算符 `==` `!=` `>` `<` `>=` `<=`

通过计算字符的编码数值来实现。

### 常用的字符串测试方法



# 循环结构

循环结构

循环体

## while循环

while 条件表达式：

​	循环体

## for 循环

知道循环次数，可用for循环较为简单。

**遍历循环**：针对某一数据集合

### 语句语法

for <循环变量> in <数据集>：

​	<语句块>

### range()函数

range(start,end,step)

range()函数返回一个可迭代对象，可理解为一个序列，**序列中的数包括start,不包括end.**

## 循环嵌套

`print()`为换行

## 循环的终止控制

### break

用来结束整个循环

### continue

用来结束当前当次循环

实际运用中不常用

## 字符串访问

字符串中的编号叫做“索引”。

<string>[<索引>]

**索引从0(前向)或-1(后向)开始**

### 切片形式访问

选择字符串的子序列

[ start : finish]

start:子序列开始位置的索引值

finish:子序列结束位置的**下一个字符的**索引值

#### 接收三个参数

start : finish : countBy

默认 countBy 为1

#### 获得逆字符串

```python
my_str='span'
reverse_str=my_str[::-1]
print(reverse_str)
```

输出结果为

maps

#### 遍历字符串

for 循环遍历字符串

`len(s)`表示s的长度。

### 搜索字符串

`str.count(substring)` 返回Str中substring子串出现的无覆盖的次数

`str.find(s1)` 返回s1在这个字符串中的最低下标，如果不存在，则返回-1

`str.rfind(s1)` 返回s1在这个字符串的最高下标，如果不存在，则返回-1

`str.startswith(s1)` 如果字符串以s1开始，返回True

`str.endswith(s1)` 如果字符串以s1结尾，返回True



## random库主要生成随机数

`random()` 生成一个$[0.0,1.0)$之间的随机小数

`randint(a,b)` 生成一个$[a,b]$之间的整数

`uniform(a,b)` 生成一个$[a,b]$之间的随机小数

### 对random库的引用方法

import random

from random import$^{*}$ (*引入random库中的所有函数*)

```python 
from random import random
```

*引入random库中的random函数*

# 函数

## 函数基础

### 函数作用

### 函数分类

1.内置函数

2.标准库函数

3.第三方库函数

4.自定义函数

## 函数的定义与调用

### 定义

def 函数名([形参列表])：

​	函数题

### 调用

函数名([实参列表])

例：

```python
def average(a,b):
  return (a+b)/2

```

### 函数语法规范

1.函数名需要自定义

2.形参可以没有，但必须保留一对空的圆括；如果有多个参数，用逗号隔开。

3.括号后的冒号必不可少

4.函数体相对于def关键字必须保持一定的缩进。

## 函数返回值

return语句将一个结果对象返回给被调者

return也可以不带返回值，同样默认返回None

返回值可以有多个，中间用逗号隔开，返回结果可按顺序赋值给多个变量。







# 其他

## 输入用逗号隔开

``` python
a,b,c,d,f = input().split(',')
```

## 找出一个整数的所有因子

``` python
a=int(input())
i=2
ans=[]
while(i<=a):
    while(a%i==0):
        ans.append(str(i))
        a=a/i
    i=i+1
print(','.join(ans))

```

输入 120

输出 2,2,2,3,5

也可用 `for`循环

```python
a=int(input())
ans=[]
for i in range(2,a+1):
    while(a%i==0):
        ans.append(str(i))
        a=a/i
print(','.join(ans))

```



















