.. _articles2097:

如何修改微软人体工学键盘的Zoom键
================================

2010年2月7日 `mailper <http://coolshell.cn/articles/author/mailper>`__

如果你不是订阅本站的用户，你很肯能可能是通过搜索引擎的魔力来到本文的。

微软的软件产品咱们暂且不谈，他们生产的键盘鼠标确实很不错。例如，经典的
microsoft natural ergonomic keyboard 4000
（见图）。著名Google工程师博主Matt
Cutts用的就是这个（\ `参考链接 <http://www.mattcutts.com/blog/30-days-no-microsoft-software/>`__\ ）。

可是每个入手该键盘的geek都会觉得，这个弱智的设计师把zoom键放在中间干嘛，应该用来当上下滚轮嘛。

|image0|

无独有偶，该问题已经被先辈们解决，笔者只搜到了\ `英文文章 <http://paininthetech.com/2006/04/29/hack-the-microsoft-natural-4000-keyboard>`__

为了让中文读者方便找到并使用，暂且将关键步骤翻译如下：

#. 下载微软键盘驱动
   `http://www.microsoft.com/hardware/download/download.aspx?category=MK <http://www.microsoft.com/hardware/download/download.aspx?category=MK>`__
#. 找到command.xml文件，应该是在 C:\\Program Files\\Microsoft
   IntelliType Pro\\
#. 编辑command.xml文件（建议之前备份），替换\ **所有** 为ScrollUp” />**,
    所有** 替换为\ **ScrollDown”
   />**\ 用Notepad或者记事本可以实现，应该是10个左右。
#. 重启电脑（貌似这一步不能省）

图例：修改前

|image1|

图例：修改后

|image2|

这样你就可以用Zoom来替代鼠标滚轮了。

.. |image0| image:: /coolshell/static/20140922094454898000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2010/02/keyboard.jpg
.. |image1| image:: /coolshell/static/20140922094454957000.png
   :target: http://coolshell.cn//wp-content/uploads/2010/02/before.png
.. |image2| image:: /coolshell/static/20140922094454992000.png
   :target: http://coolshell.cn//wp-content/uploads/2010/02/after.png
.. |image9| image:: /coolshell/static/20140922094455019000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/2097.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com