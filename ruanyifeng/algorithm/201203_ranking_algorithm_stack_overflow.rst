.. _201203_ranking_algorithm_stack_overflow:

基于用户投票的排名算法（三）：Stack Overflow
===============================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_stack_overflow.html>`__

上一篇文章，我介绍了\ `Reddit <http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_reddit.html>`__\ 的排名算法。

它的特点是，用户可以投赞成票，也可以投反对票。也就是说，除了时间因素以外，只要考虑两个变量就够了。

但是，还有一些特定用途的网站，必须考虑更多的因素。世界排名第一的程序员问答社区\ `Stack
Overflow <http://stackoverflow.com/?tab=hot>`__\ ，就是这样一个网站。

你在上面提出各种关于编程的问题，等待别人回答。访问者可以对你的问题进行投票（赞成票或反对票），表示这个问题是不是有价值。

一旦有人回答了你的问题，其他人也可以对这个回答投票（赞成票或反对票）。

排名算法的作用是，找出某段时间内的热点问题，即哪些问题最被关注、得到了最多的讨论。

在Stack
Overflow的页面上，每个问题前面有三个数字，分别表示问题的得分、回答的数目和该问题的浏览次数。以这些变量为基础，就可以设计算法了。

创始人之一的Jeff
Atwood，曾经在几年前，\ `公布 <http://meta.stackoverflow.com/questions/11602/what-formula-should-be-used-to-determine-hot-questions>`__\ 过排名得分的计算公式。

|image0|

写成\ `php代码 <http://pastebin.com/FWJRbf1N>`__\ ，就是下面这样：

各个算法变量的含义如下：

**（1）Qviews（问题的浏览次数）**

　　|image1|

某个问题的浏览次数越多，就代表越受关注，得分也就越高。这里使用了以10为底的对数，用意是当访问量越来越大，它对得分的影响将不断变小。

**（2）Qscore（问题得分）和Qanswers（回答的数量）**

　　|image2|

首先，Qscore（问题得分）=
赞成票-反对票。如果某个问题越受到好评，排名自然应该越靠前。

Qanswers表示回答的数量，代表有多少人参与这个问题。这个值越大，得分将成倍放大。这里需要注意的是，如果无人回答，Qanswers就等于0，这时Qscore再高也没用，意味着再好的问题，也必须有人回答，否则进不了热点问题排行榜。

**（3）Ascores（回答得分）**

　　|image3|

一般来说，”回答”比”问题”更有意义。这一项的得分越高，就代表回答的质量越高。

但是我感觉，简单加总的设计还不够全面。这里有两个问题。首先，一个正确的回答胜过一百个无用的回答，但是，简单加总会导致，1个得分为100的回答与100个得分为1的回答，总得分相同。其次，由于得分会出现负值，因此那些特别差的回答，会拉低正确回答的得分。

**（4）Qage（距离问题发表的时间）和Qupdated（距离最后一个回答的时间）**

　　|image4|

改写一下，可以看得更清楚：

　　|image5|

Qage和Qupdated的单位都是秒。如果一个问题的存在时间越久，或者距离上一次回答的时间越久，Qage和Qupdated的值就相应增大。

也就是说，随着时间流逝，这两个值都会越变越大，导致分母增大，因此总得分会越来越小。

**（５）总结**

Stack
Overflow热点问题的排名，与\ **参与度**\ （Qviews和Qanswers）和\ **质量**\ （Qscore和Ascores）成正比，与\ **时间**\ （Qage和Qupdated）成反比。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_stack_overflow.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com