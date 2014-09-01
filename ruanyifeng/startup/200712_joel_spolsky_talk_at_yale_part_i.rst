.. _200712_joel_spolsky_talk_at_yale_part_i:

Joel Spolsky在耶鲁大学的演讲（上）
=====================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2007/12/joel_spolsky_talk_at_yale_part_i.html>`__

Joel
Spolsky是一个美国的软件工程师，他的网络日志\ `“Joel谈软件” <http://www.joelonsoftware.com/>`__\ （Joel
on Software）非常有名，读者人数可以排进全世界前100名。

上个月28号，他回到母校耶鲁大学，与计算机系的学生座谈。他发表了一个演讲，回顾自己的人生经历，并总结了一些个人的体会。

我读完他的演讲稿，很受触动，觉得他的人生体会非常具有启示性。这篇演讲非常长，分为三个部分（\ `一 <http://www.joelonsoftware.com/items/2007/12/03.html>`__\ 、\ `二 <http://www.joelonsoftware.com/items/2007/12/04.html>`__\ 、\ `三 <http://www.joelonsoftware.com/items/2007/12/05.html>`__\ ）。下面是其中的一些精彩段落，共有四段。

（更新：此篇演讲的全文收录在我翻译的《软件随想录》一书，人民邮电出版社，2009年出版。）

**一、大学里最有用的课程**

Joel说，他在大学里上过的最有用的课，是一门他只上了一回、然后就再也没有去过的课。

由于父母都是大学教授，亲戚朋友都是学术界里的，大多有博士学位，所以Joel从小就认定自己也会去读博士，将来搞学术。可是，有一门课程改变了他的想法，使他最终没有去报考研究生院。

这门课程叫做”动态逻辑”（Dynamic
Logic）。在第一堂课上，教授证明了一个命题。假定有一个程序”f := not f,”
f是表示真假的逻辑值，那么结论是程序运行偶数次后，f的值保持不变。整个证明过程非常冗长，要花几个小时讲解，一共有几十步。课后习题则是，证明如果f值保持不变，那么程序必然运行了偶数次。

课后，Joel花了很多时间做题，还去图书馆借来了参考书。但是，他逐渐感到这样做没有意义：用大量琐碎的、容易出错的步骤，去证明一个凭直觉就能认定成立的命题，这不是一个富有实效的工作方法。在Joel看来，计算机更应该用来解决错误，而不是让人们陷入逻辑的陷阱，去产生错误。（I
decided that this Dynamic Logic stuff was really not a fruitful way of
proving things about actual, interesting computer programs, because
you’re more likely to make a mistake in the proof than you are to make a
mistake in your own
intuition.）通过这件事，他认识到，自己不适合做纯思辨性的学术研究。因此，他就退掉了这门课，并且以后也没有选择去上研究生院。

Joel认为，就是这门只上了一次的课，恰恰成为了他在大学中上过的最有用的课，因为它帮助他选择了正确的人生道路。

**所以，Joel的第一个结论是：人生中重要的，是关注那些真正的问题（real
problem），而不是陷入那些没有意义的琐碎问题（trivial
problem）。就像苏格拉底说的，”认识你自己”。**

此外，Joel说，还有一门叫做CS
323的课，也很有用。这门课有大量的课后习题，都是关于编程的，平均每星期要花40个小时来做题。

Joel发现他能够做出大部分的题目，更重要的是，他发现自己喜欢做这些题。这样一来，他就明白自己是适合编程的。另一方面，很多其他学生对这门课感到无比头疼，觉得编程既枯燥又痛苦，每周40小时做这种题简直是一种刑罚。这些人于是明白，虽然同样是计算机系的学生，但是他们并不适合编程。这是一件好事，因为这样他们就避免了以后选择错误的职业。否则，让一个不喜欢编程的人，一生都与程序打交道，这是多么悲惨的一件事啊！

**二、在Viacom的日子**

毕业以后，Joel先在微软公司干了一段日子，然后回到纽约，进入维亚康母公司（Viacom），为这家巨型的娱乐传播公司编写软件，成为IT部门里一个程序员（in-house
programmer）。

后来，Joel回忆起来，认为这是他一生中最痛苦的日子，并且劝告计算机系的学生尽可能不要去做”in-house
programmer”。

原因有三个。

    首先，你永远没有办法正确地编写软件，你不得不用最方便的方法编写软件。因为软件支出非常高昂，所以公司会要求尽可能节省成本，你不可能试用新技术，只能使用现有的最成熟、最保守的技术。

    其次，你没有办法将一个项目做到尽善尽美。一旦程序可以正常运行，你的工作也就结束了，可以接下去干公司的下一个项目了。你的作用是解决问题，而不是将软件写得尽可能好。如果你是在一个专业的技术性公司，比如Google或Facebook，情况就完全不一样，你的软件写得越好，公司就会越成功，所以公司会支持你在一个项目上不断做下去。

    最后，传统公司IT部门里的程序员，只属于公司内部的维护人员，而不是直接从事核心业务的人员。因此，你永远办法进入管理层。但是，在技术性公司，程序员会变成CEO。

因为这三个原因，Joel觉得in-house
programmer不是一个好的职业，不幸的是，80%的程序员属于这一类，年复一年，很多人的生命就是这样被耗干的。（it’s
frightening because this is what probably 80% of programming jobs are
like, and if you’re not very, very careful when you graduate, you might
find yourself working on in-house software, by accident, and let me tell
you, it can drain the life out of you.）

**Joel的第二个结论是：选择职业时，不要只考虑职位是否专业对口，应该尽量选择业务方向与你专业相同的公司。**

（未完待续）

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2007/12/joel_spolsky_talk_at_yale_part_i.html>`__

Evernote

**

Highlight

Remove Highlight

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2007/12/joel_spolsky_talk_at_yale_part_i.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com