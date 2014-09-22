.. _articles1788:

程序语言性能比拼
================

2009年11月16日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

  下面这个网页，你可以比较各种程序语言的性能：

`http://shootout.alioth.debian.org/u64/index.php <http://shootout.alioth.debian.org/u64/index.php>`__

这个页面，安装的是x64 Ubuntu，CPU是Intel® Q6600®
单核。这个网页支持的语言很多，什么C，C++，Java，python，PHP，Erlang，C#，Ruby，……，还有最新的G0语言。

在主页上，你可以选择一个语言。比如，我们选择Google的Go语言——Go
6g8g，然后，点击Show按钮，于是，你会看到下面这个界面：

|go vs gnuc| 

在这个界面上方，你可以选择两种语言，我们选择的是，上面的是Go
6g8g，而下面是的GNU
C，于是下面的图表，是这两个语言各种参数和算法的比较图表。

在这个图表中，其实就是“Go的性能” 除以 “C的性能”，所以，

-  如果柱状图是大于1的（也就是基线以上的）则说明Go的性能不如C。
-  如果柱状图小于1的（也就是基线以下的），说明Go的性能超过了C。

再往下，是用来做比较的算法的图表，如下所示。在这个表中，我们可以看到很多算法，单击语言的链接，你就可以看到具体的实现源代码了。

|measurements table|

 （全文完）

.. |go vs gnuc| image:: /coolshell/static/20140921224019382000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2009/11/govsgnuc.jpg
.. |measurements table| image:: /coolshell/static/20140921224019979000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2009/11/measurements_table.jpg
.. |image8| image:: /coolshell/static/20140921224020165000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1788.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com