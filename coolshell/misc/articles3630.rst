.. _articles3630:

Error handling in Egypt
=======================

2011年2月9日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

以前发布过《\ `C语言的错误处理 <http://coolshell.cn/articles/551.html>`__\ 》一文，不过今天想说的是Egypt的“错误处理”。埃及的事闹得挺大的，国外和中文twitter上更是炸了锅。不要以为程序员就只会写程序——看看程序员举出来的标语吧。呵呵。

|image0|

Error handling in Egypt

| 当然，作为程序员来说，这段代码显然还需要重构：

::

    try{
        elections(free,fare);
    } catch(DemocracyNotFoundException){
        System.err.println("Time for Mubarak to leave");
    }

也有的程序员说，System.err.println不是处理错误的最好方法，正确的方法应该是：

::

    try {
        elections(free,fair);
    } catch (DemocracyNotFoundException e) {
        throw new MubarakDepartureParty(e);
    }

最后，我们希望Egypt不要出现：

::

    ...
    finally {
        Security.shootProtesters();
    }

.. |image0| image:: /coolshell/static/20140922093323869000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2011/02/Error-handling-in-Egypt.jpg
.. |image7| image:: /coolshell/static/20140922093324262000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/3630.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com