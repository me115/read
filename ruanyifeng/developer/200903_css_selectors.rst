.. _200903_css_selectors:

Css选择器笔记
================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/03/css_selectors.html>`__

去年我学\ `jQuery <http://docs.jquery.com/Selectors>`__\ 的时候，曾经做过一点选择器（selector）的笔记。

这几天拿出来看了一下，发现很多都忘记了。所以，我决定把它们贴在这里，方便以后查看。这对其他朋友应该也是有用的，毕竟选择器是制作网页效果的第一步。

笔记分为两个部分，今天是CSS的选择器，以后还有一部分xPath的选择器。今天的笔记中包括44个选择器，基本涵盖了CSS
2和CSS 3的所有规定。


=====================

**CSS选择器笔记**

阮一峰 整理

参考网址：\ `456 Berea
Street <http://www.456bereastreet.com/archive/200509/css_21_selectors_part_1/>`__

**一、基本选择器**

序号选择器含义1. **\*** 通用元素选择器，匹配任何元素2. **E**
标签选择器，匹配所有使用E标签的元素3. **.info**
class选择器，匹配所有class属性中包含info的元素4. **#footer**
id选择器，匹配所有id属性等于footer的元素

实例：

    \* { margin:0; padding:0; }

    p { font-size:2em; }

    .info { background:#ff0; }

    p.info { background:#ff0; }

    p.info.error { color:#900; font-weight:bold; }

    #info { background:#ff0; }

    p#info { background:#ff0; }

**二、多元素的组合选择器**

序号选择器含义5. E,F
多元素选择器，同时匹配所有E元素或F元素，E和F之间用逗号分隔6. E F
后代元素选择器，匹配所有属于E元素后代的F元素，E和F之间用空格分隔7. E > F
子元素选择器，匹配所有E元素的子元素F8. E + F
毗邻元素选择器，匹配所有紧随E元素之后的同级元素F

实例：

    div p { color:#f00; }

    #nav li { display:inline; }

    #nav a { font-weight:bold; }

    div > strong { color:#f00; }

    p + p { color:#f00; }

**三、CSS 2.1 属性选择器**

序号选择器含义9. E[att]
匹配所有具有att属性的E元素，不考虑它的值。（注意：E在此处可以省略，比如”[cheacked]”。以下同。）10.
E[att=val] 匹配所有att属性等于”val”的E元素11. E[att~=val]
匹配所有att属性具有多个空格分隔的值、其中一个值等于”val”的E元素12.
E[att\|=val]
匹配所有att属性具有多个连字号分隔（hyphen-separated）的值、其中一个值以”val”开头的E元素，主要用于lang属性，比如”en”、”en-us”、”en-gb”等等

实例：

    p[title] { color:#f00; }

    div[class=error] { color:#f00; }

    td[headers~=col1] { color:#f00; }

    p[lang\|=en] { color:#f00; }

    blockquote[class=quote][cite] { color:#f00; }

**四、CSS 2.1中的伪类**

序号选择器含义13. E:first-child 匹配父元素的第一个子元素14. E:link
匹配所有未被点击的链接15. E:visited 匹配所有已被点击的链接16. E:active
匹配鼠标已经其上按下、还没有释放的E元素17. E:hover
匹配鼠标悬停其上的E元素18. E:focus 匹配获得当前焦点的E元素19. E:lang(c)
匹配lang属性等于c的E元素

实例：

    p:first-child { font-style:italic; }

    input[type=text]:focus { color:#000; background:#ffe; }

    input[type=text]:focus:hover { background:#fff; }

    q:lang(sv) { quotes: “\\201D” “\\201D” “\\2019” “\\2019”; }

**五、 CSS 2.1中的伪元素**

序号选择器含义20. E:first-line 匹配E元素的第一行21. E:first-letter
匹配E元素的第一个字母22. E:before 在E元素之前插入生成的内容23. E:after
在E元素之后插入生成的内容

实例：

    p:first-line { font-weight:bold; color;#600; }

    .preamble:first-letter { font-size:1.5em; font-weight:bold; }

    .cbb:before { content:”“; display:block; height:17px; width:18px;
    background:url(top.png) no-repeat 0 0; margin:0 0 0 -18px; }

    a:link:after { content: ” (” attr(href) “) “; }

**六、CSS 3的同级元素通用选择器**

序号选择器含义24. E ~ F 匹配任何在E元素之后的同级F元素

实例：

    p ~ ul { background:#ff0; }

**七、CSS 3 属性选择器**

序号选择器含义25. E[att^=”val”] 属性att的值以”val”开头的元素26.
E[att$=”val”] 属性att的值以”val”结尾的元素27. E[att\*=”val”]
属性att的值包含”val”字符串的元素

实例：

    div[id^=”nav”] { background:#ff0; }

**八、CSS 3中与用户界面有关的伪类**

序号选择器含义28. E:enabled 匹配表单中激活的元素29. E:disabled
匹配表单中禁用的元素30. E:checked
匹配表单中被选中的radio（单选框）或checkbox（复选框）元素31.
E::selection 匹配用户当前选中的元素

实例：

    input[type=”text”]:disabled { background:#ddd; }

**九、CSS 3中的结构性伪类**

序号选择器含义32. E:root 匹配文档的根元素，对于HTML文档，就是HTML元素33.
E:nth-child(n) 匹配其父元素的第n个子元素，第一个编号为134.
E:nth-last-child(n) 匹配其父元素的倒数第n个子元素，第一个编号为135.
E:nth-of-type(n) 与:nth-child()作用类似，但是仅匹配使用同种标签的元素36.
E:nth-last-of-type(n) 与:nth-last-child()
作用类似，但是仅匹配使用同种标签的元素37. E:last-child
匹配父元素的最后一个子元素，等同于:nth-last-child(1)38. E:first-of-type
匹配父元素下使用同种标签的第一个子元素，等同于:nth-of-type(1)39.
E:last-of-type
匹配父元素下使用同种标签的最后一个子元素，等同于:nth-last-of-type(1)40.
E:only-child
匹配父元素下仅有的一个子元素，等同于:first-child:last-child或
:nth-child(1):nth-last-child(1)41. E:only-of-type
匹配父元素下使用同种标签的唯一一个子元素，等同于:first-of-type:last-of-type或
:nth-of-type(1):nth-last-of-type(1)42. E:empty
匹配一个不包含任何子元素的元素，注意，文本节点也被看作子元素

实例：

    p:nth-child(3) { color:#f00; }

    p:nth-child(odd) { color:#f00; }

    p:nth-child(even) { color:#f00; }

    p:nth-child(3n+0) { color:#f00; }

    p:nth-child(3n) { color:#f00; }

    tr:nth-child(2n+11) { background:#ff0; }

    tr:nth-last-child(2) { background:#ff0; }

    p:last-child { background:#ff0; }

    p:only-child { background:#ff0; }

    p:empty { background:#ff0; }

**十、CSS 3的反选伪类**

序号选择器含义43. E:not(s) 匹配不符合当前选择器的任何元素

实例：

    :not(p) { border:1px solid #ccc; }

**十一、CSS 3中的 :target 伪类**

序号选择器含义44. E:target 匹配文档中特定”id”点击后的效果

请参看HTML
DOG上关于该选择器的\ `详细解释 <http://htmldog.com/articles/suckerfish/target/>`__\ 和\ `实例 <http://htmldog.com/articles/suckerfish/target/example/>`__\ 。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/03/css_selectors.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com