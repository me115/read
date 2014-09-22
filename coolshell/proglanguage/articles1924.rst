.. _articles1924:

Javascript 曲线表作图库
=======================

2009年12月11日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

`dygraphs <http://www.danvk.org/dygraphs/>`__ 是一个开源的Javascript库，它可以产生一个可交互式的，可缩放的的曲线表。其可以用来显示大密度的数据集（比如股票，气温，等等），并且可以让用户来浏览和解释这个曲线图。在它的主页（`http://www.danvk.org/dygraphs/ <http://www.danvk.org/dygraphs/>`__\ ），你可以看到一些示例和用法。

|dygraphs Javascript 曲线图库|

要使用这个库，很简单，只需要包括\ ``dygraph-combined.js``\ 文件，其文件尺寸很经济，也就45K。

::

下面两个示例，你可以把数据写在javascript中，也可以设置一个csv文件。

**示例一，你可以在代码中指定数据**

::



      g = new Dygraph(

        // containing div
        document.getElementById("graphdiv"),

        // CSV or path to a CSV file.
        "Date,Temperature\n" +
        "2008-05-07,75\n" +
        "2008-05-08,70\n" +
        "2008-05-09,80\n"

      );

**示例二、你可以引入外部的CSV文件**\ 。(\ ``temperatures.csv)``

::


      g2 = new Dygraph(
        document.getElementById("graphdiv2"),
        "temperatures.csv", // path to CSV file
        {}          // options
      );

.. |dygraphs Javascript 曲线图库| image:: /coolshell/static/20140922105158190000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2009/12/dygraphs.jpg
.. |image7| image:: /coolshell/static/20140922105158288000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1924.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com