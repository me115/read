.. _200705_freebase_com:

Freebase.com 介绍
====================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2007/05/freebase_com.html>`__

3个月前，就在\ `freebase.com <http://www.freebase.com/>`__\ 上线的第二天，我在日志里\ `惊呼 <http://www.ruanyifeng.com/blog/2007/03/odp_freebase.html>`__\ “这将是互联网上继Wikipedia之后又一个杀手级的应用”。可惜当时\ `freebase.com <http://www.freebase.com/>`__\ 不对外开放，我不能进去看个究竟。

上个星期，我终于得到了它的邀请信，成为了注册用户。于是，我将这个网站初步研究了一下。

**Freebase的作用**

首先，我来说一下，这个网站到底是干什么的。

简单说，Freebase是个类似wikipedia的创作共享类网站，所有内容都由用户添加，采用创意共用许可证，可以自由引用。两者之间最大的不同在于，Freebase中的条目都采用结构化数据的形式，而wikipedia不是。

比如，下图是已故美国总统肯尼迪的条目（点击看大图）。可以发现其中所有的内容都是格式化的，一条一条的，有点像履历表，包括出生时间、死亡时间、性别、职业、国籍、配偶等等。

这一套格式是固定的，所有人物条目都包含同样的字段。这样一来，数据之间就可以很容易地联系在一起，为信息的查询和处理提供了巨大的方便。

举例来说，将来可以很方便地在Freebase中查到”出生于1946年的美国电影导演的名单”，然后你就可以根据这份名单，立即从Freebase中提取他们每个人的简历。要想在wikipedia中完成类似的查询是非常困难的，事实上，wikipedia最大的缺点就是它的数据不是结构化的，因此难于引用和处理。

推而广之，Freebase的目标是包含地球上的所有信息，因此可以设想，理论上，将来可以从freebase中得到任何信息。我立刻能想到的一个应用是，将来在电脑上播放DVD或mp3时，播放器可以到Freebase中获取光盘或专辑的出版信息。

**Freebase的结构**

Freebase的结构分为三层：Domain -> Type -> Topic。

1)
在Freebase中，每个条目叫做一个Topic，每个Topic中的固定字段，叫做”属性”（Property）；

2)
所有同类的Topic组成一个Type，比如所有电影Topic就属于同一个Type，每个Type都有一套固定的Property，因此同类信息可以直接比较和关联；

3)
所有相关的Type组成一个”域”（Domain），比如电影和音乐都属于”艺术和娱乐”
Domain。

截至现在（2007年5月30日），Freebase中共有61个DOMAIN、765个Type，2,312,676个Topic。

**元数据的威力**

如果你熟悉图书馆学的话，其实可以看出来，Freebase的核心功能就是为每一类条目（Type）定义了一套\ `元数据 <http://www.ruanyifeng.com/blog/2007/03/metadata.html>`__\ 。元数据是否准确和适用，是影响Freebase成败的关键。

Freebase最强大的地方就在于，它里面的元数据是可变的，具有弹性。

具体的操作机制，我还没有完全搞清楚，好像是用户可以定义自己私人的元数据，然后在某些条件下，某些私有元数据的Property可以变为共有的Property。

**对Freebase的一些意见和展望**

现在Freebase全站完全都是用Ajax搭建的，HTML页面中根本不包含具体数据，完全要靠Javascript去读取。这等于拒绝了搜索引擎，我认为是极其不智的。

另外，也许是Alpha版的原因，现在的网站中还不包括信息输出，使得用户无法引用。我认为，每个条目都应当提供xml文件才好。

不管怎样，Freebase是一个革命性的网站，就像\ `一个国外程序员 <http://semantic.nodix.net/2007/03/freebase.html>`__\ 所说：”Freebase是2007年迄今互联网上最激动人心的东西”（This
is the most exciting Web thingy 2007 until
now.）我想我将在这个网站里面，继续花费大量的时间，四处逛逛，熟悉整个系统。

我预计，到明年的这个时候（2008年6月），Freebase将成为互联网世界中最热门的话题之一。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2007/05/freebase_com.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com