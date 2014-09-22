.. _articles6913:

神奇的CSS形状
=============

2012年3月24日 `Neo <http://coolshell.cn/articles/author/neo>`__

【感谢 Neo 投递本文 –
微博帐号：\ `@\_锟\_ <http://weibo.com/gandalfthegrey>`__ 】

在StackOverflow上有这么一个问题，有位同学在\ `http://css-tricks.com/examples/ShapesOfCSS/  <http://css-tricks.com/examples/ShapesOfCSS/>`__
找到一些使用CSS做的形状，其中一位同学对下面的这个形状充满了疑问。

形状是：

|image0|

代码是：

::

    #triangle-up {
    width: 0;
    height: 0;
    border-left: 50px solid transparent;
    border-right: 50px solid transparent;
    border-bottom: 100px solid red;
    }

| 这位同学就提问啦，为啥这么这么几句就能画出一个三角形呢？
|  于是呢，有高人出现，这个高人图文并茂的解释了这个三角的成因

| 
|  首先呢，我们需要了解HTML标记的Box
Model（盒模型），这个例子中呢我们将content，padding都看作content。忽略掉margin。那么一个盒模型就是下图

|image1|

| 中间是内容，然后是4条边。每一条边都有宽度。
|  根据上面CSS的定义，没有border-top（顶边）的情形下 ,我们的图形如下：

|image2|

width设置为0后 ，内容没有了就成为下图：

|image3|

height也设置为0，只有底边了。

|image4|

然后两条边都是设置为透明，最后我们就得到了

|image5|

这个属于奇技淫巧，但是也说明CSS的强大，没有做不到只有想不到。另外\ `http://css-tricks.com/examples/ShapesOfCSS/  <http://css-tricks.com/examples/ShapesOfCSS/>`__\ 还能找到很多其他的形状，感兴趣的同学可以自己去看。还有酷壳以前的这篇文章《\ `CSS实现的各种形状 <http://coolshell.cn/articles/5164.html>`__\ 》

.. |image0| image:: /coolshell/static/20140922103055295000.png
.. |image1| image:: /coolshell/static/20140922103058460000.png
.. |image2| image:: /coolshell/static/20140922103058503000.png
.. |image3| image:: /coolshell/static/20140922103058542000.png
.. |image4| image:: /coolshell/static/20140922103058569000.png
.. |image5| image:: /coolshell/static/20140922103058629000.png
.. |image12| image:: /coolshell/static/20140922103058693000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/6913.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com