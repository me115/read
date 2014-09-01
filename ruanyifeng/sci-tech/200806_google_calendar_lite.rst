.. _200806_google_calendar_lite:

Google日历简易版
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/06/google_calendar_lite.html>`__

一直想找个地方，记录生活琐事，如同《鲁迅日记》那般：

    \* 下午孙福源来。刘半农来，交与书籍两册。

    \* 十二日 晴。午后骤雨一阵，即霁。

主要是为了备忘，不是为了交流，没必要公开。但是，必须能够方便地更新和查阅。

我试过自己搭建软件，但又懒得维护。使用过\ `twitter <http://twitter.com/>`__\ ，但它的档案查阅和时间序列功能实在太弱了。

|image0|

最后，我想到了\ `Google日历 <http://www.google.com/calendar/>`__\ 。虽然它主要是行事历，但用来写日记也很不错，而且它出自Google，相对可靠一点。

问题是，它的界面太复杂，太不友好，太笨重，要加载很多东西。不要说日常使用，看一眼就让人生厌。它倒是有一个专供手机使用的\ `移动版 <http://www.google.com/calendar/m>`__\ ，但是功能之弱让人震惊，居然不支持手机更新。

我知道，Google日历的\ `编程接口 <http://code.google.com/apis/calendar/>`__\ API是开放的，因此想着，也许自己可以编一个简易的更新界面。

这几天，我把它的开发文档读了一遍，写出了一个\ `“Google日历简易版” <http://www.ruanyifeng.com/webapp/calendar/>`__\ ，网址是\ `http://www.ruanyifeng.com/webapp/calendar/ <http://www.ruanyifeng.com/webapp/calendar/>`__\ 。

虽然我主要是为了个人使用，但是其他朋友应该也有类似的需要。我把它公开出来，欢迎大家用，同时帮我查查错。

最后特别声明，不用担心隐私泄漏。我只不过提供一个界面，所有的数据交换都通过ajax渠道，直接与google服务器联系，不经过第三方。安全性与直接使用google的网站完全一样。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/06/google_calendar_lite.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com