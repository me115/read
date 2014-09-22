.. _articles455:

9个强大免费的PHP库
==================

2009年4月12日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

1. ReCAPTCHA
~~~~~~~~~~~~

`reCAPTCHA  <http://recaptcha.net/plugins/php/>`__
允许你的网站集成一个Advanced CAPTCHA
系统，这个系统可以帮助你阻止一些垃圾信息。可视化的CAPTCHA
同样也有一个有用的声音功能。另外，在reCAPTCHA
服务里，这个PHP库也包含了一个给 “Mailhide”
服务用的API，这个可以把你的邮件地址隐藏于一些抓邮件地址的程序。

这个API是免费并且非常容易使用的，你需要做的就是申请一个API的KEY。

|ReCAPTCHA|

2. Akismet
~~~~~~~~~~

`Akismet <http://akismet.com/>`__
是一个免费的服务项目，对于一些小型的网站它是完全免费的，对于一些大型的网址，他是部分免费的。这个库也是提供了处理一些和垃圾信息相关的功能。它主要通过比对自己数据库中已存在的被认定为垃圾的信息，而做出决定的。当然，数据库中的垃圾信息可能通过各个网站举报，大家供享的。这是一个每天都在更新，每天都在改进的库。许多许多的WordPress都装有这个库。

|Akismet|

`实施Akismet <http://net.tutsplus.com/tutorials/tools-and-tips/the-best-ways-to-fight-spam/>`__

3. Services\_JSON
~~~~~~~~~~~~~~~~~

JSON
是一个非常小巧敏捷的PHP库，它主要用于把一些数据格式转成易于人们阅读的格式。并不是所有的人都会喜欢PHP5
（因为自PHP5.20后其中已经集成了JSON），所以，这个小PHP库可以在低版本的PHP中让你得到
JSON 的功能。

|JSON|

`查看 Services\_JSON <http://pear.php.net/package/Services_JSON>`__

4. Smarty
~~~~~~~~~

`Smarty <http://smarty.net/>`__
是一个网面模板引擎，它主要是把程序和界面分开。Smarty
提供了许多强大的功能，比如循环，变量，以及一个强大的缓存系统。这个库不是一个新库了，其已经发展了很多年了，虽然只有3个release版，但应该是比较成熟了。

|Smarty|

`下载 Smarty <http://smarty.net/download.php>`__ \|
`查看文档 <http://smarty.net/docs.php>`__

5. pChart
~~~~~~~~~

这是一个强大的画统计图的PHP库，像一些饼图或是柱状图，\ `pChart <http://pchart.sourceforge.net/index.php>`__ 还允许你通过SQL查询语句或是手动的输入数据来创建一个统计图。当然它需要GD库的支持以便创建图片。这个库一看就是有很多非常专业的美工设计过，因为它可以让你的统计图显示的相当漂亮。

|pChart|

6. SimplePie
~~~~~~~~~~~~

`SimplePie <http://simplepie.org/>`__  允许你可以容易地 pull
一些信息，比如RSS
feeds。它同样可以被集成于不同的平台和语言。并且可以通过很多不同的方法来处理远端的feed。

|SimplePie|

7. XML-RPC PHP
~~~~~~~~~~~~~~

我们的应用程序有时需要一些类似于 “ping”
的功能去探测一下其它站点，如BLOG的
trackbacks。一般来说，这都是通过一个叫做XML-RPC的协议来完成的。\ `XML-RPC
PHP <http://phpxmlrpc.sourceforge.net/>`__
库可以让你的站点集成这些功能。

|XML-RPC|

`下载 XML-RPC PHP <http://phpxmlrpc.sourceforge.net/#download>`__ \|
`相关文档 <http://phpxmlrpc.sourceforge.net/#interest>`__

8. Amazon S3
~~~~~~~~~~~~

Amazon 提供了一个“云服务”叫”S3″.
这个PHP库可以让你不需要第三方的插件就可以上传大的文件。

|Amazon S3|

`下载 Amazon S3 PHP
类 <http://amazon-s3-php-class.googlecode.com/files/s3-php5-curl_0.3.9.tar.gz>`__

9. PHPMailer
~~~~~~~~~~~~

很多应用都需要对外发送邮件，但是PHP的mail() 函数并不是特别好用。于是
PHPMailer
应运而生，这是一个功能强大的类，其允许你发送不同格式的邮件，并支持附件和自定义邮件头。

|Sending Mail|

`下载
PHPMailer <http://phpmailer.codeworxtech.com/index.php?pg=sf&p=dl>`__ \|
`相关文档 <http://phpmailer.codeworxtech.com/index.php?pg=tutorial>`__

文章：\ `来源 <http://net.tutsplus.com/articles/web-roundups/9-extremely-useful-and-free-php-libraries/>`__

.. |ReCAPTCHA| image:: /coolshell/static/20140922095250094000.png
.. |Akismet| image:: /coolshell/static/20140922095251571000.jpg
.. |JSON| image:: /coolshell/static/20140922095252856000.png
.. |Smarty| image:: /coolshell/static/20140922095253533000.png
.. |pChart| image:: /coolshell/static/20140922095254248000.png
.. |SimplePie| image:: /coolshell/static/20140922095255352000.png
.. |XML-RPC| image:: /coolshell/static/20140922095256086000.png
.. |Amazon S3| image:: /coolshell/static/20140922095256811000.png
.. |Sending Mail| image:: /coolshell/static/20140922095258103000.png
.. |image15| image:: /coolshell/static/20140922095258804000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/455.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com