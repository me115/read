.. _201202_a_history_of_unix_directory_structure:

Unix目录结构的来历
=====================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/02/a_history_of_unix_directory_structure.html>`__

Unix（包含Linux）的初学者，常常会很困惑，不明白目录结构的含义何在。

举例来说，根目录下面有一个子目录/bin，用于存放二进制程序。但是，/usr子目录下面还有/usr/bin，以及/usr/local/bin，也用于存放二进制程序；某些系统甚至还有/opt/bin。它们有何区别？

长久以来，我也感到很费解，不明白为什么这样设计。像大多数人一样，我只是根据\ `《Unix文件系统结构标准》 <http://www.pathname.com/fhs/pub/fhs-2.3.html>`__\ （Filesystem
Hierarchy Standard），死记硬背不同目录的区别。

昨天，我读到了Rob
Landley的\ `简短解释 <http://lists.busybox.net/pipermail/busybox/2010-December/074114.html>`__\ ，这才恍然大悟，原来Unix目录结构是历史造成的。

话说1969年，\ `Ken
Thompson <http://www.ruanyifeng.com/blog/2009/06/unix_turns_40.html>`__\ 和\ `Dennis
Ritchie <http://www.ruanyifeng.com/blog/2011/10/dennis_ritchie.html>`__\ 在小型机PDP-7上发明了Unix。1971年，他们将主机升级到了PDP-11。

当时，他们使用一种叫做RK05的储存盘，一盘的容量大约是1.5MB。

没过多久，操作系统（根目录）变得越来越大，一块盘已经装不下了。于是，他们加上了第二盘RK05，并且规定第一块盘专门放系统程序，第二块盘专门放用户自己的程序，因此挂载的目录点取名为/usr。也就是说，根目录”/”挂载在第一块盘，”/usr”目录挂载在第二块盘。除此之外，两块盘的目录结构完全相同，第一块盘的目录（/bin,
/sbin, /lib, /tmp…）都在/usr目录下重新出现一次。

后来，第二块盘也满了，他们只好又加了第三盘RK05，挂载的目录点取名为/home，并且规定/usr用于存放用户的程序，/home用于存放用户的数据。

从此，这种目录结构就延续了下来。随着硬盘容量越来越大，各个目录的含义进一步得到明确。

　　**/**\ ：存放系统程序，也就是At&t开发的Unix程序。

　　**/usr**\ ：存放Unix系统商（比如IBM和HP）开发的程序。

　　**/usr/local**\ ：存放用户自己安装的程序。

　　**/opt**\ ：在某些系统，用于存放第三方厂商开发的程序，所以取名为option，意为”选装”。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/02/a_history_of_unix_directory_structure.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com