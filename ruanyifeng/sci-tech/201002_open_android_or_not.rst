.. _201002_open_android_or_not:

Android，开源还是封闭？
==========================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/02/open_android_or_not.html>`__

满大街都在谈论Android。

它是当红炸子鸡。许多人觉得，iPhone将受到它的强力挑战。

我也曾经对它充满了期待，但是后来的事态发展，令我改变了看法。前几天，我就在网志上写了自己的\ `担忧 <http://www.ruanyifeng.com/blog/2010/02/samsung_omnia_ii_i8000_part_i.html>`__\ ：

    “首先，Android应用程序只能用java语言开发，莫非所有的应用程序都运行在一个巨大的虚拟机上？（【更正】网友留言指出，2009年6月Android发布NDK工具包，支持C/C++语言编程，不过性能不如SKD工具包中的Java语言。
    ）

    其次，Google对Android采用了一种全面霸权式的管理，完全不是其他开源软件的开发方式，一切都由Google说了算，很多地方是黑箱，外界不得而知。”

没有想到，仅仅过了两天，担忧就变成了现实。Linux Kernel的维护者\ `Greg
Kroah-Hartman <http://en.wikipedia.org/wiki/Greg_Kroah-Hartman>`__\ 宣布，\ `将Android
代码从 Linux kernel
代码库中删除 <http://linux.slashdot.org/story/10/02/03/1932222/Android-and-the-Linux-Kernel-Community>`__\ 。这意味着，Linux
Kernel的开发小组不认可Android的贡献，两者产生了冲突。

消息公布以后，外界普遍觉得惊讶和可惜。好不容易，才有了一个这么受欢迎的开源手机系统，应该齐心协力、共同开发才对，为什么要”窝里斗”呢？到底是什么矛盾，使得Linux
Kernel小组剔除Android代码呢？

Greg
Kroah-Hartman写了一篇详细的\ `文章 <http://www.kroah.com/log/linux/android-kernel-problems.html>`__\ ，解释这个决定。下面就来看看，他是怎么说的，以及Android到底是一个什么样的系统。

在这之前，你最好知道Greg Kroah-Hartman是谁。他是目前Linux
Kernel的核心开发人员，负责stable软件包的发布。就是说，每一个新版本的Linux
Kernel，都是经过他的手流出来的。此外，他还负责硬件驱动的部署。而他的手机就是HTC
G1，每天都在使用。所以，他是绝对有资格谈论这个问题的，他的看法代表了Linux社区对Android的看法。

首先，他指出Android和其他的Linux发行版不一样：

    “Google has taken the Linux kernel, and nothing else from a
    “traditional” Linux system.

    Google只用了kernel，别的东西都没用。”

这就是说，与Ubuntu、Debian、Redhat这样的传统Linux发行版相比，只有系统的底层结构是一样的，其他东西在Android里都不一样，尤其是程序员的编程接口是完全不同的。因此，Android应用程序都必须重新写过，现存的Linux程序无法移植上去。所以，从严格意义上说，Android是一种全新的系统，它与Linux的距离，比Mac
OS与Linux的距离还要远。

然后，Greg Kroah-Hartman肯定了Android这样做的积极意义：

    “Android also solves the problem that the phone manufacturers had
    been having for many years: a free version of Java and a unified
    application layer that programmers can write to that will work on
    all phone platforms that integrate it.

    它解决了长期令手机制造商头痛不已的问题：业界缺乏一个开源的Java虚拟机，以及统一的应用程序接口。现在，程序员只要写一次程序，就能在各种手机硬件平台之上使用。”

这段话解释了，为什么Android的应用程序，都必须用Java语言开发。因为不这样做的话，没法让程序做到硬件无关。

且慢，这真的是理由吗？传统的Linux系统，也并不依赖特定的硬件啊！只要把源代码根据不同的平台，分别编译一下，同一个程序不也照样可以在不同的硬件架构、不同的Linux发行版中使用吗？

那么，Android只采用kernel、只允许用java编程的真正原因，到底是什么？

台湾的科技网志\ `MMDays <http://mmdays.com/2008/10/11/android-%E6%B7%BA%E6%8E%A2%E4%BA%8C%EF%BC%9A%E7%B3%BB%E7%B5%B1%E6%9E%B6%E6%A7%8B/>`__\ 一语道破真相：

    “Linux kernel 的版权是 GPL。

    这下问题来了：如果你是硬件厂商，希望你的硬件能在 Linux kernel
    下运作，那么就必须要有驱动程序。如果驱动程序的程序代码公开，等于硬件规格也公开的差不多了。许多厂商不愿意这么做，所以就提供编好的驱动程序，但不提供原始码。

    Android
    的重点就是商业应用，Google采用了一些手法来绕过这问题。他们把驱动程序移到
    “userspace”，也就是说，把驱动程序变成在 Linux kernel
    上头跑，而不是一起跑的东西，这样就可以避过GPL。然后，在 kernel
    这边开个小门，让本来不能直接控制到硬件的 “userspace”
    程序也可以碰得到，这样只要把”开个小门”的程序代码公布就行啦。”

看明白了吗？

这段话的意思是说，Google玩了一个花招，在kernel和应用程序之间，自己做了一个中间层，这样就既不违反GPL许可，又能不让外界看到厂商的硬件驱动和应用程序的源码。

里面的关键在于，Kernel和Android的许可证不一样，前者是GPL许可证，后者是Apache
Software
License（简称ASL）许可证。GPL许可证规定，对源码的任何修改都必须开源，所以Android开源了，因为它修改了Kernel。而ASL许可证规定，可以随意使用源码，不必开源，所以建筑在Android之上的硬件驱动和应用程序，都可以保持封闭。为了得到更多厂商的支持，Google有意选择了这样做，并且特意修改Kernel，使得原本应该包括在kernel中的某些功能，都被转移到了userspace之中，因此得以避开开源。

这样做或许有利于推广Android，吸引厂商和软件开发商的加入，但是Google也放弃了构建一个真正开源的手机系统的机会，从而也就不能获得由全世界程序员提供智慧、分享代码、推动创新的好处。关于许可证问题的深入讨论，请阅读Ryan
Paul的文章\ `《Why Google chose the Apache Software License over GPLv2
for
Android》 <http://arstechnica.com/old/content/2007/11/why-google-chose-the-apache-software-license-over-gplv2.ars>`__\ 。

Google的这种做法，直接后果就是给Linux Kernel带来了麻烦。Greg
Kroah-Hartman清楚地说出了自己的不满。

    “…any drivers written for Android hardware platforms, can not get
    merged into the main kernel tree because they have dependencies on
    code that only lives in Google’s kernel tree, causing it to fail to
    build in the kernel.org tree.

    所有为Android写的硬件驱动，都不能合并入kernel。因为它们只在Google的代码里有效，在kernel里根本没法用。

    Because of this, Google has now prevented a large chunk of hardware
    drivers and platform code from ever getting merged into the main
    kernel tree. Effectively creating a kernel branch that a number of
    different vendors are now relying on.

    由于这个原因，Google也从不把大量的硬件驱动程序和平台源码向kernel提交。实际上，它创造出了一个kernel的分支，大量的开发者都依赖那个分支。”

这就是Android干的事情：它修改了Kernel，但是又不提供修改的细节，自己搞了一个封闭的系统。说得难听一点，它利用了开源社区，要求开源社区为它做贡献，却又不愿提供回报。

所以，Linux Kernel就把Android踢出去了，真是再正常不过了。

人们有权利质疑，Android这样的哲学是否正确？是否符合Google”不作恶”的口号？如果Android继续这样封闭下去，那么开源社区为什么要为它免费制作软件呢？因为我又不是在为开源社区服务，而是在为Google服务。既然这样的话，那还不如去支持iPhone呢，至少能在软件商店里多卖一点钱，而且乔布斯看上去也更酷一点。

`slashdot <http://linux.slashdot.org/story/10/02/03/1932222/Android-and-the-Linux-Kernel-Community>`__\ 上有很多关于此事的讨论。有人指出：

    “Google自己的网站，与微软的网站一样封闭。它开源出来的东西，都是根据GPL许可证不得不开源的。”

好吧，姑且不谈Google本身，因为它至少不要求外界提供支持。但是Android不一样，你不能假装成开源系统，骗取社区的支持，然后又干着封闭系统的勾当。以你的实力，不用Linux
Kernel，自己开发一个Google
Kernel，想必也不是难事。要是这样做，任何人都不会有非议。可是，既然你选择了Linux
Kernel，并且大张旗鼓地宣传，那么你奉献出什么呢？难道你的奉献就是给Kernel开一个口子吗？

Google必须做出改变。正如Greg Kroah-Hartman最后的呼吁：

    “I really don’t know. Google shows no sign of working to get their
    code upstream anymore.

    我真的不知道未来。Google看上去没有任何改变代码的迹象。

    I do hold out hope that Google does come around and works to fix
    their codebase to get it merged upstream to stop the huge blockage
    that they have now caused in a large number of embedded Linux
    hardware companies.

    我确实希望Google做出改变，把它的代码合并进我们的代码，弥补已经出现的代码分裂。

    I’ve privately offered in the past to help this work get done, and
    am doing again here publicly. But I need the help of the Google
    developers to make it happen, without them, nothing can change.

    我私底下已经说过，我愿意帮助完成这项工作，在这里我再次公开这样说。但是如果没有Google程序员的加入，什么也不会发生。”

Android必须变成一个真正的开源系统。如果像现在这样封闭下去，就会被开源社区抛弃，就一定不会成功，即使有Google的支持。

**UPDATE ONE**

liufeng针对此文，写了一篇很好的\ `评论 <http://www.cnliufeng.com/blog/2010/02/linux-and-android.html>`__\ ，推荐阅读。

我接受他的批评，我确实有点感情用事。主要是因为对Google有太大的期望，所以不能接受它现在的这种做法。

这一次，也许不能说Google做错了什么，毕竟都符合GPL许可证的要求。但是代价也是巨大的——它放弃了创造未来的机会。我坚信，未来主流的手机操作系统一定是开源的，就像我坚信未来Linux一定胜过Windows一样。现在，既然Google放弃了这个选择，那么只能等待其他人来做出开源的手机系统了。这也意味着，我们还要在黑暗中等待更久。

**UPDATE TWO**

Greg
Kroah-Hartman原文中有一些关于技术的部分，由于我不太懂，就没翻译出来。网友\ `黑日白月 <http://linuxtoy.org/archives/android-linux.html#comment-138679>`__\ 做了意译和点评。

    简单的来讲，Android 的硬件驱动依赖在 Google
    代码树里的东西，于是尽管大多数厂商都将它们的驱动反馈给社区了，但是对
    Google 代码树的依赖导致它们无法并入主线(merge into mainline)。而
    Google 代码树一直没并入主线是由于 Android
    平台安全架构模型需要额外的钩子以及完全不同的帧缓存驱动。

    这次在 2.6.33 主线中把 Android
    部分清理掉是由于厂商贡献的这部分代码在离开 Google
    的代码树之后对其他嵌入式 Linux 没有用处，干脆从主线中除掉好了……

    这跟前段时间 Linus 指责 Red Hat 把 Nouveau
    并入主线的积极性不高一样，最后 Red Hat 也是把 Nouveau 并入 2.6.33
    的主线了么……

    没有并入主线对于社区和厂商都不利，社区得不到驱动程序的扩展，厂商也得不到内核新特性的改善。但是并不是所有模块在一开始的时候都是并入主线的，总是要发展到某个相对成熟的阶段或者解决了潜在的授权问题后才并入的。总之并入主线对双方都有利，这个问题反应这次
    Google 的并入主线积极性不高（不代表不开源），社区打它屁屁了……

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/02/open_android_or_not.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com