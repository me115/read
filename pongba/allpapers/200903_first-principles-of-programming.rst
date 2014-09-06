.. _200903_first-principles-of-programming:

编程的首要原则(s)是什么？
=========================

`mindhacks.cn <http://mindhacks.cn/2009/03/09/first-principles-of-programming/>`__

半年前，JoelOnSoftware和CodingHorror合搞的stackoverflow.com刚上线不久，我兴冲冲地跑过去扔了一个问题：

**你们认为编程的首要原则是什么？**

作为我的\ `学习原则 <http://mindhacks.cn/2008/07/08/learning-habits-part1/>`__\ 的一个实践：\ |important|

    8. 学习一项知识，必须问自己三个重要问题：1. 它的本质是什么。2.
    它的第一原则是什么。3. 它的知识结构是怎样的。

5个月过去了，这个问题到现在还有人回复，我得到了一大堆有意思的答案，忍不住翻译过来与大家分享：

1. 获得\ **最多认同的答案**\ ：

    **KISS – Keep It Simple Stupid**

    **DRY – Don’t Repeat Yourself**

一点不感到意外吧？

注：DRY原则倒是比较好理解和实践的。但KISS原则则是看上去直白，其实实践起来不那么容易的一个原则，因为simple和stupid的定义并不是每个人、在每个场景下都是一致且明显的，一个人的simple可能是另一个人的stupid，一个人的stupid可能是另一个人的unnecessary。一旦一个标准取决于具体场景，事情就不那么简单了。所以我们经常要说“\ `It
depends <http://c2.com/cgi/wiki?ItDepends>`__\ ”。

2. 获得\ **第二认同的答案**\ ：

    **写代码时时刻设想你就是将来要来维护这坨代码的人。**

在这个答案后面有人添加到：

    最好设想你的代码会被一个挥着斧头的精神病来维护。

有人接着又YY道：

    而且这个挥着斧头的精神病还知道你住在哪儿。 (( 事实上后面有人指出这是
    Martin Golding 的一句名言 ))

注：其实这个原则在设计API时也有用：

    **写API时时刻设想你就是要去使用这坨API的人。**

3. **一些众所不一定周知的答案**\ ：

    **先弄清你的问题是什么！**

`弄清问题 <http://www.douban.com/subject/1135754/>`__\ 永远是问题解决过程中的第一步和最重要的一步。

    **代码只是工具，不是手段。**

不知道怎么最好地解决你手头的问题（注：需求、架构、算法，技术选型，etc..），写上一万坨代码也是浪费比特。

    **知道什么时候不该编码**\ 。

（类似条目：YAGNI——“你并不需要编写这坨代码！”，针对你的需求编码，“写你所需”，别做“聪明事”，为一个不确定的未来编码。同时也注意模块化设计，以便能在未来新增需求时无痛扩充系统）

    **永远不要假定你已经了解一切了！**

    **不作没有证据的推论。**

    **想清楚了再编写**\ 。类似条目：\ **如果方案在你脑子里面或者纸上不能工作，写成代码还是不能工作。**

4. 一些众所很可能周知的答案：

    越懒越好。

    过早优化是一切罪恶的根源。

    不要重新发明轮子。

    测试通过前说什么“它可以工作”都是纯扯淡。

    了解你的工具。

    一切以用户需求为导向。

    利用分治、抽象，解开子问题之间的耦合。

5. **最幽默的答案**\ ：

    **咖啡进，代码出**\ 。（Coffee in, Code out） (( 参见 `Garbage in,
    Garbage
    out <http://en.wikipedia.org/wiki/Garbage_in,_garbage_out>`__. ))

最后，整个问题的 thread
在\ `这里 <http://stackoverflow.com/questions/159176>`__\ 。

`mindhacks.cn <http://mindhacks.cn/2009/03/09/first-principles-of-programming/>`__

.. |important| image:: /pongba/static/20140906161151652000.png
   :target: http://mindhacks.cn/wp-content/uploads/2009/03/important.png

.. note::
    原文地址: http://mindhacks.cn/2009/03/09/first-principles-of-programming/ 
    作者: 刘未鹏 

    编辑: 木书架 http://www.me115.com