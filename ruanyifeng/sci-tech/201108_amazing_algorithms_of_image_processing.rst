.. _201108_amazing_algorithms_of_image_processing:

神奇的图像处理算法
=====================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/08/amazing_algorithms_of_image_processing.html>`__

几周前，我介绍了\ `相似图片搜索 <http://www.ruanyifeng.com/blog/2011/07/principle_of_similar_image_search.html>`__\ 。

这是利用数学算法，进行高难度图像处理的一个例子。事实上，图像处理的数学算法，已经发展到令人叹为观止的地步。

`Scriptol <http://www.scriptol.com/programming/graphic-algorithms.php>`__\ 列出了几种神奇的图像处理算法，让我们一起来看一下。

**一、像素图生成向量图的算法**

数字时代早期的图片，分辨率很低。尤其是一些电子游戏的图片，放大后就是一个个像素方块。\ `Depixelizing <http://research.microsoft.com/en-us/um/people/kopf/pixelart/>`__\ 算法可以让低分辨率的像素图转化为高质量的向量图。

**二、黑白图片的着色算法**

让老照片自动变成彩色的\ `算法 <http://www.cs.huji.ac.il/~yweiss/Colorization/index.html>`__\ 。

**三、消除阴影的算法**

不留痕迹地去掉照片上某件东西的阴影的\ `算法 <http://www.cs.huji.ac.il/~danix/ShadowRemoval/index.html>`__\ 。

**四、HDR照片的算法**

所谓”HDR照片”，就是扩大亮部与暗部的对比效果，亮的地方变得非常亮，暗的地方变得非常暗，亮暗部的细节都很明显。

实现HDR的软件有很多，这里推荐\ `G’MIC <http://gmic.sourceforge.net/>`__\ 。它是GIMP图像编辑软件的一个插件，代码全部开源。

**五、消除杂物的算法**

所谓”消除杂物”，就是在照片上划出一块区域，然后用背景自动填补。\ `Resynthesizer <http://www.logarithmic.net/pfh/resynthesizer>`__\ 可以做到这一点，它也是GIMP的一个插件。

**六、自动合成照片的算法**

根据一张草图，选择原始照片，然后把它们合成在一起，生成新照片。这是清华大学的\ `科研成果 <http://cg.cs.tsinghua.edu.cn/montage/main.htm>`__\ 。

**七、美容算法**

自动对容貌进行”美化”的\ `算法 <http://www.leyvand.com/research/beautification2008/>`__\ 。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/08/amazing_algorithms_of_image_processing.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com