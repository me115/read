.. _articles2184:

BT工作原理演示
==============

2010年3月16日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

下面这个网站使用Javascript编写了一个BT工作原理演示动画程序。当然，你可能需要使用Chrome浏览器打开，因为他真的很耗CPU。在我的双核（2GHz）T60电脑上用Chrome打开CPU一下就被耗了50%左右。

`http://mg8.org/processing/bt.html <http://mg8.org/processing/bt.html>`__

下面是我截的一个图，每个圆代表一个结点，其会通过其它结点下载需要的文件段。结点中间的那个Bar有点类似于eDonkey中的下载进度条。至于为什么要用像彩虹一样的颜色，主要是为了让你看到不同的段是从不同的结点下载的。

你可以按热键S来加入一个下载完了的结点，用P来加入一下空结点，按R来删除一个结点（有点慢，要等10秒左右吧）。

|image0|

BT工作原理演示动画

关于其它Javascript的一些小玩意，你可以看看\ `这篇文章 <http://coolshell.cn/articles/1932.html>`__\ 。

.. |image0| image:: /coolshell/static/20140921215355685000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2010/03/bt_js_demo.jpg
.. |image7| image:: /coolshell/static/20140921215355796000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/2184.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com