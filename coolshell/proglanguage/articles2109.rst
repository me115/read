.. _articles2109:

Python处理encoding的小技巧
==========================

2010年2月8日 `mailper <http://coolshell.cn/articles/author/mailper>`__

用Python写过处理文本经常会遇到需要decoding或者encoding,
尤其是处理中文的时候。

encoding的问题处理起来是个脏活儿，报错不太容易看懂，网上相关资料不太好查。有同感？请继续读下去。

常规做法是读取文件的时候立刻decode,
所有的处理工作都用unicode，写会文件的时候encode.
但是等到读取的时候在处理的代码读/写起来都很别扭，感觉像穿上鞋以后袜子滑下来了…Python
3.1.1以上的版本解决了该问题。在Python
3.1.1中，打开文件可以加入encoding的参数：

::

    file = open(filename, encoding='xxx')

啊，这样看起来终于舒坦了。 不同写如下的code了

::

    file = open(filename)
    for line in file:
        decoded_line = line.decode('xxx')
        do something else
    提倡使用utf8

.. |image6| image:: /coolshell/static/20140922105003565000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/2109.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com