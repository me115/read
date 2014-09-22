.. _articles1684:

把ASCII图转成图片
=================

2009年11月8日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

我们都知道有很多软件帮我们把图片转成ASCII码图，这里这个工具是帮我们把ASCII图转成漂亮的图片。这个开源的软件是一个用Java写成的一个命令行的工具。对于这个工具的目的，我个人以为如下：

-  其一，可以把别人的ASCII图转成图片，于是更好看一些。
-  其二，你可以使用ASCII码画图，而不需要使用图片编辑器。
-  其三，因为是命令行，所以，你完全可以以脚本或程序的方法来作图了。

这个工具软件叫ditaa，其网址是：\ `http://ditaa.sourceforge.net/ <http://ditaa.sourceforge.net/>`__\ 。

|image0|\ |image1|

这个小工具支持一些语法定义，可以帮你更好地产生图片，如下所示：

**圆角矩形**

::

    /--+
    |  |
    +--/

**定义颜色**

::

    Color codes
    /-------------+-------------\
    |cRED RED     |cBLU BLU     |
    +-------------+-------------+
    |cGRE GRE     |cPNK PNK     |
    +-------------+-------------+
    |cBLK BLK     |cYEL YEL     |
    \-------------+-------------/

|color code|

**一些图示**

名字 ASCII 图版 注释 文档

::

    +-----+
    |{d}  |
    |     |
    |     |
    +-----+

|image3| 表示文件 存储

::

    +-----+
    |{s}  |
    |     |
    |     |
    +-----+

| |image4| 表示数据库或磁盘 输入
|  输出

::

    +-----+
    |{io} |
    |     |
    |     |
    +-----+

|image5| 输入/输出标志。

**线条设置**

::

    ----+  /----\  +----+
        :  |    |  :    |
        |  |    |  |{s} |
        v  \-=--+  +----+

|image6|

**线上的链接点**

::

    *----*
    |    |      /--*
    *    *      |
    |    |  -*--+
    *----*

|point marker demo|

**文本**

::

    /-----------------\
    | Things to do    |
    | cGRE            |
    | o Cut the grass |
    | o Buy jam       |
    | o Fix car       |
    | o Make website  |
    \-----------------/

|bullet point demo|

.. |image0| image:: /coolshell/static/20140922102032925000.png
.. |image1| image:: /coolshell/static/20140922102033482000.png
.. |color code| image:: /coolshell/static/20140922102033992000.png
.. |image3| image:: /coolshell/static/20140922102034482000.png
.. |image4| image:: /coolshell/static/20140922102034979000.png
.. |image5| image:: /coolshell/static/20140922102035483000.png
.. |image6| image:: /coolshell/static/20140922102035966000.png
.. |point marker demo| image:: /coolshell/static/20140922102036464000.png
.. |bullet point demo| image:: /coolshell/static/20140922102036955000.png
.. |image15| image:: /coolshell/static/20140922102037449000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1684.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com