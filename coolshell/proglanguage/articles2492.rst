.. _articles2492:

WTF Javascript
==============

2010年6月2日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

请先看一下下面的这段Javascript程序以及其结果。

::

    1 + + 1              // => 2
    1 + - + 1            // => 0
    1 + - + - + 1        // => 2
    1 + - + - + - + 1    // => 0
    1 + - + + + - + 1    // => 2
    1 + / + + + / + 1    // => 1/ + + + /1

提示一下，1++1等价于1 +
(+1)，也就是1加上一个正数1，如果你能搞懂其它的表达式的话，请看看下面的这段程序，你能说出其结果吗？

::

    1 + / + / + / + 1    // => ?

如果不知道的话，你可以到这个\ `网页上去讨论讨论 <http://mir.aculo.us/2010/05/28/valid-javascript-or-not/>`__\ 。当然，如果你不懂也没有什么关系，因为Javascript本身就是一个很怪异的语言，再加上浏览器的种种不是，所以，\ `Javascript程序员也是很郁闷的 <http://coolshell.cn/articles/1850.html>`__\ 。在以前的“\ `最为奇怪的程序语言的特性 <http://coolshell.cn/articles/2053.html>`__\ ”中也说过一些。Javascript最怪异的特性导致了\ `wtfjs.com <http://wtfjs.com/>`__\ 这样的一个网站，还有一个\ `WTF
JS的开源站点 <http://github.com/brianleroux/wtfjs>`__\ 。呵呵。

.. |image6| image:: /coolshell/static/20140922104742924000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/2492.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com