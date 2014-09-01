.. _201307_how_to_make_search_engines_find_ajax_content:

如何让搜索引擎抓取ajax内容？
===============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2013/07/how_to_make_search_engines_find_ajax_content.html>`__

越来越多的网站，开始采用\ `“单页面结构” <http://en.wikipedia.org/wiki/Single-page_application>`__\ （Single-page
application）。

整个网站只有一张网页，采用\ `Ajax <http://zh.wikipedia.org/wiki/AJAX>`__\ 技术，根据用户的输入，加载不同的内容。

这种做法的好处是用户体验好、节省流量，缺点是AJAX内容无法被搜索引擎抓取。举例来说，你有一个网站。

    ::

        　　http://example.com  
        　　

用户通过\ `井号结构 <http://www.ruanyifeng.com/blog/2011/03/url_hash.html>`__\ 的URL，看到不同的内容。

    ::

        　　http://example.com#1
        　　http://example.com#2
        　　http://example.com#3  
        　　

但是，搜索引擎只抓取example.com，不会理会井号，因此也就无法索引内容。

为了解决这个问题，Google提出了”井号+感叹号”的结构。

    ::

        　　http://example.com#!1
        　　

当Google发现上面这样的URL，就自动抓取另一个网址：

    ::

        　　http://example.com/?_escaped_fragment_=1
        　　

只要你把AJAX内容放在这个网址，Google就会收录。但是问题是，”井号+感叹号”非常难看且烦琐。Twitter曾经采用这种结构，它把

    ::

        　　http://twitter.com/ruanyf
        　　

改成

    ::

        　　http://twitter.com/#!/ruanyf
        　　

结果用户抱怨连连，只用了半年就废除了。

那么，有没有什么方法，可以在保持比较直观的URL的同时，还让搜索引擎能够抓取AJAX内容？

我一直以为没有办法做到，直到前两天看到了\ `Discourse <http://www.discourse.org/>`__\ 创始人之一的\ `Robin
Ward <http://eviltrout.com/2013/06/19/adding-support-for-search-engines-to-your-javascript-applications.html>`__\ 的解决方法，不禁拍案叫绝。

Discourse是一个论坛程序，严重依赖Ajax，但是又必须让Google收录内容。它的解决方法就是放弃井号结构，采用
`History API <http://html5doctor.com/history-api/>`__\ 。

所谓 History
API，指的是不刷新页面的情况下，改变浏览器地址栏显示的URL(准确说，是改变网页的当前状态)。这里有一个\ `例子 <http://inserthtml.com/demo/history/>`__\ ，你点击上方的按钮，开始播放音乐。然后，再点击下面的链接，看看发生了什么事？

地址栏的URL变了，但是音乐播放没有中断！

History API
的详细介绍，超出这篇文章的范围。这里只简单说，它的作用就是在浏览器的History对象中，添加一条记录。

    ::

        　　window.history.pushState(state object, title, url);
        　　

上面这行命令，可以让地址栏出现新的URL。History对象的pushState方法接受三个参数，新的URL就是第三个参数，前两个参数都可以是null。

    ::

        　　window.history.pushState(null, null, newURL); 
        　　

目前，各大浏览器都支持这个方法：Chrome（26.0+），Firefox（20.0+），IE（10.0+），Safari（5.1+），Opera（12.1+）。

下面就是Robin Ward的方法。

**首先，用History
API替代井号结构，让每个井号都变成正常路径的URL，这样搜索引擎就会抓取每一个网页。**

    ::

        　　example.com/1
        　　example.com/2
        　　example.com/3
        　　

**然后，定义一个JavaScript函数，处理Ajax部分，根据网址抓取内容（假定使用jQuery）。**

    ::

        　　function anchorClick(link) {
        　　　　var linkSplit = link.split('/').pop();
        　　　　$.get('api/' + linkSplit, function(data) {
        　　　　　　$('#content').html(data);
        　　　　});
        　　}
        　　

再定义鼠标的click事件。

    ::

        　　$('#container').on('click', 'a', function(e) {
        　　　　window.history.pushState(null, null, $(this).attr('href'));
        　　　　anchorClick($(this).attr('href'));
        　　　　e.preventDefault();
        　　});
        　　

还要考虑到用户点击浏览器的”前进 /
后退”按钮。这时会触发History对象的popstate事件。

    ::

        　　window.addEventListener('popstate', function(e) {     
        　　　　anchorClick(location.pathname);     
         　　});
        　　

定义完上面三段代码，就能在不刷新页面的情况下，显示正常路径URL和AJAX内容。

**最后，设置服务器端。**

因为不使用井号结构，每个URL都是一个不同的请求。所以，要求服务器端对所有这些请求，都返回如下结构的网页，防止出现404错误。

    ::

        　　
        　　　　
        　　　　　　
        　　　　　　
        　　　　　　　　... ...
         　　　　　　
        　　　　
        　　
        　　

仔细看上面这段代码，你会发现有一个noscript标签，这就是奥妙所在。

我们把所有要让搜索引擎收录的内容，都放在noscript标签之中。这样的话，用户依然可以执行AJAX操作，不用刷新页面，但是搜索引擎会收录每个网页的主要内容！


===================================

[通知]

接下来三周，我外出旅行，暂停更新网志。

大家可以从
`http://www.ruanyifeng.com/tweets/ <http://www.ruanyifeng.com/tweets/>`__\ ，了解我的行程。欢迎关注。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2013/07/how_to_make_search_engines_find_ajax_content.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com