.. _articles3595:

如何“加密”你的email地址
=======================

2011年1月27日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

现在在网上要小心，无论是\ `保护好你的用户名和帐号 <http://coolshell.cn/articles/2428.html>`__\ ，还是我们的电子邮件地址。在网上有很多爬虫程序专爬我们的电子邮件地址，一量被爬中了，那么你的邮箱里就是一堆又一堆的垃圾邮件，就好像我的haoel(at)hotmail.com一样，在7、8年前，每天几千封的垃圾邮件。现在hotmail的垃圾邮件过滤得好一些了，不过也有每天40封左右的垃圾邮件。但是我们在自己的网页上又需要发布自己的email地址。所以我们需要搞乱我们的邮件地址，就像那种非常规的\ `搞乱代码一样 <http://coolshell.cn/articles/933.html>`__\ 。不过，我们还需要能认人读的出来。

一般来说，在网上现在很普遍的做法是——

-  1）用图片，可以用PHP动态生成那个验证码式的。
-  2）把@变成at，把点变成dot，如 haoel(at)hotmail(dot)com之类的。
-  3）把a变成@，写成haoel@hotm@mail.com

不过这些还是能被爬到，用图片的方法不利于用户拷贝粘贴。下面介绍几种方法：

第一种：使用CSS样式
^^^^^^^^^^^^^^^^^^^

**反转字序**

::

    span.codedirection { unicode-bidi:bidi-override; direction: rtl; }
    moc.liamtoh@leoah

**加入些不显示的字符串**

::

    p span.hide { display:none; }
    foo@barnull.baz

第二种：使用Javascript
^^^^^^^^^^^^^^^^^^^^^^

最为简单的方法是：

::

    document.write("haoel" + "@" + "hotmail" + "." + "com");

或是：

::

不过更为强大的是使用ROT13加密，这里有一个\ `ROT13的在线工具 <http://rot13.de/>`__\ ，或是使用PHP的ROT13的函数\ `str\_rot13 <http://ch2.php.net/str_rot13>`__\ 。

::

    document.write(“”.replace(/[a-zA-Z]/g,
    function(c){return String.fromCharCode((c<=”Z”?90:122)>=(c=c.charCodeAt(0)+13)?c:c-26);}));
    陈皓的电子邮件

这些方法还是很有效果的。

.. |image6| image:: /coolshell/static/20140921222136847000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/3595.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com