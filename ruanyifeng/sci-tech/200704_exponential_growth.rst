.. _200704_exponential_growth:

指数式增长（Exponential Growth）
===================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2007/04/exponential_growth.html>`__

前几天，我在日志中写到，有人根据我国历代\ `古籍的数量 <http://www.ruanyifeng.com/blog/2007/04/the_amount_of_chinese_ancient_books.html>`__\ ，整理出一个指数方程。当时我还嘲笑说，这种做法有点无聊。今天我才发现，不是人家无聊，而是我太无知。

原来，文献数量呈指数式增长，不是回归方程做出来的，而是一项定理，在文献学中有专门的名字，叫”普赖斯公式”。

1963年，英国学者\ `普赖斯 <http://www.answers.com/topic/derek-j-de-solla-price>`__\ （Derek
J. de Solla Price），提出文献数量的增长遵守如下方程：

F=a·e\ :sup:`rt`

其中，F表示本期文献量，a表示初期文献量，t表示时间，r表示文献增长的即时速率，也就是导数。

上面这个方程事实上是一个通用方程，任何指数式增长都可以用上面这个方程来刻画。

所谓指数式增长，就是指一个变量增长的速率与它此时的数量成比例。假设变量x随时间t指数式增长，那么根据定义，x的变化量遵守如下的微分方程：

其中，k>0，是一个常数，表示x增长的一个比例。对这个方程求解，可以得到x的解为。将这个解同普赖斯公式进行比较，可以发现两者是一样的。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2007/04/exponential_growth.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com