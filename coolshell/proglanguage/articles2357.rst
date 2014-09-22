.. _articles2357:

一个jQuery的插件
================

2010年4月14日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

jQuery这个强大的玩意我就不多说了，不知道可以上网搜搜看。IE6我也不多说了，这可能是史上骂名最多的一个浏览器，网上有N多的声讨IE6的文章，你也可以参看本站的《\ `9个最常见IE的Bug及其fix <http://coolshell.cn/articles/1817.html>`__\ 》和《\ `IE的CSS相关的BUG <http://coolshell.cn/articles/1245.html>`__\ 》，如果你今天还在用IE6，或是IE类浏览器，那请让我小小的BS你一下。

这个jQuery的Plugin可能是有史以来所有plugin中最有个性的一个，因为这个plugin什么也不干，其会用户的IE6版的浏览器直接Crash掉。这个plugin叫jQuery
Crash，其网页链接在下面，是一个四星级的插件，仅仅435个字节。

`http://plugins.jquery.com/project/crash <http://plugins.jquery.com/project/crash>`__

其是这样介绍自己的，有脏话，我就不翻译了。

    A jQuery plugin for crashing IE6. That’ll teach those motherf!%@\*#s
    to upgrade their s#\*t.

其它，让IE系例的浏览器挂掉，并不需要Javascript，你可以尝试点击下面这个页面，这是一个纯HTML的页面，没有任何的CSS，或是JS的东西，只有HTML。请小心打开（如果在Firefox中打开也可能会挂，Chrome中没事）

`http://www.gregmerideth.net/html/iecrash.html <http://www.gregmerideth.net/html/iecrash.html>`__

这个纯HTML的来源是本来是作者写了一个程序生成了一个N层嵌套的表格，结果在IE5中导致了IE5不响应直到Crash并使用了100%的CPU资源，这么多年过去了，还是老样子，在我的dual-core+IE7上，也是一样，占了50%的CPU，而且还有很高的内核使用，最后只能把进程给kill了。BT啊，纯HTML都会让IE这样。

.. |image6| image:: /coolshell/static/20140922104841364000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/2357.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com