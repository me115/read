.. _articles1484:

TCP网络关闭的状态变换时序图
===========================

2009年9月27日 `Neo <http://coolshell.cn/articles/author/neo>`__

TCP共有11个网路状态，其中涉及到关闭的状态有5个。

在我们编写网络相关程序的时候，这5个状态经常出现。因为这5个状态相互关联，相互纠缠，而且状态变化触发都是由应用触发，但是又涉及操作系统和网络，所以正确的理解TCP
在关闭时网络状态变化情况，为我们诊断网络中各种问题，快速定位故障有着非常重要的作用和意义。

下是是根据W.Richard Stevens的《TCP/IP详解》一书的TCP状态转换图。

|image0|

|image1|\ |image2|\ |image3|\ |image4|

.. |image0| image:: /coolshell/static/20140922112234274000.jpg
.. |image1| image:: /coolshell/static/20140922112234357000.jpg
.. |image2| image:: /coolshell/static/20140922112234451000.jpg
.. |image3| image:: /coolshell/static/20140922112234489000.jpg
.. |image4| image:: /coolshell/static/20140922112234534000.jpg
.. |image11| image:: /coolshell/static/20140922112234571000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1484.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com