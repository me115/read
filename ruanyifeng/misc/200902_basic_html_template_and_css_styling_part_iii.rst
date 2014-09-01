.. _200902_basic_html_template_and_css_styling_part_iii:

Html模板和css基准样式（三）
==============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/02/basic_html_template_and_css_styling_part_iii.html>`__

今天是这个连载的最后一部分，内容关于网页的布局。

废话少说，大家先看我做的一个范例网页，请\ `点击进入 <http://www.ruanyifeng.com/webapp/html_template/example.html>`__\ 。

然后，我对这个范例做一点解释。


================

从布局上看，世界上所有的网页，大多由三个部分构成：

    \* Header（头部）

    \* Footer（尾部）

    \* Content（内容区）

一般来说，Header总是在网页的上方，Footer总是在网页的下方，Content是中间的一大块。在
Content中又可以分成很多栏，从一栏式到三栏式都很常见。

我们的目的是通过CSS文件，实现栏位和布局的自动调整。网上有很多现成的布局模板，我采用的是\ `Tripoli <http://devkick.com/lab/tripoli/>`__\ 项目中的\ `布局模板 <http://devkick.com/lab/tripoli/plugins/tripoli.layout.css>`__\ ，然后做了一些修改。

它要求的网页代码结构是这样的：

    | 

    | 

    | 

    | 

    | 

    | 

    | 

    | 

    | 

    | 

在body标签下面，直接是一个”container”，所有网页的内容都属于这个容器。然后，container又分成五个部分，分别是：header、primary、secondary、tertiary和footer。primary
是主内容区，secondary是次内容区，tertiary是第三内容区。也就是说，这个模板最多只支持三栏式布局。

另外，请注意，在body标签的后面，class属性是需要你自己设置的。Tripoli默认提供9种布局，用l1-l9来表示。

    \* l1：2栏式 66% - 33%

    \* l2：2栏式 33% - 66%

    \* l3：2栏式 50% - 50%

    \* l4：3栏式 33% - 33% - 33%

    \* l5：3栏式 16% - 66% - 16%

    \* l6：3栏式 25% - 50% - 25%

    \* l7: 3栏式 66% - 16% - 16%

    \* l8: 3栏式 50% - 25% - 25%

    \* l9：3栏式 25% - 25% - 50%

你选择一种，将它填入class属性就可以，比如class=”l2”。

class属性值中还可以设置一个equal类，这将使得各个栏位的垂直长度保持相等，比如class=”l2
equal”。

其他设置就没有了，是不是很简单？


======================

最后，就是这一套完整的模板下载：\ `html\_template.zip <http://www.ruanyifeng.com/blog/upload/2009/02/html_template.zip>`__\ （3.4KB）。

欢迎使用。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/02/basic_html_template_and_css_styling_part_iii.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com