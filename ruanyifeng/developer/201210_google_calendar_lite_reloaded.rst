.. _201210_google_calendar_lite_reloaded:

Google日历简易版 2.0
=======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/10/google_calendar_lite_reloaded.html>`__

长假期间，我写了一个小程序，现在正式发布。

大家用不用\ `Google日历 <https://www.google.com/calendar/>`__\ ？

它可以用来规划日程、记录事项、甚至写日记，既安全（数据保存在Google的机房）又方便（各种平台都能访问），甚至还很贴心地提供\ `手机同步 <http://mobile.zol.com.cn/249/2493609.html>`__\ 和\ `免费短信提醒 <http://www.williamlong.info/archives/935.html>`__\ 。

相信很多人与我一样，非常需要这个产品。但是，又不喜欢它的界面：拥挤丑陋，辨识困难，操作麻烦。于是，2008年，我\ `写了 <http://www.ruanyifeng.com/blog/2008/06/google_calendar_lite.html>`__\ 一个”Google日历简易版”。

今年四月份，Google启用新版本API，我的那个程序彻底无法使用了。考虑到还有需求，利用这几天，我索性就重写了一遍。

现在就让我，正式推出\ **`“Google日历简易版
2.0” <http://calendar.ruanyifeng.com>`__**\ ！

    　　＊　操作简便，只需鼠标一点，就可以看到近期事件；

    　　＊　界面清爽，放大了字体，易于阅读；

    　　＊　快速安全，直接与Google交互，全程https加密通信。

欢迎大家试用，看看有没有bug。网址是：

    　　**`http://calendar.ruanyifeng.com <http://calendar.ruanyifeng.com>`__**

两点使用说明：

    　　1）支持各大浏览器的最新版本，IE6、7、8、9除外（因为它们不支持ajax跨域）。

    　　2）这个程序对Javascipt的要求比较高，移动终端方面，我的Android平板可以使用，但是Android手机不行。有ios设备的朋友，帮忙看看，ipad/iphone能不能用。


======================================

（关于发布软件的内容到此为止，接下来是插播时间，我实在忍不住，想谈谈Google。）

这个程序全靠Google的\ `API <https://developers.google.com/google-apps/calendar/>`__\ ，但是Google是怎么开放API的？用户是不知道，开发者看了，心都凉了。

今年四月生效的API\ `第三版 <https://developers.google.com/google-apps/calendar/v3/reference/>`__\ ，比\ `第二版 <https://developers.google.com/google-apps/calendar/v2/developers_guide_protocol>`__\ 少了很多功能。其中有两个，影响尤其巨大。

    　　1.　只提供所有事件（按日期）升序排列，不提供（按日期）降序排列。

    　　2.　不提供某个时间段内的事件总数。

少了这两个基本功能，还怎么玩呀？！你写了一个日历程序，可是连用户的最新事件都取不到……（我现在的解决方法是，一个时间段内限定取回30个事件。如果超出这个数量，只有用户自行缩短时间段了。）

此外，Google还规定，日历API每天请求上限是10000次。你没有看错，真的只有四个零。我数了好几遍，都不敢相信自己的眼睛。

这就是说，你的用户总数，每天最多只能有几百人，Google不允许你发展更多的用户。（相比之下，Google的\ `短网址API <http://www.ruanyifeng.com/blog/2011/01/api_for_google_s_url_shortener.html>`__\ ，每天请求上限是100万次！）所以，基于这个API的任何程序，大概只能是写写玩玩，不可能考虑运营与发展。

我认为，Google这样地封闭平台，无非就是为了防止外部开发者与其竞争，尽量把用户留在自家网站上。这种鼠目寸光、画地为牢的行为，哪来还有半点理想主义的色彩？

Google，枉费我还为你\ `呐喊 <http://www.ruanyifeng.com/blog/2010/01/google_to_quit_china.html>`__\ 过！


========================================

不管怎么说，这个\ `“Google日历简易版” <http://calendar.ruanyifeng.com/>`__\ ，我还是会维护下去的（毕竟眼前找不到更好的在线日历）。

下一次大版本的更新，我打算实现下面两个功能：

    　　1.　颜色标签，不同事件采用不同的背景色；

    　　2.　所有事件都用LocalStorage储存在本地（要不是想到得太晚，这一次我就应该实现这个功能）。

顺便提一下，这一次我是用\ `Bootstrap <http://twitter.github.com/bootstrap/>`__\ 框架开发的，感觉它方便好用，效果也不错。但是下一次，大概不会用它了，因为觉得不够灵活，很多地方都被它限制住了。\ `Foundation <http://foundation.zurb.com/>`__\ 框架对我有可能是一个更好的选择。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/10/google_calendar_lite_reloaded.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com