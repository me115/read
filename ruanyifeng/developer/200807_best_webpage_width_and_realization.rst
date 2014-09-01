.. _200807_best_webpage_width_and_realization:

最佳网页宽度及其实现
=======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/07/best_webpage_width_and_realization.html>`__

1.

设计网页的时候，确定宽度是一件很苦恼的事。

以\ `minifun.cn <http://minifun.cn>`__\ 为例，根据\ `Google
Analytics <http://www.google.com/analytics/>`__\ 的统计，半年多以来，访问者的屏幕分辨率一共有81种。最小的分辨率是122x160，这应该是手机；最大的分辨率是3360x1050，天知道是什么设备。

一张网页要在大小如此悬殊的各种屏幕上，都呈现令人满意的效果，难度可想而知。举例来说，一张400px宽的图片，在800px的屏幕上会占据50%的宽度，而在1920px的屏幕上（Windows
Vista的流行设置），只占据20%。

2.

目前，常见的屏幕分辨率宽度大概有6种：800px，1024px，1280px，1440px，1680px和1920px。其中，1024px最常见，但是随着大屏幕显示器的流行，更高的分辨率正变得越来越多。

常见的解决方法有两种：

    第一种：用javascript根据不同的客户端分辨率，选择css样式表文件，具体的做法可以看\ `这里 <http://www.google.cn/search?aq=f&complete=1&hl=zh-CN&newwindow=1&rlz=1B3GGGL_zh-CNCN216CN216&q=Change+CSS+resolution+Javascript&btnG=Google+%E6%90%9C%E7%B4%A2&meta=>`__\ 。

    第二种：采用弹性布局（Fluid Width Layout），实现网页宽度的自适应。

第一种方法的优点是，可以根据不同屏幕分辨率，采用完全不同的布局，缺点是要设计和维护多张样式表，比较麻烦。第二种方法只采用一张样式表，比较省事。

下文就根据\ `css-tricks <http://css-tricks.com/the-perfect-fluid-width-layout/>`__\ 上的解决方案，讨论如何实现第二种方法，实际上是很简单的。

|image0|

3.

**首先，网页的缺省宽度，确定为满足1024px宽度的显示器。**\ 这不仅因为1024x768是现在最常见的分辨率，还因为这个宽度对网页最合适：1）它放得下足够的内容，足够三栏的布局；2）单行文字不宜太长，1024px已是极限，否则容易产生阅读疲劳；3）在当前的互联网带宽条件下，网页难以采用大分辨率所要求的大尺寸图片。

**其次，网页宽度会在780px-1260px的范围内，自动变化**\ ，即最小不小于780px，最大不超过1280px。

**最后，对于更大的分辨率，网页内容会自动居中。**

4.

下面就是CSS文件的写法，只要4行。需要注意的是，这几行的语句都针对整个页面，即body标签或者最外层的那个div区域。

    margin: 10px auto;

这一行保证了网页在任何分辨率下，都会居中。

    | min-width: 780px;
    |  max-width: 1260px;

这二行规定了网页的最小和最大宽度。注意，IE6不支持这二行，即它们在IE6中是无效的。

    width:expression(document.body.clientWidth 1262? “1260px” : “auto”);

这一行是针对IE6的解决方法。它采用了CSS表达式，也可以通过javascript实现。

另外，如果想让内层的各个区块也自动伸缩，它们的宽度可以采用百分比的形式，比如：

    | #div-left{
    |  width:50%;
    |  }

    | #div-right{
    |  width:50%;
    |  }

最后的效果和源码下载请查看\ `这里 <http://css-tricks.com/examples/PerfectFluidWidthLayout/>`__\ 。通过变动浏览器窗口的大小，可以发现网页在780px-1260px的范围内会自动伸缩。

5.

最后，建议大家平时使用计算机的时候，不要盲目采用高分辨率，意义不大。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/07/best_webpage_width_and_realization.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com