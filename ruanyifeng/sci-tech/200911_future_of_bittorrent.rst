.. _200911_future_of_bittorrent:

Bt下载的未来
===============================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/11/future_of_bittorrent.html>`__

1.

前天，世界最大BT下载网站”海盗湾”（thepiratebay.org），在官方网志上宣布，永久关闭Tracker服务器：

    **TPB has decided that there is no need to run a tracker anymore, so
    it will remain down! It’s the end of an era.**

    **我们认为没有必要再维护Tracker服务器了，它不会再上线了！它的时代已经结束了。**

无论对于海盗湾，还是对于整个互联网社区，这都是一个非常重大的事件，就像官方网志中所说，”一个时代结束了”。因为从今以后，我们使用BT下载的方式将发生革命性变化。

2.

表面上看，这个事件似乎是经过一系列法律纠纷之后，”海盗湾”做出了妥协，对版权组织的压力屈服了。要知道2009年整个一年，海盗湾都是麻烦缠身。

事情的起源是在2008月1月31日，瑞典检察官对”海盗湾”提起公诉，起诉该网站违反版权法。根据检察官的记录，控告海盗湾的案件已经达到了34起，其中涉及音乐行业的21起、电影行业9起、游戏行业4起。

形势在2009年出现了急剧发展。

    2月16日，瑞典法庭开庭审判此案，庭审持续了9天，到3月3日结束。

    4月17日，四个主要负责人\ `被判有罪 <http://www.ruanyifeng.com/blog/2009/04/some_thoughts_on_the_pirate_bay_guilty.html>`__\ ，入狱一年，支付罚金360万美元。四人随后提起上诉，目前此案仍在上诉中。

    5月13日，几家唱片公司对海盗湾提出追加起诉，并连带起诉了海盗湾的网络接入商Black
    Internet。

    6月30日，瑞典广告娱乐公司GGF宣布与海盗湾达成协议，将以850万美元的价格\ `收购后者 <http://www.ruanyifeng.com/blog/2009/07/the_pirate_bay_sold_and_usenet_being_guilty.html>`__\ 。

    7月30日，美国一些主要的电影公司（包括Disney、Universal、Time
    Warner、Columbia、Sony、NBC和Paramount），加入起诉海盗湾的行列。

    8月21日，法庭宣判Black
    Internet必须立即停止为海盗湾提供网络接入，否则将面临6万美元罚款。

    8月24日，海盗湾下线。但是，24小时之内，海盗湾更换了服务商，又重新上线。

    9月9日，瑞典证券交易所以”严重违规”为由勒令GGF退市，GGF面临破产压力，导致收购海盗湾协议流产。

    10月5日，由于反盗版组织的压力，海盗湾的新网络接入商NForce切断网线，海盗湾再次下线。

    10月6日，海盗湾将服务器搬入荷兰，在一个建在废弃的北约军事基地中的机房重新上线。

    11月17日，海盗湾宣布永久性关闭所有Tracker服务器，此时距离它成立刚好满六年。

3.

难道”海盗湾”真的要”弃暗投明”，做一个顺服的”良民”吗？

不，真正的反抗者永远不会向腐朽的旧势力妥协，不会在金钱和权势面前低头。他们只会改变战斗的方式，继续抵抗下去。

“海盗湾”是这样解释为什么要关闭Tracker服务器的：

    **Now that the decentralized system for finding peers is so well
    developed, …the era is no longer up2date. We have put a server in a
    museum already, and now the tracking can be put there as well.**

    **去中心化的下载模式已经非常成熟了，……tracker模式过时了。我们已经把一台服务器送入了博物馆，现在是时候将旧的下载模式也送进博物馆了。**

这就是说，海盗湾认为，关闭Tracker服务器只是因为它过时了，有更好的技术出现了。海盗湾为什么这么说呢？Tracker模式真的过时了吗？

4.

为了说清楚这个问题，我们必须了解传统的BT下载模式是什么样的，以及Tracker服务器到底起到什么作用。

请回忆一下，你是如何使用BT下载的。

    首先，你从浏览器中找到你感兴趣的内容，下载相应的torrent文件。然后，你用一个BT下载客户端软件，打开这个文件。这时，客户端软件就会根据torrent文件中的网址，自动连接Tracker服务器，从它那里接收到其他正在下载该文件的人的网址名单。下一步，软件就一一与名单上的网址取得联系，从他们那里获取文件的片段，直到整个下载完成。

从这个过程中，我们可以看到，Tracker服务器是整个BT下载的灵魂，文件可以不存在，但是Tracker服务器却不能不存在。要是连不上它，BT下载根本没法启动，因为你无从知道，找谁索要文件。就是由于这个原因，Tracker服务器成为了版权组织打击的重点。他们的想法很明确，只要除掉了Tracker，BT下载就完了。他们的理由是，虽然Tracker本身不传递内容，但是为传播盗版提供了便利，是犯罪的协助者。更何况，Tracker服务器的网址是公开的，很容易找到它的所有者，逃都逃不掉。

在这种形势下，Tracker提供者的日子都很难过。海盗湾是世界排名第一的Tracker提供者，它已经在被追杀了。排名第二的Demonoid从今年9月15日起，就一直处于维护状态，不知道何时重新开放。其他的Tracker提供者基本上也是在法律诉讼的阴影下度日。那些不提供Tracker服务，只提供torrent文件索引服务的网站，比如\ `Mininova <http://mininova.org/>`__\ 、\ `Torrentz <http://www.torrentz.com/>`__\ 、\ `isoHunt <http://isohunt.com/>`__\ ，日子稍微好过一点。但是明摆着，版权组织收拾完Tracker以后，就要收拾它们了。比如，今年8月，Mininova就在一场官司中败诉，荷兰法官判决，该网站必须移除所有侵权内容的torrent文件。

5.

既然，Tracker服务器在法律上很难立足，那么有没有办法，在不使用Tracker的情况下，依然使用BT下载呢？

2002年，纽约大学的两个教授Petar Maymounkov和David
Mazières发表了一篇论文，提出了一种真正去中心化的”点对点”下载模型，他们把它叫做\ `Kademlia方法 <http://en.wikipedia.org/wiki/Kademlia>`__\ 。Emule率先在软件中支持这种方法，KAD网络就是这样来的。到了2005年，BT软件也开始跟进了。目前，所有主流的BT下载客户端软件都支持这种方法。在BT下载中，这被叫做\ `DHT协议 <http://en.wikipedia.org/wiki/Distributed_hash_table>`__\ （Distributed
hash table，分布式哈希表）。

为什么有了DHT协议以后，就不再需要Tracker服务器了，真正实现了去中心化的点对点下载？

根据我对这个协议有限的理解，它是这样做的：

    每一台加入BT下载的计算机，都被称为一个节点（node），有一个自己的ID。这个ID是一个哈希函数值，通过对要分享的文件内容或它的元数据进行哈希运算而得到。这就是说，如果两台计算机正在下载同一个文件，那么它们的ID应该是彼此相似的。于是，每一台计算机就通过寻找与自己相似的ID，来找到自己可以与之交换数据的其他节点。

    DHT协议的另一个巧妙之处在于，每一台计算机只保留自己附近的一部分节点信息。因此，为了得到更多的节点信息，就必须采用接龙方式，在一个个节点之间跳跃，逐步得到全网的节点分布图。这种信息获取方式，就保证了整个网络没有单个的中心，即使一个节点下线了，依然可以通过其他节点来获取文件，因此也就不需要Tracker服务器来告诉你，其他节点在什么地方了。

我对这个协议有一个细节还不是很清楚，我不知道，当BT下载刚刚启动的时候，如何获得第一个外部节点的位置？需不需要有人告诉你，你首先应该去找谁？如果需要的话，那么这个协议或多或少还是有一个中央服务器的。但是，如果不需要的话，那就真的是纯粹的去中心化的分布式下载协议了。

现在所有主流的BT下载客户端，都支持DHT协议，也就是说，它们都能在没有Tracker的情况下完成下载。事实证明，它们不仅能完成，而且还能完成得很好！海盗湾和Demonoid的Tracker服务器都已经关掉了，但是如果你使用它们以前的torrent文件，依然能够完成下载。为什么？这就是DHT协议在发挥作用啊。所以，正是由于DHT可以取代Tracker，海盗湾才会宣布放弃Tracker模式。

6.

让我们看看，现在在海盗湾上，如何使用BT下载。

如果你细心观察的话，你会发现在每一个文件后面，现在都有一个磁铁标志。点击以后，会打开一个地址，这被叫做magnet
URI。

举例来说，今天的热门下载文件是Inglourious.Basterds.DVDRip.XviD-iMBT.avi，按照以前的方式，我们需要下载它的torrent文件，然后才能下载这部电影本身。但是，在新的模式下面，我们不需要下载torrent文件，我们只需要知道它的magnet
URI，就可以了。只要把这个地址告诉下载软件，软件就会开始自动下载。这和emule下载非常相似，只需要一个资源定位信息，其他都不需要。

Inglourious.Basterds.DVDRip.XviD-iMBT.avi的magnet URI如下：

    **magnet: ?xt=urn:btih:60c423137f453492ca34c2d69f6f573408dca35a
     &dn=Inglourious.Basterds.DVDRip.XviD-iMBT.avi
     &tr=http%3A%2F%2Ftracker.publicbt.com%2Fannounce**

分解一下这个网址：

    **magnet**\ ：协议名。

    **xt**\ ：exact topic的缩写，表示资源定位点。BTIH（BitTorrent Info
    Hash）表示哈希方法名，这里还可以使用SHA1和MD5。这个值是文件的标识符，是不可缺少的。

    **dn**\ ：display
    name的缩写，表示向用户显示的文件名。这一项是选填的。

    **tr**\ ：tracker的缩写，表示tracker服务器的地址。这一项也是选填的。

简单说，只要知道\ **magnet:?xt=urn:btih:60c423137f453492ca34c2d69f6f573408dca35a**\ 这个地址，不用下载torrent文件，也不用再了解其他信息，就能开始BT下载这个文件了。

7.

这样做有什么好处？

显而易见的好处是，整个下载网络的可靠性提高了，每一个节点都是可以被替代的。另一个好处是，审查变得更困难了，因为每次下载的路径都是不一样的，而且每个节点都是动态变化的，导致实际上无法追踪谁在下载。此外，magnet
URI只是一个字符串，非常容易传播，根本无法禁止。

因此，从这些方面考虑，magnet
URI取代Tracker模式是大势所趋，迟早成为主流的BT下载方式。

根据\ `TorrentFreak <http://torrentfreak.com/the-pirate-bay-tracker-shuts-down-for-good-091117/%20>`__\ 的消息，下一步，海盗湾连Torrent文件也不打算支持了，将彻底放弃传统的BT下载模式，只提供Magnet
URI。当然，这样一来，BT下载和emule下载就是同一种东西了，因此很可能这两者最终也会统一起来。

更重要的是，我们可以想像，这种模式既然可以安全地、匿名地传播文件，就一定可以安全地、匿名地传播其他东西。当互联网上每一台机器都在自动交换信息的时候，谎言和封锁又能持续多久呢？

8.

最后是几个目前还在运行的Tracker服务器地址，大家可以继续使用，更多的tracker网址请参考\ `Trackon.org <http://www.trackon.org/>`__\ （大陆访问者需翻墙）。

　　\* `OpenBitTorrent <http://openbittorrent.com>`__

　　\* `The HiddenTracker <http://z6gw6skubmo2pj43.tor2web.com/>`__

　　\* `OpenBitTorrent.kg <http://www.openbittorrent.kg/>`__

　　\* `PublicBitTorrent <http://publicbt.com/>`__

　　\* `BitTrk <http://bittrk.appspot.com/>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/11/future_of_bittorrent.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com