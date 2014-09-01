.. _200903_creating_gmail-like_buttons:

制作Gmail式按钮
==================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/03/creating_gmail-like_buttons.html>`__

一个月前，\ `Gmail <https://mail.google.com>`__\ 重新设计了所有按钮。

原来的按钮是这样的。

新设计的按钮是这样的。

事实上，不仅是Gmail，Google公司很多其他项目都在使用后一种风格的按钮。

比如\ `Google Site <http://sites.google.com/>`__\ 。

再比如\ `Picasa <http://picasaweb.google.com>`__\ 。

这种按钮设计最大的特点，就是完全不使用背景图片，是纯粹的HTML+CSS。同时，它也不使用任何表单元素，目的是在不同浏览器下，争取视觉效果的最大统一。

Google的工程师、设计者\ `Douglas
Bowman <http://stopdesign.com/archive/2009/02/04/recreating-the-button.html>`__\ 最近写了篇文章，介绍了设计思路。但是，他最后没有给出代码，只是说：

    To see the final code we ended up using in Gmail and Reader, you’ll
    have to reverse engineer the button code in one of those products.

    如果你想看我们在Gmail和Google
    Reader中使用的最终代码，你必须自己对按钮代码进行反向工程。

我对这个很有兴趣，昨天晚上就真的去做反向工程了。由于Gmail的CSS文件都是被压缩过的，简直无法读，不过好在按钮部分还没有被压缩，因此还算顺利，就把代码提取出来了。

下面我就来介绍，如何制作Gmail式的按钮。使用的全部都是Gmail中的实际代码。

请先看我制作的一个\ `范例页面 <http://www.ruanyifeng.com/webapp/google_button/>`__\ 。

第一步，按钮的HTML代码如下：

    　　

    　　　　

    　　　　　　

    　　　　　　　　

     

    　　　　　　　　

    Button

    　　　　　　

    　　　　

    | 
    |  　　

    | 

每个按钮都是一个四层的盒状结构，共包含6个div区块。

第二步，将\ `button.css <http://www.ruanyifeng.com/webapp/google_button/button.css>`__\ 文件加入样式表。

    @import url(“button.css”);

这个时候，按钮就应该可以正常显示了。

第三步，做一些修饰工作。

你可以根据按钮的不同情况，为前面HTML代码中第1个div区块，添加相应的class。

    i. 如果一个按钮是主按钮，那么添加”goog-imageless-button-primary”。

    ii.
    如果一个按钮不允许用户使用，那么添加”goog-imageless-button-disabled”。

    iii. 如果好几个按钮组成一个”按钮组”，就像范例中的Example
    3，那么最左边的按钮添加”goog-imageless-button-collapse-right”，最右边的按钮添加”goog-imageless-button-collapse-left”，中间的按钮则是同时添加这两个class。

    iv.
    如果一个按钮保持选中状态，那么添加”goog-imageless-button-checked”。

第四步，用Javascript加入动作代码。我使用的库是\ `jQuery <http://jquery.com/>`__\ 。

i. 加入鼠标悬停效果。

    | 　　$(“.goog-imageless-button”).hover( 　　　　function(){
    　　　　　　if(!$(this).hasClass(“goog-imageless-button-disabled”)){
    　　　　　　　　$(this).addClass(“goog-imageless-button-hover”);
    　　　　　　} 　　　　}, 　　　　function(){
    　　　　　　if(!$(this).hasClass(“goog-imageless-button-disabled”)){
    　　　　　　　　$(this).removeClass(“goog-imageless-button-hover”);
    　　　　　　}
    |  　　　　}
    |  　　);

ii. 加入鼠标点击的效果。

    | 　　$(“.goog-imageless-button”).mousedown( 　　　　function(){
    　　　　　　if(!$(this).hasClass(“goog-imageless-button-disabled”)){
    　　　　　　　　$(this).addClass(“goog-imageless-button-checked”);
    　　　　　　} 　　　　} 　　 ).mouseup( 　　　　function(){
    　　　　　　if(!$(this).hasClass(“goog-imageless-button-disabled”)){
    　　　　　　　　$(this).removeClass(“goog-imageless-button-checked”);
    　　　　　　}
    |  　　　　}
    |  　　 );

iii. 加入focus和blur事件的代码。

    $(“.goog-imageless-button”).focus(function(){$(this).addClass(“goog-imageless-button-focused”)});

    $(“.goog-imageless-button”).blur(function(){$(this).removeClass(“goog-imageless-button-focused”)});

到了这一步，就算基本完成了。以后只要再针对按钮的click或submit事件，写入相应代码与服务器端互动，就可以了。

最后，说一点我的看法。

虽然这种按钮的视觉效果比较理想，有很多设计上的优点，但是局限性也很大。一方面，它需要大量的冗余代码，与语义网的原则相违背；另一方面，它太依赖Javascript和桌面环境，一旦用户使用移动设备或不支持Javascript的浏览器上网，那么整张网页的就完全失效了。所以，除非你开发的是针对桌面浏览器的互联网应用程序，否则还是不要使用上面的设计方法，而是用Douglas
Bowman提供的一种比较\ `简化的形式 <http://stopdesign.com/eg/buttons/3.0/code.html>`__\ （需要背景图片）。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/03/creating_gmail-like_buttons.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com