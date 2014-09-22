.. _articles200:

20 你应该知道的PHP库
====================

2009年3月18日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

下面是一些非常有用的PHP类库，相信一定可以为你的WEB开发提供更好和更为快速的方法。

图表库\ |021151lephpant-e\_png|
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

下面的类库可以让你很简的创建复杂的图表和图片。当然，它们需要GD库的支持。

#. `pChart <http://pchart.sourceforge.net/>`__ –
   一个可以创建统计图的库。
#. `Libchart <http://naku.dohcrew.com/libchart/pages/introduction/>`__ –
   这也是一个简单的统计图库。
#. `JpGraph <http://www.aditus.nu/jpgraph/>`__ –
   一个面向对象的图片创建类。
#. `Open Flash Chart <http://teethgrinder.co.uk/open-flash-chart/>`__ –
   这是一个基于Flash的统计图。

 

RSS 解析
~~~~~~~~

解释RSS并是一件很单调的事情，不过幸好你有下面的类库可以帮助你方便地读取RSS的Feed。

#. `MagpieRSS <http://magpierss.sourceforge.net/>`__ –
   开源的PHP版RSS解析器，据说功能强大，未验证。
#. `SimplePie <http://simplepie.org/>`__ –
   这是一个非常快速，而且易用的RSS和Atom 解析库。

缩略图生成
~~~~~~~~~~

#. `phpThumb <http://phpthumb.sourceforge.net/>`__ –
   功能很强大，如何强大还是自己去体会吧。

支付
~~~~

你的网站需要处理支付方面的事情？需要一个和支付网关的程序？下面这个程序可以帮到你。

#. `PHP Payment
   Library <http://www.phpfour.com/blog/2009/02/php-payment-gateway-library-for-paypal-authorizenet-and-2checkout/>`__
   – 支持Paypal, Authorize.net 和2Checkout (2CO)

OpenID
~~~~~~

#. `PHP-OpenID <http://www.openidenabled.com/php-openid/>`__ –
   支持OpenID的一个PHP库。OpenID是帮助你使用相同的用户名和口令登录不同的网站的一种解决方案。如果你对OpenID不熟悉的话，你可以到这里看看：\ `http://openid.net.cn/ <http://openid.net.cn/>`__

数据为抽象/对象关系映射ORM
~~~~~~~~~~~~~~~~~~~~~~~~~~

#. `ADOdb <http://adodb.sourceforge.net/>`__ – 数据库抽象
#. `Doctrine <http://www.doctrine-project.org/>`__ – 对象关系映射Object
   relational mapper (ORM) ，需要 PHP 5.2.3+
   版本，一个非常强大的database abstraction layer (DBAL).
#. `Propel <http://propel.phpdb.org/trac/>`__ – 对象关系映射框架- PHP5
#. `Outlet <http://www.outlet-orm.org/site/>`__ –
   也是关于对象关系映射的一个工具。

注：对象关系映射（Object Relational
Mapping，简称ORM）是一种为了解决面向对象与关系数据库存在的互不匹配的现象的技术。
简单的说，ORM是通过使用描述对象和数据库之间映射的元数据，将程序中的对象自动持久化到关系数据库中。本质上就是将数据从一种形式转换到另外一种形式。
这也同时暗示者额外的执行开销；然而，如果ORM作为一种中间件实现，则会有很多机会做优化，而这些在手写的持久层并不存在。
更重要的是用于控制转换的元数据需要提供和管理；但是同样，这些花费要比维护手写的方案要少；而且就算是遵守ODMG规范的对象数据库依然需要类级别的元数据。

PDF 生成器
~~~~~~~~~~

#. `FPDF <http://www.fpdf.org/>`__ –
   这量一个可以让你生成PDF的纯PHP类库。

Excel 相关
~~~~~~~~~~

你的站点需要生成Excel？没有问题，下面这两个类库可以让你轻松做到这一点。

#. `php-excel <http://code.google.com/p/php-excel/>`__ –
   这是一个非常简单的Excel文件生成类。
#. `PHP Excel Reader <http://code.google.com/p/php-excel-reader/>`__ –
   可以解析并读取XLS文件中的数据。

E-Mail 相关
~~~~~~~~~~~

不喜欢PHP的mail函数？觉得不够强大？下面的PHP邮件相关的库绝对不会让你失望。

#. `Swift Mailer <http://swiftmailer.org/>`__ –
   免费的超多功能的PHP邮件库。
#. `PHPMailer <http://phpmailer.codeworxtech.com/>`__-
   超强大的邮件发送类。

单元测试
~~~~~~~~

如果你在使用测试驱动的方法开发你的程序，下面的类库和框架绝你能帮助你的开发。

#. `SimpleTest <http://www.simpletest.org/>`__ –
   一个PHP的单元测试和网页测试的框架。
#. `PHPUnit <http://www.phpunit.de/>`__ – 来自xUnit
   家族，提供一个框架可以让你方便地进行单元测试的案例开发。并可非常容易地分析其测试结果。

文章：\ `来源 <http://komunitasweb.com/2009/03/20-great-php-library-you-need-to-know/>`__

.. |021151lephpant-e\_png| image:: /coolshell/static/20140921220708632000.jpg
   :target: http://coolshell.cn//wp-content/uploads/2009/03/021151lephpant-e_png.jpg
.. |image7| image:: /coolshell/static/20140921220708731000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/200.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com