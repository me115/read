.. _201203_ranking_algorithm_newton_s_law_of_cooling:

基于用户投票的排名算法（四）：牛顿冷却定律
=============================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_newton_s_law_of_cooling.html>`__

这个系列的前三篇，介绍了\ `Hacker
News <http://www.ruanyifeng.com/blog/2012/02/ranking_algorithm_hacker_news.html>`__\ ，\ `Reddit <http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_reddit.html>`__\ 和\ `Stack
Overflow <http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_stack_overflow.html>`__\ 的排名算法。

今天，讨论一个更一般的数学模型。

这个系列的每篇文章，都是可以分开读的。但是，为了保证所有人都在同一页上，我再说一下，到目前为止，\ **我们用不同方法，企图解决的都是同一个问题：根据用户的投票，决定最近一段时间内的”热文排名”。**

你可能会觉得，这是一个全新的课题，伴随着互联网而产生，需要全新的方法来解决。但是，实际上不是。我们可以把”热文排名”想象成一个”自然冷却”的过程：

    　　（1）任一时刻，网站中所有的文章，都有一个”当前温度”，温度最高的文章就排在第一位。

    　　（2）如果一个用户对某篇文章投了赞成票，该文章的温度就上升一度。

    　　（3）随着时间流逝，所有文章的温度都逐渐”冷却”。

    　　

这样假设的意义，在于我们可以照搬物理学的冷却定律，使用现成的公式，建立”温度”与”时间”之间的函数关系，轻松构建一个\ `“指数式衰减” <http://en.wikipedia.org/wiki/Exponential_decay>`__\ （Exponential
decay）的过程。

伟大的物理学家牛顿，早在17世纪就提出了温度冷却的数学公式，被后人称作\ `“牛顿冷却定律” <http://episte.math.ntu.edu.tw/applications/ap_cooling/index.html>`__\ （Newton’s
Law of Cooling）。我们就用这个定律构建排名算法。

“牛顿冷却定律”非常简单，用一句话就可以概况：

    **物体的冷却速度，与其当前温度与室温之间的温差成正比。**

写成数学公式就是：

　　|image0|

其中，

    　　-
    T(t)是温度（T）的时间（t）函数。微积分知识告诉我们，温度变化（冷却）的速率就是温度函数的导数T’(t)。

    　　-
    H代表室温，T(t)-H就是当前温度与室温之间的温差。由于当前温度高于室温，所以这是一个正值。

    　　-
    常数α（α>0）表示室温与降温速率之间的比例关系。前面的负号表示降温。不同的物质有不同的α值。

这是一个微分方程，为了计算当前温度，需要求出T(t)的函数表达式。

第一步，改写方程，然后等式两边取积分。

　　|image1|

　　|image2|

| 
|  第二步，求出这个积分的解（c为常数项）。

　　|image3|

　　|image4|

　　|image5|

第三步，假定在时刻t\ :sub:`0`\ ，该物体的温度是T(t\ :sub:`0`)，简写为T\ :sub:`0`\ 。代入上面的方程，得到

　　|image6|

　　|image7|

第四步，将上一步的C代入第二步的方程。

　　|image8|

假定室温H为0度，即所有物体最终都会”冷寂”，方程就可以简化为

　　|image9|

上面这个方程，就是我们想要的最终结果：

    　　**本期温度 = 上一期温度 x exp(-(冷却系数) x 间隔的小时数)**

将这个公式用在”排名算法”，就相当于（假定本期没有增加净赞成票）

    　　**本期得分 = 上一期得分 x exp(-(冷却系数) x 间隔的小时数)**

其中，”冷却系数”是一个你自己决定的值。如果假定一篇新文章的初始分数是100分，24小时之后”冷却”为1分，那么可以计算得到”冷却系数”约等于0.192。如果你想放慢”热文排名”的更新率，”冷却系数”就取一个较小的值，否则就取一个较大的值。

[参考文献]

　　\*　`Rank Hotness With Newton’s Law of
Cooling <http://www.evanmiller.org/rank-hotness-with-newtons-law-of-cooling.html>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/03/ranking_algorithm_newton_s_law_of_cooling.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com