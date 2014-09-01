.. _200902_how_to_create_a_dvdrip:

如何制作DVDrip？
===================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/02/how_to_create_a_dvdrip.html>`__

最近，我需要从DVD上剥离一些视频。

我就研究了一下，如何制作DVDrip。下面是我的一点笔记。因为我对视频转换其实完全不懂，所以说得不对的地方，欢迎大家指正。如果你知道其他好的工具软件，也欢迎推荐。


===========================

**1. 什么是ripping？**

ripping直译为”剥离”，可以形象地称为”压制”。

简单说，将多媒体节目从一种格式转化为另一种格式，就是ripping。

**2. 什么是DVDrip？**

将视频节目从DVD上剥离到硬盘中，转化成另一种便于携带的格式，就是DvDrip。

**3. 为什么要DVDrip？**

主要有两个原因：

    1）缩小文件体积。DVD光盘上1小时的节目，大概占2~3GB的空间。ripping之后，可以变为原体积的1/5，甚至1/10。

    2）便于保存和后期处理。DVD光盘上的节目，都是vob格式，需要专门软件或播放机才能观看，很不方便。变为其他格式后，就可以得到更多数字设备的支持，比如存入U盘或储存卡，然后在手机、PSP或mp4播放机中观看。

**4. DVDrip主要有哪些格式？**

目前，国际上最常见的dvdrip格式是avi，主要原因是这种格式比较灵活，可以封装不同编码的视频。而且，这种格式是开源的，没有版权问题。rmvb格式和wma格式就都是有版权的，不能免费用。如果你需要其他格式的话，可以先做成avi文件，然后再转换成相应的格式。

**5. 制作DVDrip使用什么软件？**

DVDrip的制作软件有许多选择。在我用过的软件中，我觉得最容易操作、压制速度最快的是\ `Super
DVD ripper <http://www.dvdtodivx.net>`__\ 。
但是，这个软件是收费软件，Trial版只能免费用10次。不过，网上可以找到\ `破解版 <http://www.google.com/search?hl=en&rlz=1B3GGGL_zh-CNCN213CN213&q=Super+DVD+ripper+%E7%A0%B4%E8%A7%A3%E7%89%88&btnG=Search>`__\ 。

使用这个软件之前，有二个注意点：

    1）你的系统中必须已经有各种视频和音频的解码器。一般来说，如果你的系统已经能播放avi文件了，那么就不用再装解码器了，否则你就需要专门装一次。这方面，国外的\ `K-Lite
    Codec <http://www.free-codecs.com/download/K_lite_codec_pack.htm>`__\ 和国内的\ `PureCodec <http://www.google.com/search?q=%E5%AE%8C%E7%BE%8E%E8%A7%A3%E7%A0%81&sourceid=navclient-ff&ie=UTF-8&rlz=1B3GGGL_zh-CNCN213CN213&aq=t>`__\ （完美解码），我觉得都还可以。

    2）如果你的DVD是加过密的，或者有区码保护。那么必须先用\ `DVD
    Decrypter <http://www.google.com/search?hl=en&rlz=1B3GGGL_zh-CNCN213CN213&q=DVD+Decrypter+%E4%B8%8B%E8%BD%BD&btnG=Search>`__\ 将DVD拷到硬盘上以后，才能进行ripping。

**6. 如何使用Super DVD Ripper？**

Super DVD Ripper用起来非常简单。

1）在软件主界面上，选择”精灵”。

2）在跳出窗口中选择”DVD->AVI”，然后在文件夹窗口，选择你的DVD光驱就可以了。

3）软件读取DVD盘片后，会让你选择需要ripping的title（通常是只有1个Title）。然后，点击select按钮。

4）这时需要设置转换参数。”索引”是选择不同的节目段，”音轨”和”字幕”是选择不同的语言，其他选项一般不用变。选完后，点击”下一步”。

5）选择输出的文件名和目录。

6）确定输出的分辨率和文件大小。

7）点击”视频编码”，选择视频格式。我一般选择”Xvid MPEG-4 Codec”。

8）最点，点击”开始”，视频压缩就开始了。根据硬件和分辨率设置的不同，所需的时间可能为几十分钟，也可能是几个小时。在这个过程中，软件提供视频预览，你可以了解压缩进展到哪个部分了。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/02/how_to_create_a_dvdrip.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com