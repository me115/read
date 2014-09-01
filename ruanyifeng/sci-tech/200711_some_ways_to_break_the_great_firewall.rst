.. _200711_some_ways_to_break_the_great_firewall:

绕过gfw的方法
================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2007/11/some_ways_to_break_the_great_firewall.html>`__

昨天，美国《大西洋月刊》的驻华记者James
Fallows在Blog上高兴地\ `宣布 <http://jamesfallows.theatlantic.com/archives/2007/11/the_best_3999_i_have_spent_in.php>`__\ ，他终于能够打破GFW（中国国家防火墙）的屏蔽，浏览那些以前不能访问的网站了。他甚至说，这是他在中国花得最值得的39.99美元。

他的方法就是从\ `witopia.net <http://www.witopia.net/personalmore.html>`__\ 上购买了Personal
VPN服务，每年的费用是39.99美元。根据他在Blog里提供的信息，这个服务在国内的访问速度相当快，是绕过GFW的一种有效方法。

所谓VPN，意思是”Virtual Private
Network”（虚拟私人网络），可以理解成”加密通信”。它绕过GFW的原理是，与一台国外的主机建立加密连接，然后用那台主机去访问其他网站，再将信息以加密的形式传回来，这样就可以看到那些被屏蔽的网站了。

我觉得，一年39.99美元的费用不算贵，是一种可以接受的方案。此外，网上有不少免费VPN，可以\ `搜索 <http://www.google.com/search?q=%E5%85%8D%E8%B4%B9+vpn&sourceid=navclient-ff&ie=UTF-8&rlz=1B3GGGL_zh-CNCN216CN216>`__\ 一下，也许能找到不用花钱的替代方案。

除了这种方法以外，我还能想到三种方法，可以打破GFW的屏蔽。原理同上面的差不多，我就不细说了，大家自己到网上去搜。

    1）使用\ `加密https代理 <http://www.google.cn/search?q=https+%E4%BB%A3%E7%90%86&sourceid=navclient-ff&ie=UTF-8&rlz=1B3GGGL_zh-CNCN216CN216>`__\ 。

    2）使用\ `Tor <http://www.google.cn/search?complete=1&hl=zh-CN&newwindow=1&rlz=1B3GGGL_zh-CNCN216CN216&q=tor&btnG=Google+%E6%90%9C%E7%B4%A2&meta=>`__\ 。

    3）使用SSH隧道技术，请参考车东翻译的\ `教程 <http://www.chedong.com/blog/archives/001246.html>`__\ 。

最后，我谈一下对GFW的感想。

以前，我一直认为阻扰互联网通信是不可能的，总有打破屏蔽的方法。但是，现在我不是那么乐观了。上个星期我同一个朋友吃饭的时候，我说GFW可能真的能够实现审查互联网的目的。

大约在上个月，很多朋友\ `发现 <http://www.cnbeta.com/articles/41324.htm>`__\ 从国内访问一些国外网站时，会自动跳到Baidu的页面。虽然很快就恢复正常了，但是这件事证明了国内存在大规模的\ `DNS劫持 <http://www.google.cn/search?complete=1&hl=zh-CN&newwindow=1&rlz=1B3GGGL_zh-CNCN216CN216&q=DNS+%E5%8A%AB%E6%8C%81&btnG=Google+%E6%90%9C%E7%B4%A2&meta=>`__\ ，也就是说电信有办法控制域名的指向。有网友建议使用\ `OpenDNS <http://www.opendns.com/>`__\ 就可以避免这种事件，但是OpenDNS本身也可能被劫持或屏蔽，所以这也不是一种绝对有效的方法。

我在想，要是国内以后规定所有域名都必须备案，或者建立一张域名的”白名单”，凡是不在名单上的域名就不能访问，那可怎么办？……

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2007/11/some_ways_to_break_the_great_firewall.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com