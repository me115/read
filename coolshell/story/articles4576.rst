.. _articles4576:


    =
    选择二：真正搞清楚为什么会错，并且有分析地修改他（理解问题才能真正解决之，并且，只有没有“魔法发生”的时候你才可以来争论）

    Now, the whole analytic approach (aka “computer sciency” approach),
    where you can actually think about the problem without having any
    pesky “reality” impact the solution is obviously the one we tend to
    prefer. Sadly, it’s seldom the one we can use in reality when it
    comes to things like resource allocation, since we end up starting
    off with often buggy approximations of what the actual hardware is
    all about (ie broken firmware tables).

    现在，整个分析方法（亦称作“计算机科学”的方法）应该是你可以在没有在外界干扰下真正思考这个问题而得到的解决方案，这很明显是我们推崇的。只有在极罕见地情况下我们可以在有外界干扰下分析这种资源分配的事，因为我们只有了解倒底是什么样的硬件，我们才能最终远离bug（如：错误的固件表）

    So I’d love to know exactly why one random number works, and why
    another one doesn’t. But as long as we do \_not\_ know the “Why” of
    it, we will have to revert.

    所以，我希望你能知道为什么一个随机数能行，而另一个不行。只要我们不知道，那么我们就不得和回滚整个改动。

    It really is that simple. It’s \_always\_ that simple.

    这真的是很简单，而且这\ **一直**\ 是那么简单。

    So the numbers shouldn’t be “magic”, they should have real
    explanations. And in the absense of real explanation, the model that
    works is “this is what we’ve always done”. Including, very much, the
    whole allocation order. Not just one random number on one random
    machine.

    所以，那些数不应该是“magic”的，他们应该有真正的说明。在有真正的说明的情况下，我们的开发模式才会工作。其包括了整个分配顺序。不只是那个在任意机器上的随机数。

    Linus

后面的事不用说了。我没有想到Linux
内核组会有像Yinghai这样工作的方式，毕竟这是一个黑客级的开发团队。我个人对这个乱写代码的人执零容忍的态度，不管你干过什么，不管你哪里毕业的，不管你简历怎么样，不求甚解随意写代码的人我无法接受。我不知道Yinghai
Lu会怎么样想，他/她会像我在“\ `程序员那些悲催的事儿 <http://coolshell.cn/articles/3980.html>`__\ ”中谈我经历那样知耻而后勇吗？能得到Linus的教导真是一件很不错的事。虽然，Linus教导的这些东西，都应该是程序员最最最基本的技能。\ **fix
bug一定要fix在root
cause上啊**\ ，\ **了解一个问题，不但要知其然，还要知其所以然啊**\ ，这都是老生长谈了。本站有很多提高程序员能力的文章，比如，\ `这篇 <http://coolshell.cn/articles/222.html>`__\ ，\ `这篇 <http://coolshell.cn/articles/1007.html>`__\ ，还有\ `这篇 <http://coolshell.cn/articles/2606.html>`__\ 。

各位朋友，我真心希望你能从这个小插曲中明白点什么。

**—– 更新2011/04/27**—–

从本贴的回复中可以看到有朋友说如果时间紧，没有办法只能在不求甚解的地去fix
bug，因为老板催。我认为这是老板的“急功近利”的问题。我想和大家说一下，你得想清楚你属于下面那种人：

#. 你的老板给你压力，让你不得不乱fix，
#. 你认同只要时间紧bug是可以乱fix的。

如果你属于1），那我觉得还情由可原，这是管理问题。但这不能成为你对乱fix
bug的理由。一般这种问题怎么解决：\ **首先，给一个hot
fix去救火，然后，有时间去调查root
cause，最后经过分析和测试，给出一个final 的 offical
fix**\ 。这就是应急的做法，根本不存在什么可以乱fix bug的做法。

如果你属于2），那么我只能“过激”地说你没有成为程序员的资质！

另外，\ **快速地fix bug，并不等于，不求甚解的fix
bug**\ 。大家不要把这两件事等同。

 

**（请勿用于商业用途，转载时请注明作者和出处）**

.. |image6| image:: /coolshell/static/20140922113331261000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/4576.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com