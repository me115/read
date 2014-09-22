.. _articles4170:

我有一个Hello World的C++程序编译不过
====================================

2011年4月2日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

在StackOverflow上有这样\ `一个贴子 <http://stackoverflow.com/questions/5508110/why-is-this-program-erroneously-rejected-by-three-c-compilers>`__\ ，楼主说，我有下面这样的一个C++程序，为什么编译不通过啊。其让我想起了以前的这两个帖子《\ `编程真难啊 <http://coolshell.cn/articles/1391.html>`__\ 》和《\ `给我一个序列号 <http://coolshell.cn/articles/1693.html>`__\ 》。\ **仅以此篇文章祝大家假期快乐吧**\ 。

|hello world 程序|

hello world 程序

楼主还给出了相关的编译出错的信息（相信你一看就明白问题在哪里了，你应该还会发出一声“靠”！！！）

先是用Visual C++ 2010编译

::

    c:\dev>cl /nologo helloworld.png
    cl : Command line warning D9024 : unrecognized source file type 'helloworld.png', object file assumed
    helloworld.png : fatal error LNK1107: invalid or corrupt file: cannot read at 0x5172

再用G++ 4.5.2编译

::

    c:\dev>g++ helloworld.png
    helloworld.png: file not recognized: File format not recognized
    collect2: ld returned 1 exit status

再用clang编译

::

    c:\dev>clang++ helloworld.png
    helloworld.png: file not recognized: File format not recognized
    collect2: ld returned 1 exit status
    clang++: error: linker (via gcc) command failed with exit code 1 (use -v to see invocation)

| 不过，最强大的，有人居然给出了一个fix，靠！
| 
（下面的图片是一个4M大的gif动画，演示了整个过程，下载可能需要一定的时间。）

|hello world 的解决方案|

hello world 的解决方案 （图片有点大4M，请耐心等待下载）

真是BT啊，呵呵。\ **仅以此篇文章祝大家假期快乐吧**\ 。

.. |hello world 程序| image:: /coolshell/static/20140922113342957000.png
.. |hello world 的解决方案| image:: http://i.imgur.com/QlGpd.gif
   :target: http://i.imgur.com/QlGpd.gif
.. |image8| image:: /coolshell/static/20140922113344580000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/4170.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com