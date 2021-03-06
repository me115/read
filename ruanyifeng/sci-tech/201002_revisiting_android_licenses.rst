.. _201002_revisiting_android_licenses:

再谈Android的许可证
======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/02/revisiting_android_licenses.html>`__

1.

两周前，我写了一篇\ `《Android，开源还是封闭？》 <http://www.ruanyifeng.com/blog/2010/02/open_android_or_not.html>`__\ 。

其中有一些内容，我今天要做修正，还想谈一些别的感想。

2.

在谈具体的修正之前，我先来说说，那篇文章的一些情况。

那天白天，我在外面办事，从手机上读到Linux内核撤下所有Android代码的消息，感到很震惊。晚上回家后，仔细读完了相关报道，就一口气写了一些感想。写完已经将近半夜12点。我改了几个错别字，直接把文章贴上网，然后就上床睡觉了。当时也没多想，不觉得它和我的其他文章有何不同。

但是，第二天起床以后，我发现事情变得复杂了。那篇文章被转贴到许多技术论坛和网络媒体，产生了很多回复和议论。要是早知道它会被那么多专业开发人员读到，我一定会写得更谨慎。

更令我意外的是，超过半数的读者，都在批评那篇文章。尤其是一些认识很久的朋友，也对它持负面看法。这令我反思，到底哪里写错了？

节假日期间，我也在思考这个问题。下面就是一些结果。

3.

首先，我必须老老实实承认，那篇文章确实有重大错误。

别的不说，单单文章的标题就是错的。我用《Android，开源还是封闭？》这样的标题，暗示Android表面是开源系统，实质上是封闭系统。我的这种说法是错的。

理由如下：

　　\* Android使用的是Apache许可证，这是一个开源许可证。

　　\* 它的所有源码都公布在网上，你可以用来干任何事情。

　　\*
对于不喜欢这个许可证的人，可以完全合法地把自己的Android程序，改为GPL许可证。

无论从表面还是从实质上看，Android都是一个开放的系统，不是封闭系统。所以，我指责Android是封闭系统，这是不正确的。

由于我把不正确的论断作为那篇文章的基本论据，直接导致结论不可信。因此，文章遭到批评和鄙视，确实也是理所应当。

4.

不过，我的文章写错了，并不代表Google没有做错。你可以这样想，如果Google的所作所为都是无可指责的话，那么为什么Linux内核开发小组会撤下它的代码呢？

这就是我今天想说的第二件事：Android的许可证选择是有问题的。它的问题不在于系统是不是开放，而在于它造成了Linux的分裂。

为什么Android分裂了Linux？

因为Google修改了Linux内核，使得Android与内核不兼容。所有Android上的开源驱动，不经过修改，都无法用于内核，而Google又不愿意修改。因此，内核开发小组只好把它撤下来，因为留着也没用。

这就是Google最让人不满的地方。为了吸引外部程序员，它故意选择Linux内核，而不是自己开发内核。但是开发出来的东西，只能用于Google的产品，不能用于内核。这种分裂行为的后果，就是把Linux社区削弱了。

为了便于思考，让我来举一个类比。

很久以前，有一帮很穷的程序员，在森林里面打游击、闹革命。由于反革命力量实在太强大了，游击队屡战屡败，士气低落。这时，有一个大佬宣布要加入游击队，大家都很振奋，有了大佬的支持，革命有希望成功了。可是没想到，大佬来了以后，宣称他对革命的定义跟别人不一样，要求别人跟着他闹革命。双方谈判不成，大佬就带走了一部分人，自己单干了。所以，大佬加入革命以后，革命势力反而变得更弱小了，还不如不加入呢。

同样地，Android系统越发达，受益的只是Google和手机厂商，而不是Linux社区。后者因为程序员和厂商的流失，力量还会变得更加积弱。事实上，Android的推出，已经使得\ `Maemo <http://maemo.org/>`__\ 、\ `LiMo <http://www.limofoundation.org/>`__\ 、以及其他基于Linux的手机系统，生存处境越发艰难。

可惜我没有早点认识到这些。如果我从这个角度评价Android，那篇文章的错误就会少一些，也不会遭到那么多反对意见了。

5.

在所有的批评中，有些不是针对那篇文章的具体内容，而是针对我个人的。

举几个典型的例子：

　　\* 他开始乱喷了！

　　\* 这个知道分子，又在卖弄自己不懂的东西了。

　　\* 此人大言不惭，就是一个不靠谱的妄人。

虽然我觉得，这些评价对我不太公平，但是我还是要谢谢这些朋友的指教。我愿意虚心汲取教训，以后写文章一定更加严谨，减少错误。

6.

不过，我也想借这个机会澄清一些误解。

我不知道，这些朋友是怎么看待这个网志的。我想问问他们，你们以为我为什么要写这个网志？为了出名？为了赚钱？为了满足虚荣心，显示本人无所不知，很能写？……

不，这些都不是理由。事实上，从任何利益的角度考虑，写网志都是很不值得的事情。一方面，这里的任何一篇文章，写作时间通常都需要2~6小时，而我写了1000多篇，付出的时间和精力难以想像。另一方面，网站唯一的直接收入就是Google广告，但是只能刚好弥补主机和域名的费用，一点都没有多余。如果想出名和赚钱的话，我想一定有比这更轻松的方法吧。至于虚荣心，写了这么久，每天访问量也只有几千IP，我想聪明一点早该知难而退了。

我之所以还在写，是因为我把这个网志当作自己的学习笔记。不断地积累新知识，思考、总结、记录下来，令我感到一种学习的乐趣。所以，我希望大家知道一点，我的网志首先是一个私人空间，不是公共媒体。有些人的网志是为了向公众发言，我的不是。

正是因为我把这里看作一个私人笔记本，所以有时候写作比较随便，经常写一些自己刚刚接触到、没有全面认识的东西。因为笔记里记录的，总是你需要学习的东西，而不是你已经学会的东西，对不对？另一方面，也是因为这是笔记，所以有时候我怕麻烦，没有给出充分的论证和足够的核对，就匆忙写下自己的看法。但是，这不代表我不严谨和粗疏，我只是认为，个人笔记和公开发表的作品不一样。如果是公开发表的论文，每句话都必须有依据，经得起考验，而如果是笔记的话，那就不一定那么严格了。这也是为什么我公开发表的文章，远远少于网志文章的原因之一。

当然，我不为自己的错误辩解，可以告诉大家，我比任何人都更严厉地对待自己的错误。我时刻愿意听取他人的批评，修正自己的错误，因为这是对我有利的。我只是希望大家知道，这个网志的内容本来就不可避免地包含着错误，所以请不要因为文章中有错误，就对我这个人下评判。借用一句张五常的话，”要斩，就斩我的文章，不要斩我的人”。

7.

现在再回到Android的话题，我还有最后一点感想要说。

请先看一些网友对此次Linux内核撤下Android代码事件的评论：

　　\* Google是上市公司，它当然选择对自己最有利的做法。

　　\* Linux内核是Google能找到的最便宜的内核，为什么不用？

　　\* Google又没违反License，还有什么可说的。

　　\* 为什么Android的代码非要回馈给Linux呢？奇怪的想法。

这些意见似乎认为Google的行为符合合约和”自利原则”，因此无可指责。当然，我也同意，从这个角度看，Google没有做错。但是，如果换个角度，让我们从”利他原则”的角度思考，会不会得到不一样的结论呢？比如，Google这样做是不是符合开源运动的理想？有没有伤害到开源社区的利益？……

不过，我不打算在这个问题上深究下去。在一个不正义的第三世界人口大国，讨论到底是”利己”重要，还是”利他”重要，实在是一个太艰难的问题。与其想要找到答案，还不如对自身命运叹息。

令我真正愤怒的，是下面这样的评论：

　　\* GPL这个病毒又作恶了！

　　\*
早觉得Linux像宗教。有时候在想，那个RMS驾崩了怎么办呢？五六十岁的人了，得个病死了很正常。

　　\* 我看RMS没那么容易挂，一般教主都是长命百岁的老妖怪。

我早就感到了，在中国的软件业中，有一种针对自由软件运动的仇恨。不是一般的反感，而是那种咬牙切齿、死而后快的真正仇恨。我想问问这些人，你们的仇恨是从哪里来的？

自由软件运动和它的创始人Richard
Stallman，在没有任何索取的前提下，向全世界无偿奉献出了高质量的软件，全人类都受益于他们的代码，难道这样的人应该被仇恨和诅咒吗？你们的良心到哪里去了？

自由软件运动的理想，是让地球上每一个人都能使用高质量的软件，决不让软件成为阻挡人类自由的障碍。难道这样的理想不值得赞美和追随吗？你们自己没有这种理想，难道还想消灭别人的理想？难道你们非要把软件做成他人的监狱，才感到心满意足？

说到底，不过是因为自由软件可以免费获得，阻碍了这些人的发财梦，所以他们才会恨得这样咬牙切齿。是的，地球上就是有这种人类，谁妨碍了他发财，他就想除掉你。只要自身的利益得到保障，他人的死活才无所谓呢。

正是由于这种自私的人的存在，才需要我们更坚定地支持自由软件。许多人觉得Richard
Stallman顽固得可笑，任何非GPL许可证的软件一概拒绝，有必要吗？但是你要知道，如果不是因为他这样坚守原则，自由软件运动绝对坚持不到今天。因为这个世界到处都是陷阱和烂泥，还有时刻准备着的阴谋家，所以你不能做一点妥协。你退让了一步，整个阵地就全没了。

8.

回想十年前，Windows 98正是如日中天，Windows
XP即将上市，IE的市场份额超过90%，微软公司多么得不可一世，没有人相信它会被击败。大家觉得，只要跟着微软公司走，一定不会错。那时的Linux，还只是很不成熟的黑客玩具，不要说桌面了，就连服务器市场的份额也很小。那时，要是有人说，Linux一定会胜过Windows，大家都会觉得这是痴人说梦。

但是，十年过去了，发生了什么？微软公司依然强大，但已不是不可战胜了；Linux已经跻身主流操作系统，装有它的笔记本电脑在商场里很容易买到；以Firefox为代表的开源浏览器，占据了越来越多的市场份额，超过IE的时刻已经近在眼前了。这就是自由软件的力量，不管你愿意不愿意，就像那副著名油画的名字\ `《自由引导人民》 <http://images.google.cn/images?hl=zh-CN&q=%E8%87%AA%E7%94%B1%E5%BC%95%E5%AF%BC%E4%BA%BA%E6%B0%91&sourceid=navclient-ff&rlz=1B3GGGL_zh-CNCN213CN213&um=1&ie=UTF-8&sa=N&tab=wi>`__\ ，就是这样。

你敢想像，再过十年会发生什么情况吗？如果一边是封闭软件，另一边是开源软件，你赌哪一边？相信我，跟随自由的东西，绝对不会错。历史已经证明，并将继续证明这一点。

所以，我还是要重复前一篇文章中的话：如果Android继续走这种分裂Linux的道路，它不会成功的，不要说超过iPhone，再过二三年，它自己就会被别的开源手机操作系统取代。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/02/revisiting_android_licenses.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com