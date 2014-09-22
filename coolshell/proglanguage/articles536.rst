.. _articles536:

一个显示排序过程的Python脚本
============================

2009年4月15日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

之前向大家介绍过《\ `一个排序算法比较的网站 <http://coolshell.cn/articles/399.html>`__\ 》，那个网站用动画演示了各种排序算法，并分析了各种排序算法。这里，要向大家推荐一个Python脚本，其可以把排序的过程给显示出来。

下图是“\ **冒泡排序**\ ”的一个示例，其中：

#. 折线表示了各个元素的位置变化。
#. 折线的深浅表示了元素的大小。越深则越大。

|bubble|

同样，还有其它一些排序算法的图片：

**堆排序（Heap Sort）**

|heap|

**选择排序（Selection）**

|selection|

**快速排序（Quick）**

|quick|

**Shell排序**

|shell|

**插入排序（Insertion）**

|listinsertion|

你可以使用如下的Python代码来制作这些图片：（需要
`Cairo <http://cairographics.org/>`__\ 图片库支持）

`**Python排序脚本** <http://coolshell.cn//wp-content/uploads/2009/04/visualise.py>`__

这个脚本\ ``参数如下：``

-  ``-a 表示使用什么样的算法，取值为"quick", "heap", "selection", "insertion", "bubble", "shell"。``
-  ``-n 表示要排序的数据个数。``
-  ``-f 表示输入文件。``
-  ``-p 表示文件前缀。``
-  ``-d 表示输出顺序。``
-  ``-x 图片宽度。``
-  ``-y 图片高度。``
-  ``-l 所有线的宽度。``
-  ``-b 边界宽度。``

``使用示例如下：``

``./visualise.py -l 6 -x 700 -y 300 -n 15 ``

文章：\ `来源 <http://www.hatfulofhollow.com/posts/code/visualisingsorting/index.html>`__

.. |bubble| image:: /coolshell/static/20140922110338787000.png
   :target: http://coolshell.cn//wp-content/uploads/2009/04/bubble.png
.. |heap| image:: /coolshell/static/20140922110338833000.png
   :target: http://coolshell.cn//wp-content/uploads/2009/04/heap.png
.. |selection| image:: /coolshell/static/20140922110338898000.png
   :target: http://coolshell.cn//wp-content/uploads/2009/04/selection.png
.. |quick| image:: /coolshell/static/20140922110338947000.png
   :target: http://coolshell.cn//wp-content/uploads/2009/04/quick.png
.. |shell| image:: /coolshell/static/20140922110339253000.png
   :target: http://coolshell.cn//wp-content/uploads/2009/04/shell.png
.. |listinsertion| image:: /coolshell/static/20140922110339397000.png
   :target: http://coolshell.cn//wp-content/uploads/2009/04/listinsertion.png
.. |image12| image:: /coolshell/static/20140922110339914000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/536.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com