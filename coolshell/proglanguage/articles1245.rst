.. _articles1245:

IE的CSS相关的BUG
================

2009年8月12日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

|ie-bug|\ 这个网页（\ `http://haslayout.net/css/index <http://haslayout.net/css/index>`__\ ）上例举了所有的IE和CSS相关的BUG。如果你在开发网页的时候，你需要看看。

目前，这个网站上包含了 **28 个“普通的Bug”** ， **4 个“布局方面的Bug”**
， **6 个“可以绕开的Bug”** 以及 **1
个“IE崩溃的Bug”**\ ，所有的这些Bug有39个指南和48个解决方法。这个列表目前更新到
**2009年8月11日，19:50:22 **

下面是所有的bug列表，你可以点击每个BUG名的链接查看更详细的说明。

普通Bug
^^^^^^^

这部分 IE 的 bug
是比较普通的无法归到其它种类，或是同时属于多个种类的Bug。

名称 IE的版本 描述

`Hover White Background Ignore
Bug <http://haslayout.net/css/view?tut=Hover-White-Background-Ignore-Bug>`__
IE7 background 不会因为 :hover而改变 `IE7 Child Selector Comment
Bug <http://haslayout.net/css/view?tut=IE7-Child-Selector-Comment-Bug>`__
IE7 一个 selector
包含了一个子的selector，如果后面跟着一个注释，则会被完全忽略。 `Star
HTML Bug <http://haslayout.net/css/view?tut=Star-HTML-Bug>`__ IE6 \*
html selector 在 IE6 中没有被忽略 `IE6 !important Ignore
Bug <http://haslayout.net/css/view?tut=IE6--important-Ignore-Bug>`__ IE6
!important 关键字会忽略，如果有相同的属性被设置了 `PNG Image and
Background Color
Mismatch <http://haslayout.net/css/view?tut=PNG-Image-and-Background-Color-Mismatch>`__
IE8 及以下版本
背景颜色和指定的图片的颜色不一致。而他们本来是一致的。IE认为这是他一个Feature。太可笑了。
`No Auto Margin Center
Pseudo-Bug <http://haslayout.net/css/view?tut=No-Auto-Margin-Center-Pseudo-Bug>`__
IE8 及以下版本 如果把margins 设置成 \`auto\`
，IE不会把组件放置在中间的位置。所有的浏览器都会，只有IE不会。
`:first-line !important Rule Ignore
Bug <http://haslayout.net/css/view?tut=-first-line--important-Rule-Ignore-Bug>`__
IE8 如果在伪class :first-line 内使用!important，那么其所有定义会被忽略。
`:first-letter Ignore
Bug <http://haslayout.net/css/view?tut=-first-letter-Ignore-Bug>`__ IE6
整个:first-letter 的属性定义会被除数完全忽略。 `:first-letter !important
Rule Ignore
Bug <http://haslayout.net/css/view?tut=-first-letter--important-Rule-Ignore-Bug>`__
IE8 如果在伪class
:first-letter内使用!important，那么其所有定义会被忽略。 `Partial Click
Bug v2 <http://haslayout.net/css/view?tut=Partial-Click-Bug-v2>`__ IE8以
设置了整个区域是可以点击的，但在IE中只有文本可以点击。 `Staircase
Bug <http://haslayout.net/css/view?tut=Staircase-Bug>`__ below IE8
浮动的元素排序起来就像一个楼梯。 `Disappearing List Background
Bug <http://haslayout.net/css/view?tut=Disappearing-List-Background-Bug>`__
IE6 B

,

,

没有背景。 `noscript Ghost
Bug <http://haslayout.net/css/view?tut=noscript-Ghost-Bug>`__ IE8 and
below

标识中只有 borders/background 才有用。 `No Transparency Click
Bug <http://haslayout.net/css/view?tut=No-Transparency-Click-Bug>`__ IE8
and below
背景透明的图片在作为链接时，并且其“filter”被设置成了PNG透明，但其背景还是不可点击。
`List Drop Shift
Bug <http://haslayout.net/css/view?tut=List-Drop-Shift-Bug>`__ IE8 在

中的内容被换行了。 `No Increase
on <http://haslayout.net/css/view?tut=No-Increase-on--ol--Numbers-Bug>`__

Numbers Bug below IE8

中的

列表序号不会增加。 `No Bullets
on <http://haslayout.net/css/view?tut=No-Bullets-on--ul--and--ol--Bug>`__

and

Bug below IE8 在

和

中看不到列表序号/数字了。 `No line-height Vertical Center on Images
Bug <http://haslayout.net/css/view?tut=No-line-height-Vertical-Center-on-Images-Bug>`__
IE8以下版 图片使用line-height 方法不能垂直居中 `No Background Image
Bug <http://haslayout.net/css/view?tut=No-Background-Image-Bug>`__
IE8及以下版 在IE中使用background无法定义背景图 `Custom Cursor
Bug <http://haslayout.net/css/view?tut=Custom-Cursor-Bug>`__ IE8及以下版
自定义鼠标不工作 `Leaking Background
Bug <http://haslayout.net/css/view?tut=Leaking-Background-Bug>`__ IE6
背景从一个元件的内部溢出到外部 `Expanding Height
Bug <http://haslayout.net/css/view?tut=Expanding-Height-Bug>`__ IE6
元件的高度比指定的要长得多。 `Expanding Width
Bug <http://haslayout.net/css/view?tut=Expanding-Width-Bug>`__ IE6
元件的宽度比指定的要长得多。 `Double Margin
Bug <http://haslayout.net/css/view?tut=Double-Margin-Bug>`__ IE6
float元件的左和右的空白（margins）被加倍了。 `Negative Margin
Bug <http://haslayout.net/css/view?tut=Negative-Margin-Bug>`__ IE8以下版
如果使用负数来指定页白（margins）里面的元件会被外面的元件所遮挡。
`Italics Float
Bug <http://haslayout.net/css/view?tut=Italics-Float-Bug>`__ IE6
float的元件中的字体会被设置成倾斜。 `3px Gap Bug aka Text Jog
Bug <http://haslayout.net/css/view?tut=3px-Gap-Bug-aka-Text-Jog-Bug>`__
IE6 下一个float的元件不是有一个3px的空隙，就是被换行了。 `Text-Align
Bug <http://haslayout.net/css/view?tut=Text-Align-Bug>`__ IE8以下版
text-align属性会影响整个元件内的所有内容。

布局类 Bug
^^^^^^^^^^

名称 IE的版本 描述

`Border Chaos
Bug <http://haslayout.net/css/view?tut=Border-Chaos-Bug>`__ IE6
连框显示是混乱的 `Sub-Hover
Bug <http://haslayout.net/css/view?tut=Sub-Hover-Bug>`__ IE6
一些selectors 如 a:hover foo{} 无法正常工作 `Partial Click
Bug <http://haslayout.net/css/view?tut=Partial-Click-Bug>`__ IE6
在定义了display: block的链接中() 只有文本是可以点的。 `Disappearing
Content
Bug <http://haslayout.net/css/view?tut=Disappearing-Content-Bug>`__ IE6
当我们滚动窗口的时候，或是最大化最小化窗品的时候，有一些内容会重复显示。

不支持的功能
^^^^^^^^^^^^

名称 IE的版本 描述

`No Child Selector Support
Workaround <http://haslayout.net/css/view?tut=No-Child-Selector-Support-Workaround>`__
IE6 子 selector 无效 `Max-Height
Workaround <http://haslayout.net/css/view?tut=Max-Height-Workaround>`__
IE6 max-height 无效 `Max-Width
Workaround <http://haslayout.net/css/view?tut=Max-Width-Workaround>`__
IE6 max-width 无效
`Opacity <http://haslayout.net/css/view?tut=Opacity>`__ IE8及以下版
opacity 属性无效 `Min-Width
Workaround <http://haslayout.net/css/view?tut=Min-Width-Workaround>`__
IE6 min-width 属性无效 `Min-Height
Workaround <http://haslayout.net/css/view?tut=Min-Height-Workaround>`__
IE6 min-height 属性无效

程序崩溃 Bug
^^^^^^^^^^^^

这个BUG可以导致整个 IE 崩溃。

名称 IE的版本 描述

`Hover Crash Bug <http://haslayout.net/css/view?tut=Hover-Crash-Bug>`__
IE6 当你把鼠标移上 :hover 的链接时，浏览器会崩溃

(全文完)

.. |ie-bug| image:: /coolshell/static/20140922105602891000.jpg
.. |image7| image:: /coolshell/static/20140922105602993000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1245.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com