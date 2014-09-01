.. _201306_html_email:

HTML Email 编写指南
======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2013/06/html_email.html>`__

今天，我想写一个”低技术”问题。

话说我订阅了不少了新闻邮件（Newsletter），比如\ `JavaScript
Weekly <http://javascriptweekly.com/>`__\ 。每周收到一封邮件，了解本周的大事。

有一天，我就在想，是不是我也能做一个这样的邮件？

然后，就发现这事不那么容易。抛开后台和编辑工作，单单是设计一个Email样板，就需要不少心思。

因为这种带格式的邮件，其实就是一张网页，正式名称叫做\ `HTML
Email <http://en.wikipedia.org/wiki/HTML_email>`__\ 。它能否正常显示，完全取决于邮件客户端。大多数的邮件客户端（比如Outlook和Gmail），会过滤HTML设置，让邮件面目全非。

我发现，编写HTML
Email的窍门，就是使用15年前的网页制作方法。下面就是我整理的编写指南。

**1. Doctype**

目前，兼容性最好的Doctype是XHTML 1.0
Strict，事实上Gmail和Hotmail会删掉你的Doctype，换上这个Doctype。

    　

使用这个Doctype，也就意味着，不能使用HTML5的语法。

**2. 布局**

网页的布局（layout）必须使用表格（table）。首先，放置一个最外层的大表格，用来设置背景。

    　

    　　

    | 
    |  　　　

    Hello!

    | 
    |  　　

    　

表格的 border 属性等于1,
是为了方便开发。正式发布的时候，再把这个属性设为0。

在内层，放置第二个表格。用来展示内容。第二个table的宽度定为600像素，防止超过客户端的显示宽度。

    　

    | 
    |  　　

    Row 1

    | 
    |  　

    　

    | 
    |  　　

    Row 2

    | 
    |  　

    　

    | 
    |  　　

    Row 3

    | 
    |  　

邮件内容有几个部分，就设置几行（row）。

**3. 图片**

图片是唯一可以引用的外部资源。其他的外部资源，比如样式表文件、字体文件、视频文件等，一概不能引用。

有些客户端会给图片链接加上边框，要去除边框。

    　　img {outline:none; text-decoration:none; -ms-interpolation-mode:
    bicubic;}

    　　a img {border:none;}

    　　

需要注意的是，不少客户端默认不显示图片（比如Gmail），所以要确保即使没有图片，主要内容也能被阅读。

**4. 行内样式**

所有的CSS规则，最好都采用行内样式。因为放置在网页头部的样式，很可能会被客户端删除。客户端对CSS规则的支持情况，请看\ `这里 <http://www.campaignmonitor.com/css/>`__\ 。

另外，不要采用CSS的简写形式，有些客户端不支持。比如，不要写成下面这样：

    　　style=”font: 8px/14px Arial, sans-serif;”

如果想表达

    　　

要写成下面这样：

    　　

**5. W3C校验和测试工具**

要保证最终的代码，能够通过\ `W3C <http://validator.w3.org/>`__\ 的校验，因为某些客户端会把不合格属性剥离。还要使用测试工具（\ `1 <http://mailchimp.com/features/inbox-inspector/>`__,
`2 <https://litmus.com/>`__,
`3 <http://www.emailonacid.com/>`__\ ），查看在不同客户端的显示结果。

发送HTML Email的时候，不要忘记MIME类型不能使用

    　　Content-Type: text/plain;

而要使用

    　　Content-Type: Multipart/Alternative;

发送工具可以考虑使用 `MailChimp <http://mailchimp.com/>`__ 和 `Campaign
Monitor <http://www.campaignmonitor.com/>`__ 。

**6. 模板**

使用别人已经做好的模板，是一个不错的选择（\ `这里 <http://mailchimp.com/features/email-templates/>`__\ 和\ `这里 <http://www.campaignmonitor.com/templates/all/>`__\ ），网上还可以搜到\ `更多 <http://www.google.com.hk/search?q=email+template>`__\ 。

自己开发的话，可以参考\ `HTML Email
Boilerplate <http://htmlemailboilerplate.com/>`__\ 和\ `Emailology <http://www.emailology.org/#1>`__\ 。

**7. 参考链接**

进一步研究，请参考下面的文章。

| 　　- Sean Powell，\ `Say Hello to the HTML Email
Boilerplate <http://hub.tutsplus.com/tutorials/say-hello-to-the-html-email-boilerplate--webdesign-5143>`__
|  　　- Nicole Merlin，\ `Build an HTML Email Template From
Scratch <http://webdesign.tutsplus.com/tutorials/htmlcss-tutorials/build-an-html-email-template-from-scratch/>`__
|  　　- Nicole Merlin， `What You Should Know About HTML
Email <http://hub.tutsplus.com/tutorials/what-you-should-know-about-html-email--webdesign-12908>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2013/06/html_email.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com