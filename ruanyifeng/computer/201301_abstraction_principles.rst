.. _201301_abstraction_principles:

代码的抽象三原则
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2013/01/abstraction_principles.html>`__

软件开发是\ `“抽象化”原则 <http://en.wikipedia.org/wiki/Abstraction_principle_(computer_programming)>`__\ （Abstraction）的一种体现。

所谓”抽象化”，就是指从具体问题中，提取出具有共性的模式，再使用通用的解决方法加以处理。

开发软件的时候，一方面，我们总是希望使用别人已经写好的代码，另一方面，又希望自己写的代码尽可能重用，以求减少工作量。要做到这两个目标，这需要”抽象化”。

最近，我读到美国程序员\ `Derick
Bailey <http://lostechies.com/derickbailey/2012/10/31/abstraction-the-rule-of-three/>`__\ 的一篇文章，谈到”抽象化”应该遵循的三个原则，觉得很有启发。

**一、DRY原则**

`DRY <http://en.wikipedia.org/wiki/Don%27t_repeat_yourself>`__\ 是 Don’t
repeat yourself 的缩写，意思是”不要重复自己”。

软件工程名著\ `《The Pragmatic
Programmer》 <http://en.wikipedia.org/wiki/The_Pragmatic_Programmer>`__\ 首先提出了这个原则。它的涵义是，系统的每一个功能都应该有唯一的实现。也就是说，如果多次遇到同样的问题，就应该抽象出一个共同的解决方法，不要重复开发同样的功能。

这个原则有时也称为\ `“一次且仅一次”原则 <http://zh.wikipedia.org/wiki/%E4%B8%80%E6%AC%A1%E4%B8%94%E4%BB%85%E4%B8%80%E6%AC%A1>`__\ （Once
and Only Once）。

**二、YAGNI原则**

`YAGNI <http://en.wikipedia.org/wiki/You_ain't_gonna_need_it>`__\ 是 You
aren’t gonna need it 的缩写，意思是”你不会需要它”。

这是\ `“极限编程” <http://en.wikipedia.org/wiki/Extreme_programming>`__\ 提倡的原则，指的是你自以为有用的功能，实际上都是用不到的。因此，除了最核心的功能，其他功能一概不要部署，这样可以大大加快开发。

它背后的指导思想，就是尽可能快、尽可能简单地让软件运行起来（do the
simplest thing that could possibly work）。

但是，这里出现了一个问题。仔细推敲的话，你会发现DRY原则和YAGNI原则并非完全兼容。前者追求”抽象化”，要求找到通用的解决方法；后者追求”快和省”，意味着不要把精力放在抽象化上面，因为很可能”你不会需要它”。所以，就有了第三个原则。

**三、Rule Of Three原则**

`Rule of
three <http://en.wikipedia.org/wiki/Rule_of_three_(computer_programming)>`__
称为”三次原则”，指的是当某个功能第三次出现时，才进行”抽象化”。

这是软件开发大家\ `Martin
Fowler <http://en.wikipedia.org/wiki/Martin_Fowler>`__\ 在《Refactoring》一书中提出的。

它的涵义是，第一次用到某个功能时，你写一个特定的解决方法；第二次又用到的时候，你拷贝上一次的代码；第三次出现的时候，你才着手”抽象化”，写出通用的解决方法。

这样做有几个理由：

（1）省事。如果一种功能只有一到两个地方会用到，就不需要在”抽象化”上面耗费时间了。

（2）容易发现模式。”抽象化”需要找到问题的模式，问题出现的场合越多，就越容易看出模式，从而可以更准确地”抽象化”。

比如，对于一个数列来说，两个元素不足以判断出规律：

    　　1, 2, \_, \_, \_, \_,

第三个元素出现后，规律就变得较清晰了：

    　　1, 2, 4, \_, \_, \_,

（3）防止过度冗余。如果一种功能同时有多个实现，管理起来非常麻烦，修改的时候需要修改多处。在实际工作中，重复实现最多可以容忍出现一次，再多就无法接受了。

综上所述，”三次原则”是DRY原则和YAGNI原则的折衷，是代码冗余和开发成本的平衡点，值得我们在”抽象化”时遵循。


==========================================================

附：

**[广告]**

图灵公司打算重新出版\ `《Joel on
Software》 <http://www.amazon.com/Joel-Software-Occasionally-Developers-Designers/dp/1590593898/>`__\ 的中文版，正在寻找译者。如果你对此有兴趣，请与朱巍编辑联系（Email：zhuw(at)turingbook.com）试译。关于此书的更多情况，可参考我翻译的续集\ `《More
Joel on
Software》 <http://www.ruanyifeng.com/docs/mjos/>`__\ 。特别提醒：翻译是非常辛苦、但是报酬很低的工作，写信前请想清楚，你是真的想翻译这本书。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2013/01/abstraction_principles.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com