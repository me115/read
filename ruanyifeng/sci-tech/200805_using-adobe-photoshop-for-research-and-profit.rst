.. _200805_using-adobe-photoshop-for-research-and-profit:

巧用Photoshop进行科学研究
============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/05/using-adobe-photoshop-for-research-and-profit.html>`__

**巧用Photoshop进行科学研究**

原文网址：\ `Jacks of
Science <mailto:http://www.jacksofscience.com/general/using-adobe-photoshop-for-research-and-profit/>`__

译者：阮一峰

Photoshop CS3
Extended是一个强大的软件。你可以用它，让你的报名照变得漂亮一些，然后上传到社交网站上；你也可以将一个名人的脑袋，移植到一张裸体照片上。但是，你知道吗，Photoshop还可以用来完成很多图片测量工作？

用Photoshop处理图片非常简单和有趣。甚至有好几本书，教你如何用Photoshop进行\ `法医研究 <http://www.amazon.com/Photoshop-CS3-Forensics-Professionals-Investigators/dp/0470114541>`__\ 。

我最近在网站Lynda.com上读到两个教程，一个是\ `《生物医学研究中的Photoshop应用》 <http://movielibrary.lynda.com/html/modPage.asp?ID=470>`__\ ，另一个是\ `《科研工作中的Photoshop》 <http://movielibrary.lynda.com/html/modPage.asp?ID=526>`__\ 。后者一步步地教你，如何从一个组织样本中分析出蛋白质的表达式。但是，我想大多数读者应该对这种生物医学的课题，没有多大兴趣。所以，我决定把这种技巧，用到其他方面去。

在本文中，我会简单列出几个Photoshop测量工具的应用方法，它们非常有用。请注意，本教程假设，你已经掌握了一些基本知识，比如如何打开图片、如何使用层、以及如何选择图片的不同部分。

**一、测量积木塔的斜度**

你用积木搭起了一座斜塔，你想比较一下，它是否斜得同著名的比萨斜塔一样。

    | 1. 用Ruler
    Tool沿塔的斜边，画出一条直线。然后在窗口顶部的Options工具条上读出A值。
    |  2. 另一种方法是，从Analysis下拉菜单中，选择Record
    Measurements，然后拉动滚动条，从Measurements Log读出角度。

比萨斜塔的斜度大约是86.03°，因此这个模型搭得不错！

**二、测量月球的圆度值**

在Photoshop中，圆度值（Circularity）是这样定义的：它在数值上等于”4\*Pi\*面积/周长”，这个值越接近1，就意味着形状越接近圆形。

用这个值可以做很多有趣的事情，比如你可以比一比，你和同学，谁的头更圆一些。

我测量了月亮在一个盈亏周期中的圆度值。

    1. 使用Magic Wand选择背景区域。

    2. 使用”Select > Inverse”进行反选，这样就可以得到月亮的形状。

    3. 用与上例类似的方法，打开Analysis和Record Observations命令。

    4. 在Measurement Log中记录Circularity的值。

有一种传说，狼人总是在月圆之夜变身。现在你只用Photoshop和数码相机，就可以知道那是一月中的哪一个夜晚了。

**三、测量糖果数**

    1. 使用Magic Wand工具，选择图片中的一粒绿色的糖果。

    2. 从Select下拉菜单中，选择
    Similar命令，将选区扩张到整张图片。你可能需要反复调整tolerance的数值。

    3. 一旦选择完毕，打开”Analysis > Record Observations”菜单。

    4. 观察Measurement
    Log中的Count值，你就会看到有多少粒绿色糖果被选中了。

我用上面的方法，得到的数字是70，然后我又手工数了一遍，一共是74粒。误差不算大。这种方法还可以用来数脸上的雀斑、天上的星星，以及其他颜色有明显区别的物体。

**四、测量牙齿增白剂的效果**

市场上有一种叫做Crest Teeth
Whitening的牙齿增白剂的产品，是一种含有过氧化氢的化合物，据说可以让你的牙齿变白。

我在网上搜来搜去，也用不到有用的评论。看来，客观地记录牙齿是否变白，并不是很容易的事情。但是如果有了photoshop，难事就会变容易。

    1. 将你露齿一笑的照片，在Photoshop CS3 Extended中打开。

    2. 用Rectangular Marquee在你想要比较的牙齿上，选择一个样本区。

    3. 打开Analysis和Record Measurements菜单。

    4. 在跳出窗口中，找到”Mean Gray Value”这一项，记录它的数值。

    5. 当增白剂疗程结束后，重复1-4步。

“Mean Gray
Value”这个值的取值范围是0到255之间，如果这个值变大了，那么你的牙齿就是真的变白了。

**五、计算Kirsten Dunst的身高**

如果你看过电影《蜘蛛人》，那么你也许记得里面的女演员Kirsten
Dunst。然后你又得到了一张她的照片，她手中的书是卡尔·萨根的\ `“The
Varieties of Scientific
Experience” <http://www.amazon.com/Varieties-Scientific-Experience-Personal-Search/dp/1594201072>`__\ 。你从亚马逊网上书店查到，该书的高度是9.2英寸。然后，你就可以计算Kirsten
Dunst的身高了。

    1. 打开Analysis菜单，选择”Set Measurement Scale >
    Custom”命令，然后就可以新建一套新的测量比例。

    2. 在Measurement Scale对话框中，点击并拖曳Ruler
    tool工具，画出书的长度。

    3. 将9.2英寸填入对话框中，点击OK。以后的所有测量都会参照这个比例尺。

    4. 用一系列测量，得到Kirsten Dunst每一部分的高度，然后加总。

我最后得到的结果是67英寸，也就是65英尺7英寸。这比\ `Chickipedia <http://www.chickipedia.com/Kirsten_Dunst>`__\ 上记载的身高，略高了一点。

**六、估算非洲有多少只鸡**

要想知道非洲鸡的数量，首先必须有一张鸡密度图。感谢上帝，从google里你就可以找到这样的图。你必须对这张图做一些预处理，这稍微有点麻烦。然后，Photoshop中的”Integrated
Density”命令，可以完成接下来的事，这个命令的作用是得到选择区域中的平均灰度值。

预处理的步骤非常乏味，所以我只是简单说一下：

    1. 建立一个选择区，包括所有非洲大陆和它的岛屿。

    2. 将比例尺定为公里。

    3. 将所有表示政区边界的颜色，都替换成与邻近区域相近的颜色。

    4. 将整张图转为灰度状态。

做完这些麻烦的事情以后，确定你已经将非洲选择了出来，然后打开”Analysis >
Record
Measurements”菜单。你应该会看到许多内容，其中有一项会告诉你，选择区域的总面积是3011万平方公里，这很接近非洲3000万平方公里的实际面积。

然后，你使用”Integrated
Density”命令，得到这个区域的平均灰度值是36.32。由于灰度值的最大值是255，所以你必须将36.32除以255，再乘以125。这是因为每平方公里最大的鸡数目是125。最后的结果是，非洲大陆每平方公里有18只鸡。

再乘以非洲大陆的面积，就得到非洲一共有5.42亿只鸡。每平方公里18只鸡，似乎有点太大了，毕竟非洲有很多地方都是沙漠，但是谁知道呢！

正如你所见，Photoshop是一个如此强大的工具，难怪它的售价高达1000美元！你还能想到用它来做什么有趣的测量工作？

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/05/using-adobe-photoshop-for-research-and-profit.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com