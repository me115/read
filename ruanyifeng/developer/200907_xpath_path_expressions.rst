.. _200907_xpath_path_expressions:

xpath路径表达式笔记
======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/07/xpath_path_expressions.html>`__

简单说，xpath就是选择XML文件中节点的方法。

所谓节点（node），就是XML文件的最小构成单位，一共分成7种。

    | - element（元素节点） - attribute（属性节点） - text （文本节点）
    - namespace （名称空间节点） - processing-instruction
    （处理命令节点）
    |  - comment （注释节点）
    |  - root （根节点）

xpath可以用来选择这7种节点。不过，下面的笔记只涉及最常用的第一种element（元素节点），因此可以将下文中的节点和元素视为同义词。

**一、xpath表达式的基本格式**

| xpath通过”路径表达式”（Path
Expression）来选择节点。在形式上，”路径表达式”与传统的文件系统非常类似。

    | # 斜杠（/）作为路径内部的分割符。 #
    同一个节点有绝对路径和相对路径两种写法。 # 绝对路径（absolute
    path）必须用”/”起首，后面紧跟根节点，比如/step/step/…。 #
    相对路径（relative path）则是除了绝对路径以外的其他写法，比如
    step/step，也就是不使用”/”起首。 # “.”表示当前节点。
    |  # “..”表示当前节点的父节点

**二、选择节点的基本规则**

    | - nodename（节点名称）：表示选择该节点的所有子节点 -
    “/”：表示选择根节点 - “//”：表示选择任意位置的某个节点
    |  - “@”： 表示选择某个属性

**三、选择节点的实例**

先看一个XML实例文档。

           Harry Potter

    | 
    |      29.99
    |    

           Learning XML

    | 
    |      39.95
    |    

[例1]

bookstore ：选取 bookstore 元素的所有子节点。

[例2]

/bookstore ：选取根节点bookstore，这是绝对路径写法。

[例3]

bookstore/book ：选取所有属于 bookstore 的子元素的
book元素，这是相对路径写法。

[例4]

//book ：选择所有 book 子元素，而不管它们在文档中的位置。

[例5]

bookstore//book ：选择所有属于 bookstore 元素的后代的 book
元素，而不管它们位于 bookstore 之下的什么位置。

[例6]

//@lang ：选取所有名为 lang 的属性。

**四、xpath的谓语条件（Predicate）**

所谓”谓语条件”，就是对路径表达式的附加条件。

所有的条件，都写在方括号”[]”中，表示对节点进行进一步的筛选。

[例7]

/bookstore/book[1] ：表示选择bookstore的第一个book子元素。

[例8]

/bookstore/book[last()] ：表示选择bookstore的最后一个book子元素。

[例9]

/bookstore/book[last()-1] ：表示选择bookstore的倒数第二个book子元素。

[例10]

/bookstore/book[position()

| [例11]
|  //title[@lang] ：表示选择所有具有lang属性的title节点。

[例12]

//title[@lang=’eng’] ：表示选择所有lang属性的值等于”eng”的title节点。

[例13]

/bookstore/book[price]
：表示选择bookstore的book子元素，且被选中的book元素必须带有price子元素。

| [例14]
|  /bookstore/book[price>35.00]
：表示选择bookstore的book子元素，且被选中的book元素的price子元素值必须大于35。

[例15]

/bookstore/book[price>35.00]/title
：表示在例14结果集中，选择title子元素。

[例16]

/bookstore/book/price[.>35.00]
：表示选择值大于35的”/bookstore/book”的price子元素。

**五、通配符**

    # “\*”表示匹配任何元素节点。

    | # “@\*”表示匹配任何属性值。
    |  # node()表示匹配任何类型的节点。

[例17]

//\* ：选择文档中的所有元素节点。

[例18]

| /\*/\* ：表示选择所有第二层的元素节点。
|  [例19]

| /bookstore/\* ：表示选择bookstore的所有元素子节点。
|  [例20]

//title[@\*] ：表示选择所有带有属性的title元素。

**六、选择多个路径**

用”\|”选择多个并列的路径。

[例21]

//book/title \| //book/price
：表示同时选择book元素的title子元素和price子元素。

【相关文章】

\*
`CSS选择器笔记 <http://www.ruanyifeng.com/blog/2009/03/css_selectors.html>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/07/xpath_path_expressions.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com