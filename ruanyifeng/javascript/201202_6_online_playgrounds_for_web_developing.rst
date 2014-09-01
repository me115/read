.. _201202_6_online_playgrounds_for_web_developing:

网页开发的6种在线调试环境
============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/02/6_online_playgrounds_for_web_developing.html>`__

如今的网页代码，一般由三个部分组成：

    　　\* HTML，语义层，提供网页的内容。

    　　\* CSS，表现层，规定网页的外观。

    　　\* Javascript，动作层，定义用户与网页的互动。

理想的开发环境，应该既可以分别调试这三种代码，又可以轻松查看它们合并在一起的整体效果。

浏览器是最合适的效果查看工具，所以很多人想到，代码调试环境也可以直接部署在浏览器中，以网站的形式提供服务。

下面，我根据\ `Design
Shack <http://designshack.net/articles/css/5-online-playgrounds-for-html-css-and-javascript-compared/>`__\ 的文章，总结一下目前最常见的6种网页开发在线调试环境。它们大大方便了网页设计师的工作，极大地提供了工作效率。

**一、CSSDesk**

网址：\ `http://cssdesk.com/ <http://cssdesk.com/>`__ （需翻墙）

这个网站是最早出现的在线调试环境之一，主要用于调试CSS。

左侧两个面板，可以分别输入html和css代码，但不支持Javascript调试。

你可以改变”预览区”的背景颜色，可以保存或下载调试完成的代码。

**二、Dabblet**

网址：\ `http://dabblet.com/ <http://dabblet.com/>`__

Dabblet也是一个CSS调试环境，不支持Javascript调试。

它将网页效果分成”CSS效果”、”HTML效果”和”整体效果”三个面板，方便单独调试。

它最大的特点有两个，一是动态显示代码效果，代码一输入，效果就自动显示出来；二是显示CSS提示，比如上图的字体效果和长度效果。

**三、JS Bin**

网址：\ `http://jsbin.com <http://jsbin.com>`__

这是一个较早出现的Javascript在线调试环境。

它分成Javascript、html和”效果预览”三个区域，你可以自行勾选显示哪些区域。它没有独立的CSS代码区，CSS代码必须嵌入html代码，这点很不方便。

它支持加载常用的Javascript库。除此以外，其他特色不多。

**四、jsFiddle**

网址：\ `http://jsfiddle.net/ <http://jsfiddle.net/>`__

jsFiddle是目前最受欢迎的在线调试环境。

它的默认界面分成5个区域，左边是参数设置，右边依次是HTML、Javascript、CSS和”效果预览区”。

除了加载常见的Javascript库，它还支持SCSS代码和CoffeeScript代码。你甚至可以把它的窗口嵌入自己的网页。

**五、Tinkerbin**

网址：\ `http://tinkerbin.com/ <http://tinkerbin.com/>`__

Tinkerbin很像jsFiddle，也是分成HTML、Javascript、CSS和”效果预览区”。

它的特点在于，你可以选择某种代码独占整个编辑区，这样就增大了代码编辑的可视空间。另外，它可以实时显示代码运行结果，这是jsFiddle不支持的。

它支持的代码种类相当多，比如 HAML、SCSS、LESS和CoffeeScript。

**六、Rendur**

网址：\ `http://rendur.com/ <http://rendur.com/>`__

Rendur是一个轻量级在线调试环境，功能不多，但是加载和运行都很快。

用户可以在HTML、CSS、Javascript三个面板中切换，输入相应代码。代码的运行结果，会自动显示在背景网页上。最后一个面板，显示的是整个网页的源码。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/02/6_online_playgrounds_for_web_developing.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com