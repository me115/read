.. _201005_my_wp_tweet_archive:

我的Tweet档案
================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/05/my_wp_tweet_archive.html>`__

“微博”就是不超过140个字的微型网志。

很长一段时间，我都想不出它有什么用，140个字可以说什么？大概只有自恋狂，才会把自己的一举一动贴上网，让全世界看到吧！

所以，尽管我在2007年5月就注册了，但是一直没有使用。我还做了一个试验，用它直播我的\ `大连之行 <http://www.ruanyifeng.com/blog/2007/06/my_live_blogging_experiment.html>`__\ ，最后的结论是，它对我真的没用！

不过，从今年开始，我的看法变了。

我发现，查看最新消息，比如某地发生地震，”微博”是最好的工具。而且，人与人之间的直接联络，用它也非常方便。

所以，我就重新启用自己的帐户了。我的ID是@ruanyf，欢迎大家follow。

但是，官方网站的用户界面有很多缺点，比如不能使用标签，不能查看档案，不提供档案搜索等等。所以，我就决定自己做一个本地档案，方便使用。

网址是：\ `http://www.ruanyifeng.com/tweets/ <http://www.ruanyifeng.com/tweets/>`__
，欢迎访问。


=============================

它基本上采用\ `Doug
Bowman <http://stopdesign.com/archive/2010/03/02/browsable-searchable-archive-of-tweets.html>`__\ 的方案，非常容易搭建，你完全可以用20分钟，自己做一个。下面就是具体步骤。

**第一步**\ ，从\ `TweetBackup.com <http://tweetbackup.com/>`__\ 下载你的所有发言。不过，最多只能返回3200条结果。

**第二步**\ ，用文字编辑器打开下载的RSS文件，把每段话前面的”\ *发言人:*\ “用替换功能去掉，比如我的是”\ *ruanyf:*\ “。另外，这个文件中每段话的title部分，可能会出现乱码，你可以不用管它，也可以用正则替换来处理。

**第三步**\ ，搭建一个新的\ `Wordpress <http://wordpress.org/>`__\ ，然后打开”Import”功能，选择RSS格式，将上一步的文件上传输入。

**第四步**\ ，安装\ `Twitter Tools
plugin <http://wordpress.org/extend/plugins/twitter-tools/>`__\ 插件，并做相应设置。

**第五步**\ ，安装\ `Autolink
URI <http://wordpress.org/extend/plugins/sem-autolink-uri/>`__\ 插件。它的作用是将网址字符串，转成超级链接。但是，除了网址以外，我们还要转”@”、”#”这两个特殊字符，所以要对这个插件做一些修改。

打开这个插件的sem-autolink-uri.php文件，找到下面这一行：

    $text = autolink\_uri::unescape($text);

在它前面，再加两行，

    $text =
    preg\_replace\_callback(“/(^\|\\s)@(\\w+)/”,array(‘autolink\_uri’,
    ‘tweet\_callback1’), $text);

    $text =
    preg\_replace\_callback(“/(^\|\\s)#(\\w+)/”,array(‘autolink\_uri’,
    ‘tweet\_callback2’), $text);

然后，找到email\_callback()函数，

    | function email\_callback($match) { $email = end($match);
    |  return ‘\ `’ . $email . ‘ <”’>`__\ ’;
    |  } # email\_callback()

在它后面，再加两个函数，

    | function tweet\_callback1($match) {
    |  return $match[1].’@\ `’ . $match[2] .
    ‘ <”http://twitter.com/’>`__\ ’;
    |  }

    | function tweet\_callback2($match) {
    |  return $match[1].’#\ `’ . $match[2] .
    ‘ <”http://search.twitter.com/search?q=%23’>`__\ ’;
    |  }

如果，你觉得这样修改太麻烦，也可以直接下载Autolink
URI插件的\ `修改版 <http://www.ruanyifeng.com/blog/2010/05/sem-autolink-uri.zip>`__\ （4KB）。

**第六步**\ ，下载\ `Doug
Bowman <http://stopdesign.com/archive/2010/04/30/tweet-archive-theme-files.html>`__\ 的样式文件，39KB。（需要修改头像、网址等一些小地方。）

到此就全部完成了。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/05/my_wp_tweet_archive.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com