.. _200402_firebird:

我也爱Firebird浏览器
=======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2004/02/firebird.html>`__

只有用过才知道\ `Firebird <http://home.bomoo.com/mt-archives/2004_01_24_34.html>`__\ 有多好，比IE强多了，我是越用越喜欢。

下面是Firebird开发者的一篇访谈。最喜欢里面的这段话：

    “我是这样一种人，我很少会对招摇的东西留下印象，更多是对可用性感兴趣，大体上，我更喜欢与我的系统结合得更好的朴素的主题。”

哈哈，我也是这样的人。


======================================

**Neowin采访Firebird开发者Ben Goodger（转载）**

原文来源：\ `Playin’ with
IT <http://keso.donews.net/keso/posts/2661.aspx>`__

Mozilla Firebird是来自Mozilla小组最新浏览器的商标。采访中Ben
Goodger作为该浏览器的开发负责人，阐述了有关浏览器的独特观点。

问：首先，感谢你来跟neowin对话！你何不先谈谈你自己，以及你在Mozilla.org中的角色。

答：我叫Ben Goodger，我是Mozilla
Firebird的开发负责人，我为Mozillla基金会工作。我的工作主要就是帮助完成Firebird
1.0。

问：能不能向我们简单描述一下Mozilla Firebird的情况和历史？

答：就像你们知道的，Mozilla由Netscape创建于1998年，当时是希望以某种方式寻求帮助，以便打造下一代浏览器。这一工作的结果就是Mozilla
1.x套件（开发者称之为”Seamonkey”），它构成了Netscape
6和7系列的产品基础。在这段时间中我是Navigator项目组的工程师，并且有不少人为那些产品做了大量工作。对于很多的决策都是让用户界面被关注，我们中的一些人感到不满，决策的做出是因为假定的商业事实。在Navigator和XPToolkit项目组中的一些成员有一种感觉，能够做一个更好的浏览器，这个浏览器关注真正的用户而不是特殊兴趣，一个可以体现大量市场要求的浏览器。Dave
Hyatt和我2001年中期在这方面有了一个不成功的开始，我们用C#开发了一个嵌入Gecko引擎的Windows版浏览器，名为Manticore，但它没什么动静就失败了。

2002年，Blake Ross、David Hyatt、Joe Hewitt和Pierre
Chanial开始做一个新的XUL浏览器，叫做Phoenix，力图解决某些问题，但开始还是做了大量基于老的Seamonkey产品进行前期编码的工作，以使事情能轻松一点。到2002年下半年，Phoenix
0.5已经足够好，我把它作为一个默认浏览器使用。到此时，我已经不再在AOL的浏览器产品部门工作，但当这个项目开始出现与Manticore注定相似的命运的时候，我与此项目已经关系密切。一个全新的主题，一些用户界面的有意义的新变化，以及一个饱受争议的新名字——Firebird，我们在2003年5月发布了0.6版。这个发行版真正让这个项目变得知名，不只是因为有争议的命名，还因为它是如此的好，有更多卖点。经过这个夏天，我们在0.7发行版上增加了更多的改进，最终在2003年10月发布。那以后，我们又开始忙于0.8版，这个版本的发布已经非常非常近了。

问：在Firebird中你最喜欢哪个特性？

答：我现在真的再也不能使用任何其他的浏览器，因为集成了Google搜索栏，只要一个Ctrl+K，就可以在页面上查找你搜索的文本；卡片式浏览；阻拦弹出窗口；以及自动下载（一个带给Windows用户Mac风格的文件自动下载到你的桌面的特性）。

问：你能不能给个理由，为什么Internet Explorer用户应该转换到Firebird？

答：很多特性我已经描述过了。就算给IE增加了阻拦弹出窗口和Google搜索栏的插件，你还是不能进行卡片式浏览，也不能查找你输入的文本（只要开始输入文本，浏览器就会跳到页面上第一个匹配位置），没有改进的文件下载，很多很多。我们的用户界面看上去很简单，但却高度可定制，尤其是跟Mozilla
1.x产品相比，我们试图确切掌握IE用户的实际需求是什么，并让迁移变得很简单。

问：一些用户还是会被Firebird吓住，因为他们担心页面不能被”正确”显示，而用IE则可以。你对此怎么看？

答：这当然取决于你在访问什么页面。网上有一定数量的站点是专为微软技术设计的，一个典型例子是MSDN。需要专门启动IE去浏览一个站点的事情并不常见，我想在正确显示专有网页方面，我们比任何其他的非IE浏览器做得更好。

问：Firebird按其本性是一个”紧凑的”浏览器，通过”扩展”添加功能。你有什么特别喜欢的，或者有哪些扩展在你看来是精华？

答：我并不大量使用扩展，一般而言我也不考虑任何”精华”。我们是一个紧凑的浏览器，但我们不是一个”小”浏览器，从这个意义上说，我们故意去掉了很多人不需要的特性。我们试图把浏览器的默认安装做成各种特性的最佳设置并适用于每个人。当然有特殊兴趣的人可以自由定制他们的浏览器扩展以适合他们的使用习惯。有能力的下载者可以找到许多可下载扩展可以简化不同的操作，就像我自己的Magpie（这是我给我自己写的）以及来自其他人的扩展如DownloadSort和DownloadStatusbar。Web开发者可以找到能简化他们许多工作的扩展，如设定浏览窗口大小以适应不同的分辨率、HTML检查，等等。基本上惟一的目的就是让Firebird适应你的需求。

问：Firebird最主要的特色之一就是高度可换肤，你个人使用什么主题？借这个话题再问一下，你发现有很多老的主题不兼容新版本的Firebird吗？

答：我用默认主题。我是这样一种人，我很少会对招摇的东西留下印象，更多是对可用性感兴趣，大体上，我更喜欢与我的系统结合得更好的朴素的主题。但这只是个人的喜好。我们提供几乎任何应用的高度可修改和最易于理解的主题引擎，所以人们可以拿出极其眩目的材料。至于旧主题的不兼容，或者它们的作者可以对这些主题进行升级，或者别人可以自愿地加以解决。在Firebird
0.9中，我们会加入新的功能，防止旧的主题和扩展妨碍浏览器的启动或引起其他问题。

问：有没有什么特别令人兴奋的新特性会出现在下面几个新版本（0.8，0.9）中？

答：有，我刚刚说的有关扩展和主题的功能就是很大的一部分工作，它将使扩展的作者更容易创建并分发不可抗拒的插件。我们还会加入一个功能，使从其他浏览器移植设置变得更简单。除此之外，在1.0之前不会有太多重大的新特性。0.9暂时列出的”已完成特性”就是一个艰巨的bug修复任务，并努力地进一步简化并改善用户界面，在这期间我并不期望有更多重大的新特性。

问：你能告诉我们你在这条路上遇到过的问题吗，比如说Mozilla
Firebird的命名以及”商标图片”的确定？它们在何种程度上拖延了这个项目？

答：命名问题是一个不合时宜的难题。我们还没有做完我们的商标的元素，到目前为止更多的注意力已经放到了工程上，但在有效地推进产品方面仍有大量的事要做。希望未来会有更多的时间放到这方面。

问：最后，告诉我们在Firebird上你还有什么秘密武器。

答：关于1.0版以后还会发生什么我们也不知道，有对A或者B的改进版本的讨论，但我们还没有制定出一个策略或任何类似的计划。至于不远的将来——比如接下来的6个月——中心将是把可靠的1.0版送出门。我们相信2004年将会是潮流开始改变，我们拿回市场份额的一年。

问：非常感谢Ben跟我们说的这些话，祝你在接下来的几个版本中好运，并希望未来某个时间我们再来聊一聊。

| Posted by Mr magoo on 23 January 2004
|  Source:
`neowin <http://www.neowin.net/articles.php?action=more&id=76>`__

|  Download: `Firebird for
Windows <http://ftp.mozilla.org/pub/mozilla.org/firebird/releases/0.7/MozillaFirebird-0.7-win32.zip>`__,
`Linux <http://ftp.mozilla.org/pub/mozilla.org/firebird/releases/0.7/MozillaFirebird-0.7-i686-pc-linux-gnu.tar.gz>`__,
and
`Mac <http://ftp.mozilla.org/pub/mozilla.org/firebird/releases/0.7.1/firebird-0.7.1-mac.dmg.gz>`__.
|   View: `Mozilla
Firebird <http://www.mozilla.org/projects/firebird/>`__
|   View: `Mozillazine.org, Mozilla News and
Communities <http://www.mozillazine.org/>`__
|   View: `Discuss this Article in the
Forums <http://www.neowin.net/forum/index.php?act=ST&f=12&t=134854>`__

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2004/02/firebird.html>`__

Evernote

**

Highlight

Remove Highlight

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2004/02/firebird.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com