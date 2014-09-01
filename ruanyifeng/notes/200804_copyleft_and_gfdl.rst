.. _200804_copyleft_and_gfdl:

Copyleft和GFDL许可证
=======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/04/copyleft_and_gfdl.html>`__

昨天，我做了一些关于\ `创作共用许可证 <http://www.ruanyifeng.com/blog/2008/04/creative_commons_licenses.html>`__\ （Creative
Commons Licenses，以下简称CC）的笔记，只写了一半，今天接着往下写。

**一、什么是copyleft**

要讲copyleft，必须先讲copyright。”版权”这个词copyright，按照字面解释，就是”复制的权利”（copy+right）。这就是说，只要是有版权的作品，都是不等随便复制的。

程序员\ `Richard
Stallman <http://www.ruanyifeng.com/blog/2005/03/post_112.html>`__\ 对此很不满，认为这阻碍了创新，不利于人们分享成果。因此，他在上个世纪70年代创建了自由软件基金会FSF，致力于智力成果的自由分享。

如果你希望自己的作品自由传播，最简单的方法就是声明放弃版权，使作品进入公共领域（public
domain）。但是，这样做有一个缺点，就是你无法防止某些人对你的作品进行加工，然后把加工的作品变为他们的私有财产，进行出售。所以，只有一个人放弃版权是不够的，必须保证后面的所有使用者都不会将其据为己有。

因为这个原因，Richard
Stallman设计出了\ `copyleft <http://www.gnu.org/copyleft/>`__\ 的做法。所谓copyleft，就是为作品附上一个许可证，这个许可证基本上允许你对作品做任何事，除了不能限制他人的自由，即如果你对原作品修改后再发布，那么你也必须使用同样的许可证。所以，只要一个作品被copyleft了，那么此后基于它的所有作品都会被copyleft。

copyleft这个词，是对copyright的戏谑，故意与copyright对立，比如我们经常看到copyrighted
materials，现在就有了copylefted
materials。这个词好像很难找到合适的中文译名。copyright的标志是正写的圈c，copyleft的标志是反写的圈c。

不过，有一点需要注意，虽然copyleft与copyright对立，但是它是符合版权制度的，copyleft的作品也是有版权的。

**二、GPL和GFDL许可证**

copyleft只是一个规范（paradigm），只要符合这个规范，就属于copyleft许可证。

Richard
Stallman建立FSF以后，主要提出了两个copyleft许可证：\ `GPL许可证 <http://www.ruanyifeng.com/blog/2004/06/gpl.html>`__\ （GNU
General Public
License）和\ `GFDL许可证 <http://www.gnu.org/copyleft/fdl.html>`__\ （GNU
Free Documentation
License）。前者主要用于软件作品，后者主要用于文字作品。

一旦一个文字作品采用了GFDL许可证，那么他人就可以自由使用这个作品，包括用于商业用途，唯一的条件是所有衍生作品也必须采用GFDL许可证。

目前，世界上最著名、最成功的使用GFDL的项目，是维基百科\ `wikipedia <http://wikipedia.org>`__\ 。这意味着，如果你利用wikipedia的材料写成一本书，那么你的这本书，他人也可以自由使用。

**三、GFDL和CC的关系**

CC许可证中，只有保留”相同方式共享”（share
alike）权利的许可证，才属于copyleft规范。也就是说，只有”署名-相同方式共享”（cc-by-sa）\ |Creative
Commons
License|\ 和”署名-非商业用途-相同方式共享”（cc-by-nc-sa）\ |Creative
Commons License|\ 这两种许可证，达到了这个标准。

当然，这并不意味着其他cc许可证就不自由，相反的，单独的”署名”（cc-by）许可证\ |Creative
Commons
License|\ 提供的自由，其实比前两种许可证都大，因为它允许你将原作品变为私有财产。

一个有趣的问题是，GFDL和CC是不兼容的。虽然这两个许可证都允许自由使用作品，但是你不能将它们混合在同一个作品里使用。

在基本精神上，GFDL其实等同于cc-by-sa（署名-相同方式共享）\ |Creative
Commons
License|\ ，但是两者都要求衍生作品必须使用与原作品相同的许可证，这使得它们没有办法互换。唯一可以单向互换的是GFDL和cc-by（署名）许可证\ |Creative
Commons
License|\ ：使用cc-by的文字，可以加入使用GFDL的文章，但是反过来就不行。

在现实中，Flickr采用的是CC许可证，那么上面那些采用cc-by的照片，是可以加入wikipedia的，而那些采用cc-by-sa的照片勉强也可以加入，因为wikipedia会对单张图片注明该照片采用cc-by-sa的许可证。但是，使用cc-by-sa的文字就不能加入，因为wikipedia对文字统一采用GFDL许可证。

2007年12月，创作共用基金会\ `决定修改cc-by-sa <http://en.wikipedia.org/wiki/Wikipedia:Wikipedia_Signpost/2005-11-21/CC_compatibility>`__\ 许可证，允许将其并入GFDL。从此以后，wikipedia也就可以加入采用cc-by-sa的文字了。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/04/copyleft_and_gfdl.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com