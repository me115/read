.. _articles582:

使用Google API做统计图
======================

2009年4月20日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

Google提供了一个的统计图的API。你可以通过构造一个URL链接来获得Google提供的统计图方案。

比如：如果我们使用如下链接：

::

| 我们就可能通过如下的HTML代码显示一个60:40的饼图：
| |image0|

Google的这个API支持的统计图风格相当的多。

比如：

::

|Sparkline chart in blue|

还甚至支持有世界地图式的统计图：

::

更多的内容请到\ `http://code.google.com/apis/chart/ <http://code.google.com/apis/chart/>`__
上查看吧。

.. |image0| image:: http://chart.apis.google.com/chart?cht=p3&chd=t:60,40&chs=250x100&chl=酷壳|Cocre
.. |Sparkline chart in blue| image:: http://chart.apis.google.com/chart?chs=200x125&cht=ls&chco=0077CC&chd=t:27,25,60,31,25,39,25,31,26,28,80,28,27,31,27,29,26,35,70,25
.. |image8| image:: /coolshell/static/20140921220543156000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/582.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com