.. _201201_how_to_synchronize_weibo_with_twitter:

Twitter同步新浪微博的一个解决方案
====================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/01/how_to_synchronize_weibo_with_twitter.html>`__

国内的微博服务之中，\ `新浪 <http://weibo.com>`__\ 和\ `腾讯 <http://t.qq.com>`__\ 的市场份额最大。

但是，它们的平台比较封闭，不提供Feed输出，而且存在强行删除用户发言、关闭用户帐号的情况。所以，我一直以来都使用\ `Twitter <http://twitter.com/ruanyf>`__\ 。

Twitter属于墙外网站，墙内的大部分用户看不到。春节假期里，我就在想，能不能把Twitter同步到墙内？

下面就是我的解决方案：

总体思路是，先将Twitter同步到一个自建的Wordpress，然后再将Wordpress同步到新浪和腾讯。

具体做法如下：

**第一步，搭建一个Wordpress。**

安装方法请参考\ `官方网站 <http://codex.wordpress.org/Installing_WordPress>`__\ 。注意，这个Wordpress必须搭建在墙外。

**第二步，安装\ `Twitter
Tools <http://wordpress.org/extend/plugins/twitter-tools/>`__\ 插件。**

参考\ `Doug
Bowman <http://stopdesign.com/archive/2010/03/02/browsable-searchable-archive-of-tweets.html>`__\ 和\ `我 <http://www.ruanyifeng.com/blog/2010/05/my_wp_tweet_archive.html>`__\ 的说明，将Wordpress改建成Twitter备份。完成后的效果请看\ `我的备份 <http://www.ruanyifeng.com/tweets/>`__\ 。

**第三步，安装\ `wp-sns-share <http://wordpress.org/extend/plugins/wp-sns-share/>`__\ 插件。**

在该插件的设置页面，打开”微博同步功能”，将”微博同步”选项设为”发布文章时”，将”微博格式”改成”%desc”，然后完成新浪微博和腾讯微博的授权，就可以了。

（2012年4月更新：wp-sns-share
2.5版代码有错。请打开wp-sns-share/wp-sns-share.php文件，找到下面这行代码，把它注释掉

if(!isset($\_POST[‘WPSNSShare\_widget\_sync’])) return;

把它注释掉。）

**第四步，安装\ `untco <http://wordpress.org/extend/plugins/untco/>`__\ 插件。**

Twitter默认把一切链接，转化成t.co短域名，而新浪微博提示这个域名为有害链接，会报错。所以，我只好自己写了\ `上面的插件 <http://www.ruanyifeng.com/webapp/untco.html>`__\ ，将所有t.co链接转成对应的原始链接。

完成上面四步以后，Twitter应该已经可以同步到新浪和腾讯了。大家试用以后，有问题的话请在下面留言。

最后，我的Twitter账户是\ **`twitter.com/ruanyf <http://twitter.com/ruanyf>`__**\ ，新浪微博的账户是\ **`weibo.com/ruanyf <http://weibo.com/ruanyf>`__**\ ，欢迎follow。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/01/how_to_synchronize_weibo_with_twitter.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com