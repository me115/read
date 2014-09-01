.. _200805_css_background_image_positioning:

Css中背景图片定位方法
========================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/05/css_background_image_positioning.html>`__

CSS中背景图片的定位，困扰我很久了。今天总算搞懂了，一定要记下来。

在CSS中，背景图片的定位方法有3种：

    　　1）关键字：background-position: top left;

    　　2）像素：background-position: 0px 0px;

    　　3）百分比：background-position: 0% 0%;

上面这三句语句，都将图片定位在背景的左上角，表面上看效果是一样的，实际上第三种定位机制与前两种完全不同。

前两种定位，都是将背景图片左上角的原点，放置在规定的位置。请看下面这张图，规定的位置是”20px
10px”和”60px 50px”，都是图片的原点在那个位置上，图中用X表示。

但是第三种定位，也就是百分比定位，不是这样。\ **它的放置规则是，图片本身（x%,y%）的那个点，与背景区域的（x%,y%）的那个点重合。**\ 比如，如果放置位置是”20%
10%”，实际结果如下图，可以看到这个点是在图片本身的”20% 10%”的位置上。

下面是一个有趣的例子。

背景图片是四个边长为100px的方块叠在一起：

请问怎样才能将其横过来：

答案是，在网页中先设置四个div区域：

    | 

    | 

    | 

    | 

然后，这样编写CSS：

    | .box1, .box2, .box3, .box4 { 　　float:left; 　　width:100px;
    　　height:100px; 　　position:relative;
    |  　　background: #F3F2E2 url(1234.png) no-repeat;
    |  }

    | .box1 {
    |  　　background-position:0% 0%;
    |  }

    | .box2 {
    |  　　background-position:0% 33.33333%;
    |  }

    | .box3 {
    |  　　background-position:0% 66.66666%;
    |  }

    | .box4 {
    |  　　background-position:0% 100%;
    |  }

点击\ `这里 <http://www.sitepoint.com/examples/jquery/test.php>`__\ 查看最后的效果。可以看到第二和第三个方块的设置，并不是一般想象中的”0%
25%”和”0% 75%”。

不过说实话，这个例子用像素设置法更容易一些。使用百分比设置的主要优势在于，当页面缩放的时候，背景图片也会跟着一起缩放，具体请参考下面”延伸阅读”中的第二篇文章。

[延伸阅读]

1. `CSS: Using Percentages in
Background-Image <http://www.sitepoint.com/blogs/2007/07/05/css-using-percentages-in-background-image/>`__

2. `Creating Liquid Faux
Columns <http://www.communitymx.com/content/article.cfm?cid=afc58>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/05/css_background_image_positioning.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com