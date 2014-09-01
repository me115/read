.. _201110_characters_per_line:

每行字符数（cpl）的起源
==========================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/10/characters_per_line.html>`__

前几天，我收到网友小龙的Email。

他想与我讨论一个问题：

    **“各种计算机语言的编码风格，有的建议源码每行的字符数（characters
    per
    line）不超过72个，还有的建议不超过80个，这是为什么？区别在哪里？怎么来的？”**

我一下子就被问住了。

命令行状态下，终端窗口的显示宽度，默认是80个字符，这个我早就知道，但是并不清楚原因；至于72个字符，更是从未注意过。

幸好，世界上还有Wikipedia，我在里面找到了\ `答案 <http://en.wikipedia.org/wiki/Characters_per_line>`__\ 。

每行72个字符的限制，来源于打字机。上图是20世纪60年代初，非常流行的IBM公司生产的\ `Selectric <http://en.wikipedia.org/wiki/IBM_Selectric>`__\ 电动打字机。

当时，美国最通用的信笺大小是8.5英寸x11英寸（215.9 mm ×
279.4 mm），叫做\ `US
Letter <http://en.wikipedia.org/wiki/Letter_(paper_size)>`__\ 。打字的时候，左右两边至少要留出1英寸的页边距，因此每行的长度实际为6英寸。打字机使用等宽字体（monospaced）的情况下，每英寸可以打12个字符，就相当于一行72个字符。

早期，源码必须用打字机打出来阅读，所以有些语言就规定，每行不得超过72个字符。直到今天，\ `RFC <http://www.ietf.org/download/rfc-index.txt>`__\ 文档依然采用这个规定，因为它从诞生起就采用打字稿的形式。

20世纪70年代，显示器出现了。它的主要用途之一，是将\ `打孔卡 <http://en.wikipedia.org/wiki/Punched_card>`__\ （punched
card）的输入显示出来。当时，最流行的打孔卡是IBM公司生产的80栏打孔卡，每栏为一个字符，80栏就是80个字符。

上图是一张Fortran语言的源码填写单，一共有80栏，程序员在每一栏选择想要输入的字符，最多为80个字符。

然后，用机器自动生成打孔卡，在每栏选定的位置打一个孔。

计算机读取打孔卡以后，把每个孔转换为相应的字符。如果显示器每行显示80个字符，就正好与打孔卡一一对应，终端窗口的每行字符数（CPL）就这样确定下来了。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/10/characters_per_line.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com