---
title: Style Guide for Python Code
date: "2023-01-26"
tags: []
draft: false
---
{{< katex >}}

## 1  Lines and Indentation

每个语句独占一行  不要在行尾使用分号，不建议复合语句（用分号将几个命令放在同一行）\
有时可以将极简单的 `if` `for` `while` `def` 等写在同一行上（无 `else` 子句时）

行长不超过80个字符，以下情况除外：1.长的导入模块语句 2.注释里的URL

不应用反斜杠连接行；建议利用圆括号（包括方括号和花括号）隐式的连接行\
若含有二元运算符，建议在其前断行\
有结构的序列可以分行写（注意缩进），末尾括号可以选择齐平或不缩进

```python
x = ("This is Python\n"
     "Then continue\n"
     "Do not use '\' at the end of each line\n"
     "Strings can add in this way, omitting the plus sign")

income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

my_list = [
    1, 2, 3,
    4, 5, 6,
    ]

# Or it may be lined up under the first character of the line.
result = some_function_that_takes_arguments(
    'a', 'b', 'c',
    'd', 'e', 'f',
)
```

当多个语句不能隐式连续时，反斜杠仍是可以接受的

```python
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

字符串使用单引号或双引号在文档中保持一致\
多行字符串应使用三重双引号（仅当文档使用单引号作定界符才可能采用三重单引号）

注意括号使用宁缺毋滥，除非类似于行连接，否则无需在语句中添加括号\
不过元组两端可以适当括起，如`for (x, y) in dict.items():`

用 4 个空格缩进代码而不要使用 Tab 甚至混用\
对于行连接的情况，要么垂直对齐换行的内容，要么使用 4 空格悬挂式缩进（这时第一行不应留有参数内容）

```python
foo = long_function_name(var_one, var_two,
                         var_three, var_four)

foo = long_function_name(
    var_one, var_two, var_three,
    var_four)

if (this_is_one_thing and
    that_is_another_thing):
    do_something()
    
# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()
```

顶级定义如函数或类定义之间空两行\
方法定义之间及类定义与第一个方法定义之间空一行\
顶级程序、函数或方法中有合适的地方（如功能的分别）可以空一行

## 2  Spaces

逗号、冒号、分号前面不要加空格，而应在后面加一个空格（除了行尾）\
切片中的冒号、尾随逗号后无需空格\
（尾随逗号：单项的元组或期待增加的序列（需要分行缩进写）中使用）\
调用的参数列表、索引、切片的圆括号和方括号前不加空格\
括号内部不添加空格

```python
# Correct:
     if x == 4:
         print(x, y)
     x, y = y, x

# Wrong:
     spam( ham[ 1 ], { eggs: 2 }, [ ] )
     def complex (real, imag = 0.0): return magic (r = real, i = imag)
```

二元操作符两边都应加上空格，包括赋值（`=` `+=` 等）、比较（`==` `>` `in` `is` 等）、布尔运算（`and` `or` `not`）\
算术操作符两边的空格视个人情况而定（但两边应保持一致），考虑在优先级最低的运算符两边空开

当 `=` 用于指示关键字参数或未注释的带有默认值的形参时，不要在其两侧使用空格\
而有注释和默认值的形参 `=` 两边需加上一个空格

不要用空格来垂直对齐行间的标记，如 `#`、`=`、`:` 等，这会成为维护的负担

```python
# Wrong:
     foo       = 1000  # comments
     long_name = 2     # comments do not need alignment

     dictionary = {
         "foo"      : 1,
         "long_name": 2,
         }
```

避免在任何地方尾随空格\
这会带来混乱和影响，如反斜杠后跟空格和换行符都不算作行继续标记

## 3  Comments and Docstrings

确保对模块、函数、方法和行使用正确的风格注释\
使用文档字符串，它是包、模块、类或函数里的第一个语句，可以通过对象的 `__doc__` 成员被自动提取

文档字符串使用双三引号 `"""`，首先为摘要行，位于三引号的同一行或下一行（可能仅需单行文档字符串，如 `"""Return sth."""`）\
接着分段分行介绍，它们应与第一行的引号对齐\
末尾应单独一行 `"""`，后还需一空行隔开

模块的文档字符串应列出导出的类、函数及异常，每个都用一行概述

函数或方法的文档字符串应概述其行为，并记录参数、返回值、副作用、异常和何时调用的限制\
可选参数也需要指示，同时也要记录某些关键字参数是否为接口的一部分

类的文档字符串应概述其行为，并列出公开的方法和实例变量\
如果它将被继承，接口应单独列出在文档字符串里\
私有方法注释在它们自己的文档字符串里\
如果它大幅继承了父类的行为，其文档字符串应提及并概述差异\
用 `'override'` 表示重写了该方法，`'extend'` 表示该方法中调用了父类方法

对每个元素或参数用单独一行概述，组织可以参考下例

```python
def fetch_bigtable_rows(big_table, keys, other_silly_variable=None):
    """Fetches rows from a Bigtable.

    Retrieves rows pertaining to the given keys from the Table instance
    represented by big_table.  Silly things may happen if
    other_silly_variable is not None.

    Args:
        big_table: An open Bigtable Table instance.
        keys: A sequence of strings representing the key of each table row
            to fetch.
        other_silly_variable: Another optional variable, that has a much
            longer name than the other args, and which does nothing.

    Returns:
        A dict mapping keys to the corresponding table row data
        fetched. Each row is represented as a tuple of strings. For
        example:

        {'Serak': ('Rigel VII', 'Preparer'),
         'Zim': ('Irk', 'Invader'),
         'Lrrr': ('Omicron Persei 8', 'Emperor')}

        If a key from the keys argument is missing from the dictionary,
        then that row was not found in the table.

    Raises:
        IOError: An error occurred accessing the bigtable.Table object.
    """
    pass


def complex(real=0.0, imag=0.0):
    """Form a complex number.

    Keyword arguments:
    real -- the real part (default 0.0)
    imag -- the imaginary part (default 0.0)
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...
```

块注释应与下面部分的缩进一致\
每一行都以一个`#`和一个空格开头，如果要分段则单独一行一个`#`

谨慎使用行注释\
行注释应至少离开代码两个空格并以`#`和一个空格起始

不要描述代码，应假设阅读的人比你更懂Python，只是不知道这个程序干什么

```python
x = x + 1    # Don't: Increment x  Do: Compensate for border
```

变量可能需要注释\
推荐使用类型注释（其规范一致，如冒号后加一空格而前无需，等号两边各需要一空格）

```python
primes: List[int] = []

captain: str  # Note: no initial value!

class Starship:
    stats: ClassVar[Dict[str, int]] = {}
```

尽量使用英文注释\
注释内应是若干完整的句子，首字母应大写（除非是标识符，不应改变）且每句句号结束后使用两个空格

```python
# We use a weighted dictionary search to find out where i is in
# the array.  We extrapolate position based on the largest num
# in the array and the array size and then do binary search to
# get the exact number.
#
# Another paragraph.
```

## 4  Names

核心发行版的代码必须使用UTF-8，且无须编码声明\
谨慎使用非ASCII字符（仅限特殊地名和人名）

命名样式一共有：1.单大写/小写字母 2.小写/小写加下划线 3.大写/大写加下划线 4.首字母大写（驼峰式）5.混合式（首字母大写但第一个单词的首字母小写）6.首字母大写加下划线（不推荐）

避免使用 `l` `I` `O` 作为单字母名称，可以用 `L` 替代

模块应具有简短的小写式名称，可以使用下划线提高可读性（包名并不建议）

类名采用驼峰式，不过当其记录为接口并主要作可调用对象使用时，可以采用函数的命名方式\
注意内建名称中绝大多数都是单词或双词合并，驼峰式出现在异常名和内建常量（`False` `True` `None` `Ellipsis` `__debug__`）里\
异常也属于类，遵循同样的命名方式，记得加上后缀Error（如果是错误的话）

模块的全局变量命名与函数方式一致\
模块应防止全局变量被导出，可以在名称前加一个下划线的老办法，或者指定它们不公开\
（模块应显式的在 `__all__` 中声明公共接口，同时给所有内部接口加上单下划线前缀）

函数和变量名应采用小写式，可以使用下划线提高可读性\
混合式仅允许当文档风格都以其主导时使用，保留向后的兼容性

函数和方法参数的名字常为一个小写单词，注意实例方法与类方法第一个参数永远是 `self` 与 `cls`\
如果其名字与保留关键字冲突，应在前面添加一个下划线而不是损坏拼写，或者更换为同义词

方法名和实例变量名应采用小写式，可以使用下划线提高可读性\
使用单个下划线前缀来保护非公开的方法和实例变量，它们是不想被第三方访问的且可能修改（一般用作“子类API”）\
使用两个下划线前缀来避免名称与子类冲突或不允许子类访问（Python 对此提供了弱的保护机制）

公开属性供给不相关的对象使用，并且能够承诺不会有向后不兼容的改变\
其开头不使用下划线，如果与保留关键字冲突，可以加一个下划线后缀而不是损坏拼写\
对于简单的公开数据属性，更推荐直接暴露而不是复杂的访问或修改方法  如果需要增添函数行为，使用属性包装\
注意，该行为应该尽量无副作用（尽管有些如缓冲很好），避免复杂的计算（这与便捷的调用表象不符）

常量名采用大写式，可以使用下划线提高可读性，如 `MAX_TOTAL`；其应该定义在模块级别

## 5  Progamming Recommendations

`import`请分行单个导入\
位于模块注释和文档字符串之后，模块全局变量和常量之前\
导入顺序按照通用程度递减分组：1.标准库 2.相关第三方库 3.本地特定的应用程序和库

避免在循环中累加字符串等创建临时对象的方式 如 `a += b` 可以改为 `bs.append(b)  a = ''.join(bs)`

与像 `None` 这样的单项比较时应该使用 `is` 或 `is not`，而不是 `==`\
使用运算符 `is not`，而不是 `not ... is`

不要把布尔值用 `==`（甚至 `is`）与 `True` `False` 比较，略去它们\
注意写 `if x` 与 `if x is not None` 的区别\
推荐写 `if seq` `if not seq` 而不是 `if len(seq)` `if not len(seq)`

当实现比较丰富的比较操作时，最好实现所有六个操作，而不要依赖其他代码执行某一个特定的比较\
（`__eq__` `__ne__` `__lt__` `__le__` `__gt__` `__ge__`）\
（由于 Python 假定反身性，可能交换如 `y > x` 和 `x < y`，`x == y` 和 `y == x`，这还出现在 `sort()` `min()` `max()` 等函数里）

直接绑定标识符的函数语句不要使用 lambda 表达式，没有好处且不方便回溯

```python
# Correct:
def f(x): return 2*x

# Wrong:
f = lambda x: 2*x
```

从 `Exception` 而非 `BaseException` 派生异常（只有当是不应该捕获它的时候才去继承基类异常）\
异常层次结构的分别和名称应注重发生错误的原因或机理，而不仅是发生的地方

捕获尽可能明确的异常，而不是使用裸子句 `except`，它会捕获系统退出和键盘中断，可能掩盖其他问题\
如果需要所有程序错误的捕获使用 `except Exception:`

限制 `try` 结构里的代码量至最小

不要在 `try`/`finally` 结构里使用流控制语句（`return`/`break`/`continue`）

```python
# Correct:
try:
    value = collection[key]
except KeyError:
    return key_not_found(key)
else:
    return handle_value(value)

# Wrong:
try:
    # Too broad!
    return handle_value(collection[key])
except KeyError:
    # Will also catch KeyError raised by handle_value()
    return key_not_found(key)
```

当源是本地特定的代码段时，用 `with` 确保在使用后可靠的清理，`try`/`finally` 语句也可以接受\
`with` 如果干了超出获取与释放资源以外的事，应显式的说明，在单独的函数或方法下调用

```python
# Correct:
with conn.begin_transaction():
    do_stuff_in_transaction(conn)
    
# Wrong:
with conn:
    do_stuff_in_transaction(conn)
```

同一个函数的返回语句保持一致（全部返回一表达式或全部不返回）\
如果某些情况不返回值，应完整的写出 `return None`\
尽量在函数的末尾给出清晰的返回表达式（如果可以的话）

```python
# Correct:

def foo(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return None

def bar(x):
    if x < 0:
        return None
    return math.sqrt(x)
```

使用 `''.starswith()` 和 `''.endswith()` 而不是字符串切片来检查前后缀，它们更加简洁且不易出错

不要使用依赖于有特定尾随空格的字符串文本，它们可能难以分辨或遭到修剪

对象类型的比较应使用 `isinstance()` 而不是直接比较它们的类型

```python
# Correct:
if isinstance(obj, int):

# Wrong:
if type(obj) is type(1):
```
