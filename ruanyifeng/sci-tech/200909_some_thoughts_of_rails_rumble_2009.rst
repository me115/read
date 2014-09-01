.. _200909_some_thoughts_of_rails_rumble_2009:

对于Rails Rumble 2009的一点感想
==================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/09/some_thoughts_of_rails_rumble_2009.html>`__

Rails Rumble是一项年度的编程比赛。

所有参赛团队必须在2天之内，从零开始做出一个网站，然后由组委会评出优胜者。

2009年的比赛已经在上个月结束了，8月22日-23日的那个周末就是比赛时间，并且\ `获奖名单 <http://r09.railsrumble.com/entries>`__\ 也在上月底对外公布了。48个小时能够做出什么东西？这些网站就是最好的说明。你从中可以看到，目前国际主流的网站开发者的水准。

你会很震惊地发现，所有作品都很成熟，几乎没有任何半成品的痕迹。它们有精美的界面、完全可用的功能、简单但完整的使用说明，而且最重要的一点是，开发者确实将一个点子变成了一个可以直接推向市场的网站，在48小时之中！

比如，第一名的\ `hi.im <http://hi.im/>`__\ 是一个提供个人信息聚合的网络门户，第四名的\ `Lowdown <http://lowdownapp.com/>`__\ 是一个项目开发的任务管理网站，第六名的\ `hurl <http://hurl.r09.railsrumble.com/>`__\ 是一个调试API头信息的网站，第七名的\ `omnominator <http://omnominator.r09.railsrumble.com/>`__\ 是一个找朋友聚会的网站，第九名的\ `bartender <http://bartender.r09.railsrumble.com/>`__\ 是一个鸡尾酒调配法大全的网站。

下面，我想着重谈谈第五名\ `ZenVDN <http://zenvdn.com/>`__\ 。它的四个作者之一的\ `Jon
Dahl <http://railspikes.com/2009/8/28/buiding-a-video-distribution-in-48-hours>`__\ 写了一篇很好的文章，介绍开发过程。

简单说，ZenVDN是一个视频上传网站，用户上传视频后，可以将播放器嵌入网志，与他人分享。从这点看，它与Youtube很像，但是它比Youtube更专业，用户对自己的视频有更多的输出选项和更多的管理权。

初看之下，你会觉得，这种功能的网站不可能在48个小时内做出来，它能将几十种格式的视频互相转换。只用48个小时就能支持这么多种类的视频格式，怎么可能呢？就连一个评委都提出了这样的质疑。

奥妙就在于，ZenVDN是一个组装起来的网站。它的视频转化功能由\ `Zencoder <http://zencoder.tv/>`__\ 提供，Flash播放器由\ `Flowplayer <http://flowplayer.org/>`__\ 提供，视频的储存使用了类似Amazon
S3的服务，视频的分发使用了现成的CDN网络，将来的收费服务则打算使用\ `Spreedly <http://spreedly.com/>`__\ 。因此，ZenVDN才有可能在48小时中做出来，它的开发团队实际上只是做出了一个用户界面，然后将各种第三方服务整合好就可以了。

我感到，这就是未来网站开发的方向。未来的网站，恐怕很少从头到尾都是一个团队做出来的，而更像是积木，大量使用第三方服务组合和搭建出来。这样做有许多好处，别的不说，单单是四个程序员一个周末就能做出原型，就非常吸引人了。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/09/some_thoughts_of_rails_rumble_2009.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com