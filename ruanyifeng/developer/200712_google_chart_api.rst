.. _200712_google_chart_api:

Google Chart API
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2007/12/google_chart_api.html>`__

上周，Google公布了制图服务（Google
Chart）的接口，可以用来为统计数据自动生成图片。

这项服务用起来相当简单，不用安装任何软件，只使用浏览器就可以。比如，在浏览器的地址栏中，键入如下的地址：

`http://chart.apis.google.com/chart?cht=p3&chd=s:hW&chs=250x100&chl=Hello\|World&chtt=Hello+World <http://chart.apis.google.com/chart?cht=p3&chd=s:hW&chs=250x100&chl=Hello|World&chtt=Hello+World>`__\ ，

就可以看到下面的图片：

|image0|

各个参数的含义：

　　\* cht（chart type）：图表种类，cht=p3表示生成3D饼图。

　　\* chs（chart
size）：图表面积，chs=250x100表示宽200像素，高100像素。

　　\* chtt（chart title）：图表标题，chtt=Hello+World表示标题是Hello
World。

　　\* chd（chart data）：图表数据，chd=s:hW表示数据是普通字符串（simple
string）hW。目前，允许的编码选择有simple (s)、extended (e)和text (t)。

目前，Google Chart一共提供五种图，分别是折线图（line
charts）、条状图（bar charts）、饼图（pie charts）、Venn图（venn
diagrams）和散点图（scatter plots）。

|googlechartex.png|

下面，我根据\ `说明文档 <http://code.google.com/apis/chart/>`__\ ，简单介绍一下，如何生成最常见的条状图和饼图。

**条状图**

下面这张表是各大洲最高峰一览表。

山峰高度（单位：米）珠穆朗玛峰（亚洲）8848乞力马扎罗山（非洲）5895厄尔布鲁士山（欧洲）5642麦金利山（北美）6194阿空加瓜山（南美）6960查亚山（大洋洲）5029文森山（南极洲）5140

根据上表，可以生成下面的条状图：

使用的网址是：

    **`http://chart.apis.google.com/chart? chs=250x250&
    chd=t:88.48,58.95,56.42,61.94,69.60,50.29,51.40& cht=bvs&
    chco=ff0000& chf=c,s,76A4FB\|bg,s,FFF2CC&
     chxt=x,y&

    chxl=0:\|Asia\|Afri\|Euro\|AmeN\|AmeS\|Ocea\|Anta\|1:\|0\|5km\|10km <http://chart.apis.google.com/chart?chs=250x250&chd=t:88.48,58.95,56.42,61.94,69.60,50.29,51.40&cht=bvs&chco=ff0000&chf=c,s,76A4FB|bg,s,FFF2CC&chxt=x,y&chxl=0:|Asia|Afri|Euro|AmeN|AmeS|Ocea|Anta|1:|0|5km|10km>`__**

虽然这个网址看起来很复杂，但实际上很容易编写，请跟着我一项项分解：

**1. http://chart.apis.google.com/chart?**

这部分是google图表服务的网址，所有生成的图表都必须使用这个网址。

“？”后面跟的是参数，格式是”参数名=参数值”。不同的参数之间用”&”分割，次序无所谓。

**2. chs=250x250**

这一项表示图片的面积，宽x长，单位是像素。

面积最大不能超过30万像素，长和宽最大不超过1000像素。比如，如果上图放大一倍，可以使用\ `chs=500x500 <http://chart.apis.google.com/chart?chs=500x500&chd=t:88.48,58.95,56.42,61.94,69.60,50.29,51.40&cht=bvs&chco=ff0000&chf=c,s,76A4FB|bg,s,FFF2CC&chxt=x,y&chxl=0:|Asia|Afri|Euro|AmeN|AmeS|Ocea|Anta|1:|0|5km|10km>`__\ 。

**3. chd=t:88.48,58.95,56.42,61.94,69.60,50.29,51.40**

这一项”chd=t:”表示图表所用的数据集，最小的值是0.0，最大的值是100.0。

因此，山峰的高度必须改写为88.48、58.95、56.42、61.94、69.60、50.29、51.40，数据与数据之间用逗号分割。

**4. cht=bvs**

这一项表示所使用的图表类型，bvs表示”竖直条形图”，bhs表示”水平条形图”，\ `lc <http://chart.apis.google.com/chart?chs=250x250&chd=t:88.48,58.95,56.42,61.94,69.60,50.29,51.40&cht=lc&chco=ff0000&chf=c,s,76A4FB|bg,s,FFF2CC&chxt=x,y&chxl=0:|Asia|Afri|Euro|AmeN|AmeS|Ocea|Anta|1:|0|5km|10km>`__\ 表示折线图。

**5. chco=ff0000**

这一项表示条块的颜色，ff0000表示红色。如果想生成蓝色条块，就使用\ `0000ff <http://chart.apis.google.com/chart?chs=250x250&chd=t:88.48,58.95,56.42,61.94,69.60,50.29,51.40&cht=bvs&chco=0000ff&chf=c,s,76A4FBs|bg,s,FFF2CC&chxt=x,y&chxl=0:|Asia|Afri|Euro|AmeN|AmeS|Ocea|Anta|1:|0|5km|10km>`__\ 。

**6. chf=c,s,76A4FB\|bg,s,FFF2CC**

这一项表示填充色，其中又分为两个部分。

“c,s,76A4FB”表示内容部分（c）用蓝色（76A4FB）填充，”bg,s,FFF2CC”表示背景色（bg）用淡黄色（FFF2CC）填充。它们之间用竖线”\|”分割。

**7. chxt=x,y**

这一项表示坐标轴采用底部的x轴和左边的y轴。

**8.
chxl=0:\|Asia\|Afri\|Euro\|AmeN\|AmeS\|Ocea\|Anta\|1:\|0\|5km\|10km**

这一项表示坐标轴的刻度。

由于只能使用英语，所以x轴的刻度是各大洲的英语缩写，用”0:”开头，y轴的刻度是5千米和1万米，用”1:”开头，所有数据之间用竖线分割。

**饼图**

下面再举一个饼图的例子。

假定某商场上半年各月份的销售额占总销售额的比例，依次为19%、21%、14%、16%、15%和15%。那么画成饼图，就是下面的样子：

|image2|

使用的网址是：

    **
    `http://chart.apis.google.com/chart? chs=250x100&
    chd=t:19,21,14,16,15,15& cht=p3&
     chco=ff0000&

    chl=Jan\|Feb\|Mar\|Apr\|May\|June <http://chart.apis.google.com/chart?chs=250x100&chd=t:19,21,14,16,15,15&cht=p3&chco=ff0000&chl=Jan|Feb|Mar|Apr|May|June>`__**

与上面的条状图相比，只有两个地方需要说明。

**1. cht=p3**

这一项表示图片类型为三维饼图，如果使用二维饼图，这一项要改为”\ `cht=p <http://chart.apis.google.com/chart?chs=250x100&chd=t:19,21,14,16,15,15&cht=p&chco=ff0000&chl=Jan|Feb|Mar|Apr|May|June>`__\ “。

**2. chl=Jan\|Feb\|Mar\|Apr\|May\|June**

这一项表示为饼图中每一项数据加上图例。

更多的选项和如何使用多个数据集，请参考Google
Chart的\ `说明文档 <http://code.google.com/apis/chart/>`__\ 。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2007/12/google_chart_api.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com