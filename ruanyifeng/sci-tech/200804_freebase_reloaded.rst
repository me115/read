.. _200804_freebase_reloaded:

Freebase再研究
=================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/04/freebase_reloaded.html>`__

将近一年前，我在Blog里\ `介绍 <http://www.ruanyifeng.com/blog/2007/05/freebase_com.html>`__\ 了\ `Freebase.com <http://www.freebase.com/>`__\ 。在结尾处，我这样说：

    Freebase是一个革命性的网站，就像一个国外程序员所说：”这是2007年迄今互联网上最激动人心的东西”。我想我将在这个网站里面，继续花费大量的时间，四处逛逛，熟悉整个系统。

Freebase的目标很宏伟，就是收集世界上的所有信息，并且整理出信息之间的关系。这件事情最难的地方，倒还不是收集地球上的所有信息，而是怎样确定数据结构，换言之，怎样用一种格式描述出所有信息。这恰恰也是我对Freebase最感兴趣的地方。

前几天，我又去看了，发现整个网站已经基本成型了，数据大量增加，结构也比以前更完整。更重要的是，它开放了编程接口API，允许外部调用它的数据。

请看一个例子——电影数据库\ `FMDB <http://jameshome.com/freebase/fmdb/index.html>`__\ ，在里面可以查到每一部电影、每一个导演、每一个演员，简直就是一个轻量级的\ `IMDB <http://www.imdb.com/>`__\ 。但是，这样一个数据库其实只有一张网页，总的大小不超过100k，一个有经验的程序员最多一天时间就可以完成。因为数据全部来自Freebase，你所要写的其实就是一个查询和展示过程而已。这就是Freebase的意义所在：如果世界上所有相关信息都分门别类放在一个数据库里，那么信息之间的查询和比较将变得异常容易。

借助FMDB和Freebase本身提供的异常强大的\ `查询编辑器 <http://www.freebase.com/view/queryeditor/>`__\ 和\ `开发手册 <http://www.freebase.com/view/en/documentation>`__\ ，我一边学一边猜，终于自己也制作了一个作品——\ `欧美流行音乐数据库 <http://www.ruanyifeng.com/php/music/>`__\ ，里面可以查到所有的欧美歌手、以及他们的专辑和单曲。完成以后，程序小得令人震惊，所有代码加在一起只有十几k。

下面简单介绍一下Freebase的数据结构。

    首先，在Freebase中，每一条信息叫做Topic，也就是一个条目，这就好比字典里的每一个可以查到的词。

    然后，每一个Topic包含一个或多个Type（类型），比如”check”这个词，既可以当动词，又可以当名词，于是它就同时属于”动词”和”名词”这两个Type。

    接着，每一个Type又包含一个或多个Property（属性），比如字典里的每一个单词的每一种词性，都同时包括读音和释义两部分，因此”读音”和”释义”就是两个property。

    最后，每一个属性都有一个值，这个值又是另一个Topic，因此两个Topic就被连接了起来。比如，check当动词时，释义是examine（检查），它本身就是一个Topic，因此这两个词之间就被建立了某种联系。

请看下面这张图。

黄色的方框表示Topic，绿色的方框表示Type。原点”Arnold
Schwarzenegger”同时属于四个Type：Person（人物）、Body
Builder（健美运动员）、Actor（演员）和Politician（政治家）。Type:Person有一个属性Country
of
Birth（出生国），它的值是Austria（奥地利）。Type:Politician有一个属性Party（党派），它的值是Republic（共和党）。Type:Actor有一个属性Films（演出的电影），它的值是Terminator（终结者）。

因此，这里一共有四个Topic：Arnold
Schwarzenegger、Austria、Republic、Terminator。它们就这样被连了起来。

Freebase本身发展了一套数据查询语言MQL，比如我想查出Arnold
Schwarzenegger一共演出过多少部电影，查询语句必须这样写：

    | { 　q0:{ 　　query:[{ 　　　”name”:”Arnold Schwarzenegger”,
    　　　”type”:”/film/actor”, 　　　”film”:[{ 　　　　”film”:[{
    　　　　　”name”:null 　　　　}] 　　　}] 　　}]
    |  　}
    |  }

将上面这段代码，拷贝入\ `查询编辑器 <http://www.freebase.com/view/queryeditor/>`__\ 左面的窗口，点击上方”read»”按钮，就可以在右面的窗口得到查询结果。或者，直接点击这个\ `链接 <http://www.freebase.com/api/service/mqlread?queries={%22q0%22:{%22query%22:[{%22film%22:[{%22film%22:[{%22name%22:null}]}],%22name%22:%22Arnold%20Schwarzenegger%22,%22type%22:%22/film/actor%22}]}}>`__\ ，也可以看到查询结果。

实事求是的说，Freebase的数据结构和MQL语言都很复杂，一点都不符合直觉，我认真研究了好几天，都没有完全搞懂。这使得我感到Freebase的解决方案并不令人满意，它的前途可能也不会很顺利。但是不管怎样，这个网站是一个了不起的尝试，我会继续关注它，试图更好地理解和应用它。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/04/freebase_reloaded.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com