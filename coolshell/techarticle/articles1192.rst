.. _articles1192:

一些单元测试的Guideline
=======================

2009年7月27日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

Jimmy Bogard 曾经写过一篇文章：
《\ `从单元测试中获益 <http://www.lostechies.com/blogs/jimmy_bogard/archive/2008/12/18/getting-value-out-of-your-unit-tests.aspx>`__\ 》，这这篇文章中给出了下面三条规则：

#. “\ **测试名应该从用户的角度描述是什么和为什么**\ ” –
   这样一来，程序员可以从名字就可以知道用户需要什么样的软件行为。
#. “\ **测试也是代码，同样也需要我们更多的爱**\ ” –
   真实运行在生产环境下的代码不仅仅只是我们需要去关心和花心思的代码。对于单元测试中的代码同样也需要易读易维护，以及可重用的特性。“\ *我非常痛恨那些又长又复杂的测试代码，如果一个测试需要30行的单元测试代码，请把其放在一个方法中。一个长的测试步骤只会激怒程序员。如果你在正式的代码中都没有这么长的代码，那么为什么我们需要在测试代码中容忍这样的情形呢？*\ ”
#. “\ **不要只用一种固定的模式或组织风格**\ ”\ *–*\ 有些时候，对于一些特殊的测试案例，标准的类设计模式，或一个固有的测试装置可能并不能有效的工作。

`Lior
Friedman <http://tech.groups.yahoo.com/group/testdrivendevelopment/message/31412>`__
加上： “第0条 –
测试应该只测试单元其外部的行为，而不是内部的结构”。或者说，只测试对一个单元的期望，而不是这个单元的构成。

`Ravichandran
Jv <http://groups.google.com/group/nunit-discuss/msg/56c9d75647731502?hl=en>`__
也加上了他的条例：

#. 一个测试一个断言（如果可能）。 
#. 如果在测试中有“if else”
   的语句，请把if和else两个分支拆分成两个测试案例。 
#. 如果一个测试案例中也有if else 分枝，那么这个测试案例也需要被重构。
#. 测试案例的命名代表了这种测试的类型。例如：TestMakeReservation()
   和TestMakeNoReservation()是不一样的类型。

`Charlie
Poole <http://groups.google.com/group/nunit-discuss/msg/fb335c19a8a44821?hl=en>`__\ ，NUnit的作者，重述了“一个测试一个断言”成“一个逻辑断言Logical
Assert” – 他说，
“有时候，因为我们测试API的表现不足，你需要写多个物理的Assert才能达到一个完整的结果。许多使用NUnit框架API进行单元测试的开发，很不可能只使用一个Assert就完成了一个测试”。

`Bryan
Cook <http://www.bryancook.net/2008/06/test-naming-conventions-guidelines.html>`__
也提供了一个不错的可供考虑的列表：

#. 做到：对Fixture一致地命名
#. 做到：使用namespace
#. 做到：测试方法的命名和Setup/TearDown 一致
#. 考虑：分离你的测试和开发代码
#. 做到：测试的命令和被测试的功能一致
#. 考虑：使用”Cannot” 前缀命名期望的异常

Bryan 有超过 \ `一打的建议 <http://www.bryancook.net/2008/06/test-naming-conventions-guidelines.html>`__\ 。

最后，有些人建议大家读一下 Gerard Meszaros的书： “\ `xUnit Test
Patterns: Refactoring Test
Code <http://www.amazon.com/xUnit-Test-Patterns-Refactoring-Addison-Wesley/dp/0131495054/ref=sr_1_1?ie=UTF8&s=books&qid=1248380993&sr=8-1>`__\ ”

文章：\ `链接 <http://www.infoq.com/news/2009/07/Better-Unit-Tests>`__

.. |image| image:: /coolshell/static/20140921224230637000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1192.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com