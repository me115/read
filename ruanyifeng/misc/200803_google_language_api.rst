.. _200803_google_language_api:

Google翻译的API
==================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/03/google_language_api.html>`__

Google的\ `在线翻译 <http://translate.google.com/>`__\ 服务，大概是目前最强大的机器翻译，但是一直没开放编程接口API。

上个星期，Google终于开始提供自动翻译的\ `API <http://code.google.com/apis/ajaxlanguage/>`__\ ，这意味着，从此可以在任何一个网页上调用Google翻译了。

我看了\ `开发文档 <http://code.google.com/apis/ajaxlanguage/documentation/>`__\ ，真的是非常简单，复制几行代码就可以了。但是，它存在两个重大缺陷：

    缺点一：一次最多翻译500个字。

    缺点二：不支持嵌入HTML标签的文本，只支持纯文本翻译。

由于这两个缺点，所以几乎不可能将其投入实际使用。

不过，我还是动手做了一个\ `《毛主席语录》的自动翻译 <http://www.ruanyifeng.com/php/mao/>`__\ ，大家可以体验一下它的效果，好像还蛮好玩。下面是一些截图。

[相关文章]

\* `Google Chart
API <http://www.ruanyifeng.com/blog/2007/12/google_chart_api.html>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/03/google_language_api.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com