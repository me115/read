.. _201004_css_speech_bubbles:

制作css气泡框
================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/04/css_speech_bubbles.html>`__

气泡状文本框，是一种很生动的网页设计手段。

它可以用来表示用户的发言。

也可以用来作为特定信息的提示符。

DVD租借网站Netflix，还用它显示碟片的详细信息。


=========================

制作CSS气泡框的传统方法，需要5张背景图片，分别是：

| 　　\* |image0| tl.gif，左上方的圆角。
|  　　\* |image1| tr.gif，右上方的圆角。
|  　　\* |image2| bl.gif，左下方的圆角。
|  　　\* |image3| br.gif，右下方的圆角。
|  　　\* |image4| angle.gif，突出的三角形。

现在假定有这样一段代码：

    　　

        床前明月光，疑是地上霜。

    　　

    李白

我们希望通过气泡框，产生一种视觉效果，将李白与诗句对应起来。

那么，首先需要为诗句添加四个”钩子”（handler）：

    　　

    　　　

    　　　　

    　　　　　

    　　　　　　

        床前明月光，疑是地上霜。

    　　　　　

    　　　　

    | 
    |  　　　

    | 
    |  　　

然后，为最外面的容器div.tl指定高度和宽度，使它形成一个视觉方框：

    | 　　.tl{ 　　　　width:300px; 　　　　height:50px;
    　　　　text-align:center;
    |  　　　　line-height:50px;
    |  　　}

接着，为四个”钩子”依次添加四个不同的圆角背景：

    | 　　.tl{background:url(‘tl.gif’) top left no-repeat #ff8c45;}
    　　.tr{background:url(‘tr.gif’) top right no-repeat;}
    |  　　.bl{background:url(‘bl.gif’) bottom left no-repeat;}
    |  　　.br{background:url(‘br.gif’) bottom right no-repeat;}

最后，在”李白”前面加上三角形图片。

    | 　　p{ 　　　　padding: 15px 0px 0px 50px;
    |  　　　　background: url(‘angle.gif’) 40px top no-repeat;
    |  　　}

气泡框就生成了。

这种方法的优点是所有浏览器都支持，缺点是比较麻烦，必须制作专门的图片，增加多余的标签，代码的灵活性较小。


============================

随着CSS3的出现，现在有了更好的方法，不需要任何背景图片和多余的标签，就能生成漂亮的文本框。

请看新方法发明人\ `Nicolas
Gallagher <http://nicolasgallagher.com/progressive-enhancement-pure-css-speech-bubbles/>`__\ 制作的范例：

由于这种方法用到了CSS3，所以IE6不支持，IE7和IE8无法显示圆角效果。其他浏览器的最新版本，都能够正常显示。

还是以前面的代码为例。

    　　

        床前明月光，疑是地上霜。

第一步，生成基本的方框。

    | 　　.bubble{ 　　　　position:relative; 　　　　padding:15px;
    　　　　margin:1em 0em 3em; 　　　　width:300px;
    　　　　line-height:1.2; 　　　　text-align:center;
    　　　　color:#fff;
    |  　　　　background:#075698;
    |  　　}

第二步，生成圆角。

    | 　　.bubble{ 　　　　-moz-border-radius:10px;
    　　　　-webkit-border-radius:10px;
    |  　　　　border-radius:10px;
    |  　　}

第三步，制作线性渐变的效果。

    | 　　.bubble{ 　　　　background:-webkit-gradient(linear, left top,
    left bottom, from(#f9d835), to(#f3961c));
    　　　　background:-moz-linear-gradient(top, #f9d835, #f3961c);
    　　　　background:-o-linear-gradient(top, #f9d835, #f3961c);
    |  　　　　background:linear-gradient(top, #f9d835, #f3961c);
    |  　　}

第四步，在容器后面添加一个空元素，并将长度和宽度都设为0。

    | 　　.bubble:after { 　　　　content:”\\00a0”; 　　　　width:0;
    |  　　　　height:0;
    |  　　}

第五步，指定这个空元素为块级元素，并且四个边框之中，只显示上方的边框，其他三个边框，都设为透明。因为该元素的大小为0，所以它的每一个边框，都是一个等腰三角形。

    | 　　.bubble:after{ 　　　　display:block;
    　　　　border-style:solid; 　　　　border-width:15px;
    |  　　　　border-color:#f3961c transparent transparent transparent;
    |  　　}

这时，已经可以看见这个三角形了（其实是一个上边框）。

第六步，指定空元素的定位方式为absolute。然后，以容器元素的左下角为基点，将空元素水平右移一定的距离（这里是50像素），再垂直下移两个边界的距离。（由于第五步将空元素的边界设为15像素，所以这里就是下移30像素。）

    | 　　.bubble:after{ 　　　　position:absolute; 　　　　z-index:-1;
    　　　　bottom:-30px;
    |  　　　　left:50px;
    |  　　}

至此，一个不需要任何背景图片和多余标签的气泡框，就出现在我们眼前了。

灵活处理空元素的边框，或者改变大小，或者生成圆角，或者将两个空元素的边框重叠，就会产生各种各样的变化。具体的效果和代码，请参考\ `Nicolas
Gallagher <http://nicolasgallagher.com/demo/pure-css-speech-bubbles/bubbles.html>`__\ 的范例页。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/04/css_speech_bubbles.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com