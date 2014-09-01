.. _201210_asynchronous_module_definition:

Javascript模块化编程（二）：AMD规范
======================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/10/asynchronous_module_definition.html>`__

这个系列的\ `第一部分 <http://www.ruanyifeng.com/blog/2012/10/javascript_module.html>`__\ 介绍了Javascript模块的基本写法，今天介绍如何规范地使用模块。

（接\ `上文 <http://www.ruanyifeng.com/blog/2012/10/javascript_module.html>`__\ ）

**七、模块的规范**

先想一想，为什么模块很重要？

因为有了模块，我们就可以更方便地使用别人的代码，想要什么功能，就加载什么模块。

但是，这样做有一个前提，那就是大家必须以同样的方式编写模块，否则你有你的写法，我有我的写法，岂不是乱了套！考虑到Javascript模块现在还没有官方规范，这一点就更重要了。

目前，通行的Javascript模块规范共有两种：\ `CommonJS <http://wiki.commonjs.org/wiki/Modules/1.1>`__\ 和\ `AMD <https://github.com/amdjs/amdjs-api/wiki/AMD>`__\ 。我主要介绍AMD，但是要先从CommonJS讲起。

**八、CommonJS**

2009年，美国程序员Ryan
Dahl创造了\ `node.js <http://nodejs.org/>`__\ 项目，将javascript语言用于服务器端编程。

这标志”Javascript模块化编程”正式诞生。因为老实说，在浏览器环境下，没有模块也不是特别大的问题，毕竟网页程序的复杂性有限；但是在服务器端，一定要有模块，与操作系统和其他应用程序互动，否则根本没法编程。

node.js的\ `模块系统 <http://nodejs.org/docs/latest/api/modules.html>`__\ ，就是参照\ `CommonJS <http://wiki.commonjs.org/wiki/Modules/1.1>`__\ 规范实现的。在CommonJS中，有一个全局性方法require()，用于加载模块。假定有一个数学模块math.js，就可以像下面这样加载。

    　　var math = require(‘math’);

然后，就可以调用模块提供的方法：

    　　var math = require(‘math’);

    　　math.add(2,3); // 5

因为这个系列主要针对浏览器编程，不涉及node.js，所以对CommonJS就不多做介绍了。我们在这里只要知道，require()用于加载模块就行了。

**九、浏览器环境**

有了服务器端模块以后，很自然地，大家就想要客户端模块。而且最好两者能够兼容，一个模块不用修改，在服务器和浏览器都可以运行。

但是，由于一个重大的局限，使得CommonJS规范不适用于浏览器环境。还是上一节的代码，如果在浏览器中运行，会有一个很大的问题，你能看出来吗？

    　　var math = require(‘math’);

    　　math.add(2, 3);

第二行math.add(2,
3)，在第一行require(‘math’)之后运行，因此必须等math.js加载完成。也就是说，如果加载时间很长，整个应用就会停在那里等。

这对服务器端不是一个问题，因为所有的模块都存放在本地硬盘，可以同步加载完成，等待时间就是硬盘的读取时间。但是，对于浏览器，这却是一个大问题，因为模块都放在服务器端，等待时间取决于网速的快慢，可能要等很长时间，浏览器处于”假死”状态。

因此，浏览器端的模块，不能采用”同步加载”（synchronous），只能采用”异步加载”（asynchronous）。这就是AMD规范诞生的背景。

**十、AMD**

`AMD <https://github.com/amdjs/amdjs-api/wiki/AMD>`__\ 是”Asynchronous
Module
Definition”的缩写，意思就是”异步模块定义”。它采用异步方式加载模块，模块的加载不影响它后面语句的运行。所有依赖这个模块的语句，都定义在一个回调函数中，等到加载完成之后，这个回调函数才会运行。

AMD也采用require()语句加载模块，但是不同于CommonJS，它要求两个参数：

    　　require([module], callback);

第一个参数[module]，是一个数组，里面的成员就是要加载的模块；第二个参数callback，则是加载成功之后的回调函数。如果将前面的代码改写成AMD形式，就是下面这样：

    　　require([‘math’], function (math) {

    　　　　math.add(2, 3);

    　　});

math.add()与math模块加载不是同步的，浏览器不会发生假死。所以很显然，AMD比较适合浏览器环境。

目前，主要有两个Javascript库实现了AMD规范：\ `require.js <http://requirejs.org/>`__\ 和\ `curl.js <https://github.com/cujojs/curl>`__\ 。本系列的第三部分，将通过介绍require.js，进一步讲解AMD的用法，以及如何将模块化编程投入实战。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/10/asynchronous_module_definition.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com