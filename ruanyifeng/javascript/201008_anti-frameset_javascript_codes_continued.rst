.. _201008_anti-frameset_javascript_codes_continued:

防止网页被嵌入框架的代码（续）
=================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/08/anti-frameset_javascript_codes_continued.html>`__

两年前，我写过一段代码，\ `防止网页被嵌入框架 <http://www.ruanyifeng.com/blog/2008/10/anti-frameset_javascript_codes.html>`__\ （Frame）。

这段代码是有效的。但是，有一个问题：使用后，任何人都无法再把你的网页嵌入框架了，包括你自己在内。

于是，我今天就在考虑，\ **有没有一种方法，使得我的网页只能被嵌入我自己的框架，而不是别人的框架？**

表面上看，这个问题很简单。只要做一个判断：当前框架和顶层框架的域名是否相同，如果答案是否，就做了一个URL重定向。

    if (top.location.hostname != window.location.hostname) {

    　　top.location.href = window.location.href;

    }

但是，出乎意料的是，这样写是错误的，根本无法运行。你能看出，错在哪里吗？

假定 top.location.hostname 是 www.111.com，而 window.location.hostname
是 www.222.com。也就是说，111.com把222.com嵌入了它的网页中。这时，比较
top.location.hostname != window.location.hostname 会有什么结果？

浏览器会提示代码出错！

因为它们跨域（cross-domain）了，浏览器的安全政策不允许222.com的网页操作111.com的网页，反之亦然。IE把这种错误叫做”没有权限”。进一步说，浏览器甚至不允许你查看top.location.hostname，跨域情况下，一看到这个对象，就直接报错。

那么，代码应该如何修改？

事实上，这提示我们，只要查看top.location.hostname是否报错就可以了。如果报错了，表明存在跨域，就对top对象进行URL重导向；如果不报错，表明不存在跨域（或者未使用框架），就不采取操作。

    try{

    　　top.location.hostname;

    }

    catch(e){

    　　top.location.href = window.location.href;

    }

这样写已经正确了，在IE和Firefox中可以正确运行。但是，Chrome浏览器会出现错误，不知为何，在跨域情况下，Chrome对top.location.hostname不报错！

没办法，只能为了Chrome，再加一段补充代码。

    try{

    　　top.location.hostname;

    　　if (top.location.hostname != window.location.hostname) {

    　　　　top.location.href =window.location.href;

    　　}

    }

    catch(e){

    　　top.location.href = window.location.href;

    }

好了，升级版代码完成。除了本地域名以外，其他域名一律无法将你的网页嵌入框架。我的Blog现在就使用这段代码。


==============================

P.S.

除了代码以后，我还有一件事要说。

今年6月5日，在\ `《创业途径：手工杂志》 <http://www.ruanyifeng.com/blog/2010/06/zine.html>`__\ 一文的最后，我说：

    “喜欢手工的女同学们，建议你们试试。只要你的作品有趣，我帮你在我的Blog上推广。”

结果，真的有女同学找我。Daisy来信说，她和女友做了一本电子杂志\ `《上班族》 <http://cn.calameo.com/groups/1482>`__\ ，希望我帮忙推广。

虽然我对上班这件事一点兴趣也没有，也不觉得这种主题值得做，但是我不想食言，而且我一向觉得，追求梦想的人值得鼓励。所以，欢迎大家\ `阅读 <http://cn.calameo.com/books/00033283802dff23973f4>`__\ 。

最后，为了增加点击率，Daisy同学自愿提供了一张生活照。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/08/anti-frameset_javascript_codes_continued.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com