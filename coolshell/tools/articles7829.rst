.. _articles7829:

28个Unix/Linux的命令行神器
==========================

2012年7月11日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

下面是\ `Kristóf
Kovács <http://kkovacs.eu/>`__\ 收集的28个Unix/Linux下的28个命令行下的工具（\ `原文链接 <http://kkovacs.eu/cool-but-obscure-unix-tools>`__\ ），有一些是大家熟悉的，有一些是非常有用的，有一些是不为人知的。这些工具都非常不错，希望每个人都知道。本篇文章还在\ `Hacker
News上被讨论 <http://news.ycombinator.com/item?id=2567186>`__\ ，你可以过去看看。我以作者的原文中加入了官网链接和一些说明。

dstat & sar
^^^^^^^^^^^

iostat, vmstat, ifstat
三合一的工具，用来查看系统性能（我在《\ `性能调优攻略 <http://coolshell.cn/articles/7490.html>`__\ 》中提到过那三个xxstat工具）。

官方网站：\ `http://dag.wieers.com/rpm/packages/dstat/ <http://dag.wieers.com/rpm/packages/dstat/>`__

你可以这样使用：

::

    alias dstat='dstat -cdlmnpsy'

|dstat screenshot|

slurm
^^^^^

查看网络流量的一个工具

官方网站：\ *  `Simple Linux Utility for Resource
Management <https://computing.llnl.gov/linux/slurm/>`__*

|slurm screenshot|

vim & emacs
^^^^^^^^^^^

真正程序员的代码编辑器。

|vim screenshot|

screen, dtach, tmux, byobu
^^^^^^^^^^^^^^^^^^^^^^^^^^

你是不是经常需要 SSH 或者 telent 远程登录到 Linux
服务器？你是不是经常为一些长时间运行的任务而头疼，比如系统备份、ftp
传输等等。通常情况下我们都是为每一个这样的任务开一个远程终端窗口，因为他们执行的时间太长了。必须等待它执行完毕，在此期间可不能关掉窗口或者断开连接，否则这个任务就会被杀掉，一切半途而废了。

`**Screen** <http://www.gnu.org/software/screen/>`__\ 是一个可以在多个进程之间多路复用一个物理终端的窗口管理器。Screen中有会话的概念，用户可以在一个screen会话中创建多个screen窗口，在每一个screen窗口中就像操作一个真实的telnet/SSH连接窗口那样。请参看IBM
DeveloperWorks的这篇文章《\ `使用 screen
管理你的远程会话 <http://www.ibm.com/developerworks/cn/linux/l-cn-screen/>`__\ 》

|gnu screen screenshot|

`**dtach** <http://dtach.sourceforge.net/>`__\ 是用来模拟screen的detach的功能的小工具，其可以让你随意地attach到各种会话上
。下图为dtach+dvtm的样子。

|image4|

**`tmux <http://tmux.sourceforge.net/>`__**\ 是一个优秀的终端复用软件，类似\ `GNU
Screen <http://www.gnu.org/software/screen/>`__\ ，但来自于OpenBSD，采用BSD授权。使用它最直观的好处就是，通过一个终端登录远程主机并运行tmux后，在其中可以开启多个控制台而无需再“浪费”多余的终端来连接这台远程主机；当然其功能远不止于此。与screen相比的优点：可以横向和纵向分割窗口，且窗格可以自由移动和调整大小。可在多个缓冲区进行复制和粘贴，支持跨窗口搜索；非正常断线后不需重新detach；……
 有人说——**与tmux相比，screen简直弱爆了**\ 。

|image5|

`**byobu** <https://launchpad.net/byobu/>`__\ 是Ubuntu开发的，在Screen的基础上进行包装，使其更加易用的一个工具。最新的Byobu，已经是基于Tmux作为后端了。可通过“byobu-tmux”这个命令行前端来接受各种与tmux一模一样的参数来控制它。Byobu的细节做的非常好，效果图如下：\ |image6|

multitail
^^^^^^^^^

MultiTail是个用来实现同时监控多个文档、类似tail命令的功能的软件。他和tail的区别就是他会在控制台中打开多个窗口，这样使同时监控多个日志文档成为可能。他还可以看log文件的统计，合并log文件，过滤log文件，分屏，……。

官网：\ `http://www.vanheusden.com/multitail/ <http://www.vanheusden.com/multitail/>`__

|multitail screenshot|

tpp
^^^

终端下的PPT，要是在某某大会上用这个演示PPT，就太TMD的Geek了。

官网：\ `http://www.ngolde.de/tpp.html <http://www.ngolde.de/tpp.html>`__

|tpp screenshot|

xargs & parallel
^^^^^^^^^^^^^^^^

Executes tasks from input (even multithread).

xargs 是一个比较古老的命令，有简单的并行功能，这个不说了。对于\ `GNU
parallel <http://www.gnu.org/software/parallel/>`__ ( `online
manpage <http://savannah.gnu.org/projects/parallel>`__ )来说，它不仅能够处理本机上多执行绪，还能分散至远端电脑协助处理。而使用GNU
parallel前，要先确定本机有安装GNU parallel / ssh /
rsync，远端电脑也要安装ssh。

|xargs screenshot|

duplicity & rsyncrypto
^^^^^^^^^^^^^^^^^^^^^^

`Duplicity <http://duplicity.nongnu.org/>`__\ 是使用rsync算法加密的高效率备份软件，Duplicity支持目录加密生产和格式上传到远程或本地文件服务器。

`rsyncrypto <http://rsyncrypto.lingnu.com/index.php/Home_Page>`__ 就是
rsync +
encryption。对于rsync的算法可参看酷壳的\ `rsync核心算法 <http://coolshell.cn/articles/7425.html>`__\ 。

Encrypting backup tools.

|duplicity screenshot|

nethack & slash’em
^^^^^^^^^^^^^^^^^^

`NetHack <http://www.nethack.org/>`__\ （\ `Wiki <http://zh.wikipedia.org/zh/NetHack>`__\ ），20年历史的古老电脑游戏。没有声音，没有漂亮的界面，不过这个游戏真的很有意思。网上有个家伙说：\ **如果你一生只做一件事情，那么玩NetHack**\ 。这句话很惹眼，但也让人觉得这个游戏很复杂不容易上手。其实，这个游戏很虽然很复杂，却容易上手。虽然玩通关很难，但上手很容易。NetHack上有许多复杂的规则，”the
DevTeam thinks of
everything”（开发团队想到了所有的事情)。各种各样的怪物，各种各样的武器….，有许多spoilers文件来说明其规则。除了每次开始随机生成的地图，每次玩游戏，你也都会碰到奇怪的事情:
因为喝了一种药水，变成了机器人;因为踢坏了商店的门被要求高价赔偿;你的狗为你偷来了商店的东西…..
这有点象人生，你不能完全了解这个世界，但你仍然可以选择自己的面对方式。

网上有许多文章所这是最好的电脑游戏或最好的电脑游戏之一。也许是因为它开放的源代码让人赞赏，古老的历史让人宽容，复杂的规则让人敬畏。虽然它不是当前流行的游戏，但它比任何一个当前流行的游戏都更有可能再经受20年的考验。

`Slash’EM <http://www.slashem.org>`__ 也是一个基于NetHack的经典游戏。

|nethack screenshot|

lftp
^^^^

利用\ `lftp <http://lftp.yar.ru/>`__\ 命令行ftp工具进行网站数据的增量备份，镜像，就像使用rsync一样。

|lftp screenshot|

ack
^^^

`ack <http://betterthangrep.com/>`__\ 是一个perl脚本，是grep的一个可选替换品。其可以对匹配字符有高亮显示。是为程序员专门设计的，默认递归搜索，省提供多种文件类型供选。

|ack screenshot|

calcurse & remind + wyrd
^^^^^^^^^^^^^^^^^^^^^^^^

`calcurse <http://calcurse.org/>`__\ 是一个命令行下的日历和日程软件。\ `remind <http://www.roaringpenguin.com/products/remind>`__
+
`wyrd <http://pessimization.com/software/wyrd/>`__\ 也很类似。关于日历，我不得不提一个\ `Linux的Cycle日历 <http://coolshell.cn/articles/3489.html>`__\ ，也是一个神器，呵呵。

|calcurse screenshot|

newsbeuter & rsstail
^^^^^^^^^^^^^^^^^^^^

`newsbeuter  <http://newsbeuter.org/>`__\ 和
`rsstail <http://www.vanheusden.com/rsstail/>`__
是命令行下RSS的阅读工具。

|newsbeuter screenshot|

powertop
^^^^^^^^

`做个环保的程序员 <http://coolshell.cn/articles/7186.html>`__\ ，看看自己的电脑里哪些程序费电。\ `PowerTOP <https://01.org/powertop/>`__ 是一个让
Intel 平台的笔记本电脑节省电源的 Linux 工具。此工具由 Intel
公司发布。它可以帮助用户找出那些耗电量大的程序，通过修复或者关闭那些应用程序或进程，从而为用户节省电源。

|powertop screenshot|

htop & iotop
^^^^^^^^^^^^

`htop <http://htop.sourceforge.net/>`__ 和
`iotop <http://guichaz.free.fr/iotop/>`__  用来查看进程，内存和IO负载。

|htop screenshot|

ttyrec & ipbt
^^^^^^^^^^^^^

`ttyrec <http://0xcc.net/ttyrec/index.html.en>`__ 是一个 tty
控制台录制程序，其所录制的数据文件可以使用与之配套的 ttyplay
播放。不管是你在 tty 中的各种操作，还是在 tty
中耳熟能详的软件，都可进行录制。

`ipbt <http://www.chiark.greenend.org.uk/~sgtatham/ipbt/>`__ 是一个用来回放
ttyrec 所录制的控制台输入过程的工具。

与此类似的还有\ `Shelr <http://shelr.tv/>`__
和 \ `termrec  <http://sourceforge.net/projects/termrec/>`__

|ipbt screenshot|

rsync
^^^^^

通过SSH进行文件同步的经典工具（\ `核心算法 <http://coolshell.cn/articles/7425.html>`__\ ）

|rsync screenshot|

mtr
^^^

`MTR <http://www.bitwizard.nl/mtr/>`__ – traceroute 2.0，其是把
traceroute 和 ping 集成在一块的一个小工具 用于诊断网络。

|mtr screenshot|

socat & netpipes
^^^^^^^^^^^^^^^^

`socat <http://www.dest-unreach.org/socat/>`__\ 是一个多功能的网络工具，名字来由是”
Socket CAT”，可以看作是netcat的N倍加强版。

`netpipes <http://web.purplefrog.com/~thoth/netpipes/>`__ 和socat一样，主要是用来在命令行来进行socket操作的命令，这样你就可以在Shell脚本下行进socket网络通讯了。

|socat screenshot|

iftop & iptraf
^^^^^^^^^^^^^^

`iftop <http://www.ex-parrot.com/~pdw/iftop/>`__\ 和\ `iptraf <http://iptraf.seul.org/>`__\ 可以用来查看当前网络链接的一些流量情况。

|iftop screenshot|

|image23|

siege & tsung
^^^^^^^^^^^^^

`Siege <http://www.joedog.org/siege-home/>`__\ 是一个压力测试和评测工具，设计用于WEB开发这评估应用在压力下的承受能力：可以根据配置对一个WEB站点进行多用户的并发访问，记录每个用户所有请求过程的相应时间，并在一定数量的并发访问下重复进行。

`Tsung <http://tsung.erlang-projects.org/>`__
是一个压力测试工具，可以测试包括HTTP, WebDAV, PostgreSQL, MySQL, LDAP,
and XMPP/Jabber等服务器。针对 HTTP 测试，Tsung 支持 HTTP 1.0/1.1
，包含一个代理模式的会话记录、支持 GET、POST 和 PUT 以及 DELETE
方法，支持 Cookie 和基本的 WWW 认证，同时还支持 SSL。

参看：\ `十个免费的Web压力测试工具 <http://coolshell.cn/articles/2589.html>`__

|siege screenshot|

ledger
^^^^^^

`ledger <http://ledger-cli.org/>`__ 一个命令行下记帐的小工具。

|ledger screenshot|

taskwarrior
^^^^^^^^^^^

`TaskWarrior <http://taskwarrior.org/projects/show/taskwarrior>`__ 是一个基于命令行的
TODO
列表管理工具。主要功能包括：标签、彩色表格输出、报表和图形、大量的命令、底层API、多用户文件锁等功能。

|taskwarrior screenshot|

下图是TaskWarrior 2.0的界面：

|image27|

curl
^^^^

`cURL <http://curl.haxx.se/>`__\ 是一个利用URL语法在命令行下工作的文件传输工具，1997年首次发行。它支持文件上传和下载，所以是综合传输工具，但按传统，习惯称cURL为下载工具。cURL还包含了用于程序开发的libcurl。cURL支援的通訊協定有FTP、FTPS、HTTP、HTTPS、TFTP、SFTP、Gopher、SCP、Telnet、DICT、FILE、LDAP、LDAPS、IMAP、POP3、SMTP和RTSP。

|curl screenshot|

rtorrent & aria2
^^^^^^^^^^^^^^^^

`rTorrent <http://libtorrent.rakshasa.no/>`__
是一个非常简洁、优秀、非常轻量的BT客户端. 它使用了 ncurses 库以 C++
编写, 因此它完全基于文本并在终端中运行. 将 rTorrent 用在安装有 GNU
Screen 和 Secure Shell 的低端系统上作为远程的 BT 客户端是非常理想的。

`aria2 <http://aria2.sourceforge.net/>`__ 是 Linux
下一个不错的高速下载工具。由于它具有分段下载引擎，所以支持从多个地址或者从一个地址的多个连接来下载同一个文件。这样自然就大大加快了文件的下载速度。aria2
也具有断点续传功能，这使你随时能够恢复已经中断的文件下载。除了支持一般的
http(s) 和 ftp 协议外，aria2 还支持 BitTorrent
协议。这意味着，你也可以使用 aria2 来下载 torrent 文件。

 |rtorrent screenshot|

ttytter & earthquake
^^^^^^^^^^^^^^^^^^^^

`TTYtter <http://www.floodgap.com/software/ttytter>`__ 是一个Perl写的命令行上发Twitter的工具，可以进行所有其他平台客户端能进行的事情，当然，支持中文。脚本控、CLI控、终端控、Perl控的最愛。

`Earthquake <https://github.com/jugyo/earthquake>`__\ 也是一个命令行上的Twitter客户端。

|ttytter screenshot|

|image31|

vifm & ranger
^^^^^^^^^^^^^

`Vifm <http://vifm.sourceforge.net/>`__ 基于ncurses的文件管理器，DOS风格，用键盘操作。

|vifm screenshot|

`Ranger <http://savannah.nongnu.org/projects/ranger>`__\ 用 Python
完成，默认为使用 Vim 风格的按键绑定，比如
hjkl（上下左右），dd（剪切），yy（复制）等等。功能很全，扩展/可配置性也非常不错。类似MacOS
X下Finder（文件管理器）的多列文件管理方式。支持多标签页。实时预览文本文件和目录。

|image33|

cowsay & sl
^^^^^^^^^^^

`cowsay  <http://www.nog.net/~tony/warez/cowsay.shtml>`__ 不说了，如下所示，哈哈哈。还有xcowsay，你可以自己搜一搜。

|cowsay screenshot|

 sl是什么？ls？，呵呵，你会经常把ls
打成sl吗？如果是的话，这个东西可以让你娱乐一下，你会看到一辆火车呼啸而过~~，相当拉风。你可以使用sudo
apt-get install sl 安装。

|image35|

| 最后，再介绍一个命令中linuxlogo，你可以使用 sudo apt-get install
linuxlogo来安装，然后，就可以使用linuxlogo -L
|  来看一下各种Linux的logo了

|image36|

（全文完）

.. |dstat screenshot| image:: /coolshell/static/20140922101543775000.png
.. |slurm screenshot| image:: /coolshell/static/20140922101543955000.png
.. |vim screenshot| image:: /coolshell/static/20140922101544092000.png
.. |gnu screen screenshot| image:: /coolshell/static/20140922101544169000.png
.. |image4| image:: /coolshell/static/20140922101544234000.png
.. |image5| image:: /coolshell/static/20140922101544295000.png
.. |image6| image:: /coolshell/static/20140922101544622000.jpg
.. |multitail screenshot| image:: /coolshell/static/20140922101544675000.png
.. |tpp screenshot| image:: /coolshell/static/20140922101544751000.png
.. |xargs screenshot| image:: /coolshell/static/20140922101544793000.png
.. |duplicity screenshot| image:: /coolshell/static/20140922101544838000.png
.. |nethack screenshot| image:: /coolshell/static/20140922101545133000.png
.. |lftp screenshot| image:: /coolshell/static/20140922101545428000.png
.. |ack screenshot| image:: /coolshell/static/20140922101545943000.png
.. |calcurse screenshot| image:: /coolshell/static/20140922101546256000.png
.. |newsbeuter screenshot| image:: /coolshell/static/20140922101546369000.png
.. |powertop screenshot| image:: /coolshell/static/20140922101546470000.png
.. |htop screenshot| image:: /coolshell/static/20140922101546582000.png
.. |ipbt screenshot| image:: /coolshell/static/20140922101546914000.png
.. |rsync screenshot| image:: /coolshell/static/20140922101547068000.png
.. |mtr screenshot| image:: /coolshell/static/20140922101547182000.png
.. |socat screenshot| image:: /coolshell/static/20140922101547300000.png
.. |iftop screenshot| image:: /coolshell/static/20140922101547443000.png
.. |image23| image:: http://coolshell.cn//wp-content/uploads/2012/07/iptraf-tcpudp.gif
.. |siege screenshot| image:: /coolshell/static/20140922101547663000.png
.. |ledger screenshot| image:: /coolshell/static/20140922101548083000.png
.. |taskwarrior screenshot| image:: /coolshell/static/20140922101548194000.png
.. |image27| image:: /coolshell/static/20140922101548291000.png
.. |curl screenshot| image:: /coolshell/static/20140922101548386000.png
.. |rtorrent screenshot| image:: /coolshell/static/20140922101548553000.png
.. |ttytter screenshot| image:: /coolshell/static/20140922101548883000.png
.. |image31| image:: /coolshell/static/20140922101549052000.jpg
.. |vifm screenshot| image:: /coolshell/static/20140922101549188000.png
.. |image33| image:: /coolshell/static/20140922101549321000.png
.. |cowsay screenshot| image:: /coolshell/static/20140922101549383000.png
.. |image35| image:: /coolshell/static/20140922101549492000.jpg
.. |image36| image:: /coolshell/static/20140922101549657000.jpg
.. |image43| image:: /coolshell/static/20140922101549808000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/7829.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com