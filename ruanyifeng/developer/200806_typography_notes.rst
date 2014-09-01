.. _200806_typography_notes:

字体笔记
===========================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/06/typography_notes.html>`__

昨天，我写了纪录片\ `《Helvetica》 <http://www.ruanyifeng.com/blog/2008/06/helvetica_50th_anniversary.html>`__\ 的观后感。因为内容与字体有关，我就借这个机会，整理一下关于字体的笔记。

需要说明的是，下面提到的字体都是指英语字体。中文字体因为各个平台差别太大，所以这里就不考虑了。


==================

**一、字体的种类**

字体一共可以分为6个大类。

**1. serif （衬线类）**

**2. sans-serif（无衬线类）**

字母末段带有装饰线的就是serif，反之就是sans-serif。

|image0|

上图中左边的就是衬线类字体Georgia，右边的就是无衬线类字体Verdana。

一般来说，serif比较庄重，sans-serif相对活泼。因为serif带有衬线，在小字号下，不如sans-serif清晰，所以serif字体可以用作标题，sans-serif字体可以用作正文。

**3. Handwritten Fonts（手写类字体）**

这种字体模仿人的笔迹，一般只在体现某种艺术效果时使用。下面的图中就是四种手写类字体。

|image1|

**4. Fixed-width Fonts（等宽字体）**

这种字体每个字母的宽度相等，一般用来模拟命令行输入和打字机效果，现在多用于展现程序源码。

|image2|

**5. Novelty Fonts（花式字体）**

这种字体纯粹就是追求装饰性，20世纪之前的印刷品都用这类字体。

|image3|

**6. Dingbat Fonts（符号字体）**

这类字体不是字母，而是输出各种各样的符号。

|image4|

**二、三种sans-serif字体**

在制作网页的过程中，主要使用sans-serif字体。下面就是最常用的三种。

**1. Verdana**

Verdana几乎在所有平台上都预装了，所以是sans-serif字体的第一选择。它的特点就是字母间距比较宽，字母本身的宽度也比较大，所以比较容易阅读。

|image5|

**2. Trebuchet**

Trebuchet的特点也是宽度大，形状清晰。

|image6|

**3. Helvetica**

Helvetica的特点是小写字母比较大。

|image7|

**三、互联网安全字体（web safe fonts）**

所有平台都预装的字体，被称为”安全字体”，因为它可以保证所有用户的视觉效果是一样的。

以下九种字体就是”安全字体”：Arial、Arial Black、Comic Sans MS、Courier
New、Georgia、Impact、Times New Roman、Trebuchet MS和Verdana。

|image8|

网上已经有人整理出了所有”安全字体”的\ `CSS写法 <http://www.fonttester.com/help/list_of_web_safe_fonts.html>`__\ ，我把它照抄过来，效果可以看\ `这里 <http://www.fonttester.com/web_safe_fonts.html>`__\ 。

**1. serif类**

    | font-family: Garamond, serif; font-family: Georgia, serif;
    font-family: ‘Times New Roman’, Times, serif;
    |  font-family: ‘Bookman Old Style’, serif;
    |  font-family: ‘Palatino Linotype’, ‘Book Antiqua’, Palatino,
    serif;

**2.sans-serif类**

    | font-family: Arial, Helvetica, sans-serif; font-family: ‘Arial
    Black’, Gadget, sans-serif; font-family: Impact, Charcoal,
    sans-serif; font-family: ‘Lucida Sans Unicode’, ‘Lucida Grande’,
    sans-serif; font-family: ‘MS Sans Serif’, Geneva, sans-serif;
    font-family: ‘MS Serif’, ‘New York’, sans-serif; font-family:
    Symbol, sans-serif; font-family: Tahoma, Geneva, sans-serif;
    font-family: ‘Trebuchet MS’, Helvetica, sans-serif; font-family:
    Verdana, Geneva, sans-serif;
    |  font-family: Webdings, sans-serif;
    |  font-family: Wingdings, ‘Zapf Dingbats’, sans-serif;

**3. 手写类**

    font-family: ‘Comic Sans MS’, cursive;

**4. 等宽类**

    | font-family: Courier, monospace;
    |  font-family: ‘Courier New’, Courier, monospace;
    |  font-family: ‘Lucida Console’, Monaco, monospace;

[延伸阅读]

1. `The Principles of Beautiful
Typography <http://www.sitepoint.com/article/principles-beautiful-typography>`__,
By Jason Beaird

2. `The Anatomy of Web
Fonts <http://www.sitepoint.com/article/anatomy-web-fonts>`__, By Andy
Hume

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/06/typography_notes.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com