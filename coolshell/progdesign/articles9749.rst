.. _articles9749:

Javascript 装载和执行
=====================

2013年6月5日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

|image0|\ 一两个月前在淘宝内网里看到一个优化Javascript代码的竞赛，发现有不少的人对Javascript的执行和装载的基础并不懂，所以，从那天起我就想写一篇文章，但一直耽搁了。自上篇《\ `浏览器渲染原理简介 <http://coolshell.cn/articles/9666.html>`__\ 》，正好也可以承前启后。

首先，我想说一下Javascript的装载和执行。通常来说，浏览器对于Javascript的运行有两大特性：\ **1）载入后马上执行，2）执行时会阻塞页面后续的内容（包括页面的渲染、其它资源的下载）**\ 。于是，如果有多个js文件被引入，那么对于浏览器来说，这些js文件被被串行地载入，并依次执行。

因为javascript可能会来操作HTML文档的DOM树，所以，浏览器一般都不会像并行下载css文件并行下载js文件，因为这是js文件的特殊性造成的。所以，如果你的javascript想操作后面的DOM元素，基本上来说，浏览器都会报错说对象找不到。因为Javascript执行时，后面的HTML被阻塞住了，DOM树时还没有后面的DOM结点。所以程序也就报错了。

传统的方式
^^^^^^^^^^

所以，当你写在代码中写下如下的代码：

::

基本上来说，head里的

你觉得alert的顺序是什么？你可以在不同的浏览器里试一试。这里的想关的测试页面：\ **`示例二 <http://coolshell.cn/asyncjs/async_test02.html>`__**\ 。

script的defer和async属性
^^^^^^^^^^^^^^^^^^^^^^^^

IE自从IE6就支持defer标签，如：

::

对于IE来说，这个标签会让IE并行下载js文件，并且把其执行hold到了整个DOM装载完毕（DOMContentLoaded），多个defer的

因为”cache/script”，这个东西根本就不能被浏览器解析，所以浏览器也就不能把alert.js当javascript去执行，但是他又要去下载js文件，所以就可以搞定了。可惜的是，webkit严格符从了HTML的标准——对于这种不认识的东西，直接删除，什么也不干。于是，我们的梦又破了。

所以，我们需要再hack一下，就像N多年前玩preload图片那样，我们可以动用object标签（也可以动用iframe标签），于是我们有下面这样的代码：

::

        function cachejs(script_filename){
            var cache = document.createElement('object');
            cache.data = script_filename;
            cache.id = "coolshell_script_cache_id";
            cache.width = 0;
            cache.height = 0;
            document.body.appendChild(cache);
        }

然后，我们在的最后调用一下这个函数。请参看一下相关的示例：\ **`示例六 <http://coolshell.cn/asyncjs/async_test06.html>`__**

在Chrome下按
Ctrl+Shit+I，切换到network页，你就可以看到下载了alert.js但是没有执行，然后我们再用示例五的方式，因为浏览器端有缓存了，不会再从服务器上下载alert.js了。所以，就能保证执行速度了。

关于这种preload这种东西你应该不会陌生了。你还可以使用Ajax的方式，如：

::

    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'new.js');
    xhr.send('');

到这里我就不再多说了，也不给示例了，大家可以自己试试去。

最后再提两个js，一个是\ `ControlJS <http://stevesouders.com/controljs/>`__\ ，一个叫\ `HeadJS <http://headjs.com/>`__\ ，专门用来做异步load
javascript文件的。

好了，这是所有的内容了，希望大家看过后能对Javascript的载入和执行，以及相关的技术有个了解。\ **同时，也希望各前端高手不吝赐教！**

（全文完）

.. |image0| image:: /coolshell/static/20140922100257909000.jpg
.. |image7| image:: /coolshell/static/20140922100258055000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/9749.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com