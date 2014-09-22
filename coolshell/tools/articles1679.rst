.. _articles1679:

Vim的分屏功能
=============

2009年11月7日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

本篇文章主要教你如何使用 \ `Vim <http://www.vim.org/>`__ 分屏功能。

|vim-windows|

 |image1|

分屏启动Vim
^^^^^^^^^^^

#. 使用大写的O参数来垂直分屏。

   ::

       vim -On file1 file2 ...

#. 使用小写的o参数来水平分屏。

   ::

       vim -on file1 file2 ...

**注释:** n是数字，表示分成几个屏。

关闭分屏
^^^^^^^^

#. 关闭当前窗口。

   ::

       Ctrl+W c

#. 关闭当前窗口，如果只剩最后一个了，则退出Vim。

   ::

       Ctrl+W q

分屏
^^^^

#. 上下分割当前打开的文件。

   ::

       Ctrl+W s

#. 上下分割，并打开一个新的文件。

   ::

       :sp filename

#. 左右分割当前打开的文件。

   ::

       Ctrl+W v

#. 左右分割，并打开一个新的文件。

   ::

       :vsp filename

移动光标
^^^^^^^^

Vi中的光标键是h, j, k, l，要在各个屏间切换，只需要先按一下Ctrl+W

#. 把光标移到\ **右边**\ 的屏。

   ::

       Ctrl+W l

#. 把光标移到\ **左边**\ 的屏中。

   ::

       Ctrl+W h

#. 把光标移到\ **上边**\ 的屏中。

   ::

       Ctrl+W k

#. 把光标移到\ **下边**\ 的屏中。

   ::

       Ctrl+W j

#. 把光标移到\ **下一个**\ 的屏中。.

   ::

       Ctrl+W w

移动分屏
^^^^^^^^

这个功能还是使用了Vim的光标键，只不过都是大写。当然了，如果你的分屏很乱很复杂的话，这个功能可能会出现一些非常奇怪的症状。

#. 向右移动。

   ::

       Ctrl+W L

#. 向左移动

   ::

       Ctrl+W H

#. 向上移动

   ::

       Ctrl+W K

#. 向下移动

   ::

       Ctrl+W J

屏幕尺寸
^^^^^^^^

下面是改变尺寸的一些操作，主要是高度，对于宽度你可以使用[Ctrl+W
<]或是[Ctrl+W >]，但这可能需要最新的版本才支持。

#. 让所有的屏都有一样的高度。

   ::

       Ctrl+W =

#. 增加高度。

   ::

       Ctrl+W +

#. 减少高度。

   ::

       Ctrl+W -

``也许还有其它我不知道的，欢迎你补充。``

``（全文完）``

.. |vim-windows| image:: /coolshell/static/20140922102043207000.png
.. |image1| image:: http://coolshell.cn//wp-includes/js/tinymce/plugins/wordpress/img/trans.gif
.. |image8| image:: /coolshell/static/20140922102043648000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1679.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com