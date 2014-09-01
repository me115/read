.. _201103_url_hash:

Url的井号
============================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/03/url_hash.html>`__

去年9月，twitter改版。

一个显著变化，就是URL加入了”#!”符号。比如，改版前的用户主页网址为

    　　http://twitter.com/username

改版后，就变成了

    　　http://twitter.com/#!/username

在我印象中，这是主流网站第一次将”#”大规模用于直接与用户交互的关键URL中。这表明井号（Hash）的作用正在被重新认识。本文根据\ `HttpWatch <http://blog.httpwatch.com/2011/03/01/6-things-you-should-know-about-fragment-urls/>`__\ 的文章，整理与井号有关的所有重要知识点。

**一、#的涵义**

#代表网页中的一个位置。其右面的字符，就是该位置的标识符。比如，

    　　http://www.example.com/index.html#print

就代表网页index.html的print位置。浏览器读取这个URL后，会自动将print位置滚动至可视区域。

为网页位置指定标识符，有两个方法。一是使用锚点，比如，二是使用id属性，比如

。

**二、HTTP请求不包括#**

#是用来指导浏览器动作的，对服务器端完全无用。所以，HTTP请求中不包括#。

比如，访问下面的网址，

    　　http://www.example.com/index.html#print

浏览器实际发出的请求是这样的：

    　　GET **/index.html** HTTP/1.1

    　　Host: www.example.com

可以看到，只是请求index.html，根本没有”#print”的部分。

**三、#后的字符**

在第一个#后面出现的任何字符，都会被浏览器解读为位置标识符。这意味着，这些字符都不会被发送到服务器端。

比如，下面URL的原意是指定一个颜色值：

    　　http://www.example.com/?color=#fff

但是，浏览器实际发出的请求是：

    　　GET **/?color=** HTTP/1.1

    　　Host: www.example.com

可以看到，”#fff”被省略了。只有将#转码为%23，浏览器才会将其作为实义字符处理。也就是说，上面的网址应该被写成：

    　　http://example.com/?color=%23fff

**四、改变#不触发网页重载**

单单改变#后的部分，浏览器只会滚动到相应位置，不会重新加载网页。

比如，从

    　　http://www.example.com/index.html#location1

改成

    　　http://www.example.com/index.html#location2

浏览器不会重新向服务器请求index.html。

**五、改变#会改变浏览器的访问历史**

每一次改变#后的部分，都会在浏览器的访问历史中增加一个记录，使用”后退”按钮，就可以回到上一个位置。

这对于ajax应用程序特别有用，可以用不同的#值，表示不同的访问状态，然后向用户给出可以访问某个状态的链接。

值得注意的是，上述规则对IE 6和IE
7不成立，它们不会因为#的改变而增加历史记录。

**六、window.location.hash读取#值**

window.location.hash这个属性可读可写。读取时，可以用来判断网页状态是否改变；写入时，则会在不重载网页的前提下，创造一条访问历史记录。

**七、onhashchange事件**

这是一个HTML
5新增的事件，当#值发生变化时，就会触发这个事件。IE8+、Firefox
3.6+、Chrome 5+、Safari 4.0+支持该事件。

它的使用方法有三种：

    　　window.onhashchange = func;

    　　

    　　window.addEventListener(“hashchange”, func, false);

    对于不支持onhashchange的浏览器，可以用setInterval监控location.hash的变化。

    **八、Google抓取#的机制**

    默认情况下，Google的网络蜘蛛忽视URL的#部分。

    但是，Google还\ `规定 <http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=174992>`__\ ，如果你希望Ajax生成的内容被浏览引擎读取，那么URL中可以使用”#!”，Google会自动将其后面的内容转成查询字符串\_escaped\_fragment\_的值。

    比如，Google发现新版twitter的URL如下：

        　　http://twitter.com/#!/username

    就会自动抓取另一个URL：

        　　http://twitter.com/?\_escaped\_fragment\_=/username

    通过这种机制，Google就可以索引动态的Ajax内容。

    | （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/03/url_hash.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com