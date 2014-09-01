.. _201107_formula_online_generator:

数学公式生成器
=================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/07/formula_online_generator.html>`__

上一篇文章\ `《数学常数e的含义》 <http://www.ruanyifeng.com/blog/2011/07/mathematical_constant_e.html>`__\ ，有很多数学公式。

但是，在网页上显示数学公式，是一件非常麻烦的事情。以下面的公式为例：

　　|image0|

怎样才能把这个公式放到网页上呢？

传统的方式是，先在相关软件中把公式做出来，然后截图，再把图片贴到网页上，这样既麻烦又耗时。我就在想，有没有便捷的方法，可以生成数学公式。

我知道，\ `Google
Chart <http://code.google.com/apis/chart/>`__\ 接受\ `TeX <http://en.wikipedia.org/wiki/TeX>`__\ 语言，实时返回数学公式的图片。于是，我就用了一天时间，根据它的\ `API <http://code.google.com/apis/chart/image/docs/gallery/formulas.html>`__\ ，写出了一个\ `“数学公式生成器” <http://www.ruanyifeng.com/webapp/formula.html>`__\ 。

经过初步测试，我自我感觉很不错，觉得写作数学公式从此不再麻烦了。我把这个作品推荐给大家，欢迎试用。

如果你懂得TeX语法，使用起来应该毫无困难。如果不懂，也没有关系，用起来很简单，下面我做一个初步介绍。

对于简单的公式，可以直接在文本框输入，比如”y=2x+8”：

　　

然后点击”查看”按钮，就会显示数学公式的图片，并且给出图片代码。

　　

接着，就来看怎么生成本文开头那个稍微复杂一点的公式：

　　|image1|

首先，按照顺序输入左括号、1、+：

　　

加号后面是一个分数，这时就要用到TeX语法了，点击菜单里的”结构”选项，选择”分数”那一栏：

　　

文本框中就会插入”\\frac{1}{2}”这样的结构：

　　

在TeX语法中，斜杠开头的语句表示命令，所以”\\frac”表示后面要生成分数；命令后面的大括号，表示命令的参数，”\\frac”后面的第一个大括号表示分子，第二个大括号表示分母。现在，依次在”分子”中填入”100%”，在”分母”中填入”n”。

　　

最后，加上右括号和”^n”。

　　

点击”查看”按钮，这个公式就显示出来了。

　　

其他公式的生成方法与其类似，大家可以自己摸索，任何时候都可以点击”查看”按钮，了解是否写错。

TeX几乎可以写出所有的数学公式（查看MediaWiki的\ `参考网页 <http://meta.wikimedia.org/wiki/Help:Formula>`__\ ），但是Google
Chart只支持一部分的TeX语法，因此不保证所有时候都能得到想要的结果。

除了Google
Chart，还有另一些服务，也能生成数学公式的图片，比如\ `mathtran.org <http://www.mathtran.org/>`__\ 和\ `mathurl.com <http://mathurl.com>`__\ ，还有\ `这里 <http://modis.ispras.ru/Lizorkin/math2image.html>`__\ 和\ `这里 <http://www.codecogs.com/latex/eqneditor.php>`__\ 。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/07/formula_online_generator.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com