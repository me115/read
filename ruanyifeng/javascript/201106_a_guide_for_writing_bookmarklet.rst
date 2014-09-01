.. _201106_a_guide_for_writing_bookmarklet:

Bookmarklet编写指南
======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/06/a_guide_for_writing_bookmarklet.html>`__

前一段日子，我写了两个Bookmarklet——”\ `短网址生成 <http://www.ruanyifeng.com/blog/2011/01/api_for_google_s_url_shortener.html>`__\ “和”\ `短网址还原 <http://www.ruanyifeng.com/blog/2011/05/bookmarklet_of_unshortening_url.html>`__\ “。

它们用起来很方便，除了我本人之外，其他朋友也在用。第一次发布Bookmarklet，就能有用户，我挺满意的。

下面就是我整理的《Bookmarklet编写指南》，供自己和需要的朋友参考。


====================================================

**Bookmarklet编写指南**

阮一峰 编写

| 
| **一、什么是Bookmarklet？**

Bookmarklet是一个复合词，由Bookmark（书签）和-let（小的）构成，中文可以译成”书签工具”。

它在形式上与”书签”一样，都保存在浏览器收藏夹里。但是，它不是一个以”http://”开头的网址，而是一段Javascript代码，以”javascript:”开头。点击之后，会对当前页面执行某种操作。

它通常在网页中以链接的形式出现，就像下面这样：

    　　**`xxx <”javascript:alert(‘hi’);”>`__**

用户直接把这个链接拖到地址栏或收藏夹就可以用了。

**二、Bookmarklet的优点**

它有几个很显著的优点，其他技术难以取代：

**1. 安装快速**

　　Bookmarklet的安装，就是在收藏夹中保存一段代码，一步就能完成。所有浏览器都原生支持。

**2. 使用方便**

　　用的时候，点一下这个链接就行了。

**3. 开发容易**

　　一段Javascript代码就是Bookmarklet的所有内容，不需要用到其他技术，比开发一个浏览器插件简单多了。

**4. 跨浏览器**

　　所有浏览器都支持Bookmarklet。如果写的正确，同样一个Bookmarklet在各种浏览器上都能正常使用。

**三、Bookmarklet的编写规则**

**1. 必须以”javascript:”开头**

浏览器把”javascript:”当做协议看待。有了它，浏览器才知道要用javascript解释后面的代码。它的作用等同于将代码放在

之间运行。

**2. 所有代码必须在同一行**

因为浏览器把Bookmarklet当做网址保存，而网址是不能分行的，所以Bookmarklet也不能分行。

另一方面，网址是有长度限制的。IE的最长网址不能超过2083个字符（IE6不能超过508个字符），这也就是Bookmarklet的最长长度。\ `压缩工具 <http://ted.mielczarek.org/code/mozilla/bookmarklet.html>`__\ 可以帮忙减少长度，但是使用下面提到的连接外部代码的方法，可以避开这个限制。

**3. 使用单引号**

根据Javascript的语法，单引号（’xxx’）和双引号（”xxx”）都能使用。但是由于html语言主要使用双引号，所以Bookmarklet优先使用单引号。万一遇到必须使用双引号的情况，就采用它的URL编码形式”%22”。

**4. 不要污染全局变量**

Bookmarklet最好不要生成新的全局变量，可以采用直接运行匿名函数的方式：

    　　**javascript: (function(){…})();**

上面式子的第一个括号，定义了一个匿名函数；最后一个括号表示立即执行这个匿名函数。所有的变量都是匿名函数的内部变量，不会生成任何新的全局变量。

如果必须设置全局变量，就取罕见的变量名（比如hd8ki2），防止与已经存在的全局变量同名。

**5. 对文本和URL进行编码**

为了防止出现非法字符，代码以外的文本都应该使用encodeURIComponent()函数进行编码，比如把空格变成%20。

**四、Bookmarklet的编写技巧**

**1. 获取网页信息**

获取当前页面的标题：document.title。

获取当前页面的URL： location.href。

获取当前选中的文本：

    　　var t;

    　　t = (function(){

    　　　　if (window.getSelection){

    　　　　　　return window.getSelection().toString();

    　　　　}else if(document.getSelection){

    　　　　　　return document.getSelection();

    　　　　}else if (document.selection){

    　　　　　　return document.selection.createRange().text;

    　　　　}

    　　　　return ”;

    　　})();

**2. 防止刷新页面**

如果代码对页面有改动（比如使用了document.write），浏览器就会用一个新页面替换原有页面。所以最好用void()命令，把语句放在里面。

举例来说，下面这个Bookmarklet会导致原页面被一个新页面替代：

    　　javascript:document.links[0].href=’http://www.ibm.com/’;

加上void以后，页面就不会跳转了：

    　　javascript:void(document.links[0].href=’http://www.ibm.com/’);

**3. 框架（frameset）**

对于使用”框架”（frameset）的网页，那些需要操作页面的Bookmarklet一般不起作用。所以，如果发现网页使用了框架，就告诉用户Bookmarklet无法使用。

    　　if(frames.length > 0)

    　　　　alert(‘对不起，不适用于框架。’);

    　　else{

    　　　　/\* 正常情况的代码 \*/

    　　}

但是，上面的代码有一个问题，那就是行内框架iframe也包含在frames.length之中，所以必须排除iframe的影响。

    | 　　if(frames.length >
    |  　　　document.getElementsByTagName(‘iframe’).length)

    　　　　alert(‘对不起，不适用于框架。’);

    　　else{

    　　　　/\* 正常情况的代码 \*/

    　　}

**4. 连接外部javascript代码**

有时，Bookmarklet必须再引入外部的Javascript代码，这就需要为当前页面添加一个script标签。

    　　javascript:(function(){

    　　　　var script=document.createElement(‘script’);

    | 　　　　script.setAttribute(‘src’,
    |  　　　　　　　　　　　　’http://path/to/external/file.js’);

    | 　　　　document.getElementsByTagName(‘head’)[0]
    |  　　　　　　　　.appendChild(script);

    　　})();

**5. 添加外部函数库**

如果Bookmarklet需要用到外部函数库，就必须把它也加进来。但是，前提是必须先检查一下，看看原页面是否已经加载了这个函数库。

下面以加载jQuery为例：

    　　if (!window.jQuery) {

    　　　　script=document.createElement( ‘script’ );

    | 　　　　script.src=’http://ajax.googleapis.com/
    |  　　　　　　　　　ajax/libs/jquery/1/jquery.min.js’;

    　　　　script.onload=foo;

    　　　　document.body.appendChild(script);

    | 　　} else {
    |  　　　　foo();

    | 　　}
    |  　　function foo() {

    　　　　/\* … \*/

    　　}

**五、延伸阅读**

　　\* Kalid Azad, `How To Make a Bookmarklet For Your Web
Application <http://betterexplained.com/articles/how-to-make-a-bookmarklet-for-your-web-application/>`__

　　\* Troels Jakobsen, `Rules for
Bookmarklets <http://subsimple.com/bookmarklets/rules.asphttp://subsimple.com/bookmarklets/rules.asp>`__

　　\* Troels Jakobsen, `Tips for Writing
Bookmarklets <http://subsimple.com/bookmarklets/tips.asp>`__

　　\* Siddharth, `Create Bookmarklets - The Right
Way <http://net.tutsplus.com/tutorials/javascript-ajax/create-bookmarklets-the-right-way/>`__

　　\* 2ality, `Implementing bookmarklets in
JavaScript <http://www.2ality.com/2011/06/implementing-bookmarklets.html>`__

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/06/a_guide_for_writing_bookmarklet.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com