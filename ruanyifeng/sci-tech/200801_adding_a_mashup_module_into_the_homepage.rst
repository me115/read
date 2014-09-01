.. _200801_adding_a_mashup_module_into_the_homepage:

首页增加内容聚合
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/01/adding_a_mashup_module_into_the_homepage.html>`__

昨天，我在\ `首页 <http://www.ruanyifeng.com/blog>`__\ 上添加了一个板块，内容是\ `转贴公社 <http://groups.google.com/group/paste>`__\ 最新文章的摘要输出。

效果如下图：

它的位置在\ `首页 <http://www.ruanyifeng.com/blog>`__\ 的底部，会自动滚动显示。但是，它的载入需要一点时间，依网速而定，一般在10秒左右。

原来这个位置上的”每日引言”被去掉了，虽然它也是很好的内容。

如果你也想在自己的网页上添加类似的功能，那么我可以告诉你，这很容易实现。理论上，任何Feed，甚至是Flickr和Picasa上的照片，都可以这样显示。你只要去点击进入\ `Dynamic
Feed Control
Wizard <http://www.google.com/uds/solutions/wizards/dynamicfeed.html>`__\ 这个页面，输入Feed的网址，就会自动生成相应的代码。

这项服务是\ `Google AJAX Feed
API <http://code.google.com/intl/zh-CN/apis/ajaxfeeds/>`__\ 的一部分。它实际上是\ `Google
Reader <https://www.google.com/reader>`__\ 的一个简易接口，差不多可以用来编写一个简陋但是实用的RSS在线阅读器，请看\ `示例一 <http://www.google.com/uds/samples/feedapidocs/tabbed.html>`__\ 和\ `示例二 <http://www.google.com/uds/solutions/dynamicfeed/sample.html>`__\ 。

将不同网站的内容聚合在一个页面上，这被叫做Mashup，很多人认为这是下一代网站的方向。我也是刚刚开始学习运用，感觉很好玩。

最后，希望大家会喜欢这个改动，也欢迎大家将值得分享的文章贴到\ `“转贴公社” <http://groups.google.com/group/paste>`__\ 中去。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/01/adding_a_mashup_module_into_the_homepage.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com