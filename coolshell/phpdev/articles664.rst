.. _articles664:

使用PHP的cURL库
===============

2009年4月25日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

使用PHP的cURL库可以简单和有效地去抓网页。你只需要运行一个脚本，然后分析一下你所抓取的网页，然后就可以以程序的方式得到你想要的数据了。无论是你想从从一个链接上取部分数据，或是取一个XML文件并把其导入数据库，那怕就是简单的获取网页内容，cURL
是一个功能强大的PHP库。本文主要讲述如果使用这个PHP库。

| ** 启用 cURL 设置**
| 
首先，我们得先要确定我们的PHP是否开启了这个库，你可以通过使用php\_info()函数来得到这一信息。

::

 

如果你可以在网页上看到下面的输出，那么表示cURL库已被开启。

|phpinfo\_curl|

如果你看到的话，那么你需要设置你的PHP并开启这个库。如果你是在Windows平台下，那么非常简单，你需要改一改你的php.ini文件的设置，找到php\_curl.dll，并取消前面的分号注释就行了。如下所示：

::


    //取消下在的注释
    extension=php_curl.dll 

如果你是在Linux下面，那么，你需要重新编译你的PHP了，编辑时，你需要打开编译参数——在configure命令上加上“–with-curl”
参数。

| **一个小示例**
|  如果一切就绪，下面是一个小例程：

::


     
    如何POST数据
    上面是抓取网页的代码，下面则是向某个网页POST数据。假设我们有一个处理表单的网址http://www.example.com/sendSMS.php，其可以接受两个表单域，一个是电话号码，一个是短信内容。

 从上面的程序我们可以看到，使用CURLOPT\_POST设置HTTP协议的POST方法，而不是GET方法，然后以CURLOPT\_POSTFIELDS设置POST的数据。

**关于代理服务器**

::

    下面是一个如何使用代理服务器的示例。请注意其中高亮的代码，代码很简单，我就不用多说了。

::


 **关于SSL和Cookie**

关于SSL也就是HTTPS协议，你只需要把CURLOPT\_URL连接中的http://变成https://就可以了。当然，还有一个参数叫CURLOPT\_SSL\_VERIFYHOST可以设置为验证站点。

关于Cookie，你需要了解下面三个参数：

-  CURLOPT\_COOKIE，在当面的会话中设置一个cookie
-  CURLOPT\_COOKIEJAR，当会话结束的时候保存一个Cookie
-  CURLOPT\_COOKIEFILE，Cookie的文件。

**HTTP服务器认证**

最后，我们来看一看HTTP服务器认证的情况。

::

关于其它更多的内容，请大家参看相关的cURL手册吧。

.. |phpinfo\_curl| image:: /coolshell/static/20140920235130631000.png
   :target: http://coolshell.cn//wp-content/uploads/2009/04/phpinfo_curl.png
.. |image7| image:: /coolshell/static/20140920235130666000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/664.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com