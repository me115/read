.. _200904_float_clearing:

浮动元素容器的clearing问题
=============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/04/float_clearing.html>`__

网页设计时，我经常遇到下面这个问题，一直不知道怎么解决。

今天，总算全部理解了，一定要写下来。

**1. 问题的由来**

有这样一种情形：在一个容器（container）中，有两个浮动的子元素，如图一。

    （图一 设计视图是一个父容器中含有二个浮动的子元素）

请问HTML代码应该怎么写？

很简单啦，几行字就够了。

上面的代码完全正确，但是如果在浏览器中一运行，就会出现意想不到的结果。

    （图二 实际视图是子元素显示在父容器的外部）

两者好像脱离了关系一样，怎么会这样？

**2. 问题的原因**

其实，原因很简单，与浮动定位有关。

在CSS规范中，浮动定位不属于正常的页面流（page
flow），是独立定位的。所以，只含有浮动元素的父容器，在显示时不考虑子元素的位置，就当它们不存在一样。这就造成了显示出来，父容器好像空容器一样。

**3. 解决方法一：添加空元素**

经典的解决方法，就是在浮动元素下方添加一个非浮动元素，就像图三。

    （图三 在父容器底部添加一个非浮动元素）

代码这样写：

    ****

这样一来，就没问题，能够正常显示了。原理是父容器现在必须考虑非浮动子元素的位置，而后者肯定出现在浮动元素下方，所以显示出来，父容器就把所有子元素都包括进去了。

这种方法比较简单，但是要在页面中增加冗余标签，违背了语义网的原则。那么，有没有不修改HTML代码的方法呢？

**4. 解决方法二：浮动的父容器**

另一种思路是，索性将父容器也改成浮动定位，这样它就可以带着子元素一起浮动了。

代码这样写：

    style=”float:left;”>

这种方法不用修改HTML代码，但是缺点在于父容器变成浮动以后，会影响到后面元素的定位，而且有时候，父容器是定位死的，无法变成浮动。

**5. 解决方法三：浮动元素的自动clearing**

它的思路是让父容器变得可以自动”清理”（clearing）子元素的浮动，从而能够识别出浮动子元素的位置，不会出现显示上的差错。

要做到这点，只要为父容器加上一条”overflow:
hidden”的CSS语句就行了。代码这样写：

    style=”overflow: hidden;”>

这种方法的缺点主要有二个，一个是IE
6不支持，另一个是一旦子元素的大小超过父容器的大小，就会出显示问题。

**6. 解决方法四**

还是回到方法一，能不能通过CSS语句添加子元素呢，这样就不用修改HTML代码了？

回答是可以的，我们知道CSS语句中有一个:after伪选择符，就可以在父容器的尾部自动创建一个子元素，这正好符合我们的需要。

下面的代码参照了\ `lifesinger <http://lifesinger.org/blog/?p=614>`__\ 的写法：

    | .clearfix:after { content: “\\0020”; display: block; height: 0;
    |  clear: both;
    |  }

其中的”clearfix”是父容器的class名称，”content:”020”;”是在父容器的结尾处放一个空白字符，”height:
0;”是让这个这个空白字符不显示出来，”display: block; clear:
both;”是确保这个空白字符是非浮动的独立区块。

但是，:after选择符IE 6不支持，也就是说上面的这段代码在IE
6中无效，这怎么办？

我们添加一条IE
6的独有命令”zoom:1;”就行了，这条命令的作用是激活父元素的”hasLayout”属性，让父元素拥有自己的布局。（它的具体含义，请参见本文的附录。）IE
6会读取这条命令，其他浏览器则会直接忽略它。

**7. 最后的生产代码**

    | .clearfix:after { content: “\\0020”; display: block; height: 0;
    |  clear: both;
    |  }

    | .clearfix {
    |  zoom: 1;
    |  }

**更新 2011.04.21**

`Nicolas
Gallagher <http://nicolasgallagher.com/micro-clearfix-hack/>`__\ 贴出了更通用的生产代码。

    | /\* For modern browsers \*/ .cf:before, .cf:after {
    　　content:”“;
    |  　　display:block;
    |  }

    | .cf:after {
    |  　　clear:both;
    |  }

    | /\* For IE 6/7 (trigger hasLayout) \*/ .cf {
    |  　　zoom:1;
    |  }

[参考阅读]

\* `PPK: Clearing
floats <http://www.quirksmode.org/css/clearing.html>`__

\* `How To Clear Floats Without Structural
Markup <http://www.positioniseverything.net/easyclearing.html>`__

\* `mezzoblue:
Clearance <http://www.mezzoblue.com/archives/2005/03/03/clearance/>`__


====================

**附录 什么是hasLayout**

（以下内容摘自CSS Mastery一书的中译本《精通CSS
高级Web标准解决方案》第154页，人民邮电出版社，2007）

IE使用Layout概念来控制元素的尺寸和位置。如果一个元素有Layout，它就有自身的尺寸和位置；如果没有，它的尺寸和位置由最近的拥有布局的祖先元素控制。

在默认情况下，拥有Layout的元素包括：

    ````

    ,

    ````

    ,

    ,

    ,

    ````

    ````

    --------------

    ``, ``

    , ,

    ,

    ,

    ``, ``

    ,

    ,

    ````

    （注意，

    和

    默认不拥有Layout。）

    凡是具有以下CSS属性的元素，也会拥有布局：

        -  position: absolute
        -  float: left\|right
        -  display: inline-block
        -  width: any value other than ‘auto’
        -  height: any value other than ‘auto’
        -  zoom: any value other than ‘normal’ （IE专用属性）
        -  writing-mode: tb-rl（IE专用属性）
        -  overflow: hidden\|scroll\|auto（只对IE 7及以上版本有效）
        -  overflow-x\|-y: hidden\|scroll\|auto（只对IE
           7及以上版本有效）

    hasLayout是IE特有的属性，不是CSS属性。可以用Javascript函数hasLayout查看一个元素是否拥有Layout。如果有，这个函数就返回true；否则返回false。hasLayout是一个只读属性，所以无法使用Javascript进行设置。

    [参考阅读]

    \* `On having
    layout <http://www.satzansatz.de/cssd/onhavinglayout.html>`__

    （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/04/float_clearing.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com