.. _articles23:

Fork 系统炸弹
=============

2009年3月2日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

这个炸弹很简单，就是一个命令行，如下所示：

::

    :(){ :|:& };:

在此，我严重警告你，请不要在你的Unix/Linux或Cygwin的Shell下执行这个命令。否则，这个命令会不停地fork子进程，直到你的整个系统无法响应。

再次警告你，请不要执行这个命令，除非你想重启你的系统。

.. |image6| image:: /coolshell/static/20140921000813937000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/23.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com