.. _201110_javascript_loading:

Javascript文件加载：LABjs和RequireJS
=======================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/10/javascript_loading.html>`__

传统上，加载Javascript文件都是使用

　　

　　

　　

　　

　　

上面这段代码，将依次加载4个javascript文件：script1.js、script2-a.js、script2-b.js和script3.js。在加载完前三个文件后，运行两个函数initScript1()和initScript2()；加载完第四个文件后，再运行函数initScript3()。

下面，用LABjs对其进行改写：

    　　
    　　

首先，$LAB对象替代了

　　

require()接受两个参数，第一个数组表示所要加载的Javascript文件，第二个是加载完成后所要运行的回调函数。原生的require()不支持按次序加载，所以四个Javascript文件到底先加载哪个，无法事前知道，require()只保证这四个文件全部加载完成之后，才会运行所指定的回调函数。

如果按次序加载对你很重要，你可以使用官方提供的\ `order插件 <http://requirejs.org/docs/api.html#order>`__\ 。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/10/javascript_loading.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com