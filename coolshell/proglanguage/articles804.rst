.. _articles804:

关于C++构造函数的FAQ
====================

2009年5月13日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

下面是一些关于C++构造函数的FAQ。你能回答得出来吗？你可以点链接查看答案，不过是英文版的。他们来自于\ `*C++
FAQ
Lite* <http://www.parashift.com/c++-faq-lite/index.html>`__\ 。当然，也有中文版的，只可惜中文版的太老了，只更新到了2001年。在\ `*C++
FAQ
Lite* <http://www.parashift.com/c++-faq-lite/index.html>`__\ 上还有很多关于其它部分的FAQ，大家可以去看看。

`[1]
构造函数是用来干什么的？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.1>`__

`[2] ``List x;`` 和
``List x();有什么不同``? <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.2>`__

`[3]
是否一个类的构造函数可以调用另一个构造函数来初始化自己？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.3>`__

`[4]
是否Fred类的默认的函数函数就一定是\ ``Fred::Fred()？`` <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.4>`__

`[5] 如果要创建一个\ ``Fred``
对像数组，什么样的构数函数会被调用? <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.5>`__

`[6] 构造函数初始化成员变量时，用 “初始化列表” 还是
“赋值”？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.6>`__

`[7] 在构造函数中用\ ``this``
指针是否有问题？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.7>`__

`[8]什么是“名字构造函数”（Named Constructor
Idiom）？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.8>`__

`[9]
“值返回”意味着额外的拷贝吗？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.9>`__

`[10] 为什么我们不能在构造函数初始化列表中初始化一个 ``static``
成员变量？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.10>`__

`[11] 为什么一个有 ``static``
成员变量的类会有链接错误？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.11>`__

`[12] 什么是“\ ``static`` initialization order
fiasco”？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.12>`__

`[13] 我该如果避免 “\ ``static`` initialization order
fiasco”? <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.13>`__

`[14] 为什么 construct-on-first-use
什么静态变量而不是指针？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.14>`__

`[15] 怎么才能避免静态成员中的“\ ``static`` initialization order fiasco”
？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.15>`__

`[16] 我是否要为内建类型的“\ ``static`` initialization order
fiasco”而担心？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.16>`__

`[17]
如果构造函数出错了怎么办？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.17>`__

`[18] 什么是“命名参数惯用法”（Named Parameter
Idiom）？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.18>`__

`[19] 为什么我通过\ ``Foo x(Bar())``\ 声明一个\ ``Foo``
对象会得到一个错误？ <http://www.parashift.com/c++-faq-lite/ctors.html#faq-10.19>`__

.. |image| image:: /coolshell/static/20140922110046937000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/804.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com