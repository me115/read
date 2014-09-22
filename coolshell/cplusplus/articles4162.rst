.. _articles4162:

又一个有趣的面试题
==================

2011年4月2日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

大家还记得前些天的那个\ `火柴棍式的面试题 <http://coolshell.cn/articles/3961.html>`__\ 吗？很有趣吧。下面是我今天在StackExchange上看到的一个\ `有趣的面试题 <http://programmers.stackexchange.com/questions/64132/interesting-interview-question>`__\ 。大家不妨一起来思考一下。问题如下——

有两个相同功能代码如下，\ **请在在A，B，C是什么的情况下，请给出三个原因case
1比case 2快，还有三个原因case 2会比case
1要执行的快。**\ （不考虑编译器优化）

::

    for (i=0; i

    for (i=0; i
    我的第一个反应是——

    case1 要快一些，因为只有一个i++的i
    case2如果要快的话，有一个原因是，A, B, C其中一个需要去先获得一个资源（比如一个锁），在case1下，每次都要去拿这个资源，而case2下，只需要拿一次然后。但这个可能是不对的，因为我无法想出一个相同的语句块放在case 1中会和放在case 2中有差别。（不过可能比较接近了）
    继续思考：这个题有点像是“同步和异步”的问题，case 1是同步，case 2是异步，所以，异步快于同步，也许可以从这个方向出发，写出A, B, C的语句块。
    不过，其要三个原因啊。各位，你们有想法吗？
    —-更新 1—-
    刚才在twitter上与人讨论，发现又有一种情况，case 2要比case 1要快。比如，A, B, C分别访问是不同的内存块（数组），那么case 1就得在不同的内存块上来回切换寻址，而case2则可以连续地访问内存块。访问连续的内存效率要高。尤其是三块大内存。
    —-更新 2—
    正如本贴评论中所说的，CPU的cache也是其中一个因素。大家对底层知识了解的都很不错啊。赞一个。
.. note::
    原文地址: http://coolshell.cn/articles/4162.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com