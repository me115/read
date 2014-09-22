.. _articles4875:

一个空格引发的惨剧
==================

2011年6月20日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

你是否相信如果你的程序里没有检查一个变量会导致怎么系统瘫痪？无论你相不相信，这是我一个亲身经历过的案例，你可以在本站的\ `程序员那些悲催的事儿 <http://coolshell.cn/articles/3980.html>`__\ 中找到很多这样的事。这样的事昨天在发生，今天同样在发生。\ `Unix40多年 <http://coolshell.cn/articles/2322.html>`__\ 了，在这40年里，程序员发生过各种各样的的惨剧，但是大多数的事情一而再再而三的重演。

今天的你，可能在开发者各种各样NB的系统，你会相信你的一个空格也能导致系统瘫痪吗？也许你可能很难相信这个事。不过，再下面这个事将告诉你这个血淋淋的事实
—— 一个空格产生的bug可以让你的系统瘫痪。

`bumblebee <https://github.com/MrMEEE/bumblebee>`__\ 是一个开源项目，这个名字也就是变形金刚里的大黄蜂，这个项目是这样介绍自己的——

    bumblebee is Optimus support for Linux, with real offloading, and
    not switchable graphics.. More important.. it works on Optimus
    Laptops without a graphical multiplexer..

Optimus
是NVIDIA的“优驰”技术，其可以将您的笔记本电脑PC提升到绝佳状态，提供出色的图形性能，并在需要时延长电池续航时间。这个项目是把这个技术移到Linux上来。

这个项目本来不出名，不过，程序在其安装脚本install.sh里的一个bug让这个项目一下子成了全世界最瞩目的项目，这个bug的fix如下：

::

    @@ -348,7 +348,7 @@ case "$DISTRO" in
    -  rm -rf /usr /lib/nvidia-current/xorg/xorg
    +  rm -rf /usr/lib/nvidia-current/xorg/xorg

看明白了吗？\ **空格**\ 。这个空格会导致什么样的问题呢？呵呵。你有没有感到菊花一紧？这个bug绝对的霸气外露！真是验证了\ `“如何写出无法维护代码 <http://coolshell.cn/articles/4758.html>`__\ ”的那句话——“\ **测试你的程序是一种懦夫的行为**\ ”。

不过，最精彩还不是这个bug，而是全世界程序员的对这个bug 的 code review
comments，真的相当的欢乐。请强势围望！

`https://github.com/MrMEEE/bumblebee/commit/a047be85247755cdbe0acce6#diff-1 <https://github.com/MrMEEE/bumblebee/commit/a047be85247755cdbe0acce6#diff-1>`__

重点是其中的很多图片——下面的图片众多。

|clip\_image001|

|image1|

|image2|

|clip\_image002|

|image4|

|image5|

|image6|

|image7|

|clip\_image007|

|clip\_image010|

|clip\_image011|

|clip\_image012|

|image12|

|clip\_image014|

|image14|

|image15|

|image16|

|image17|

|clip\_image016|

|image19|

|image20|

|clip\_image019|

|clip\_image020|

|clip\_image021|

|image24|

(全文完)

.. |clip\_image001| image:: http://pic003.cnblogs.com/2011/34358/201106/20110620115951113.gif
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620115950761.gif
.. |image1| image:: /coolshell/static/20140922113248479000.jpg
.. |image2| image:: /coolshell/static/20140922113248773000.jpg
.. |clip\_image002| image:: /coolshell/static/20140922113248908000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620115951580.jpg
.. |image4| image:: /coolshell/static/20140922113249035000.jpg
.. |image5| image:: /coolshell/static/20140922113249224000.jpg
.. |image6| image:: /coolshell/static/20140922113249348000.jpg
.. |image7| image:: /coolshell/static/20140922113249541000.jpg
.. |clip\_image007| image:: /coolshell/static/20140922113249662000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620115954514.jpg
.. |clip\_image010| image:: /coolshell/static/20140922113249798000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620115958341.jpg
.. |clip\_image011| image:: /coolshell/static/20140922113249923000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620115958163.jpg
.. |clip\_image012| image:: /coolshell/static/20140922113250160000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620115959641.jpg
.. |image12| image:: /coolshell/static/20140922113250390000.jpg
.. |clip\_image014| image:: http://pic003.cnblogs.com/2011/34358/201106/20110620120001634.gif
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620120001777.gif
.. |image14| image:: /coolshell/static/20140922113250482000.jpg
.. |image15| image:: http://pic003.cnblogs.com/2011/34358/201106/20110620120002955.gif
.. |image16| image:: /coolshell/static/20140922113250591000.jpg
.. |image17| image:: /coolshell/static/20140922113250753000.jpg
.. |clip\_image016| image:: /coolshell/static/20140922113250908000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620120002899.jpg
.. |image19| image:: /coolshell/static/20140922113251029000.jpg
.. |image20| image:: /coolshell/static/20140922113251235000.jpg
.. |clip\_image019| image:: /coolshell/static/20140922113251707000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620120002666.jpg
.. |clip\_image020| image:: /coolshell/static/20140922113251929000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/20110620120003129.jpg
.. |clip\_image021| image:: /coolshell/static/20140922113252074000.jpg
   :target: http://pic003.cnblogs.com/2011/34358/201106/2011062012000453.jpg
.. |image24| image:: /coolshell/static/20140922113252202000.jpg
.. |image31| image:: /coolshell/static/20140922113252299000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/4875.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com