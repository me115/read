.. _200608_antiphishing:

谨防”网络钓鱼”（Anti-Phishing）
==================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2006/08/antiphishing.html>`__

今天我收到一封eBay公司的电子邮件。

信中有个来自纽约市的叫做drlove41的家伙，语气强硬地告诉我：

    WHERE ARE MY ITEMS?!

    THIS IS MY LAST WARNING!!!

    SEND ME THE ITEMS OR MY MONEY BACK OR I WILL REPORT YOU TO THE
    POLICE AND EBAY COSTUMERS SERVICES!!!

我大吃一惊，我并没有在ebay卖过东西啊，怎么可能遭人投诉呢。

我觉得肯定是搞错了，本来不想理会。但是，又觉得如果他真得向ebay和美国警方投诉我的话，也不太好。

于是，我就点击Email中的链接，想看看到底是什么交易。系统显示要我登陆。

我很奇怪，因为ebay一般情况下是不要求登陆的。然后，我突然注意到网址是http://mabedimne.pop3.ru，不是eBay的网址。我猛然惊醒，意识到这是”钓鱼邮件”，有人想骗取我的用户名和密码信息。如果我在登陆页面输入我的用户名和密码，那么系统会”伪装”显示登陆错误，但是这个pop3.ru网站已经把这些信息记录下来，从而可以真正登陆到我在eBay上的帐户。

所谓”网络钓鱼”（phishing），就是说有人伪造一些著名网站的界面，骗取用户输入帐户或信用卡信息，从而达到侵入用户帐户的目的。

举个例子，中国工商银行的网址是http://www.\ **i**\ cbc.com.cn，结果有人伪造了一个http://www.\ **1**\ cbc.com.cn/的网站，外观上一模一样，网址只差一个字母。不注意的话，可以乱真，提示你要输入银行卡的用户名和密码。

另外，国内”手机钓鱼”也很普遍。比如，我就收到过短信，”您在xx商场刷卡消费xxxx元，请按以下电话号码，予以确认。”如果你打电话过去，对方会给你一个警方的电话号码，要求你报警。但是，那个警方其实也是他们伪装的，目的是骗取你的信任，从你口中获得银行卡信息。

最近一二年，这种事件特别频繁，已经成了社会公害。我把这件事写出来，就是为了提醒大家注意这个问题。

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2006/08/antiphishing.html>`__

Evernote

**

Highlight

Remove Highlight

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2006/08/antiphishing.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com