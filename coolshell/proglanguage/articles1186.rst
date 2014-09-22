.. _articles1186:

如何检测浏览器是否支持CSS3
==========================

2009年7月24日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

如何检测用户的浏览器是否支持CSS3，我们需要使用HTML，CSS和JavaScript来完成这件事情。下面是步骤。

**1）先制作下面的HTML**

::

**2）然后书写下面的CSS**

::

    #check {
      display: none;
      width: 0;
      height: 0;
    }
    #check[rel^="D"] {
      display: block;
      width: 0;
      height: 0;
    }

| 
| **3）下面是JavaScripts的检测脚本**

请确保下面的代码放在HTML文件头。

::


    var obj = document.getElementById("check");
    var file="special.css";
    if (window.getComputedStyle)
        var stat = window.getComputedStyle(obj,null).getPropertyValue("display");
    else if (obj.currentStyle)
        var stat = obj.currentStyle.display;
        var stat = obj.currentStyle.display;
    var css3 = (stat == "block");
    if (css3) alert("CSS3 Supported.");
    else alert("CSS3 not supported.");

文章：\ `来源 <http://www.geocities.com/seanmhall2003/css3/detect.html>`__

.. |image6| image:: /coolshell/static/20140922105626196000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1186.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com