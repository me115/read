.. _201101_api_for_google_s_url_shortener:

Google短网址的API
====================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/01/api_for_google_s_url_shortener.html>`__

2009年底，Google发布了短网址服务\ `goo.gl <http://goo.gl/>`__\ 。

Google\ `声称 <http://googlesocialweb.blogspot.com/2010/09/google-url-shortener-gets-website.html>`__\ ：

    “……（这是）互联网上最稳定、最安全、最快速的短网址服务。”

有人做了\ `比较 <http://royal.pingdom.com/2010/10/29/is-goo-gl-really-the-fastest-url-shortener-chart/>`__\ ，证明确实如此。

从上图可以看到，goo.gl的响应和跳转时间是最短的。

除了速度快，goo.gl还提供详细的点击统计。比如，Yahoo首页的短网址是\ `http://goo.gl/QuXj <http://goo.gl/QuXj>`__\ ，那么它的统计数据就在\ `http://goo.gl/info/QuXj <http://goo.gl/info/QuXj>`__\ 。加上后缀”.qr”，还能得到这个网址的二维条形码，Yahoo的就是\ `http://goo.gl/QuXj.qr <http://goo.gl/QuXj.qr>`__\ 。


======================================

但是当时，这个服务只供Google内部使用，不向外部使用者开放，大家只好眼睁睁地流口水。

上周，这个限制终于取消了。Google宣布，正式公开goo.gl的\ `API <http://code.google.com/apis/urlshortener/>`__\ 。这意味着，所有外部使用者都能利用它，得到自己想要的短网址。感兴趣的同学，可以自己去研究这个API，还是很简单的。\ `Chrome <https://chrome.google.com/extensions/detail/iblijlcdoidgdpfknkckljiocdbnlagk>`__\ 和\ `Firefox <https://addons.mozilla.org/zh-CN/firefox/addon/googl-lite/>`__\ 浏览器，都已经提供了相应的扩展。

根据这个API，我写了一个”\ `**短网址生成器** <http://www.ruanyifeng.com/webapp/url_shortener.html>`__\ “，欢迎访问，网址是：

    `**http://www.ruanyifeng.com/webapp/url\_shortener.html** <http://www.ruanyifeng.com/webapp/url_shortener.html>`__

另外，我还提供一个Bookmarklet，将”“这个链接加入书签栏，只需一次点击，就可以在当前页面上动态显示该网页的短网址。


======================================

附言

我本来还想实现”自动复制”功能（就是鼠标一点，文字自动复制到剪贴板），但是发现似乎没有通用的解决方案，除非使用Flash。我觉得太麻烦，就放弃了。

但是，我发现了一个很优秀的函数库\ `Zero
Clipboard <http://code.google.com/p/zeroclipboard/>`__\ 。如果你有类似需要，推荐使用这个库。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/01/api_for_google_s_url_shortener.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com