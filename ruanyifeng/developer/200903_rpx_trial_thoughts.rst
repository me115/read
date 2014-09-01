.. _200903_rpx_trial_thoughts:

Openid托管服务RPX试用感想
============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/03/rpx_trial_thoughts.html>`__

去年下半年，\ `微软 <http://www.readwriteweb.com/archives/microsoft_windows_live_openid.php>`__\ 和\ `Google <http://googledataapis.blogspot.com/2008/10/federated-login-for-google-account.html>`__\ 相继宣布支持\ `Openid <http://openid.net/>`__\ 。

这就是说，你不需要每个网站都注册了，Gmail帐号有望变成通用帐号。

这不仅方便了用户，而且对网站制作者也很有吸引力。所有Gmail的用户，不用注册就能使用你的网站，这是多大的一个市场啊！更重要的是，由于用户名是相同的，不同网站之间进行用户数据的同步和交换就容易多了。另一方面，用户数据的维护”外包”给了Google，你自己就不用干这活了，可以将更多的精力集中在开发网站的核心功能上。

虽然有这么多好处，但是半年过去了，很少有网站实现了这个功能。

今天，我终于明白了为什么。

不是大家不想实现，而是实现起来太难了。\ `Openid的规格 <http://openid.net/developers/specs/>`__\ 和\ `Google的开发文档 <http://code.google.com/apis/accounts/docs/OpenID.html>`__\ ，都写得非常费解，很难读懂。就算你读懂了，真正将这项功能做出来，更是一桩麻烦事。

    首先，你必须安装额外的代码库，写一些额外的代码。

    其次，用户登录的时候，网页会自动跳转到外部网站，用户输入密码以后，再跳转回来，整个过程比本地登录要慢几个数量级；

    最后，如果来自外部的用户信息不足以满足你的需要（比如你需要知道用户的性别），你就势必要让用户重新提供一次，整个系统的复杂度不仅没有减少，反而变得更大了。

所以，当我看到有一家公司提供Openid的托管服务\ `RPX <https://rpxnow.com/>`__\ 时，我是多么高兴啊。按照那家公司的宣传，你所要做的，只是在网页中插入几行代码，剩下的全部由它来完成。

我就按照它的说明，搭建了一个\ `范例 <http://www.ruanyifeng.com/webapp/openid/rpx.php>`__\ 。（你可以点击进去，感受一下通用帐号的登录过程。但是做好思想准备，这个服务的载入速度相当慢。）

它确实做到了，提供一个支持各种Openid帐号的统一接口。但是它把接口做死了，你根本没法定制，一点灵活性也没有。昨天，我原想修改它的登录界面，结果改了一天，最后发现没法成功，郁闷得不得了。而且除此之外，我上面提到各种毛病依然存在。所以，我觉得这个服务不具备实用性。

经过这件事，我对Openid转而感到悲观了。我的判断是，除非技术上出现重大突破，否则在未来很长一段时间中，Openid都不会得到大规模部署。

这意味着，每一个网站依然必须维护自己的用户管理系统，而每一个用户依然必须到处注册，苦思冥想如何记住自己的几千个用户名。

(完）

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/03/rpx_trial_thoughts.html>`__

Evernote

**

Highlight

Remove Highlight

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/03/rpx_trial_thoughts.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com