.. _201004_the_solution_of_full_text_feed:

全文Feed的终极解决方案
=========================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/04/the_solution_of_full_text_feed.html>`__

正如我们都知道的，全文Feed最有用。

但是，世界上的大部分Feed，都是摘要Feed，甚至是标题Feed。我们只好自己动手，制作全文Feed。

传统的制作方法非常麻烦，需要针对不同的网站，编写不同的内容提取规则。要是有一个傻瓜型的”全文Feed生成器”，把摘要Feed往里面一扔，全文Feed就自动生成了，那该多好。

`FiveFilters.org <http://fivefilters.org/content-only/>`__\ 提供的生成器，大概最接近于这种要求。

|image0|

举例来说，网易的社会新闻Feed（\ `http://news.163.com/special/00011K6L/rss\_sh.xml <http://news.163.com/special/00011K6L/rss_sh.xml>`__\ ）是一个摘要Feed。

|image1|

我们把这个网址，送进FiveFilters.org，点击”Create
Feed”按钮，全文Feed就自动产生了！（\ `查看效果 <http://fivefilters.org/content-only/makefulltextfeed.php?url=http%3A%2F%2Fnews.163.com%2Fspecial%2F00011K6L%2Frss_sh.xml&key=&max=4&submit=Create+Feed>`__\ ）

但是，这个生成器并不是百用百灵，比如新浪的Feed（\ `http://rss.sina.com.cn/news/society/focus15.xml <http://rss.sina.com.cn/news/society/focus15.xml>`__\ ）就无法抓取全文。

好在今年3月份，它开源了。作者\ `Keyvan
Minoukadeh <http://www.keyvan.net>`__\ 将所有代码都公开了，所以如果遇到不能生效的Feed，现在我们就可以修改源码了。因此理论上，几乎所有的摘要Feed都可以自动转成全文Feed了。

源码存放在\ `launchpad.net <https://code.launchpad.net/~keyvan-k1m/fivefilters/content-only>`__\ 上，需要安装\ `Bazaar <http://bazaar.canonical.com/en/>`__\ 的客户端才能下载。我为大家提供方便，把它们压缩成一个zip文件，\ `点击下载 <http://www.ruanyifeng.com/blog/2010/04/full-text-rss.zip>`__\ （1.0版，217KB）。

下载后，上传到支持PHP
5.2的虚拟主机上，就可以直接使用。使用的时候，需要将cache子目录设为可写（权限777）。在config-sample.php文件中，可以查看设置选项，修改默认值后，将文件名改为config.php，就会生效。（不修改亦可，config文件并不是必需的。）

这个程序的核心是readability.php文件，它负责判断当前网页中，那一部分属于页面的主要内容，然后将其抓取出来。实现原理照搬了arc90的\ `ReadAbility脚本 <http://lab.arc90.com/experiments/readability/>`__\ 。简单说，思路是这样的：1）检查页面中所有p元素的父容器；2）根据相关特征，为每一个父容器计算一个特征值；3）特征值最大的容器，就是放置主要内容的容器。

具体实现请阅读代码，源码写得非常清晰，而且有详细的注释。如果遇到不能抓取全文的Feed，你就要自己修改readability.php，增加相应的规则。比如，在我提供下载的代码中，我就设置了新浪网的规则，新浪网的全文Feed就能自动生成了。

这个程序使用的是\ `AGPL许可证 <http://en.wikipedia.org/wiki/Affero_General_Public_License>`__\ ，这就是说你可以自由地使用、修改、发布这个程序，但是只要你向他人提供基于这个程序的服务，你就必须公开源码。

作者Keyvan
Minoukadeh允诺，只要使用者向他捐款200美元，就发布2.0版。如果你喜欢这个程序，建议向他\ `捐款 <http://www.chipin.com/contribute/id/17c02430b8031b97>`__\ 。

P.S.

这几天，我还发现了一个非常优秀的开源相册软件\ `ZenPhoto <http://www.zenphoto.org>`__\ ，也推荐使用。

**UPDATE（2010.6.3）**

Full TEXT RSS
1.5版\ `下载 <http://www.ruanyifeng.com/blog/2010/04/full-text-rss_v1.5.zip>`__\ （283KB）

**UPDATE（2010.11.10）**

Full TEXT RSS
2.1版\ `下载 <http://www.ruanyifeng.com/blog/2010/04/full-text-rss_v2.1.rar>`__\ （362KB）

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/04/the_solution_of_full_text_feed.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com