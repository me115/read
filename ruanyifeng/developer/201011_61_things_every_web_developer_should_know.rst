.. _201011_61_things_every_web_developer_should_know:

网站开发人员应该知道的61件事
===============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/11/61_things_every_web_developer_should_know.html>`__

有人在\ `Stack
Overflow <http://stackoverflow.com/questions/72394>`__\ 上发问，动手开发网站之前，需要知道哪些事情？

不出意料地，他得到了一大堆回答。

通常情况下，你需要把所有人的发言从头到尾读一遍。但是，Stack
Overflow有一个很贴心的设计，它允许在问题下方开设一个wiki区，让所有人共同编辑一个最佳答案。于是，就有了下面这篇文章，一共总结出六个方面共计61条”网站开发须知”。

我发现，这种概述性的问题，最适合这种集合群智、头脑风暴式的回答方式了。这也是我第一次觉得，Stack
Overflow做到了Wikipedia做不到的事。（难怪它最近挤进了全美前400大网站。）

在我的印象中，关于网站开发，这样全面的概述性文章非常少见，因此也就非常有用。大家不妨看看，61件事情中你做到了多少？

（更新：刚刚发现，一共应该是62条建议，我先前数错了，这个……太窘了。）


=============================

**网站开发人员应该知道的61件事**

原文网址：\ `http://stackoverflow.com/questions/72394 <http://stackoverflow.com/questions/72394>`__

译者：阮一峰

**一、界面和用户体验（Interface and User Experience）**

1.1

知道各大浏览器执行Web标准的情况，保证你的站点在主要浏览器上都能正常运行。你至少要测试以下引擎：\ `Gecko <http://en.wikipedia.org/wiki/Gecko_%28layout_engine%29>`__\ （用于\ `Firefox <http://firefox.com/>`__\ ）、Webkit（用于\ `Safari <http://www.apple.com/safari/>`__\ 、\ `Chrome <http://www.google.com/chrome>`__\ 和一些手机浏览器）、IE（你可以利用微软发布的\ `Application
Compatibility VPC
Images <http://www.microsoft.com/Downloads/details.aspx?FamilyID=21eabb90-958f-4b64-b5f1-73d0a413c8ef&displaylang=en>`__\ 进行测试）和\ `Opera <http://www.opera.com/>`__\ 。同时，不同的操作系统，可能也会影响浏览器如何\ `呈现 <http://www.browsershots.org/>`__\ 你的网站。

1.2

除了浏览器，网站还有其他使用方式：手机、屏幕朗读器、搜索引擎等等。你应该知道在这些情况下，你的网站的运行状况。\ `MobiForge <http://mobiforge.com/>`__\ 提供了手机网站开发的一些相关知识。

1.3 

知道如何在基本不影响用户使用的情况下升级网站。通常来说，你必须有版本控制系统（CVS、Subversion、Git等等）和数据备份机制（backup）。

1.4

不要让用户看到那些不友好的出错提示。

1.5

不要直接显示用户的Email地址，至少不要用纯文本显示。

1.6

为你的网站设置一些\ `合理的使用限制 <http://www.codinghorror.com/blog/archives/001228.html>`__\ ，一旦超过门槛值，就自动停止服务。（这也与网站安全相关。）

1.7

知道如何实现网页的\ `渐进式增强 <http://en.wikipedia.org/wiki/Progressive_enhancement>`__\ （progressive
enhancement）。

1.8

用户发出POST请求后，总是将其\ `重导向 <http://en.wikipedia.org/wiki/Post/Redirect/Get>`__\ （redirect）至另外一个网页。

1.9

不要忘记网站的可访问性（accessibility，即残疾人如何使用网站）。对于美国网站来说，有时这是\ `法定要求 <http://www.section508.gov/>`__\ 。\ `WAI-ARIA <http://www.w3.org/WAI/intro/aria>`__\ 有一些这方面很好的参考资料。

**二、安全性（Security**\ ）

2.1

阅读\ `《OWASP开发指南》 <http://www.owasp.org/index.php/Category%3aOWASP_Guide_Project>`__\ ，它提供了全面的网站安全指导。

2.2

了解\ `SQL注入 <http://en.wikipedia.org/wiki/SQL_injection>`__\ （SQL
injection）及其预防方法。

2.3

永远不要信任用户提交的数据（cookie也是用户端提交的！）。

2.4

不要明文（plain-text）储存用户的密码，要hash处理后再储存。

2.5

不要对你的用户认证系统太自信，它可能很容易就被攻破，而你事先根本没意识到存在相关漏洞。

2.6

了解如何\ `处理信用卡 <https://www.pcisecuritystandards.org/>`__\ 。

2.7

在登录页面及其他处理敏感信息的页面，使用\ `SSL <http://www.mozilla.org/projects/security/pki/nss/ssl/draft302.txt>`__/`HTTPS <http://en.wikipedia.org/wiki/Https>`__\ 。

2.8

知道如何对付session劫持（session hijacking）。

2.9

避免”\ `跨站点执行 <http://en.wikipedia.org/wiki/Cross-site_scripting>`__\ “（cross
site scripting，XSS）。

2.10

避免”\ `跨域伪造请求 <http://en.wikipedia.org/wiki/Cross-site_request_forgery>`__\ “（cross
site request forgeries，XSRF）。

2.11

及时打上补丁，让你的系统始终跟上最新版本。

2.12

确认你的数据库连接信息的安全性。

2.13

跟踪攻击技术的最新发展，以及你使用的平台的最新安全漏洞。

2.14

阅读Google的\ `《浏览器安全手册》 <http://code.google.com/p/browsersec/wiki/Main>`__\ （Browser
Security Handbook）。

2.15

阅读\ `《网络软件的黑客手册》 <http://amzn.com/0470170778>`__\ （The Web
Application Hackers Handbook）。

**三、性能（Performance）**

3.1

只要有可能，就使用缓存（caching）。正确理解和使用\ `HTTP
caching <http://www.mnot.net/cache_docs/>`__\ 与\ `HTML5离线储存 <http://www.w3.org/TR/html5/offline.html>`__\ 。

3.2

优化图片。不要把一个20KB的图片文件，作为重复出现的网页背景图案。

3.3

学习如何用\ `gzip/deflate压缩 <http://developer.yahoo.com/performance/rules.html#gzip>`__\ 内容（\ `deflate方式更可取 <http://stackoverflow.com/questions/1574168/gzip-vs-deflate-zlib-revisited>`__\ ）。

3.4

将多个样式表文件或脚本文件，合为一个文件，这样可以减少浏览器的http请求数，以及减小gzip压缩后的文件总体积。

3.5

浏览Yahoo的\ `Exceptional
Performance <http://developer.yahoo.com/performance/>`__\ 网站，里面有大量提升前端性能的优秀建议，还有他们的\ `YSlow <http://developer.yahoo.com/yslow/>`__\ 工具。Google的\ `page
speed <http://code.google.com/speed/page-speed/docs/rules_intro.html>`__\ 则是另一个用来分析网页性能的工具。两者都要求安装\ `Firebug <http://getfirebug.com/>`__\ 。

3.6

如果你的网页用到大量的小体积图片（比如工具栏），就应该使用\ `CSS Image
Sprite <http://alistapart.com/articles/sprites>`__\ ，目的是减少http请求数。

3.7

大流量的网站应该考虑将\ `网页对象分散在多个域名 <http://developer.yahoo.com/performance/rules.html#split>`__\ （split
components across domains）。

3.8

静态内容（比如图片、CSS、JavaScript、以及其他cookie无关的网页内容）都应该放在一个\ `不需要使用cookie <http://blog.stackoverflow.com/2009/08/a-few-speed-improvements/>`__\ 的独立域名之上。因为域名之下如果有cookie，那么客户端向该域名发出的每次http请求，都会附上cookie内容。这里的一个好方法就是使用”内容分发网络”（Content
Delivery Network，CDN）。

3.9

将浏览器完成网页渲染所需要的http请求数最小化。

3.10

使用Google的\ `Closure
Compiler <http://code.google.com/closure/compiler/>`__\ 压缩JavaScript文件，\ `YUI
Compressor <http://developer.yahoo.com/yui/compressor/>`__\ 亦可。

3.11

确保网站根目录下有favicon.ico文件，因为即使网页中根本不包括这个文件，浏览器也会\ `自动发出对它的请求 <http://mathiasbynens.be/notes/rel-shortcut-icon>`__\ 。所以如果这个文件不存在，就会产生大量的404错误，消耗光你的服务器的带宽。

**四、搜索引擎优化（Search Engine Optimization，SEO）**

4.1

使用”搜索引擎友好”的URL形式，比如example.com/pages/45-article-title，而不是example.com/index.php?page=45。

4.2

不要使用”点击这里”之类的超级链接，因为这样等于浪费了一个SEO机会，而且降低了”屏幕朗读器”（screen
reader）的使用效果。

4.3

创建一个\ `XML
sitemap <http://www.sitemaps.org/>`__\ 文件，它的缺省位置一般是/sitemap.xml（即放在网站根目录下）。

4.4

当你有多个URL指向同一个内容时，在网页代码中使用\ ` <http://googlewebmastercentral.blogspot.com/2009/02/specify-your-canonical.html>`__\ 。

4.5

使用Google的\ `Webmaster
Tools <http://www.google.com/webmasters/>`__\ 和Yahoo的\ `Site
Explorer <http://siteexplorer.search.yahoo.com/>`__\ 。

4.6

从一开始就使用\ `Google
Analytics <http://www.google.com/analytics/>`__\ （或者开源的访问量分析工具\ `Piwik <http://piwik.org/>`__\ ）。

4.7

知道\ `robots.txt <http://en.wikipedia.org/wiki/Robots_exclusion_standard>`__\ 的作用，以及搜索引擎蜘蛛的工作原理。

4.8

将www.example.com的访问请求导向example.com（使用301 Moved
Permanently重定向），或者采用相反的做法，目的是防止Google把它们当做两个网站，分开计算排名。

4.9

知道存在着恶意或行为不正当的网络蜘蛛。

4.10

如果你的网站有非文本的内容（比如视频、音频等等），你应该参考Google的\ `sitemap扩展协议 <http://www.google.com/support/webmasters/bin/answer.py?hl=en&answer=40318>`__\ 。

**五、技术（Technology）**

5.1

理解\ `HTTP协议 <http://www.ietf.org/rfc/rfc2616.txt>`__\ ，以及诸如GET、POST、sessions、cookies之类的概念，包括”无状态”（stateless）是什么意思。

5.2

确保你的\ `XHTML <http://www.w3.org/TR/xhtml1/>`__/`HTML <http://www.w3.org/TR/REC-html40/>`__\ 和\ `CSS <http://www.w3.org/TR/CSS2/>`__\ 符合\ `W3C标准 <http://www.w3.org/TR/>`__\ ，使得它们能够通过\ `检验 <http://validator.w3.org/>`__\ 。这可以使你的网页避免触发浏览器的古怪行为（quirk），而且使它在”屏幕朗读器”和手机上也能正常工作。

5.3

理解浏览器如何处理JavaScript脚本。

5.4

理解网页上的JavaScript文件、样式表文件和其他资源是如何装载及运行的，考虑它们对页面性能有何影响。在某些情况下，可能应该将脚本文件\ `放置在网页的尾部 <http://developer.yahoo.net/blog/archives/2007/07/high_performanc_5.html>`__\ 。

5.5

理解JavaScript沙箱（Javascript
sandbox）的工作原理，尤其是如果你打算使用iframe。

5.6

知道JavaScript可能无法使用或被禁用，以及Ajax并不是一定会运行。记住，”不允许脚本运行”（NoScript）正在某些用户中变得流行，手机浏览器对脚本的支持千差万别，而Google索引网页时不运行大部分的脚本文件。

5.7

了解301重定向和302重定向之间的\ `区别 <http://www.bigoakinc.com/blog/when-to-use-a-301-vs-302-redirect/>`__\ （这也是一个SEO相关问题）。

5.8

尽可能多得了解你的部署平台（deployment platform）。

5.9

考虑使用\ `样式表重置 <http://stackoverflow.com/questions/167531/is-it-ok-to-use-a-css-reset-stylesheet>`__\ （Reset
Style Sheet）。

5.10

考虑使用JavaScript框架（比如\ `jQuery <http://jquery.com/>`__\ 、\ `MooTools <http://mootools.net/>`__\ 、\ `Prototype <http://www.prototypejs.org/>`__\ ），它们可以使你不用考虑浏览器之间的差异。

**六、解决bug**

6.1

理解程序员20%的时间用于编码，80%的时间用于维护，根据这一点相应安排时间。

6.2

建立一个有效的错误报告机制。

6.3

建立某些途径或系统，让用户可以与你接触，向你提出建议和批评。

6.4

为将来的维护和客服人员撰写文档，解释清楚系统是怎么运行的。

6.5

经常备份！（并且确保这些备份是有效的。）除了备份机制，你还必须有一个恢复机制。

6.6

使用某种版本控制系统储存你的文件，比如\ `Subversion <http://subversion.apache.org/>`__\ 或\ `Git <http://git-scm.org/>`__\ 。

6.7

不要忘记做单元测试（Unit
Testing），\ `Selenium <http://seleniumhq.org/>`__\ 之类的框架会对你有用。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/11/61_things_every_web_developer_should_know.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com