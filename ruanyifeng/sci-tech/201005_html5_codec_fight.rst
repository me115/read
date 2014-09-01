.. _201005_html5_codec_fight:

Html5的视频格式之争
======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/05/html5_codec_fight.html>`__

你可能听说过，HTML5支持直接播放视频。

但是，你可能不知道的是，这背后涉及到复杂的视频格式之争，甚至还牵涉到所有的电子影像设备。

未来，如何在互联网上看视频？

如果你想知道答案，请不要错过下面这篇精彩的文章。它是我迄今读到的最清晰易懂的解说。


=========================

**HTML5的视频格式之争**

作者：Ruthsarian

译者：阮一峰

原文网址：\ `http://ruthsarian.wordpress.com/2010/05/05/the-elephant-in-html5s-room/ <http://ruthsarian.wordpress.com/2010/05/05/the-elephant-in-html5s-room/>`__

发表日期：2010年5月5日

| 
| 
下一代的网页语言HTML5，提供了一个\ `video标签 <http://www.whatwg.org/specs/web-apps/current-work/multipage/video.html>`__\ 。它允许开发者直接将视频嵌入网页，不需要任何第三方插件（比如
Adobe公司的Flash）就能播放。

这当然是一大进步。

但是，有一个核心问题，却没有得到解决。HTML5没有规定，浏览器到底应该播放哪一种格式的视频。浏览器厂商可以自行选择支持的格式。

现在，最流行的视频格式是\ `H.264 <http://en.wikipedia.org/wiki/H.264/MPEG-4_AVC>`__\ 。它有很多优点，编码后生成的视频文件，体积较小，画质也不错。蓝光技术（Blu-ray）就采用这种格式，眼下几乎所有的高清摄像机——不管民用的还是商业的——都使用它。互联网上的在线视频播放，采用它的比例也正在不断上升。

不过，H.264是一种专利视频格式。它的专利被一家\ `MPEG-LA <http://en.wikipedia.org/wiki/MPEG-LA>`__\ 公司控制。

这家公司专门负责管理与H.264有关的\ `“专利池” <http://en.wikipedia.org/wiki/Patent_pool>`__\ （patent
pool）。所谓”专利池”，就是指好几家公司把各自的H.264专利放在一起，组成一个”池”。其他人如果要使用H.264，就必须向”池”的管理公司申请许可，一旦获得了许可，就可以使用”池”中的所有专利。

这就是说，MPEG-LA公司是H.264的实际管理者和收费者。任何支持播放H.264视频的DVD播放机、蓝光播放机、摄像机或者别的设备，都必定有一张MPEG-LA颁发的许可证。

目前为了推广H.264，MPEG-LA规定，只要你的视频用于互联网上的免费播放，就可以无偿获得使用许可证。这就是为什么YouTube可以免费使用MPEG-LA许可证的原因。而像Netflix这样的付费收看公司，就得不到这种优惠了。

MPEG-LA的这种促销政策，并不会永远不变。当前的H.264免费许可证，将于2010年12月31日当期。那么，从2011年1月1日起，MPEG-LA会不会向YouTube、甚至向嵌入H.264视频的个人网站收费呢？完全存在这种可能。专利使用费会是多少？谁也不知道，这由MPEG-LA说了算。另一种可能是，MPEG-LA为了进一步推广H.264，继续保持免费政策，等到2、3年后，它一统市场了，再开始收费。到了那时，如果大多数公司都依赖这种格式，那么它们就别无选择，只能向MPEG-LA交钱。

一些人对这种情形，感到担忧和不满。他们决定自行开发一种没有专利的视频格式，生成的文件体积要与H.264相仿，画质也要差不多。这种格式就叫做\ `Theora <http://www.theora.org/>`__\ 。

Theora的主要开发者，也是Ogg Vorbis（[译注]
一种开源的、无专利的音频压缩格式）的开发者。Theora的基础是On2
Technologies公司开发的VP3视频格式。本世纪初，On2公司将VP3放入了公共领域。Theora对VP3做了大量改进，并且在开发过程中非常小心，避免触犯到任何现存专利。结果，我们就有了一种任何人都可以免费使用、不用担心专利问题的视频格式。

听上去很欢欣鼓舞，对不对？但是为什么大家还在用H.264，还不是抛弃它呢？

这里有几个原因。

第一个原因。没有一家实体公司来承担Theora的专利责任，用户必须自己负责。万一将来有人起诉Theora侵犯了某某专利，用户很可能必须自己掏钱打官司。所以，业界有一种广泛的担心，现在之所以没人起诉Theora，并不是这些人不想起诉，而是要等到某一家大型公司开始采用Theora以后，有可能出现高额的专利赔偿金时，他们再来起诉。最近，苹果公司的CEO乔布斯，就公开表达了\ `这种看法 <http://yro.slashdot.org/story/10/04/30/237238/Steve-Jobs-Hints-At-Theora-Lawsuit>`__\ 。

不过，话说回来，这么多年来，一直有人在威胁Theora，但是从来没人真的起诉。部分原因可能确实是Theora目前还没有重量级使用者，敲诈不到足够的金钱。不过，很多人相信还存在另一种原因，那就是这些”黑暗中的威胁者”害怕闹上法庭以后，万一法庭最后判决Theora胜诉，不存在任何专利问题，那么MPEG-LA公司的大麻烦就来了。因为大家可能就不会再付给它专利费了，而是放心地改为使用Theora了。

第二个原因。一些主要的大公司，本身就是MPEG-LA”专利池”的所有者，比如苹果公司和微软公司。它们各自拥有一些H.264专利，可以从推广H.264中赚到钱，Theora的普及将对它们的利润产生不利影响。所以，苹果公司的Safari浏览器和微软公司的IE浏览器，完全不支持Theora。

第三个原因。有一种观点认为，Theora生成的视频质量不如H.264。早期的Theora
1.0，确实效果不好；但是Theora
1.1 \ `已经被证明 <http://people.xiph.org/~greg/video/ytcompare/comparison.html>`__\ ，效果不逊于H.264，尤其是在低码率的情况下。对Theora的怀疑，导致基于Theora的硬件解码器非常少。这一点对Theora的打击很大。因为H.264解码芯片随处可见，苹果公司的每一台iTouch、iPhone、iPad里面都有，进一步说，过去5年中全世界生产的几乎每一台摄像机都支持H.264硬解码。

现在，再回过头谈HTML5和它的video标签。

开源浏览器Firefox和KHTML，没有资源去购买H.264许可证。因此，它们原生不支持H.264格式的视频，除非用户自己安装第三方插件。而微软公司和苹果公司则是完全不支持Theora，只支持H.264。

这意味着，未来的HTML5网页，不存在一种通用的视频格式。也就是说，HTML5网站开发者必须为同一个视频，准备两个格式的版本，一个是H.264，另一个是Theora。不过，开发者还有另一个选择，就是要求用户安装第三方插件。

猜猜看，大多数开发者会怎么做？他们很可能什么也不做！保持现状不就行了，让用户继续用Flash观看视频吧，什么麻烦都没了。

等一等！苹果公司已经\ `宣布放弃Flash <http://www.apple.com/hotnews/thoughts-on-flash/?aosid=p204&siteid=1503186&program_id=2554&cid=OAS-EMEA-AFF&tduid=dd41a347651da5a6e0bb2e08da2a4ac7>`__\ 了。它的iPad、iPhone和iTouch，不支持任何形式的Flash。想在这些设备上播放视频的开发者，不得不求助于HTML5的video标签。

解决方案是什么？

我想大多数开发者会选择做一个浏览器”嗅探”，专门为苹果公司的设备提供一个H.264格式的视频，其余的设备则显示一个Flash播放器，里面也可以播放这个H.264格式的视频。所以，Flash和H.264成了赢家，Theora和开源软件成了输家，这真是一个令人悲哀的结果。

我们也许有机会避免这种结局。

去年，Google\ `收购 <http://techcrunch.com/2009/08/05/google-acquires-video-compression-technology-company-on2-for-106-million/>`__\ 了On2
Technologies，并且计划把On2的VP8格式\ `开源 <http://arstechnica.com/open-source/news/2010/04/google-planning-to-open-the-vp8-video-codec.ars>`__\ 。
VP8和VP3是同一个体系的视频格式，这意味着它和Theora有亲缘关系。但是，VP8比VP3高出5个版本，这意味着它的效果应该好于Theora。那么，我们就会有一个更好的开源格式，它的背后是一家真正的大公司（Google）在支持。此外，全世界最大的视频网站Youtube，归Google所有，毫无疑问，它会采用VP8。因此，有了这些因素，我们就可能在今后几年中，看到VP8格式的视频飞速增长，把Theora和H.264都甩在身后。

不过，我的预测是，将来的互联网上，各种视频格式都有一席之地。Theora将继续得到开源浏览器（比如Firefox）的支持，苹果公司和微软公司将不断推进H.264，Google将尝试在YouTube上使用VP8。但是，Google也会被迫保留H.264和Flash格式的视频，这是为了支持苹果公司的设备和历史遗留下来的不支持HD视频的设备。

我很希望，Google把VP8放入公共领域。那样的话，Xiph就能利用VP8，做出Theora
2.0。然后，Firefox、 WebKit和Opera都开始支持Theora
2，YouTube也开始把它的视频转为VP8/Theora
2兼容格式，而Flash也将升级支持Theora
2。那么，只剩下苹果公司一家，它要么也支持Theora
2，要么只能开一个自己的视频分享网站，因为它的iPhone用户到时将无法收看Youtube。

这样的未来，难道不值得期待吗？

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/05/html5_codec_fight.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com