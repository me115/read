.. _articles3089:

Google未公开API：转MAC地址为经纬度
==================================

2010年10月9日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

这里有一个POC（Proof of
Concept）可以通过你Web浏览器后面的路由器XSS攻击得到一个准确的GPS坐标。注意：路由器和Web浏览器以及IP地址并不包含任和地理信息。其方法是使用了一个Google未公开的API。大约方法如下：

#. 访问一个网页，这个网页隐藏了一个基于你WiFi路由器的XSS（ 参见： \ `XSS
    Verizon FiOS router <http://samy.pl/vzwfios/>`__\ ）
#. 通过这个XSS 可以获得路由器的MAC 地址。
#. 然后通过 Google Location
   Services我们可以把这个MAC地址映射到GPS坐标。Googel的这个服务是基于HTTP的服务。这并不是一个Google正式发布的API，而是通过 \ `Firefox’s
   Location-Aware
   Browsing <http://www.mozilla.com/en-US/firefox/geolocation/>`__
   发现的。

演示地点在这里：\ `http://samy.pl/mapxss/ <http://samy.pl/mapxss/>`__

我试了一下，无论无线和有线都可以准确定位我的位置。很强大，你也试试看。

.. |image6| image:: /coolshell/static/20140922093815321000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/3089.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com