
## 2. python语法基础：
### 2.0 安装环境 【TODO 看环境】
[安装参考](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001374738150500472fd5785c194ebea336061163a8a974000)

* 1. python
* 2. pycharm
* 3. 控制台、执行

### 2.1 第一个程序
* 输入、输出
 
### 2.2 python数据类型：
* 数据类型：整数、浮点数、字符串、布尔值、空值
>表示方法
>运算规则
> 字符串的常见操作:比较函数：cmp();长度:len();replace()
* 取模运算、取余运算
* 概念：变量、常量
>>>import const

>>>const.magic = 23 

>>>const.magic = 33 


* 字符编码和字符串
>unicode, gbk, utf-8
* 列表list, 元组tuple, 字典dict, 集合set
>list:
>有序的集合，可以随时添加和删除其中的元素
>列表的常见操作.len(str), str[i], list 切片:len[-1],append(),insert(1, 'Jack'),pop()
>tuple
>一旦初始化就不能修改
>元组的常见操作: 定义(1,2), 取值：t[i]

>dict
>字典的常见操作
键-值（key-value）存储;
>d['Jack']
>'Thomas' in d
>d.get('Thomas') => d.get('Thomas', None)
>d.pop('Bob')

>set
>也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
>集合的常见操作
>s.add(4)
>s.remove(4)
>a.sort()
>a.replace('a', 'A')


### 2.3 python控制结构：
if...else
while

* pep8规范中的换行，内嵌

* if...else, for, while


### 2.4 习题
#### 2.4.1 整数
>>> 1 + 2 * 4

9

>>> (1+2)*4

12

#### 2.4.2 进制
>>> 11 + 12

23

>>> 011 + 012

19

### 2.4.3 不同数据结构运算
>>> 1 + 1.1

2.1

>>> type(1.1)

<type 'float'>

>>> type(1)

<type 'int'>

### 2.4.4 编写计算器
简单的‘1+2’一级运算

### 2.4.5 字典写学号-姓名，随机打印姓名

