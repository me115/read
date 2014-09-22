.. _articles8052:

K Nearest Neighbor 算法
=======================

2012年8月17日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

K Nearest
Neighbor算法又叫KNN算法，这个算法是机器学习里面一个比较经典的算法， 总体来说KNN算法是相对比较容易理解的算法。其中的K表示最接近自己的K个数据样本。KNN算法和\ `K-Means算法 <http://coolshell.cn/articles/7779.html>`__\ 不同的是，K-Means算法用来聚类，用来判断哪些东西是一个比较相近的类型，而KNN算法是用来做归类的，也就是说，有一个样本空间里的样本分成很几个类型，然后，给定一个待分类的数据，通过计算接近自己最近的K个样本来判断这个待分类数据属于哪个分类。\ **你可以简单的理解为由那离自己最近的K个点来投票决定待分类数据归为哪一类**\ 。

Wikipedia上的\ `KNN词条 <http://en.wikipedia.org/wiki/K-nearest_neighbor_algorithm>`__\ 中有一个比较经典的图如下：

|image0|

从上图中我们可以看到，图中的有两个类型的样本数据，一类是蓝色的正方形，另一类是红色的三角形。而那个绿色的圆形是我们待分类的数据。

-  如果K=3，那么离绿色点最近的有2个红色三角形和1个蓝色的正方形，这3个点投票，于是绿色的这个待分类点属于红色的三角形。

-  如果K=5，那么离绿色点最近的有2个红色三角形和3个蓝色的正方形，这5个点投票，于是绿色的这个待分类点属于蓝色的正方形。

我们可以看到，机器学习的本质——\ **是基于一种数据统计的方法**\ ！那么，这个算法有什么用呢？我们来看几个示例。

产品质量判断
^^^^^^^^^^^^

假设我们需要判断纸巾的品质好坏，纸巾的品质好坏可以抽像出两个向量，一个是“酸腐蚀的时间”，一个是“能承受的压强”。如果我们的样本空间如下：（所谓样本空间，又叫Training
Data，也就是用于机器学习的数据）

**向量X1**

**耐酸时间（秒）**

**向量X2**

**圧强(公斤/平方米)**

**品质Y**

7

7

坏

7

4

坏

3

4

好

1

4

好

那么，如果 X1 = 3 和 X2 = 7，
这个毛巾的品质是什么呢？这里就可以用到KNN算法来判断了。

假设K=3，K应该是一个奇数，这样可以保证不会有平票，下面是我们计算（3，7）到所有点的距离。（关于那些距离公式，可以参看\ `K-Means算法中的距离公式 <http://coolshell.cn/articles/7779.html>`__\ ）

**向量X1**

**耐酸时间（秒）**

**向量X2**

**圧强(公斤/平方米)**

**计算到 (3, 7)的距离**

**向量Y**

7

7

**|image1|**

 坏

7

4

**|image2|**

 N/A

3

4

**|image3|**

 好

1

4

**|image4|**

 好

所以，最后的投票，好的有2票，坏的有1票，最终需要测试的（3，7）是合格品。（当然，你还可以使用权重——可以把距离值做为权重，越近的权重越大，这样可能会更准确一些）

**注：\ `示例来自这里 <http://people.revoledu.com/kardi/tutorial/KNN/KNN_Numerical-example.html>`__\ ，\ `K-NearestNeighbors
Excel表格下载 <http://coolshell.cn//wp-content/uploads/2012/08/K-NearestNeighbors.xls>`__**

预测
^^^^

假设我们有下面一组数据，假设X是流逝的秒数，Y值是随时间变换的一个数值（你可以想像是股票值）

|image5|

那么，当时间是6.5秒的时候，Y值会是多少呢？我们可以用KNN算法来预测之。

这里，让我们假设K=2，于是我们可以计算所有X点到6.5的距离，如：X=5.1，距离是
\| 6.5 – 5.1 \| = 1.4， X = 1.2 那么距离是 \| 6.5 – 1.2 \| = 5.3
。于是我们得到下面的表：

|image6|

注意，上图中因为K=2，所以得到X=4 和 X
=5.1的点最近，得到的Y的值分别为27和8，在这种情况下，我们可以简单的使用平均值来计算：\ |image7|

于是，最终预测的数值为：17.5

|image8|

**注：\ `示例来自这里 <http://people.revoledu.com/kardi/tutorial/KNN/KNN_TimeSeries.htm>`__\ ，\ `KNN\_TimeSeries
Excel表格下载 <http://coolshell.cn//wp-content/uploads/2012/08/KNN_TimeSeries.xls>`__**

插值，平滑曲线
^^^^^^^^^^^^^^

KNN算法还可以用来做平滑曲线用，这个用法比较另类。假如我们的样本数据如下（和上面的一样）：

|image9|

要平滑这些点，我们需要在其中插入一些值，比如我们用步长为0.1开始插值，从0到6开始，计算到所有X点的距离（绝对值），下图给出了从0到0.5
的数据：

|image10|

下图给出了从2.5到3.5插入的11个值，然后计算他们到各个X的距离，假值K=4，那么我们就用最近4个X的Y值，然后求平均值，得到下面的表：

|image11|

于是可以从0.0, 0.1, 0.2, 0.3 …. 1.1, 1.2, 1.3…..3.1, 3.2…..5.8, 5.9, 6.0
一个大表，跟据K的取值不同，得到下面的图：

|image12| |image13| |image14| |image15| |image16|

**注：\ `示例来自这里 <http://people.revoledu.com/kardi/tutorial/KNN/KNN_TimeSeries.htm>`__\ ，\ `KNN\_Smoothing
Excel表格下载 <http://coolshell.cn//wp-content/uploads/2012/08/KNN_Smoothing.xls>`__**

后记
^^^^

最后，我想再多说两个事，

1）
一个是机器学习，算法基本上都比较简单，最难的是数学建模，把那些业务中的特性抽象成向量的过程，另一个是选取适合模型的数据样本。这两个事都不是简单的事。算法反而是比较简单的事。

2）对于KNN算法中找到离自己最近的K个点，是一个很经典的算法面试题，需要使用到的数据结构是“\ `最大堆——Max
Heap <http://en.wikipedia.org/wiki/Binary_heap>`__\ ”，一种二叉树。你可以看看相关的算法。

（全文完）

.. |image0| image:: /coolshell/static/20140921233423205000.png
.. |image1| image:: http://coolshell.cn//wp-content/uploads/2012/08/KNN_Numerical-example_clip_image004.gif
.. |image2| image:: http://coolshell.cn//wp-content/uploads/2012/08/KNN_Numerical-example_clip_image006.gif
.. |image3| image:: http://coolshell.cn//wp-content/uploads/2012/08/KNN_Numerical-example_clip_image008.gif
.. |image4| image:: http://coolshell.cn//wp-content/uploads/2012/08/KNN_Numerical-example_clip_image010.gif
.. |image5| image:: /coolshell/static/20140921233423255000.jpg
.. |image6| image:: /coolshell/static/20140921233423301000.jpg
.. |image7| image:: http://coolshell.cn//wp-content/uploads/2012/08/KNN_TimeSeries_clip_image008.gif
.. |image8| image:: /coolshell/static/20140921233423337000.jpg
.. |image9| image:: /coolshell/static/20140921233423444000.jpg
.. |image10| image:: /coolshell/static/20140921233423664000.jpg
.. |image11| image:: /coolshell/static/20140921233423699000.jpg
.. |image12| image:: /coolshell/static/20140921233423754000.jpg
.. |image13| image:: /coolshell/static/20140921233423788000.jpg
.. |image14| image:: /coolshell/static/20140921233423823000.jpg
.. |image15| image:: /coolshell/static/20140921233423861000.jpg
.. |image16| image:: /coolshell/static/20140921233423898000.jpg
.. |image23| image:: /coolshell/static/20140921233423938000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/8052.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com