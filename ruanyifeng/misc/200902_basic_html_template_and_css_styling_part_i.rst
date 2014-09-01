.. _200902_basic_html_template_and_css_styling_part_i:

Html模板和css基准样式（一）
==============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/02/basic_html_template_and_css_styling_part_i.html>`__

我经常写网页。

很多人喜欢用Dreamweaver，但是我的习惯是直接手写代码。虽然那样看上去很原始，但是能够做到对网页最精确的控制，并且减少了不必要的冗余代码。

手写代码最麻烦的地方在于，每次都必须写一些重复性的代码，比如

| 

| 

它分成这样几个部分：

**1. Doctype部分**

这个部分声明网页的类型。我使用的是HTML 4.01 Strict。

除此还可以选择HTML 4.01 Transitional、XHTML 1.0 Strict和XHTML 1.0
Transitional。相应的DOCTYPE分别为

    “http://www.w3.org/TR/html4/loose.dtd”>

    | 
    |  “http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd”>

这里需要注意，如果选择xhtml类型，那么第一行必须加入xml类型说明，而且

就是根元素，它后面必须注明文档的命名空间，要写成下面这样：

    “http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd”>

我个人还是推荐使用HTML
4，因为xHTML取消了一些标签，用起来不是很灵活。根据我的观察，一些大网站，比如Google和Yahoo!，主页都是使用HTML
4。更多DocTYPE类型，请访问\ `W3C <http://www.w3.org/QA/2002/04/valid-dtd-list.html>`__\ 网站。

**2. TITLE部分**

这个部分最好写成”网站名称 - 网页描述”，或者”网页描述 -
网站名称”，有利于搜索引擎收入你的网页。

**3. META部分**

这个部分对网页进行说明。

第一行是必须要有的，对网页使用的语言编码进行说明。我在这里使用了UTF-8编码。

第二行对网页内容进行描述，第三行提供了网页的关键词。它们是选择性的，不一定要填写。

    | 

你还可以在这里加入更多的说明，比如网页生成的时间、作者、所用的软件、版权说明等等。

    | 
    | 

**4. Style部分**

这个部分加入样式表。

我使用了import命令，此外还可以使用标签，效果是一样的。

**5. Favicon部分**

这一行是加入网页的图标。

**6. Feed部分**

这一行是加入网页的Feed。

type类型除了上面的”application/atom+xml”，还可以写成”application/rss+xml”，这根据你的Feed格式而定。


======================

上面只是最基本的网页模板，还缺少起码的CSS设置和布局设置，我将在后面的文章中介绍。并且在全文结尾处，我会提供完整的模板下载。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/02/basic_html_template_and_css_styling_part_i.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com