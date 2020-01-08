上课内容：慕课，东北大学

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



## 函数参数

不限制函数的参数类型

### 关键字参数调用

- 调用的时候使用形参的名字叫做关键字调用
- 函数调用时，实参顺序和形参顺序应保持一致。如果采用了关键字参数调用，则可不按顺序。**适合参数比较多的参数**。

### 默认值参数

- 默认值参数就是声明了默认值的参数
- 一个函数既有位置参数(非默认值参数)，也有默认值参数，则必须保证在形参列表中，**位置参数在前，默认值参数在后**
- 调用函数时，如未给出默认值参数的实参，则按默认值处理。

```python
def fun(a,b,c='three',d='four'):
  print(a,b,c,d)
```

### 参数传递

- 当参数为数字或字符串时，函数内形参值的修改不会影响实参。

  ```python
  def swap(x,y):
    x,y=y,x
    print('x=',x,'y=',y)
    
  a,b=1,2
  swap(a,b)
  print('a=',a,'b=',b)
  ```

  输出结果为：

  ```python
  x=2 y=1
  a=1 b=2
  ```

  



## 变量作用域

- 变量起作用的代码范围
- 在函数内部定义的普通变量只在函数内部起作用，称为局部变量。**当函数执行结束后，局部变量自动回收**，不再可以使用
- 在函数外部定义的变量称为全局变量。**局部变量的引用比全局变量速度快**。
- 如果需要在函数内部引用全局变量并修改变量值，必须在函数内使用global关键字进行声明。

```python
def demo():
  global x
  x=3
  y=4
  print(x,y)
  
>>>x=5
>>>demo()
3 4
>>>x
3
>>>y
NameError:name'y' is not defined 
```

## 递归函数

函数调用自身称为函数递归

函数递归不会是无限的调用，其终将满足某个条件而逐层返回。

例如：求阶乘

```python
def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n*fact(n-1)
```

## 模块化程序设计

- 代码复用
- 抽象
- 模块化

## 函数调用规范

- 不会自动执行，被调用才会执行
- 没有主函数的概念

# 列表和元组

## 列表基础属性

- 列表长度可变
- 列表内容可变
- 列表中的元素数据类型可以不同
- 用中括号`[]`表示，用逗号分隔其中的元素

## 创建列表

使用`=`直接将一个列表赋值给变量即可创建列表对象

```python
# 创建空列表
a_list = []
```

### 列表元素访问

访问方式：

列表名称[索引]

- 索引从0开始而不是从1开始

#### 列表切片

切片操作不会发生越界的错误

#### 列表操作符

使用 `+`运算符将元素添加到列表中 *实际上是生成了新列表，涉及大量元素添加时不建议使用*

使用`*`来扩展列表对象

使用`in`关键字来判断一个值是否存在于列表中，返回结果为"True" or "False"

使用`not in`关键字来判断一个值是否不存在于列表中，返回结果为"True" or "False"

### 列表遍历

使用 `for`循环遍历元素

```python
a_list=['this','is','a','list','example',1,2,3]
for x in a_list:
  print(x)
  
a_list=['this','is','a','list','example',1,2,3]
for i in range(len(a_list)):
  print(a_liat[i])
```

### 序列类型

- python中的字符串和列表都是序列类型
- 字符串是字符的序列
- 列表是任何元素的序列

### 列表常用操作

#### 追加元素

**append方法**

#### 扩展列表

**extend()方法**

#### 统计元素

**count()元素**

#### 插入元素

**insert()方法**

#### 删除元素

**remove()方法** 删除首次出现的指定元素

**pop()方法** 删除并返回指定位置(默认为最后一个)

#### 查找元素位置

**index()方法** 获取指定元素首次出现的下标

#### 列表排序

**sort()方法** 在原位置对列表进行排序，默认是升序排序

```python
alist.sort() # 默认是升序排序
alist.sort(reverse=True) # 降序排序
```

#### 列表复制

复制列表变量只是在复制列表的引用

可以使用**copy方法**或**list方法**复制出一个与原列表具有相同内容的列表

#### 可用于列表的内置函数

sorted(列表):对列表进行排序并返回新列表 *不是原位置排序*

len(列表):返回列表中的元素个数

max(列表),min(列表):返回列表中的最大或最小元素

sum(列表):对列表的元素进行求和运算

#### 列表解析式

列表解析--提供了一种创建顺序元素列表的简洁方式

列表解析可以产生一个由表达式求值结果组成的列表

- 列表解析式在内部实际上是一个循环结构，只是形式上更加简洁

  ```python
  >>> aList=[x*x for x in range(10)]
  # 相当于
  >>> aList=[]
  >>> for x in range(10):
    		aList.append(x*x)
  ```


### 列表常用算法

#### 填充

- 使用循环和列表的`append`方法填充列表

  ```python
  aList = []
  for i in range(n):
    aList.append(i*i)
  ```

#### 最小值和最大值

如何求取一个字符串列表中最长的字符串？

```python
names = ['Ann','Charlotte','Zachary','Bill']
longest = max(names,key=len)
```

#### 顺序查找

如果需要查找某个特定值的位置，可以直接使用index方法。

#### 收集匹配项

```python
limit = 100
result = []
for v in values:
  if v>limit:
    result.append(v)
```

```python
result = [x for x in values if x>100]
```

#### 统计匹配项

#### 删除所有指定元素

- 如果需要删除列表中所有某个确定的元素

```python
x=100
while x in values:
  values.remove(x)
```

```python
values = [x for x in values if x!= 100]
```

#### 删除匹配项

```python
values=[99,100,101,102,103]
i=0
while i<len(values):
  if values[i]>100:
    values.pop(i)
  else:
    i += 1
  
```

```python
values = [x for x in values if x<= 100]
```

### 在函数中使用列表

#### 列表作为函数参数

列表作为函数参数，函数中可以修改原列表

##### 可变对象与不可变对象

**整数、浮点数、字符串**属于不可变对象，**列表**属于可变对象。

#### 列表作为函数返回

当函数返回一个列表时，就会返回这个列表的引用。

```python
def multiply(values,factor):
  result = []
  for i in values:
    result.append(i*factor)
  return result
```

### 元组

- 属于不可变序列，即一旦创建，用任何方法都不可以修改
- 元组定义方法与列表相同，但是是把元素放在一对圆括号`()`中。

#### 元组的创建

- 使用`=`将一个元组赋值给变量

```python
a = (3,)
```

- 使用`tuple`函数将字符串或列表转换为元组
- `tuple()`冻结列表，`list()`融化元组

#### 元组的优点

- 速度比列表快
- 对不需要改变的数据进行“写保护”

# 文件和异常

## 读取和写入文本文件

- 以文本方式存储的文件
- 可以使用下面的函数调用来打开这个文件：

```python
infile = open('input.txt','r')
```

- 以读模式打开文件(通过字符串参数'r'来表示)，并且返回一个与input.txt文件相关联的文件对象
- 调用open函数返回的文件对象必须保存在一个变量中，所有处理文件的操作都通过这个文件对象来完成。
- 以写模式打开一个文件

```python
outfile = open('output.txt','w')
```

- 如果输出文件已经存在，它在写入新数据之前会被清空。
- 如果文件不存在，会创建一个空文件。
- 处理完文件之后，确定使用close方法关闭文件

```python
infile.close()
outfile.close()
```

### 读取文件

```python
line = infile.readline()
```

- readline方法从当前位置开始读取文本，直到遇到行尾。
- 然后输入标记被移到下一行。

```python
line = inflile.readline()
while line != '':
  process the line.
  line = infile.reading()
```

读取多行文本

### 写入文件

```python
outfile.write('Hello,World!\n')
```

- print函数会在输出的尾部增加一个换行符（区别）
- 使用print函数往文件中写入文本，需要提供文件对象作为参数file的值：

```python
print('Hello,World!',file=outfile)
```

- 如果不想换行，可以使用end 参数：

- ```pyt
  print('Total:',end='',file=outfile)
  ```

### 案件实例

```python
infile = open('input.txt','r') #以读模式打开input.txt文件
outfile = open('output.txt','w') #以写模式打开output.txt

#为了方便计算total 和 average
total = 0.0
count = 0

line = infile.readline()
while line != '':
  value = float(line)
  outfile.write('%15.2f\n' % value) #%表示格式化，15表示框的长度，默认右对齐
  total += value
  count += 1
  line = infile.readline()
  
outfile.write('%15s\n' % '________')
outfile.write('Total:%8.2f\n' % total)

avg = total / count
outfile.write('Average:%6.2f\n' % avg)

#最后一定要记得关闭文件
infile.close()
outfile.close()
```

## 文本输入和输出

### 迭代文件中的行

```python
for line in infile:
  print(line)
```

- 在每个迭代的开始，循环变量line被赋值为包含文件下一行文本的字符串

- 每一行包含最后的换行符

- ```python
  line=line.rstrip()
  ```

  rstrip方法创建一个新字符串，删除原字符串尾部的所有空白字符(空格、制表符、换行符)

  ```python
  line = line.rstrip('.?')
  ```

  删除字符串尾部的一个圆点或一个问号

- lstrip方法(首部删除)

- strip方法(两侧删除)

### 读取单词

- 从文件中读取一个单词

- 使用split方法将读取的一行切分成独立的单词

  ```python
  wordList = line.split()
  ```

  split方法返回在每个空白字符处对原始字符串进行切分得到的子字符串的列表，并且按在原字符串中出现的相同顺序存储到一个列表wordList中。

- ```python
  # 切分字符串后，可以迭代子字符串来输出这些独立的单词
  for word in wordList:
    print(word)
    
  ```

- ```python
  word.rstrip('.,?!') #只想输出文件中的单词而不包括标点符号
  ```

  ```python
  inputFile = open('lyrics.txt','r')
  for line in inputFile:
    line = line.rstrip() #删除末尾的换行符
    wordList = line.split() #将单词分开并存储到列表中
    for word in wordList:
      word = word.rstrip('.,?!')
      print(word)
  inputFile.close()
  ```

- 读取单个的字符

- 使用read方法读取独立的字符，而不是一整行

- ```python
  char = inputFile.read(1) # 1表示字符的长度的参数
  ```

  #### 实际案例

  ```python
  #判断一个文件中出现字母的次数
  letterCounts = [0] * 26 #初始化每个字母的个数
  inputFile = open('lyrics.txt','r') #以读模式打开该文件
  char = inputFile.read(1) 
  while char != '':
    char = char.upper() #将所有字母调成大写字母
    if char >= 'A' and char<= 'Z':   #不考虑其他特殊的字符
      code = ord(char) - ord('A')
      letterCounts[code] += 1
    char = inputFile.read(1) #接着读取下一行
  print(letterCounts)
  inputFile.close()
  ```


## 二进制文件与随机访问

- 在二进制形式中，数据项使用字节来表示。一个字节由8位组成，每一位可以是0或1.
- 包含图像和声音的文件通常以二进制格式保存信息
- 二进制文件节省空间

### 读写二进制文件

```python
inFile = open(filename.'rb') #以读模式打开二进制文件
outFile = open(filename.'wb') #以写模式打开文件
theBytes = inFile.read(4) #对于二进制文件，不能读取文本字符串，而是独立的字节。通过这个调用读取4个字节
```

- read方法返回的字节值保存位bytes序列类型。

- 一个bytes序列中的元素是介于0到255之间的整数值。

- 必须使用下标运算符从bytes序列中将其取出：

  ```python
  value = theBytes[0]
  ```

  ```python
  value = inFile.read(1)[0] #读取单个字节
  ```

  

```python
theBytes = bytes([64,226,1,0])
outFile.write(theBytes)
#使用write方法把一个或多个字节写入二进制文件。
#需要一个bytes序列作为参数
```

### 随机访问

- 顺序访问
- 随机访问：在没有读取前面所有项的情况下直接访问特定的项。

```python
inFile.seek(position) #seek方法把标记定位到相对于文件开始的位置
```

```python
Position = inFile.tell() #获取当前位置
```

# 异常处理

- 提前检测

- 事后处理

 `try/except`

- try/except用来处理异常
- try中包含可能引发异常的语句
- except中包含处理异常的代码
- except子句可以有多个，把比较具体的异常放在通用的异常前面。



# 其他

## 一些特殊的函数

### range()函数

range(start,end,step)

range()函数返回一个可迭代对象，可理解为一个序列，**序列中的数包括start,不包括end.**

### random库主要生成随机数

`random()` 生成一个$[0.0,1.0)$之间的随机小数

`randint(a,b)` 生成一个$[a,b]$之间的整数

`uniform(a,b)` 生成一个$[a,b]$之间的随机小数

#### 对random库的引用方法

import random

from random import$^{*}$ (*引入random库中的所有函数*)

```python 
from random import random
```

*引入random库中的random函数*

### id函数

可以查看变量对象实际的内存地址。

### len函数

len函数可以用来输出字符串的长度。

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

## 判断一个数是否为素数

```python
def isPrime(i):
  for j in range(2,i // 2 + 1):
    if i % j == 0:
      return False
   return True
```

## 判断一个数是否为回文数

```python
def isPalindrome(i):
  number = i
  result = 0
  while number != 0:
    remainder = number % 10
    result = result * 10 + remainder
    number = number // 10
  return i == result
    
```

## 随机生成一个小写字母

```python
def getRandomLetter():
  code_a = ord('a')
  code_z = ord('z')
  x = random.randint(code_a,code_z)
  return chr(x)
```

## 小写字母是连续编码的，大写字母比对应的小写字母多26

















