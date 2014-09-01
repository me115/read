.. _201003_built_a_image_server:

搭建了一个图片库
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/03/built_a_image_server.html>`__

经常有读者抱怨，看不到网志中的图片。

确实如此。正常情况下，过去文章中的图片，超过60%都无法在国内正常显示。

但是，事实上，这个网志的所有图片链接都是有效的，没有一个链接是坏的。无法显示只是因为被屏蔽了，只要你不在中国大陆，所有图片都能看到。

最早的时候，我使用\ `Flickr <http://www.flickr.com/>`__\ 存放图片。但是2007年，Flickr被屏蔽了。

后来，我改用\ `Picasa <http://picasaweb.google.com/>`__\ 存放图片。2009年，Picasa也被屏蔽了。

我又改用\ `Photobucket <http://photobucket.com/>`__\ 。2010年1月，Photobucket也被屏蔽了。

怎么办？再换一个地方流浪，还是使用国内的图片储存服务？

我觉得，任何可以免费存放图片的国外服务商，都有可能被屏蔽；而国内的图片服务商，我真的信不过。比如，国内某网站的使用协议写明，他们可以随时无条件删除你的图片，并且不允许上传任何有性意味的图片。

所以，我最后决定，自己搭一个图片库，把图片都存在自己的主机上。

我的思路很简单，先搭建一个开源相册程序，然后修改成Flickr那样就行了。

一开始，我装的是\ `Movable
Type <http://movabletype.org/>`__\ 。毕竟这是每天用的程序，我最熟悉了。但是，我很快发现，它不可能改成相册。MT的长处是生成静态网页，而相册需要的是动态显示，两者根本无法融合。另一方面，MT的开发现在很不景气，\ `第三方插件 <http://www.movabletype.org/cgi-bin/mt/mt-search.cgi?IncludeBlogs=32&search=gallery&x=0&y=0>`__\ 极少，甚至连\ `ajax上传按钮 <http://www.eatdrinksleepmovabletype.com/plugins/better_file_uploader/>`__\ 都没有，必须花20美元购买商业插件，否则文件只能一个个上传。我只好放弃它了。

改用\ `WordPress <http://wordpress.org/>`__\ 以后，我又遇到了另一个问题，那就是插件太多了。WP的\ `相册插件 <http://wordpress.org/extend/plugins/tags/gallery>`__\ 足有几十种之多，我不知道该如何选择。有一个\ `NextGEN
Gallery <http://wordpress.org/extend/plugins/nextgen-gallery/>`__\ 插件的下载人数最多，我就选了它。结果发现，这个插件实在是太优秀了，专业图片网站的功能，它几乎都能实现，而且做得非常易用漂亮。如果你也想搭一个自己的相册，我强烈推荐这个插件。

最后，我搭建完成的图片库网址是\ **`http://image.beekka.com <http://image.beekka.com>`__**\ ，欢迎查看效果。这篇文章里的图片，都是来自那里。因为相册只供我个人使用，所以做得比较粗糙，但是我想要的功能都做到了。

`NextGEN
Gallery <http://alexrabe.de/wordpress-plugins/nextgen-gallery/>`__\ 的详细使用说明，请参见\ `David
Potter <http://dpotter.net/Technical/2008/03/nextgen-gallery-review-introduction/>`__\ 的长篇介绍。我修改的地方，其实只有2个文件。

　　1. 在”Options/Gallery”中的”Show ImageBrowser”选项打勾。

　　2. 修改插件中的gallery.php文件。

　　3. 修改插件中的imagebrowser.php文件。

所有的图片信息，基本上都包含在$image这个对象变量中。使用查看变量，使用filename ?>输出变量值（比如例子中的图片文件名）。

当然，这个图片库也不一定安全，照样有可能被屏蔽。但是，至少一切都在我的控制之中。万一被屏蔽了，只要对图片储存目录打包压缩，然后换一台主机解开压缩包就行了。

我感到，这个图片存储的解决方案有推广意义，值得其他网志作者考虑。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/03/built_a_image_server.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com