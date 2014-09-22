.. _articles11564:

                       1000-1499   3000, SACK=1000-1500
                                              =========

 

可见，引入了D-SACK，有这么几个好处：

1）可以让发送方知道，是发出去的包丢了，还是回来的ACK包丢了。

2）是不是自己的timeout太小了，导致重传。

3）网络上出现了先发的包后到的情况（又称reordering）

4）网络上是不是把我的数据包给复制了。

 **知道这些东西可以很好得帮助TCP了解网络情况，从而可以更好的做网络上的流控**\ 。

Linux下的tcp\_dsack参数用于开启这个功能（Linux 2.4后默认打开）

好了，上篇就到这里结束了。如果你觉得我写得还比较浅显易懂，那么，欢迎移步看下篇《\ `TCP的那些事（下） <http://coolshell.cn/articles/11609.html>`__\ 》

** `TCP的那些事儿（下）»> <http://coolshell.cn/articles/11609.html>`__**

（上篇完）

.. |image0| image:: /coolshell/static/20140922112035723000.jpg
.. |image1| image:: /coolshell/static/20140922112035772000.jpg
.. |image2| image:: /coolshell/static/20140922112035876000.jpg
.. |image3| image:: /coolshell/static/20140922112035968000.png
.. |image4| image:: /coolshell/static/20140922112036236000.jpg
.. |image5| image:: /coolshell/static/20140922112036342000.png
.. |image6| image:: /coolshell/static/20140922112036385000.jpg
.. |image7| image:: /coolshell/static/20140922112036670000.png
.. |image8| image:: /coolshell/static/20140922112036711000.jpg
.. |image15| image:: /coolshell/static/20140922112036766000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/11564.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com