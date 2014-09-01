.. _201207_three_ways_to_define_a_javascript_class:

Javascript定义类（class）的三种方法
======================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/07/three_ways_to_define_a_javascript_class.html>`__

将近20年前，\ `Javascript诞生 <http://www.ruanyifeng.com/blog/2011/06/birth_of_javascript.html>`__\ 的时候，只是一种简单的网页脚本语言。如果你忘了填写用户名，它就跳出一个警告。

如今，它变得几乎无所不能，从前端到\ `后端 <http://nodejs.org/>`__\ ，有着各种\ `匪夷所思的用途 <http://www.netmagazine.com/features/10-things-you-didnt-know-javascript-could-do>`__\ 。程序员用它完成越来越庞大的项目。

Javascript代码的复杂度也直线上升。单个网页包含10000行Javascript代码，早就司空见惯。2010年，一个工程师\ `透露 <http://googlesystem.blogspot.tw/2010/06/gmail-to-use-more-html5-features.html>`__\ ，Gmail的代码长度是443000行！

编写和维护如此复杂的代码，必须使用\ `模块化策略 <http://en.wikipedia.org/wiki/Modular_design>`__\ 。目前，业界的主流做法是采用”面向对象编程”。因此，Javascript如何实现面向对象编程，就成了一个热门课题。

麻烦的是，Javascipt语法不支持”类”（class），导致传统的面向对象编程方法无法直接使用。程序员们做了很多探索，研究如何用Javascript模拟”类”。本文总结了Javascript定义”类”的三种方法，讨论了每种方法的特点，着重介绍了我眼中的最佳方法。


==============================================

**Javascript定义类（class）的三种方法**

作者：阮一峰

在面向对象编程中，类（class）是对象（object）的模板，定义了同一组对象（又称”实例”）共有的属性和方法。

Javascript语言不支持”类”，但是可以用一些变通的方法，模拟出”类”。

**一、构造函数法**

这是经典方法，也是教科书必教的方法。它用构造函数模拟”类”，在其内部用this关键字指代实例对象。

    　　function Cat() {

    　　　　this.name = “大毛”;

    　　}

生成实例的时候，使用new关键字。

    　　var cat1 = new Cat();

    　　alert(cat1.name); // 大毛

类的属性和方法，还可以定义在构造函数的prototype对象之上。

    　　Cat.prototype.makeSound = function(){

    　　　　alert(“喵喵喵”);

    　　}

关于这种方法的详细介绍，请看我写的系列文章\ `《Javascript
面向对象编程》 <http://www.ruanyifeng.com/blog/2010/05/object-oriented_javascript_encapsulation.html>`__\ ，这里就不多说了。它的主要缺点是，比较复杂，用到了this和prototype，编写和阅读都很费力。

**二、Object.create()法**

为了解决”构造函数法”的缺点，更方便地生成对象，Javascript的国际标准\ `ECMAScript <http://en.wikipedia.org/wiki/ECMAScript>`__\ 第五版（目前通行的是第三版），提出了一个新的方法\ `Object.create() <https://developer.mozilla.org/en/JavaScript/Reference/Global_Objects/Object/create/>`__\ 。

用这个方法，”类”就是一个对象，不是函数。

    　　var Cat = {

    　　　　name: “大毛”,

    　　　　makeSound: function(){ alert(“喵喵喵”); }

    　　};

然后，直接用Object.create()生成实例，不需要用到new。

    　　var cat1 = Object.create(Cat);

    　　alert(cat1.name); // 大毛

    　　cat1.makeSound(); // 喵喵喵

目前，各大浏览器的最新版本（包括IE9）都部署了这个方法。如果遇到老式浏览器，可以用下面的代码自行部署。

    　　if (!Object.create) {

    　　　　Object.create = function (o) {

    　　　　　　 function F() {}

    　　　　　　F.prototype = o;

    　　　　　　return new F();

    　　　　};

    　　}

这种方法比”构造函数法”简单，但是不能实现私有属性和私有方法，实例对象之间也不能共享数据，对”类”的模拟不够全面。

**三、极简主义法**

荷兰程序员Gabor de
Mooij提出了一种比Object.create()更好的\ `新方法 <http://www.gabordemooij.com/articles/jsoop.html>`__\ ，他称这种方法为”极简主义法”（minimalist
approach）。这也是我推荐的方法。

**3.1 封装**

这种方法不使用this和prototype，代码部署起来非常简单，这大概也是它被叫做”极简主义法”的原因。

首先，它也是用一个对象模拟”类”。在这个类里面，定义一个构造函数createNew()，用来生成实例。

    　　var Cat = {

    　　　　createNew: function(){

    　　　　　　// some code here

    　　　　}

    　　};

然后，在createNew()里面，定义一个实例对象，把这个实例对象作为返回值。

    　　var Cat = {

    　　　　createNew: function(){

    　　　　　　var cat = {};

    　　　　　　cat.name = “大毛”;

    　　　　　　cat.makeSound = function(){ alert(“喵喵喵”); };

    　　　　　　return cat;

    　　　　}

    　　};

使用的时候，调用createNew()方法，就可以得到实例对象。

    　　var cat1 = Cat.createNew();

    　　cat1.makeSound(); // 喵喵喵

这种方法的好处是，容易理解，结构清晰优雅，符合传统的”面向对象编程”的构造，因此可以方便地部署下面的特性。

**3.2 继承**

让一个类继承另一个类，实现起来很方便。只要在前者的createNew()方法中，调用后者的createNew()方法即可。

先定义一个Animal类。

    　　var Animal = {

    　　　　createNew: function(){

    　　　　　　var animal = {};

    　　　　　　animal.sleep = function(){ alert(“睡懒觉”); };

    　　　　　　return animal;

    　　　　}

    　　};

然后，在Cat的createNew()方法中，调用Animal的createNew()方法。

    　　var Cat = {

    　　　　createNew: function(){

    　　　　　　**var cat = Animal.createNew();**

    　　　　　　cat.name = “大毛”;

    　　　　　　cat.makeSound = function(){ alert(“喵喵喵”); };

    　　　　　　return cat;

    　　　　}

    　　};

这样得到的Cat实例，就会同时继承Cat类和Animal类。

    　　var cat1 = Cat.createNew();

    　　cat1.sleep(); // 睡懒觉

**3.3 私有属性和私有方法**

在createNew()方法中，只要不是定义在cat对象上的方法和属性，都是私有的。

    　　var Cat = {

    　　　　createNew: function(){

    　　　　　　var cat = {};

    　　　　　　**var sound = “喵喵喵”;**

    　　　　　　**cat.makeSound = function(){ alert(sound); };**

    　　　　　　return cat;

    　　　　}

    　　};

上例的内部变量sound，外部无法读取，只有通过cat的公有方法makeSound()来读取。

    　　var cat1 = Cat.createNew();

    　　**alert(cat1.sound);** // undefined

**3.4 数据共享**

有时候，我们需要所有实例对象，能够读写同一项内部数据。这个时候，只要把这个内部数据，封装在类对象的里面、createNew()方法的外面即可。

    　　var Cat = {

    　　　　**sound : “喵喵喵”,**

    　　　　createNew: function(){

    　　　　　　var cat = {};

    　　　　　　**cat.makeSound = function(){ alert(Cat.sound); };**

    　　　　　　**cat.changeSound = function(x){ Cat.sound = x; };**

    　　　　　　return cat;

    　　　　}

    　　};

然后，生成两个实例对象：

    　　var cat1 = Cat.createNew();

    　　var cat2 = Cat.createNew();

    　　cat1.makeSound(); // 喵喵喵

这时，如果有一个实例对象，修改了共享的数据，另一个实例对象也会受到影响。

    　　**cat2.changeSound(“啦啦啦”);**

    　　cat1.makeSound(); // 啦啦啦

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/07/three_ways_to_define_a_javascript_class.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com