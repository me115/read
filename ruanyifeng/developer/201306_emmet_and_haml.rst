.. _201306_emmet_and_haml:

HTML代码简写法：Emmet和Haml
==============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2013/06/emmet_and_haml.html>`__

HTML代码写起来很费事，因为它的标签多。

一种解决方法是采用\ `模板 <http://html5boilerplate.com/>`__\ ，
在别人写好的骨架内，填入自己的内容。还有一种就是我今天想要介绍的方法——简写法。

常用的简写法，目前主要是\ `Emmet <http://emmet.io/>`__\ 和\ `Haml <http://haml.info/>`__\ 两种，本文都将加以介绍。

这两种简写法，功能相近，各有特点。考虑到Haml基于Ruby语言，我建议Ruby/Rails项目使用Haml，其他项目使用Emmet。

**一、Emmet的用法**

`Emmet <http://emmet.io/>`__\ 是一个编辑器插件，官方网站提供\ `多编辑器支持 <http://emmet.io/download/>`__\ 。我一般使用\ `vim <http://en.wikipedia.org/wiki/Vim_%28text_editor%29>`__\ ，下面就以\ `vim插件 <http://en.wikipedia.org/wiki/Vim_%28text_editor%29>`__\ 举例。

首先，按照\ `vim插件文档 <https://github.com/mattn/zencoding-vim/blob/master/README.mkd>`__\ 进行安装。然后，新建一个文本文件，键入

    ::

        　　html:5
        　　

按一下”,”（先按ctrl键+y键，然后再按逗号键，不同的编辑器有不同的转化键），这一行就立刻变成下面的样子。

    ::

        　　
        　　
        　　
        　　　　
        　　　　
        　　
        　　
        　　
        　　
        　　
        　　

这就是Emmet的基本用法：先写简写形式，然后用”,”将其转成HTML代码。

Emmet支持的简写规则，类似于\ `CSS选择器 <http://www.ruanyifeng.com/blog/2009/03/css_selectors.html>`__\ （大写的E代表一个HTML标签）：

    ::

        　　1. E 代表HTML标签。
        　　2. E#id 代表id属性。
        　　3. E.class 代表class属性。
        　　4. E[attr=foo] 代表某一个特定属性。
        　　5. E{foo} 代表标签包含的内容是foo。
        　　6. E>N 代表N是E的子元素。
        　　7. E+N 代表N是E的同级元素。
        　　8. E^N 代表N是E的上级元素。
        　　

请看下面的例子。

    ::

        　　p
        　　
        　　p#main.item
        　　
        　　a[href=http://wikipedia.org]{维基百科}
        　　
        　　div>p
        　　
        　　div+p
        　　
        　　p>span^div
        　　

对应的HTML代码为：

    ::

        　　
        　　
        　　
        　　
        　　维基百科
        　　
        　　
        　　　　
        　　
        　　
        　　
        　　
        　　
        　　
        　　
        　　

Emmet还提供了连写（E\*N）和自动编号（E$\*N）功能。

    ::

        　　li*3>a
        　　
        　　div#item$.class$$*3
        　　

对应的HTML代码为

    ::

        　　
        　　
        　　
        　　
        　　
        　　
        　　
        　　

下面是另外一些简写的例子，读者可以自行测试，看看它们转化成怎样的HTML代码。

    ::

        　　header+main+footer
        　　
        　　table>(thead>tr>th*5)(tbody>tr>td*5)
        　　
        　　nav>ul>(li>a[href=#]{Link})*5
        　　

Emmet使用按键”/”，让一个代码块变成HTML注释。更多功能请参考以下链接：

    　　\* Zeno Rocha, `Goodbye, Zen Coding. Hello,
    Emmet! <http://coding.smashingmagazine.com/2013/03/26/goodbye-zen-coding-hello-emmet/>`__

    　　\* Sergey Chikuyonok, `Zen Coding: A Speedy Way To Write
    HTML/CSS
    Code <http://coding.smashingmagazine.com/2009/11/21/zen-coding-a-new-way-to-write-html-code/>`__

    　　\* Joshua Johnson, `7 Awesome Emmet HTML Time-Saving
    Tips <http://designshack.net/articles/css/7-awesome-emmet-html-time-saving-tips/>`__

    　　\* `Zen-coding vim
    tutorial <https://raw.github.com/mattn/zencoding-vim/master/TUTORIAL>`__

**二、Haml的用法**

Haml不同于emmet，它是一个命令行工具。需要先\ `安装Ruby语言 <http://www.ruby-lang.org/zh_cn/downloads/>`__\ ，再安装Haml。

    ::

        　　gem install haml
        　　

使用时，用命令行将haml文件一次性转为html文件。

    ::

        　　haml input.haml output.html
        　　

haml的简化规则如下：

    ::

        　　1. !!! 5 代表 
        　　2. %E 代表HTML标签。
        　　3. %E#id 代表id属性。
        　　4. %E.class 代表class属性。
        　　5. %E(attr="xxx") 代表某一个特定属性。
        　　6. %E XXX 代表插入标签的内容。
        　　7. %E %N 代表N是E的子元素。N如果写在第二行，需要缩进。
        　　

下面是Haml的代码示例，代码块的层级关系用缩进表示。

    ::

        　　!!! 5
        　　%html{lang: 'en'}
        　　　　%head
        　　　　　　%title Haml Demo
        　　　　%body
        　　　　　　%h1 Hello World
        　　　　　　%a(href="http://wikipedia.org" title="Wikipedia") 维基百科
        　　

对应的HTML代码为：

    ::

        　　
        　　
        　　　　
        　　　　　　Haml Demo
        　　　　
        　　　　
        　　　　　　Hello World
        　　　　　　维基百科
        　　　　
        　　
        　　

在Haml中，”/ “起首的行表示HTML注释，”-# “起首的行表示Haml注释。
更多功能请参考以下链接。

    　　\* Nick Walsh, `Craft cleaner, more concise HTML with
    Haml <http://www.netmagazine.com/tutorials/craft-cleaner-more-concise-html-haml>`__

    　　\* Ian Oxley, `An Introduction to
    Haml <http://rubysource.com/an-introduction-to-haml/>`__

    　　\* `Haml
    Reference <http://haml.info/docs/yardoc/file.REFERENCE.html>`__

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2013/06/emmet_and_haml.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com