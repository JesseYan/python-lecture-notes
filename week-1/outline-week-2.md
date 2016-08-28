
### 3.1 python关键字
False       class     finally    is         return
None       continue   for        lambda     try
True       def        from       nonlocal   while
and        del        global     not        with
as         elif       if         or         yield
assert     else       import     pass
break      except     in         raise

### 3.2 python三种控制结构：
* if... (if...else...)
* for
* while

#### 1. if 结构
python语句结构控制: tab
```python
if(True):
    print "if true"
    pass
else:
    print "false"
    pass
```

#### 2. for 结构

```python
a = [1,3,5,7,9]
for i in a:
    print i
```


```python
for i in range(10):
    print i
```

#### 3. while 结构
```python
a = 0
while(a<10):
    print a
    a = a + 1
```

### 3.3 python中的概念：
常量、变量、 函数、模块、包、类、继承

#### 3.3.1 常量与变量：
Python中在程序运行时不会被更改的量称之为常量，比如数字7和字符串“abc"在运行时一直都是数字7和字符串”abc“，不会更改成其他的量，这些都是常量
常量：内存地址不改变
变量：指向常量的变量,值改变则指向也改变(指针)

```python
a = 1 //a是变量，1是常量
```
#### 3.3.2 函数
函数、抽象: [函数定义和解释](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013747383144265f6402ab37cc40c5aecc816c08d8b771000)
调用函数：
函数定义：
函数的参数：
函数签名
递归函数

#### 3.3.3 模块module、包package、库lib

module：一个 .py 文件就是个 module

package：就是个带 __init__.py 的文件夹，并不在乎里面有什么，不过一般来讲会包含一些 packages/modules

lib：抽象概念，和另外两个不是一类，只要你喜欢，什么都是 lib，就算只有个 hello world


模块：
在Python可理解为对应于一个文件。在创建了一个脚本文件后，定义了某些函数和变量。你在其他需要这些功能的文件中，导入这模块，就可重用这些函数和变量。一般用module_name.fun_name，和module_name.var_name进行使用。这样的语义用法使模块看起来很像类或者名字空间，可将module_name 理解为名字限定符。模块名就是文件名去掉.py后缀。下面演示了一个简单的例子：

```python
#moduel1.py
def say(word):
    print word

#caller.py
import module1

print __name__
print module1.__name__
module1.say('hello')
```

#### 3.3.4 面向对象知识：类、继承
 1. Python 面向对象
Python从设计之初就已经是一门面向对象的语言，正因为如此，在Python中创建一个类和对象是很容易的

 2. 面向对象技术简介
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
实例变量：定义在方法中的变量，只作用于当前实例的类。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。

 3. 创建类
使用class语句来创建一个新类，class之后为类的名称并以冒号结尾，如下实例:
```python
class ClassName:
   '类的帮助信息'   #类文档字符串
   class_suite  #类体
```
* 类的帮助信息可以通过ClassName.__doc__查看。
* class_suite 由类成员，方法，数据属性组成。


实例
以下是一个简单的Python类实例:
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
```

* empCount变量是一个类变量，它的值将在这个类的所有实例之间共享。你可以在内部类或外部类使用Employee.empCount访问。
* 第一种方法__init__()方法是一种特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法


4.创建实例对象
要创建一个类的实例，你可以使用类的名称，并通过__init__方法接受参数。
"创建 Employee 类的第一个对象"
```python 
emp1 = Employee("Zara", 2000)
```
"创建 Employee 类的第二个对象"
```python 
emp2 = Employee("Manni", 5000)
```

5. 访问属性
您可以使用点(.)来访问对象的属性。使用如下类的名称访问类变量:
```python
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
```

完整实例：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
      print "Name : ", self.name,  ", Salary: ", self.salary
      
```

"创建 Employee 类的第一个对象"
```python
emp1 = Employee("Zara", 2000)
```
"创建 Employee 类的第二个对象"
```python
emp2 = Employee("Manni", 5000)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount
```
执行以上代码输出结果如下：
```shell

Name :  Zara ,Salary:  2000
Name :  Manni ,Salary:  5000
Total Employee 2
```

你可以添加，删除，修改类的属性，如下所示：
```python
emp1.age = 7  # 添加一个 'age' 属性
emp1.age = 8  # 修改 'age' 属性
del emp1.age  # 删除 'age' 属性
```
你也可以使用以下函数的方式来访问属性：
* getattr(obj, name[, default]) : 访问对象的属性。
* hasattr(obj,name) : 检查是否存在一个属性。
* setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
* delattr(obj, name) : 删除属性。
```python
hasattr(emp1, 'age')    # 如果存在 'age' 属性返回 True。
getattr(emp1, 'age')    # 返回 'age' 属性的值
setattr(emp1, 'age', 8) # 添加属性 'age' 值为 8
delattr(empl, 'age')    # 删除属性 'age'
```

8. Python内置类属性
>__dict__ : 类的属性（包含一个字典，由类的数据属性组成）
>__doc__ :类的文档字符串
>__name__: 类名
>__module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
>__bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
>


Python内置类属性调用实例如下：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
   '所有员工的基类'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
       print "Total Employee %d" % Employee.empCount

   def displayEmployee(self):
       print "Name : ", self.name,  ", Salary: ", self.salary

print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__
```

执行以上代码输出结果如下：
```shell

Employee.__doc__: 所有员工的基类
Employee.__name__: Employee
Employee.__module__: __main__
Employee.__bases__: ()
Employee.__dict__: {'__module__': '__main__', 'displayCount': <function displayCount at 0x10a939c80>, 'empCount': 0, 'displayEmployee': <function displayEmployee at 0x10a93caa0>, '__doc__': '\xe6\x89\x80\xe6\x9c\x89\xe5\x91\x98\xe5\xb7\xa5\xe7\x9a\x84\xe5\x9f\xba\xe7\xb1\xbb', '__init__': <function __init__ at 0x10a939578>}
```

6. 类的继承
面向对象的编程带来的主要好处之一是代码的重用，实现这种重用的方法之一是通过继承机制。继承完全可以理解成类之间的类型和子类型关系。
需要注意的地方：继承语法 class 派生类名（基类名）：//... 基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。
在python中继承中的一些特点：
* 1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
* 2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
* 3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 

语法：
派生类的声明，与他们的父类类似，继承的基类列表跟在类名之后，如下所示：
```python
class SubClassName (ParentClass1[, ParentClass2, ...]):
   'Optional class documentation string'
   class_suite
```

实例：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:        # 定义父类
   parentAttr = 100
   def __init__(self):
      print "调用父类构造函数"

   def parentMethod(self):
      print '调用父类方法'

   def setAttr(self, attr):
      Parent.parentAttr = attr

   def getAttr(self):
      print "父类属性 :", Parent.parentAttr

class Child(Parent): # 定义子类
   def __init__(self):
      print "调用子类构造方法"

   def childMethod(self):
      print '调用子类方法 child method'

c = Child()          # 实例化子类
c.childMethod()      # 调用子类的方法
c.parentMethod()     # 调用父类方法
c.setAttr(200)       # 再次调用父类的方法
c.getAttr()          # 再次调用父类的方法
```

以上代码执行结果如下：
```shell

调用子类构造方法
调用子类方法 child method
调用父类方法
父类属性 : 200
```

你可以继承多个类
```shell

class A:        # 定义类 A
.....

class B:         # 定义类 B
.....

class C(A, B):   # 继承类 A 和 B
.....
```

7. 方法重写
如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法：

实例：
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Parent:        # 定义父类
   def myMethod(self):
      print '调用父类方法'

class Child(Parent): # 定义子类
   def myMethod(self):
      print '调用子类方法'

c = Child()          # 子类实例
c.myMethod()         # 子类调用重写方法
```

执行以上代码输出结果如下：
> 调用子类方法

8. 运算符重载
Python同样支持运算符重载，实例如下：
```python
#!/usr/bin/python

class Vector:
   def __init__(self, a, b):
      self.a = a
      self.b = b

   def __str__(self):
      return 'Vector (%d, %d)' % (self.a, self.b)
   
   def __add__(self,other):
      return Vector(self.a + other.a, self.b + other.b)

v1 = Vector(2,10)
v2 = Vector(5,-2)
print v1 + v2
```

以上代码执行结果如下所示: ```shell Vector(7,8) ```


9. 类属性与方法
>类的私有属性
__private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。在类内部的方法中使用时 self.__private_attrs。
类的方法
在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数
类的私有方法
__private_method：两个下划线开头，声明该方法为私有方法，不能在类地外部调用。在类的内部调用 self.__private_methods


```shell 
实例 :
```
```python
#!/usr/bin/python
# -*- coding: UTF-8 -*-

class JustCounter:
	__secretCount = 0  # 私有变量
	publicCount = 0    # 公开变量

	def count(self):
		self.__secretCount += 1
		self.publicCount += 1
		print self.__secretCount

counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
print counter.__secretCount  # 报错，实例不能访问私有变量
```

Python 通过改变名称来包含类名:
```shell

1
2
2
Traceback (most recent call last):
  File "test.py", line 17, in <module>
    print counter.__secretCount  # 报错，实例不能访问私有变量
AttributeError: JustCounter instance has no attribute '__secretCount'
```

Python不允许实例化的类访问私有数据，但你可以使用 object._className__attrName 访问属性，将如下代码替换以上代码的最后一行代码：
.........................
```python print counter._JustCounter__secretCount ```
执行以上代码，执行结果如下：
```shell

1
2
2
2
```




