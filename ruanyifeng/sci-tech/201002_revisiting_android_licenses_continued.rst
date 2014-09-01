.. _201002_revisiting_android_licenses_continued:

再谈Android的许可证（续）
============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/02/revisiting_android_licenses_continued.html>`__

写\ `前一篇网志 <http://www.ruanyifeng.com/blog/2010/02/revisiting_android_licenses.html>`__\ 时，我参考了\ `Ryan
Paul <http://arstechnica.com/author/ryan-paul/>`__\ 的文章。

他是资深Linux程序员和评论者。他对Android许可证的评论，是我见到的最准确、最通俗易懂的介绍。当时，我翻译了一些片段，打算在自己的文章中引用，但是后来没用上。我觉得不甘心，于是今天就把全文译出，贴在下面，希望让更多的朋友看到。

如果你对GPL、ASL、BSD这一类的许可证名字，只有一些模模糊糊的概念，搞不清楚它们之间的区别。那么，我强烈推荐你阅读此文，读完后，你就会对开源软件的许可证，有一个基本的认识了。

值得指出的是，此文写于2007年，当时Google刚刚宣布Android项目，代码还没有完成，工程样机更是没有，外界只能凭几句文字叙述，猜测这个系统的样子。但是，Ryan
Paul就是有这个本领，只看许可证选择，就判断出Android的开发模式。事实证明，他的判断完全正确，除了一点：他没有料到，Google会修改Linux内核，故意造成两者不兼容。

（图片说明：自由软件基金会的标志）

（图片说明：Apache基金会的标志）

（图片说明：FreeBSD基金会的标志）


=================================

**Why Google chose the Apache Software License over GPLv2 for Android**

**为什么Android不是GPL许可证？**

作者：Ryan Paul

译者：阮一峰

发表日期：2007年11月6日

原文网址：\ `http://arstechnica.com/old/content/2007/11/why-google-chose-the-apache-software-license-over-gplv2.ars <http://arstechnica.com/old/content/2007/11/why-google-chose-the-apache-software-license-over-gplv2.ars>`__

| 
|  Google finally entered the mobile software market by turning the 2005
acquisition of Android into the Open Handset Alliance.

Google终于进入了手机市场。2005年，它收购了Android。在此基础上，现在，它组建了”开放手机联盟”（Open
Handset Alliance）。

Google hopes to promote third-party mobile software development and
foster a broad developer community on top of Android’s Linux-based
mobile platform.

Android是一种Linux内核的手机操作系统。Google希望，这会吸引来第三方软件开发者，建立起一个大规模的开发者社区。

In the wake of Google’s announcement, one topic that has been discussed
by some members of the open-source software community is the
significance of Google’s licensing choice.

但是，此事公布后不久，开源软件社区就议论纷纷，大家在讨论Google为Android选择的许可证。

Although the underlying Linux kernel is licensed under version 2 of the
Free Software Foundation’s General Public License (GPLv2), much of the
user-space software infrastructure that will make up the Open Handset
Alliance’s platform will be distributed under version 2 of the Apache
Software License (ASL).

Linux内核的许可证，是自由软件基金会的GPL许可证第二版。但是，”开放手机联盟”的主要代码，却是Apache许可证（ASL）第二版。

This raises certain questions about Google’s goals in the mobile space
and the nature of the third-party application ecosystem that will emerge
around the platform.

这使得有人怀疑Google的动机。它的目标到底是什么？Android平台上，到底会有怎样的第三方软件？

ASL, which is widely used in the open-source software community and has
been approved by the Open Source Initiative, is a permissive license
that is conducive to commercial development and proprietary
redistribution. Code that is distributed under the ASL and other
permissive licenses can be integrated into closed-source proprietary
products and redistributed under a broad variety of other terms.

ASL许可证被开源软件广泛使用，并且得到了”开放源码促进会”（Open Source
Initiative）的认可。它是一种不设限的许可证（permissive
license），允许软件的商业性开发和垄断式发布。以ASL发布的代码，可以被合并入闭源的专有软件（proprietary
product），并且在各种各样的限制性条件下发布。

Unlike permissive open-source licenses, “copyleft” licenses (such as the
GPL) generally impose restrictions on redistribution of code in order to
ensure that modifications and derivatives are kept open and distributed
under similar terms.

与ASL不同，GPL则是一种Copyleft许可证。它对代码的发布做出了限制，规定所有对源码的修改和衍生，都必须公开，并且以相似的许可证发布。

Permissive licenses like the ASL and BSD license are preferred by many
companies because such licenses make it possible to use open-source
software code without having to turn proprietary enhancements back over
to the open source software community. These licenses encourage
commercial adoption of open-source software because they make it
possible for companies to profit from investing in enhancements made to
existing open-source software solutions. That potential for proprietary
investment on top of an open stack is most likely what inspired Google
to adopt the Apache Software License for its mobile platform.
Availability of Android under the ASL will ensure that a broader number
of companies will be able to adopt the platform and build on top of it
without having to expose the inner workings of proprietary technologies
that give them a competitive advantage.

许多软件公司更愿意采用不设限的许可证（比如ASL和BSD），因为这使得它们既可以使用开源软件，又不用向开源社区公开对软件所做的修改。所以，ASL和BSD鼓励了开源软件的商业性使用，使得软件公司愿意对开源软件投资，因为这些公司可以从中获利。这种在开源基础上吸引商业投资的潜力，很可能是Google为自己的手机平台选择ASL许可证的最大原因。将Android置于ASL之下，可以确保许多商业性公司会接受这个平台，并且在它上面使用自己的专有技术。

Although using a permissive license like ASL is the best way to build
support for the Android platform, critics argue that Google has
sacrificed an opportunity to encourage greater openness in the broader
mobile software space. If Android was distributed under the GPLv2,
companies building on top of the platform would have to share their
enhancements, which could theoretically lead to widespread sharing of
code and a more rapid acceleration of mobile software development.

虽然ASL确实是保证Android获得支持的最好方法，但是批评者认为，Google这样做的代价，是丧失了创造一个更开放的手机软件平台的机会。如果Android的许可证是GPLv2，那么在它上面做开发的那些公司，将不得不公开对系统所做的改进，理论上就会导致代码被更广泛地分享，因而手机软件的开发也会更快速地进步。

The counterargument is that distributing Android under a copyleft
license could potentially limit the evolution of the mobile software
ecosystem by discouraging commercial development on top of the platform.
Proprietary mobile software development companies that integrate Android
into their technologies would have to dramatically change their business
models if they aren’t given the ability to keep their enhancements
proprietary.

另一些人不同意这种看法。他们认为如果Android选择copyleft许可证，会使商业性公司不愿意介入开发，从而使系统本身的发展困难重重。如果那些公司没有办法保护自己的专有技术不公开，那么即使它们愿意采用Android平台，也必须急剧地改变经营模式，而这是有风险的。

It is important to note that the ASL is only being applied to the
assortment of user-space platform components that make up Android. The
kernel itself is still licensed under the GPLv2, and third-party
software that runs on top of the platform can be distributed under
pretty much any license, including commercial and copyleft licenses.

有一点是不能忽视的，那就是只有Android的userspace部分是ASL许可证。系统的内核依然是GPLv2许可证。而运行在系统上方的第三方软件，可以用任何许可证发布，包括商业性许可证和copyleft许可证。

It is also important to note that, although the ASL was not compatible
with previous versions of the GPL, it is entirely compatible with the
GPLv3. This means that code distributed under the ASL can be
incorporated into GPLv3 software. As a result, developers can choose to
distribute Android derivatives under the GPLv3 in order to ensure that
further development on top of their own enhancements remains open.

还有一点也很重要，那就是虽然ASL与GPLv2不兼容，但是它与GPLv3完全兼容。这意味着，在ASL下发布的代码，可以被用于GPLv3许可证的软件。因此，程序员可以选择将Android程序在GPLv3下发布，这样就能保证他们作品的进一步开发，将始终是开源的。

Ultimately, the decision to use the ASL is sensible. Although it would
be beneficial to all if Google were to use Android licensing to further
open the market, that likely would have stifled adoption of the platform
by handset makers.

最终来说，Google选择ASL是情有可原的。虽然Android如果在GPL许可下发布，会使所有人得利，但那样也会阻碍这个系统被手机厂商采用。

When it comes right down to it, the handset makers are the developers
who are most significantly affected by the Android license, since they
are the primary distributors of mobile phone platforms. The ASL will
allow individual handset makers to develop proprietary customizations
for the platform as needed to accommodate the unique technologies in
their individual products.

如果单就手机厂商而言，他们才是受Android许可证影响最大的开发者，因为他们是手机平台主要的发布渠道。ASL允许手机厂商对平台进行改造，使得Android变得好像他们的独家产品一样。

Third-party software developers who are building applications on top of
Android will largely be unaffected by Google’s licensing decision since
the individual applications can be distributed under their own licenses.

而第三方的软件开发者，总体上不受Google许可证选择的影响，因为他们可以为自己的软件选择任何的许可证。

Another point worth noting is that Linux-based mobile platforms created
by other mobile technology coalitions like the LiMo Foundation also
facilitate mixing proprietary and open software.

还有一个值得注意的地方是，其他Linux核心的手机平台，比如LiMo，也是闭源软件和开源软件的混合。

As more details emerge and more source code becomes available, it’s
likely that third-party developers and handset makers will eagerly flock
to Android in order to benefit from the ecosystem that Google is
creating.

随着更多的细节和更多的源码被公布，手机厂商和第三方开发者，很可能会热切地投入Android的怀抱，享受Google创造的这个平台。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/02/revisiting_android_licenses_continued.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com