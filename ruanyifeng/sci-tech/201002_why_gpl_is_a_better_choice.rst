.. _201002_why_gpl_is_a_better_choice:

为什么gpl是更好的开源许可证?
===============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/02/why_gpl_is_a_better_choice.html>`__

1.

让我从一件新闻讲起。

2009年，计算机业界发生了一件大事：甲骨文公司以74亿美元收购SUN公司。

消息宣布后，有一个人坚决反对这笔交易。他叫\ `Michael
Widenius <http://en.wikipedia.org/wiki/Michael_Widenius>`__\ ，是数据库软件\ `MySQL <http://www.mysql.com>`__\ 的主要创始人。

他为什么要反对呢？因为MySQL现在归SUN公司所有，一旦收购成功，就将属于甲骨文公司所有。但是，后者的主要产品是Oracle数据库，与MySQL是竞争关系。所以，甲骨文公司不可能扶持MySQL的后继开发，甚至有可能杀死MySQL。

Michael
Widenius不能接受这个事实，他发起万人签名，提交请愿书，要求欧盟委员会否决这项交易。具体情况可以参见\ `HelpMysql.org <http://helpmysql.org>`__\ 。

2.

去年12月28日，他写了一篇很长的文章”\ `Help keep the internet
free <http://monty-says.blogspot.com/2009/12/help-keep-internet-free.html>`__\ “，解释为什么反对这项交易。他是这样写的：

    “If Oracle were allowed to acquire MySQL, we would be looking at
    less competition among databases, which will mean higher license and
    support prices.”

    “如果甲骨文得到了MySQL，数据库市场的竞争将会减少，最终导致更高的价格和收费。”

你觉得这句话对不对？

我觉得不对。我认为，甲骨文公司杀不死MySQL，数据库市场的竞争不可能减少。\ **这并非由于甲骨文公司不想这样做，而是因为MySQL是无论如何都不可能被杀死的（假定始终存在市场需求的话）。**

3.

为什么MySQL是杀不死的？

答案非常简单。因为它的许可证是GPL。

GPL明确规定，任何源码的衍生产品，如果对外发布，都必须保持同样的许可证。\ **这就是说，任何人只要发布MySQL的修改版本，他就必须公开源码，并且同意他人可以自由地复制和分发。**

现在让我们假想一下：

第一种情况：甲骨文公司决定中止MySQL的开发，会怎么样？

一定会有其他人接手，继续推出MySQL的后续版本，这是GPL许可证允许的，完全合法。虽然不能再叫MySQL这个名字，但是只要代码完全兼容，名字又有什么关系呢。事实上，Michael
Widenius自己的公司，现在的产品\ `MariaDB <http://askmonty.org/wiki/index.php/MariaDB>`__\ 就是基于MySQL的。

第二种情况：甲骨文公司决定，MySQL的后续版本不再开源，或者整体并入Oracle数据库，会怎么样？

答案更简单，不可能发生这种情况。因为根据GPL许可证，只要发布基于原代码的新产品，就一定必须开源。

4.

所以，我实际上觉得，Michael
Widenius没有竭力反对的必要。不管甲骨文干什么，MySQL都不可能灭绝。

相反的，真正感到倒霉的人，应该是甲骨文公司才对，因为它花钱买来自己无法控制的财产。\ **任何的代码，只要置于GPL之下，就不再受作者或所有者控制了，想杀也杀不死了。**

5.

如果一个程序员想将自己的代码开源，他有许多种选择，大致可以分成三类：

　　1. 选择GPL许可证，要求衍生代码必须开源。

　　2. 将代码放入”公共领域”（public domain），彻底放弃版权。

　　3. 选择更宽松的许可证，比如BSD和Apache许可证，不要求衍生代码开源。

**许多人认为，选择后两种做法比选择GPL更值得赞扬，因为更加大公无私。但是，这样的看法是错误的，实际上GPL要好于后两种选择。**

让我们再来假想一下，如果MySQL的源码处于公共领域，或者BSD许可证之下，那会怎样？

那样的话，许多站长恐怕都会感到大难临头了。他们不得不做出选择，将来到底是升级到第三方小公司推出的、质量没有保证、支持力量薄弱、互相不兼容的基于MySQL
5.x版本的各种衍生数据库，还是升级到甲骨文公司推出的、与Oracle兼容的、号称具备各种新功能和最佳性能、并且广告满天飞的MySQL
6.0版本。

在BSD许可证或者公共领域代码的情况下，甲骨文公司可以从容地将MySQL
6.0变为闭源产品，推出你只有花钱才能买到的新特性和后继版本，并且只要你复制给他人使用，就要起诉你。使用开源软件的用户，将因此变为依赖甲骨文公司的用户。只有这种情况发生，才真正有必要，竭力反对甲骨文收购SUN公司。

当程序员放弃代码的版权，或者选择BSD许可证，他可能认为自己做出了世界上最无私的行为。很大程度上，事实确实如此。但是，我们要知道，这个世界是一个商业利益占主导的世界。一旦发生像甲骨文拥有MySQL这一类的事情，你的代码的价值将大大削弱，大公司先是免费利用它们，然后再设法推出取代它们的私有产品。你以为自己奉献了爱心，但是实质上变成了为大公司无偿打工。

**从这个角度看，GPL是更好的开源许可证。它保证了自由始终是自由，既无法被剥夺，也不是一种圈套或陷阱。**

6.

有的朋友读到这里，可能会提出疑问。如果GPL许可证真的这么好，那么为什么GNU基金会还推出了\ `LGPL许可证 <http://www.gnu.org/licenses/lgpl-2.1.html>`__\ ？

所谓LGPL许可证，全称是Lesser General Public
License，直译就是”限制更少的GPL许可证”，1991年时与GPL（第二版）同时发布。它近似于BSD许可证，允许将代码用于闭源产品。

这就产生了一个很有趣的问题。为什么像Richard
Stallman这种坚持自由丝毫不可侵犯的人，会同意将自己的代码用于闭源产品？

说起来，这其实是他的策略，主要与GNU C
library有关。1991年的时候，市场上有很多C语言库可以选择。如果GNU的C库是GPL许可证，那么很多私有软件不会选择它，因为一旦选择了它，就意味产品本身一定要开源。所以为了保证开源软件得到使用和推广，并且闭源软件中有开源的成分，总比一点没有好，所以才诞生了LGPL许可证。

`Richard
Stallman <http://www.gnu.org/licenses/why-not-lgpl.html>`__\ 说得很清楚：

    “After all, there are plenty of other C libraries; using the GPL for
    ours would have driven proprietary software developers to use
    another—no problem for them, only for us.”

    “毕竟，市场上的C库有的是。GPL许可证将迫使私有软件去使用他人的库，这不会给他们带来困扰，只会给我们带来困扰。”

所以，策略是这样的：\ **整体软件，或者没有替代品的代码库，一定要使用GPL许可证；有替代品的代码库，可以使用限制较少的开源许可证，但是在取到足够市场份额之后，也应该转为GPL许可证。**\ 这就是为什么javascript的代码库，大多数都是类似BSD的许可证，而不是GPL许可证的原因，因为可替代自己的竞争者实在太多了。

总之，如果你想把自己的软件开源，只要不属于上面这种例外情况，GPL就是更好的选择。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/02/why_gpl_is_a_better_choice.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com