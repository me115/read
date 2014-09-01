.. _200806_firebug_tutorial:

Firebug入门指南
==================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/06/firebug_tutorial.html>`__

|firebug01.png|

据说，对于网页开发人员来说，\ `Firebug <http://www.getfirebug.com>`__\ 是Firefox浏览器中最好的插件之一。

我最近就在学习怎么使用Firebug，网上找到一篇针对初学者的\ `教程 <http://www.evotech.net/blog/2007/06/introduction-to-firebug/>`__\ ，感觉比较有用，就翻译了出来。


=================

**Firebug入门指南**

作者：Estelle Weyl

| 原文网址：\ `http://www.evotech.net/blog/2007/06/introduction-to-firebug/
 <http://www.evotech.net/blog/2007/06/introduction-to-firebug/>`__
|  译者：阮一峰

本文是Firebug的一个概览，并不对它的所有特性进行详尽解释。不过，本文的内容对一个新手来说，应该是足够了。

目录

| 一、安装Firebug 二、打开和关闭Firebug 三、Firebug窗口概览
四、随时编辑页面 五、用Firebug处理CSS 六、盒状模型 七、评估下载速度
八、DOM 九、Javascript调试
|  十、AJAX
|  十一、附注

| 
| **一、安装Firebug**

Firebug在Firefox浏览器中运行。另外有一个Firebug
lite版本，可以通过javascript调用，包含在页面中，从而在其他非Firefox浏览器中使用。本文不涉及这个版本。

安装Firebug，请访问\ `Firebug下载页面 <http://www.getfirebug.com/>`__\ 。点击该页面右边栏中部巨大的橙黄色按钮即可。你也可以在Mozilla的\ `FireFox
Add-ons <https://addons.mozilla.org/firefox/addon/1843>`__\ 站点下载它。安装后只要重新启动FireFox，就可以使用了。

如果你已经安装过了，那么请检查是否更新到了最新版本。打开Firefox的”Tools”菜单，选择”Add-ons”命令，然后在弹出窗口中点击左下角的”Find
Updates”按钮。

**二、打开和关闭Firebug**

在Firebug网站上，可以找到它的\ `快捷键设置 <http://www.getfirebug.com/keyboard.html>`__\ 。我最常使用以下三种方法：

    \*
    打开Firebug：按F12，或者点击浏览器状态栏右边的\ |greencheck.gif|\ 绿色标志。

    |firbug03.gif|

    \*
    关闭Firebug：按F12，或者点击浏览器状态栏右边的\ |greencheck.gif|\ 绿色标志，或者点击Firebug窗口右上角的\ |redx.gif|\ 红色关闭标志。

    \*
    在单独窗口中打开Firebug：点击firebug窗口右上角的\ |uparrow.gif|\ 红色箭头标识，或者使用Ctrl+F12/⌘+F12按钮。

Firebug的相关设置：

    \*
    固定Firebug在新窗口打开：先打开firebug，点击左上角的bug标志，选择options菜单中的”Always
    Open in New Window”设置。

    \* 增加/缩小字体大小：先打开firebug，点击左上角的bug标志，选择”Text
    Size”命令。每次字体变化的幅度非常小，你可能需要使用多次。

    |firebug04.gif|

    \* 限制只对某些站点使用Firebug：先右击浏览器状态上的green check
    mark标志，选择”disable
    Firebug”命令。然后，再右击这个已经变灰的标志，选择”Allowed
    Sites…”命令，增加允许Firebug生效的域名。

    |firebug02.gif|

**三、Firebug窗口概览**

    \* Console标签：
    主要使用javascript命令行操作，显示javascript错误信息，在底部的»>提示符后，你可以自己键入javascript命令。

    \* HTML标签：
    显示HTML源码，并且像DOM等级结构那样，每行之前有缩进。你可以选择显示或不显示某个子节点。

    \*
    CSS标签：浏览所有已经装入的样式表，可以当场对其修改。在Firebug窗口上部，”edit”命令的旁边，有一个本页面中所有样式表的下拉列表，你可以选择一个样式表进行浏览。

    |firebug07.gif|

    \* Script标签：
    显示javascript文件及其所在页面。在Firebug窗口上部，”inspect”命令的旁边，有一个本页面中所有Javascript文件的下拉列表，你可以选择一个进行浏览。你可以在javascript命令中，设置断点（breakpoint）及其出现的条件。

    \* DOM标签：
    显示所有的页面对象和window物体的属性。因为在javascript中，所有变量都是window物体的属性，所以Firebug会显示所有变量和它们的值。

    \*
    Net标签：显示本页面涉及的所有下载，以及它们各自花费的时间，各自的HTTP请求头信息和服务器响应的头信息。XHR标签对AJAX调试很有用。

**四、随时编辑页面**

在HTML标签中，点击窗口上方的”inspect”命令，然后再选择页面中的文本节点，你可以对其进行修改，修改结果会马上反应在页面中。

|firebug05.gif|

Firebug同时是源码浏览器和编辑器。所有HTML、CSS和Javascript文件中的对象，都可以用单击或双击进行编辑。当你输入完毕，浏览器中的页面立刻会发生相应变化，你可以得到瞬时反馈。DOM浏览器允许你对文档结构进行彻底的编辑，不局限于文本节点。在HTML标签中，点击窗口上部”inspect”命令旁边的”edit”命令，下方的窗口就会立刻变成一个黑白的文本编辑窗口，你可以对HTML源代码进行任意编辑。在CSS标签中，Firebug会自动补全你的输入。在DOM标签中，当你按Tab键时，Firebug会自动补全属性名。

**五、用Firebug处理CSS**

在DOM标签中，每个HTML元素的style属性揭示了该元素的所有CSS设置。你可以双击对这些设置进行编辑。

|firebug06.gif|

对于那些Firefox不支持的CSS规则，Firebug会自动隐藏。比如，Firebug会隐藏针对某些浏览器的CSS特定设置，以及一些它不支持的CSS3规则。所以，它会隐藏\_height:25px;（下划线是一个针对IE6的设置）和p:first-of-type
{color: #ff0000;} (:first-of-type是一个CSS3规定的伪类，目前只有Safari
3支持）。但是，这也意味着，如果你恰巧发生了打字错误，导致某些规则无法显示，那么你只有使用其他编辑器显示全部CSS内容，找到你的错误。

Firebug允许你关闭CSS中的某些语句，页面会立刻反映相应变化，你可以立刻查看效果。”关闭”一条语句的方法是，在该语句的左边点击，会出现一个红色的\ |turnoffselector.gif|\ 禁止标志。该语句就会变灰。再次点击，该语句就会恢复。

Firebug允许你编辑CSS的属性和属性值。你只要对它们点击，就能编辑。修改后的效果会立刻在浏览器窗口中显示出来。这个特性最好的运用，是在确定准确定位的padding和margin时，firebug允许你用方向键逐单位的增加。

Firebug允许你增加新的属性和属性值。增加方法是双击现有的selector，然后就会出现一个空白的属性名输入框，完成输入后则会出现一个空白的属性值。

**六、盒状模型**

当你在HTML标签中，点击一个元素时，左面窗口显示HTML代码，右面窗口显示该元素的CSS。在CSS窗口上方，有一个layout按钮，点击后会展示与该元素相关的方块模型，包括padding、margin和border的值。要查看每一个元素的这三项值，只需点击”inspect”按钮，然后用鼠标悬停在页面中该元素的上方。

|firebug08.gif|

**七、评估下载速度**

Net标签中图形化了页面中所有http请求所用的时间。使用这个功能，必须打开Network
monitoring，默认设置就是打开，但是你可以在”options”下拉菜单中关闭这个选项。你可以用这项功能评估javascript文件下载，占用整个页面显示的时间。

|firebug09.gif|

在每个HTTP请求的左面点击，会显示该次请求的头信息。

在1.0.5版以后，你可以单独查看HTML文件、CSS文件、图像文件等各自下载的时间。

**八、DOM**

DOM标签提供页面上所有物体的所有属性的信息。Firebug最酷的功能之一是，它可以动态修改页面，反映在浏览器窗口，但是如果使用浏览器自带的查看源码功能，你会发现源码并没有改变。

**九、Javascript调试**

JavaScript
profiler可以报告你的Javascript函数执行所花的时间，因此你可以查看不同函数对速度的影响。使用这个功能的方法是，打开console标签，然后点击上面的Profile按钮（上部的按钮顺序是”Inspect
\|Clear \|
Profile”）。Firebug列出调用的所有函数，及其所花的时间。你可以针对要测试的某个函数，在其前部加上console.profile([title])，在其后部加上console.profileEnd()。

console标签的底部是命令行输入，它以”»>”开头。如果命令行输入有结果输出，那么它会展示在上部的窗口。有一个详细的\ `命令行输入API <http://www.getfirebug.com/commandline.html>`__\ 值得看一下。Firebug内置console对象有几种有用的方法可供调用，包括console.debug、console.info、console.warning、console.error等。如果这些方法产生了输出结果，Firebug会提供一个链接，让你查看相应的代码。

调试的另一个方法是设置断点。Script标签允许你在任意行暂停执行。单击行号，就会设置一个断点。右击行号，就可以设置一个断点出现的条件，只有当条件为真时，程序才会暂停执行。右面还有一个watch窗口，可以查看当前变量的值。

|firebug11.gif|

**十、AJAX**

前面已经提到，Firebug可以捕捉页面的动态内容和其他DOM变化。如果你打开这个\ `示例文件 <http://www.evotech.net/articles/ajaxlesson.html>`__\ ，点击页面上的链接后，在浏览器中查看源码，你会发现什么也没有改变，源码中依然包含那个链接。但是，如果你在Firebug中查看源码，你会发现DOM已经发生了变化，”Hello
World”已经被包括在内了。这就是Firebug的核心功能之一，没有它，AJAX的请求和回应就是不可见的。有了它，你可以看到送出的和收到的文本，已经相应的头信息。在Net标签中，你还能监控每个请求/回应各自所花费的时间。

|firebug10.gif|

Net标签中的XHR功能，对查看AJAX操作特别有用。如果你点击每个服务器端回应前的加号，你就会看到服务器端回应的头信息和内容。

当通过XMLHttpRequest对象向服务器端发出一个请求时，Firebug会记录请求的POST或GET内容，以及回应的头信息和内容。使用Net标签中的XHR功能，就可以看到这些内容。它会列出所有服务器的回应，以及所花费的时间。点击前面的+号，如果是GET请求，会显示三个标签；如果是POST请求，会显示4个标签：

    Params: 显示请求URL中所包含的name/value对。

    Headers: 显示请求和回应的头信息。

    Response: 显示实际从服务器收到的信息。

    Post：显示从通过POST请求，送到服务器的信息。（此项GET请求不包括。）

这四个标签对编写和调试程序很有用。检查POST和Params标签，确定你的请求被正确地发出了。检查Response标签查看返回的格式，确定相应的Javascript处理函数应该如何编写。

**十一、附注**

    \* Firebug 1.05 及以前版本，与Firefox 3.0不兼容。

    \* Firebug的作者Joe
    Hewitt免费提供了这个软件，为了显示我们对他的爱，你可以考虑对他进行\ `捐助 <http://getfirebug.com/contribute.html>`__\ 。

    \* Firebug的一些高级应用，请看Joe
    Hewitt的这段\ `演示视频 <http://video.yahoo.com/watch/111597>`__\ 。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/06/firebug_tutorial.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com