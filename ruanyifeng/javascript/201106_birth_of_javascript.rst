.. _201106_birth_of_javascript:

Javascript诞生记
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/06/birth_of_javascript.html>`__

1.

二周前，我谈了\ `一点 <http://www.ruanyifeng.com/blog/2011/06/designing_ideas_of_inheritance_mechanism_in_javascript.html>`__\ Javascript的历史。

今天把这部分补全，从历史的角度，说明Javascript到底是如何设计出来的。

只有了解这段历史，才能明白Javascript为什么是现在的样子。我依据的资料，主要是\ `Brendan
Eich的自述 <http://brendaneich.com/2008/04/popularity/>`__\ 。

2.

`上一篇文章 <http://www.ruanyifeng.com/blog/2011/06/designing_ideas_of_inheritance_mechanism_in_javascript.html>`__\ 写道：

    “1994年，网景公司（Netscape）发布了Navigator浏览器0.9版。这是历史上第一个比较成熟的网络浏览器，轰动一时。但是，这个版本的浏览器只能用来浏览，不具备与访问者互动的能力。……\ **网景公司急需一种网页脚本语言，使得浏览器可以与网页互动。**\ ”

网页脚本语言到底是什么语言？网景公司当时有两个选择：一个是采用现有的语言，比如Perl、Python、Tcl、Scheme等等，允许它们直接嵌入网页；另一个是发明一种全新的语言。

这两个选择各有利弊。第一个选择，有利于充分利用现有代码和程序员资源，推广起来比较容易；第二个选择，有利于开发出完全适用的语言，实现起来比较容易。

到底采用哪一个选择，网景公司内部争执不下，管理层一时难以下定决心。

3.

就在这时，发生了另外一件大事：1995年Sun公司将Oak语言改名为Java，正式向市场推出。

Sun公司大肆宣传，许诺这种语言可以”一次编写，到处运行”（Write Once, Run
Anywhere），它看上去很可能成为未来的主宰。

网景公司动了心，决定与Sun公司结成联盟。它不仅允许Java程序以applet（小程序）的形式，直接在浏览器中运行；甚至还考虑直接将Java作为脚本语言嵌入网页，只是因为这样会使HTML网页过于复杂，后来才不得不放弃。

**总之，当时的形势就是，网景公司的整个管理层，都是Java语言的信徒，Sun公司完全介入网页脚本语言的决策。**\ 因此，Javascript后来就是网景和Sun两家公司一起携手推向市场的，这种语言被命名为”Java+script”并不是偶然的。

4.

此时，34岁的系统程序员Brendan Eich登场了。1995年4月，网景公司录用了他。

Brendan
Eich的主要方向和兴趣是函数式编程，网景公司招聘他的目的，是研究将Scheme语言作为网页脚本语言的可能性。Brendan
Eich本人也是这样想的，以为进入新公司后，会主要与Scheme语言打交道。

仅仅一个月之后，\ **1995年5月，网景公司做出决策，未来的网页脚本语言必须”看上去与Java足够相似”，但是比Java简单，使得非专业的网页作者也能很快上手。**\ 这个决策实际上将Perl、Python、Tcl、Scheme等非面向对象编程的语言都排除在外了。

Brendan Eich被指定为这种”简化版Java语言”的设计师。

5.

但是，他对Java一点兴趣也没有。为了应付公司安排的任务，他只用10天时间就把Javascript设计出来了。

由于设计时间太短，语言的一些细节考虑得不够严谨，导致后来很长一段时间，Javascript写出来的程序混乱不堪。如果Brendan
Eich预见到，未来这种语言会成为互联网第一大语言，全世界有几百万学习者，他会不会多花一点时间呢？

总的来说，他的设计思路是这样的：

    　　（1）借鉴C语言的基本语法；

    　　（2）借鉴Java语言的数据类型和内存管理；

    　　（3）借鉴Scheme语言，将函数提升到”第一等公民”（first
    class）的地位；

    　　（4）借鉴`Self语言 <http://en.wikipedia.org/wiki/Self_(programming_language)>`__\ ，使用基于原型（prototype）的继承机制。

所以，\ **Javascript语言实际上是两种语言风格的混合产物——（简化的）函数式编程+（简化的）面向对象编程。**\ 这是由Brendan
Eich（函数式编程）与网景公司（面向对象编程）共同决定的。

6.

多年以后，Brendan Eich还是看不起Java。

他说：

    “Java（对Javascript）的影响，主要是把数据分成基本类型（primitive）和对象类型（object）两种，比如字符串和字符串对象，以及引入了Y2K问题。这真是不幸啊。”

把基本数据类型包装成对象，这样做是否可取，这里暂且不论。Y2K问题则是直接与Java有关。根据设想，Date.getYear()返回的应该是年份的最后两位：

    　　var date1 = new Date(1999,0,1);

    　　var year1 = date1.getYear();

    　　alert(year1); // 99

但是实际上，对于2000年，它返回的是100！

    　　var date2 = new Date(2000,0,1);

    　　var year2 = date2.getYear();

    　　alert(year2); // 100

如果用这个函数生成年份，某些网页可能出现”19100”这样的结果。这个问题完全来源于Java，因为Javascript的日期类直接采用了java.util.Date函数库。Brendan
Eich显然很不满意这个结果，这导致后来不得不添加了一个返回四位数年份的Date.getFullYear()函数。

如果不是公司的决策，Brendan
Eich绝不可能把Java作为Javascript设计的原型。作为设计者，他一点也不喜欢自己的这个作品：

    “与其说我爱Javascript，不如说我恨它。它是C语言和Self语言一夜情的产物。\ **十八世纪英国文学家约翰逊博士说得好：’它的优秀之处并非原创，它的原创之处并不优秀。’**\ （the
    part that is good is not original, and the part that is original is
    not good.）”

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/06/birth_of_javascript.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com