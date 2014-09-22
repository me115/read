.. _articles6840:

CSS 布局:40个教程、技巧、例子和最佳实践
=======================================

2012年3月19日 `Neo <http://coolshell.cn/articles/author/neo>`__

【感谢 Neo 投递本文 –
微博帐号：\ `\_锟\_ <http://weibo.com/gandalfthegrey>`__ 】

**前言：**
布局是WEB开发一个重要的课题，进入XHTML/CSS后，使用TABLE布局的方式逐渐淡出，CSS布局以众多优点成为主流，本文将介绍40个基于CSS的web布局的资源和教程。文章的出处在\ `http://www.noupe.com/css/css-layouts-40-tutorials-tips-demos-and-best-practices.html <http://www.noupe.com/css/css-layouts-40-tutorials-tips-demos-and-best-practices.html>`__\ 。文中的不少的例子在一本经典的CSS书籍\ `《CCS:
The Missing Manual, 2nd
Edition》 <http://shop.oreilly.com/product/9780596802455.do>`__\ 中都可以找到，据我所知，第二版在中国没有翻译出版。你可以从\ `这里 <http://www.itpub.net/forum.php?mod=viewthread&tid=1210179&highlight=CSS%2Bthe%2Bmissing%2Bmanual>`__\ 下载英文版（不过需要注册个用户名）

| **正文**
| **基于CSS的布局**\ 能提供更灵活布局方式和更强的用户视觉体验。一些重要技巧和关键点可以帮助初学者理解CSS布局的基础和本质。这也是本文成文的原因
——找到那些完美的布局，**完全灵活的，等高栏**\ 和工作完美的布局。
| 
因此下面这个列表就是我们整理了网络上关于基于CSS布局的一些技巧，教程和最佳实践的列表。
|  当然你也可能对下面这些和CSS相关的主题有兴趣：

**CSS 布局教程**
^^^^^^^^^^^^^^^^

1-`使用CSS完成三栏固定布局结构 <http://woork.blogspot.com/2008/01/three-column-fixed-layout-structure.html>`__-
这篇文章解释了如何实现一个基于的HTML/CSS来设计一个简单的带有基本要素（顶部的logo条，导航条，文本区，定义分类的中部栏，右边侧栏插入google的120X600的广告区）的固定三栏页面布局。

|image0|

| 2-`使用CSS设计页面布局 <http://woork.blogspot.com/2007/10/design-page-layout-using-css.html>`__-
如何使用CSS文件来为你的站点设计页面布局。
| |image1|

3-`如何创建一个水平布局的站点 <http://css-tricks.com/how-to-create-a-horizontally-scrolling-site/>`__-
创建不同于常规的水平布局的站点技术（译者注：水平布局，客户体验也就仁者见仁了）

| |image2|
|  例子\ `查看这里 <http://css-tricks.com/examples/HorzScrolling>`__
\|\ `下载 <http://css-tricks.com/examples/HorzScrolling.zip>`__

4-`超级简单的两栏布局 <http://css-tricks.com/super-simple-two-column-layout/>`__-
创建不同于常规的水平布局的站点技术（译者注：这里是原作者笔误吧和上面的内容一样）.

|image3|

例子\ `查看这里 <http://css-tricks.com/examples/SuperSimpleTwoColumn>`__
`下载 <http://css-tricks.com/examples/SuperSimpleTwoColumn.zip>`__

5-`简单两栏CSS布局 <http://www.456bereastreet.com/lab/developing_with_web_standards/csslayout/2-col/>`__-
这是一个创建简单两栏布局的教程。这种布局包含了一个标题区，一个水平导航条，主内容区，边侧栏，和页脚区。并且这个布局是水平居中的。

|image4|

例子\ `查看这里 <http://www.456bereastreet.com/lab/developing_with_web_standards/csslayout/2-col/finished.html>`__

6-`圣杯布局(The holy grail
layout) <http://dnevnikeklektika.com/en/the-holy-grail-layout-3-columns-and-a-lot-less-problems>`__
– 3栏布局会有一些问题
，这篇文章讨论了一种三栏布局——两栏固定宽度边侧栏加上一栏变宽中栏布局，保证了页面的良好结构和清晰。

|image5|

例子\ `查看这里 <http://dnevnikeklektika.com/css/3ColLayout/working.html>`__

7-`CSS居中101 <http://www.simplebits.com/notebook/2004/09/08/centering.html>`__-
如何使用CSS完成居中一个固定宽度的布局

使用CSS，通过下面两条规则完成对id为container的DIV所包含的内容居中

::


      ...entire layout goes here...

::

    body {
        text-align: center;
    }
    #container {
        margin: 0 auto;
        width: xxxpx;
        text-align: left;
    }

8-`从头创建CSS布局 <http://www.subcide.com/tutorials/csslayout/index.aspx>`__-
这个指南通过创建一个全功能的 CSS布局来一步步教你入门CSS布局。

|image6|

9-`非主流！多栏布局 <http://www.alistapart.com/articles/multicolumnlayouts/>`__-
多栏布局，等高栏（每一列的高度都相等），固定或变宽中央区，简洁标记，CSS
。(译者注：原文作者的图配的和上图一样)

|image7|

例子\ `查看这里 <http://www.alistapart.com/d/multicolumnlayouts/3ColLiquid.html>`__

10-
`创建天下无双的CSS布局 <http://www.positioniseverything.net/articles/onetruelayout/>`__-
高灵活性布局,等高栏，跨栏垂直摆放元素。本文告诉你通过何等手段完成这些目标，并使用它们创建天下无双的CSS布局（译者注:原文是One
True Layout ，不知道怎么翻译，就天下无双吧。）

|image8|

`查看这里 <http://www.positioniseverything.net/articles/onetruelayout/examples>`__

11-`从PSD到HTML，手把手完成WEB设计 <http://nettuts.com/site-builds/from-psd-to-html-building-a-set-of-website-designs-step-by-step/>`__-从Photoshop到完整HTML，全过程手把手教会你。

|image9|

例子\ `查看这里 <http://nettuts.s3.amazonaws.com/017_Creatif/Site/index.html>`__
\|
`下载 <http://nettuts.s3.amazonaws.com/017_Creatif/Site_Download.zip>`__

12-
`5个XHTML/CSS技巧 <http://tutorialblog.org/5-tips-for-coding-xhtmlcss-layouts/>`__
– 5个CSS技巧帮助你完成从基于表格的布局到基于CSS的布局。

13-`设计一个基于CSS的模板 <http://veerle.duoh.com/index.php/blog/comments/designing_a_css_based_template_part_i/>`__
–
这是一个教你创建基于CSS的模板页的基础教程。这个教程由下面几个部分构成：第一部分覆盖了在Photoshop
CS\*中的创建导航条按钮，第二部分：创建背景接下来的清单是标题和页面布局，最后的部分在XHTML和CSS中实现。

|image10|

`下载 <http://homepage.mac.com/vpieters/css_step2/step2_whooshes.mov.zip>`__

14-`使用CSS布局跳出常规布局 <http://www.sitepoint.com/article/breaking-out-of-the-box>`__-
如果你理解了基于表格布局的工作方式，你能通过合并或拆分表格创建你随心所欲的布局。就这个目标（同时支持灵活性和可维护性），CSS能够提供比基于表格更多地东西。Jina
Bolton的教程解释如何达到这个目标。

|image11|

15-`高级CSS教程:手把手 <http://www.webreference.com/authoring/style/sheets/layout/advanced/>`__-
这个教程的终极目标创建一个CSS布局，这个CSS布局精确地重组了原有使用table的WebReference.com的布局。

|image12|

16-`了解CSS布局的6个关键要素 <http://snook.ca/archives/html_and_css/six_keys_to_understanding_css_layouts/>`__-本文讲述了6件基于CSS布局需要了解的事情：盒模型(Box
Model)，浮动栏(Floated Columns)
（译者注：float是WEB布局最重要的一个属性了）。使用Em来设置尺寸（Sizing
Using Ems），图片替换（Image Replacement）,浮动导航和Sprintes。

17-`你会犯这些常见的博客布局错误吗？ <http://wisdump.com/design/are-you-making-these-common-blog-layout-mistakes/>`__-讨论4个博客布局中常见而且易修复的错误。

18-`页面布局 <http://www.htmldog.com/guides/cssadvanced/layout/>`__-CSS页面布局中的浮动元素和定位元素实践指导。

你可以查看这些例子：\ `Absolute Position within a relative
box <http://www.htmldog.com/examples/positioning4.html>`__\ `two floated
boxes <http://www.htmldog.com/examples/float2.html>`__\ 和\ `using a
border to provide the background for a
column <http://www.htmldog.com/examples/pagelayout3.html>`__

19-`Site in an Hour <http://leftjustified.net/site-in-an-hour/>`__-
使用复杂CCS布局完成简单的工作。

|image13|

**关于布局的最佳资源**
^^^^^^^^^^^^^^^^^^^^^^

下面的大多数这些资源不需要许可就能直接使用，然而，其中的一些需要先发邮件确认一下是否可以使用这些资源。因此，在使用之前最好先检查资源的版权信息。

20-`简单CSS页面布局 <http://www.maxdesign.com.au/presentation/page_layouts/>`__-
这里有一套2栏和3栏的CSS布局。

|image14|

你可以通过这里查看这些样例\ `Liquid three column
layout <http://www.maxdesign.com.au/presentation/process/example23.htm>`__,\ `Left
aligned, set
width <http://www.maxdesign.com.au/presentation/page_layouts/single04.htm>`__
and `Liquid
insanity <http://www.maxdesign.com.au/presentation/liquid/example13.htm>`__.

21-`完美的三栏变宽布局（百分比定宽度）The Perfect 3 Column Liquid Layout
(Percentage
widths) <http://matthewjamestaylor.com/blog/perfect-3-column.htm>`__-
没有CSS
hack（译者注：不知道怎么翻译，点击\ `这里 <http://baike.baidu.com/view/1119452.htm>`__\ 查看解释）.
良好地收索引擎优化.无图. 无Javascript. 跨浏览器 和IPHONE设备兼容

|image15|

你可以通过这里查看样例 `Liquid three column
layout <http://www.maxdesign.com.au/presentation/process/example23.htm>`__,
`Left aligned, set
width <http://www.maxdesign.com.au/presentation/page_layouts/single04.htm>`__
和 `Liquid
insanity <http://www.maxdesign.com.au/presentation/liquid/example13.htm>`__.
(译者注：这里的链接和上面重复了，哎，原文的错误吧)

22-`CSS模板和样例 <http://www.intensivstation.ch/en/templates/>`__

|image16|

你可以通过这里查看这些样例\ `3 columns
fixed <http://www.intensivstation.ch/files/en_templates/temp06.html>`__
`centered <http://www.intensivstation.ch/files/en_templates/temp06.html>`__,
`fixed Box
totally <http://www.intensivstation.ch/files/en_templates/temp11.html>`__\ `centered <http://www.intensivstation.ch/files/en_templates/temp11.html>`__
and `3 columns,
all <http://www.intensivstation.ch/files/en_templates/temp03.html>`__\ `dynamic <http://www.intensivstation.ch/files/en_templates/temp03.html>`__

23-`IM 布局 <http://layouts.ironmyers.com/>`__- IM
布局是一种简单地的CSS布局系统，IM布局提供了全A级的浏览器的支持。

|image17|

你可以通过这里查看这些样例:\ `The Holy Grail 3 Column
Layout <http://www.ironmyers.com/examples/three_column_layout.html>`__,
`The Classic Blog
Layout <http://www.ironmyers.com/examples/classic_blog.html>`__\ 和\ `The
Multi Column
Layout. <http://www.ironmyers.com/examples/multi_column.html>`__

24-`CSSplay <http://www.cssplay.co.uk/layouts/index.html>`__-
CSS布局列表

|image18|

你可以通过这里查看这些样例:\ `Cross browser
FIXED <http://www.cssplay.co.uk/layouts/fixit.html>`__, `Three
columns <http://www.cssplay.co.uk/layouts/threecol.html>`__ and `CSS
Frame – The Holy Grill <http://www.cssplay.co.uk/layouts/frame.html>`__.

25-`Layoutgala <http://blog.html.it/layoutgala/>`__-
基于同样的的标记l得到最大数量的不同的布局方式。没有CCS hack，没有CSS
workaround ，良好的浏览器兼容性。40种不同布局。

|image19|

你可以通过这里查看这些样例:\ `Three fixed
Columns <http://blog.html.it/layoutgala/LayoutGala07.html>`__, `Three
percentage columns <http://blog.html.it/layoutgala/LayoutGala04.html>`__
and `Liquid, three columns, hybrid
widths <http://blog.html.it/layoutgala/LayoutGala19.html>`__\ (吐槽：没有等高，不好看).

26-`Glish <http://www.glish.com/css/>`__- 许多有用的跨浏览器布局技术

|image20|

你可以通过这里查看这些样例: `3 columns, the holy
grail <http://www.glish.com/css/7.asp>`__,\ `2 columns, ALA
style <http://www.glish.com/css/9.asp>`__ and `3 columns, all
fluid <http://www.glish.com/css/2.asp>`__

27-`Thenoodleincident <http://www.thenoodleincident.com/tutorials/box_lesson/boxes.html>`__-
CSS 从简单的单盒到3盒并增加一个顶部条，所有都是变宽。

|image21|

28-`The Layout Reservoir <http://www.bluerobot.com/web/layouts/>`__-
很多有用的CSS布局技术

|image22|

你可以通过这里查看这些样例:\ `2 columns – left
menu <http://bluerobot.com/web/layouts/layout1.html>`__,\ `3 columns –
flanking
menus <http://bluerobot.com/web/layouts/layout3.html>`__\ 和\ `Auto-width
Margins <http://bluerobot.com/web/css/center1.html>`__.

29-`The only CSS layout you
need <http://www.strictlycss.com/articles/article/40/the-only-css-layout-you-need>`__-
在这篇文章中将会为你展现10个基于同一的HTML的不同的的布局。

|image23|

你可以通过这里查看这些样例: `Three column CSS layout – left and right
menu <http://www.strictlycss.com/examples/three-column-layout-1.asp>`__,
`Two column CSS layout – top and left
menu <http://www.strictlycss.com/examples/three-column-layout-2.asp>`__
和 `Three column CSS fluid layout: 100%
width <http://www.strictlycss.com/examples/three-column-layout-7.asp>`__

30-`另一个多栏布局 <http://www.yaml.de/>`__-是一个创建当代流行的变宽的浮动布局的XHTML/CSS框架。这是一个多功能实用的布局。

点击\ `这里 <http://www.yaml.de/fileadmin/download/release_306/yaml_306_080609.zip>`__\ 下载.

31-`Liquid Designs <http://www.cssliquid.com/>`__-
使用XHTML和CSS的变宽设计库。

**最佳实践**
^^^^^^^^^^^^

如果你需要寻找一些布局灵感，你可以从下面的网站链接中找到。这些站点演示了CSS布局如何应用于不同类型的网站。查看这些网站是如何分成2栏或3栏，或混合宽栏和窄栏布局。

32-`Helldesign <http://helldesign.net/>`__

|image24|

33-`Silverbackapp <http://silverbackapp.com/>`__

|image25|

34-`OS communications informatiques <http://www.os.ca/accueil.php>`__

|image26|

35-`Rockatee <http://rockatee.com/>`__

|image27|

36-`Darrenhoyt <http://www.darrenhoyt.com/>`__

|image28|

37-`Makebetterwebsites <http://www.makebetterwebsites.com/>`__

|image29|

38-`Elitetheme <http://elitetheme.com/>`__

|image30|

39-`Studio7designs <http://www.studio7designs.com/>`__

|image31|

40-`Brightcreative <http://brightcreative.com/>`__

|image32|

*(全文完)*

.. |image0| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts.gif
.. |image1| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts2.gif
.. |image2| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts3.gif
.. |image3| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts4.gif
.. |image4| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts6.gif
.. |image5| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts7.gif
.. |image6| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts9.gif
.. |image7| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts9.gif
.. |image8| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts22.gif
.. |image9| image:: /coolshell/static/20140921233749648000.jpg
.. |image10| image:: /coolshell/static/20140921233749794000.jpg
.. |image11| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts36.gif
.. |image12| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts29.gif
.. |image13| image:: /coolshell/static/20140921233749843000.jpg
.. |image14| image:: /coolshell/static/20140921233749897000.jpg
.. |image15| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts11.gif
.. |image16| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts21.gif
.. |image17| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts24.gif
.. |image18| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts25.gif
.. |image19| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts26.gif
.. |image20| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts27.gif
.. |image21| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts28.gif
.. |image22| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts30.gif
.. |image23| image:: http://coolshell.cn//wp-content/uploads/2012/03/css-layouts32.gif
.. |image24| image:: /coolshell/static/20140921233749968000.jpg
.. |image25| image:: /coolshell/static/20140921233750041000.jpg
.. |image26| image:: /coolshell/static/20140921233750109000.jpg
.. |image27| image:: /coolshell/static/20140921233750154000.jpg
.. |image28| image:: /coolshell/static/20140921233750212000.jpg
.. |image29| image:: /coolshell/static/20140921233750260000.jpg
.. |image30| image:: /coolshell/static/20140921233750342000.jpg
.. |image31| image:: /coolshell/static/20140921233750389000.jpg
.. |image32| image:: /coolshell/static/20140921233750455000.jpg
.. |image39| image:: /coolshell/static/20140921233750528000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/6840.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com