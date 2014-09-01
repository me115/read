.. _200805_twine_trial_report:

Twine试用感想
================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/05/twine_trial_report.html>`__

上一次，我写了\ `《Freebase再研究》 <http://www.ruanyifeng.com/blog/2008/04/freebase_reloaded.html>`__\ 以后，\ `徐廉之 <http://www.ruanyifeng.com/blog/2008/04/freebase_reloaded.html#c068208>`__\ 网友赠送了我一个\ `Twine.com <http://www.twine.com/>`__\ 的加入邀请。

著名IT媒体\ `ReadWriteWeb <http://www.readwriteweb.com/archives/twine_first_mainstream_semantic_web_app.php>`__\ ，曾经称Twine可能是”第一个主流的语义网应用”（The
First Mainstream Semantic Web App）。所以，我对它很有兴趣。

下面就是一些我试用后的感想。

**一、Twine是什么？**

首先，需要解释一下，Twine这个网站到底是干什么的。这并不是一件很容易的事情，因为它的构思有点复杂。

虽然不太确切，但是可以简单理解，Twine是一个加强型的美味书签\ `del.icio.us <http://del.icio.us>`__\ 。

del.icio.us的所有功能，Twine都提供，而且还有更多。它允许你保存网址的同时，将整个网页的内容都保存下来。

但是，它又不仅仅是书签网站，它还允许你上传文件。你可以将硬盘里的报告、照片、视频内容，都上传上去。换句话说，它其实还集成了一部分Flickr和Youtube的功能。

因此，从这个角度看，Twine是一个个人的互联网资料中心。

下面是用户的个人页面（点击看大图）。

**二、Twine的信息管理方式**

无论是书签，还是上传的文件，Twine都要求使用者为它们加上summary（总结）和tag（标签）。

Twine会自动分析这些文字中的名词，然后提取出其中的人名、地名和组织名。接着，通过这些标志性词语，Twine就会知道你的兴趣，会自动为你提供相关内容和组织管理信息。

比如，昨天新华社的新闻\ `《奥运圣火在香港传递
亮点频现》 <http://news.xinhuanet.com/sports/2008-05/02/content_8093114.htm>`__\ ：

    5月2日，北京奥运会圣火传递活动在中国香港举行。第一棒火炬手、曾为中国香港夺得首枚奥运会金牌的著名帆板运动员李丽珊手持火炬开始传递。

根据设计构想，Twine会为这段话加上下面一些元信息。（这一步目前只能手工做，系统还没有智能到这个程度。）

    | 人物：李丽珊
    |  地点：中国香港
    |  组织：北京奥运会

有了这些元信息以后，不同的内容就可以被联系起来了。

下面就是显示相关内容的页面图片（点击看大图）。

这正是Twine的设计目的：为所有网页包裹一个语义层（semantic
wrapper）。为以后的机器处理创造条件。这也是它被称为”语义网”应用的原因。

**三、Twine的群件功能**

所有用户添加的单个内容，都被称为item（条目）。Twine允许你将多个相关的item，组成一个节点，而且这个节点可以由许多成员共同建设。

比如，”北京奥运会”就是一个节点，你可以往这个节点里添加所有与主题相关的东西，无论是外部网页、照片、视频都可以。因此，这等于是多个成员共同建设一个project。

从这个角度看，Twine又有点像加强型的wikipedia。

下面就是”Social Network”节点的页面图片（点击看大图）。

**四、对Twine的简评**

从上面的介绍可以看到，Twine的构思还是很不错的。但是，经过我的实际使用，我发现它有一个重大的缺点：那就是对用户的要求太高。

Twine的设计目标，是建立在用户精心组织管理个人信息的基础上的。但是实际上，用户不太可能在添加信息的同时，还费心考虑应该怎么标注元信息。

这造成了Twine的信息管理优势难以发挥。从现实情况看，大多数节点的信息质量都很低下，简直就是一个没有条理的大杂烩。

难怪有用户留言表示悲观：

    这种复杂的系统不会成功。用户是懒惰的。我的一些朋友，使用del.icio.us时，甚至懒得输入tag。（Never
    seen such complicated system ever won. User is lazy; some of my
    friends now even don’t want to tag in del.icio.us any more.）

我的感觉也是这样，Twine的语义网功能其实毫无意义，因为它的使用非常麻烦。它应该马上调整定位，向个人信息管理网站靠拢，否则根本没有前途。

P.S.

我可以邀请5个人加入Twine。如果你对它有兴趣，并且以前曾经在我的Blog上留言不少于3次，请在下面留下你的Email地址。送完为止。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/05/twine_trial_report.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com