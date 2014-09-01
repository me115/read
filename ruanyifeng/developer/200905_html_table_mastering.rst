.. _200905_html_table_mastering:

精通html表格的使用
=====================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/05/html_table_mastering.html>`__

制作网页表格，需要使用table标签。

用好table标签并不容易，复杂的表格做起来就很麻烦，比如下面这张表。

我整理了一些HTML表格的高级语法。你可以看看，自己会用多少？

**1. 标题和内容描述**

表格的标题用caption标签表示，它会自动出现在整张表格的上方。

除了标题以外，对内容的更长描述可以写在table标签的summary属性中。

代码示例（为了便于阅读，tr、th、td省略关闭标签）：

    　

    *a test table with merged cells*

    　

    average 　

    | red
    | eyes 　

    height

    weight 　

    males

    1.9

    0.003

    | 40%
    |  　

    females

    1.7

    0.002

    | 43%

在浏览器中的显示效果如下图：

**2. 表头和表尾**

从结构上看，表格可以分成表头、主体和表尾三部分，在HTML语言中分别用thead、tbody、tfoot表示。

代码示例：

    | 

    | 
    |  　　

    *…header information…*

    | 

    | 
    |  　　

    *…footer information…*

    | 

    | 
    |  　　

    | *…first row of block one data…*
    |  　　

    *…second row of block one data…*

    | 

    | 
    |  　　

    | *…first row of block two data…*
    |  　　

    | *…second row of block two data…*
    |  　　

    | *…third row of block two data…*

    | 

这里有三个注意点：

    1）thead和tfoot在一张表中都只能有一个，而tbody可以有多个。

    2）tfoot必须出现在tbody前面，这样浏览器在接收主体数据之前，就能渲染表尾，有利于加快表格的显示速度。这一点对大型表格尤其重要。

    3）thead、tbody和tfoot里面都必须使用tr标签。

**3. 列的分组**

tbody可以用来对”行”进行分组，而colgroup则用来对”列”进行分组。

比如，下面的代码表示前40列为一组，每列的宽度为20像素。

    　　
     　　

span属性，可以指定colgroup标签能够影响到的列数。

在colgroup标签内部，可以使用col标签为这一列组中的每一列指定属性。

比如，下面的代码表示列组中每一列的段度为20像素：

    　　
    　　
     　　
     　　*…a total of forty COL elements…*
     　　

再比如，如果40列中只有最后一列的样式不一样，那就这样写，方便在CSS中指定：

    　　
    　　
     　　
     　　

**4. CSS中的table-layout语句**

这个语句可以用来指定表格显示的样式，比如

    table { table-layout: fixed }

它可以取三个值：

    | \* auto（缺省）
    |  \* fixed
    |  \* inherit

auto表示单元格的大小由内容决定。fixed表示单元格的大小是固定的，由第一个指定大小的单元格决定；如果所有单元格都没有指定大小，则由第一个单元格的默认大小决定；如果单元格中的内容超出单元格的大小，则用CSS中的overflow命令控制。微软公司声称使用这个命令，表格的显示速度可以加快100倍。

顺便说一句，为了加快表格显示，最好事先就在CSS（或者table标签的width和height属性）中指定表格的宽度和高度。

**5. th和td**

表示单元格的标签是th（table head）和td（table
data），前者用来显示数据的名称，后者用来显示数据的内容。

代码示例：

    　

    　

    　　

    Month

    　　

    Savings

    　

    　

    　　

    January

    　　

    $100

    | 
    |  　

    | 
    |  　

这两个标签有一些很复杂的属性，分别是abbr、axis、char、headers和scope，详细解释参阅\ `这里 <http://www.w3schools.com/TAGS/tag_td.asp>`__\ 。

**6. frame和rules**

table标签的frame和rules属性，可以控制边框的显示。frame属性控制着表格最外围的四条边框的可见性，而
rules 则控制着表格内部边框的可见性。

frame属性可取的值及含义如下：

    | \* void - 默认值。表示不显示表格最外围的边框。 \* box -
    同时显示四条边框。 \* border - 同时显示四条边框。 \* above -
    只显示顶部边框。 \* below - 只显示底部边框。 \* lhs -
    只显示左侧边框。 \* rhs - 只显示右侧边框。
    |  \* hsides - 只显示水平方向的两条边框。
    |  \* vsides - 只显示垂直方面的两条边框。

rules 属性可取的值有五个，分别是：

    | \* none - 默认值。无边框。 \* groups - 为行组或列组加边框。 \*
    rows - 为行加边框。
    |  \* cols - 为列加边框。
    |  \* all - 为所有行列（单元格）加边框

代码示例：

         

    My Ultimate Table

         

         

         

              

    cell 1-1

              

    cell 1-2

              

    cell 1-3

              

    cell 1-4

         

         

              

    cell 4-1

              

    cell 4-2

              

    cell 4-3

              

    cell 4-4

         

         

              

    cell 2-1

              

    cell 2-2

              

    cell 2-3

              

    cell 2-4

         

         

              

    cell 3-1

              

    cell 3-2

              

    cell 3-3

              

    cell 3-4

         

    | 

    | 

在浏览器中的显示效果如下图：

[延伸阅读]

\* `HTML
4.0语言中的Table模型 <http://www.w3.org/TR/html4/struct/tables.html>`__

\* `理解表格一：图解frame 和rules
属性 <http://www.cn-cuckoo.com/2007/08/23/the-frame-and-rules-attributes-of-table-element-98.html>`__

\*
`理解表格二：其他表格相关标签及属性 <http://www.cn-cuckoo.com/2007/08/26/other-markup-and-relative-properties-of-table-115.html>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/05/html_table_mastering.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com