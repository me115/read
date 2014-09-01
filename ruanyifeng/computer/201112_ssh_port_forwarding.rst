.. _201112_ssh_port_forwarding:

Ssh原理与运用（二）：远程操作与端口转发
==========================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html>`__

接着前一次的\ `文章 <http://www.ruanyifeng.com/blog/2011/12/ssh_remote_login.html>`__\ ，继续介绍SSH的用法。


=======================================

**SSH原理与运用（二）：远程操作与端口转发**

作者：阮一峰

（Image credit: `Tony
Narlock <http://www.flickr.com/photos/skiquel/>`__\ ）

**七、远程操作**

SSH不仅可以用于远程主机登录，还可以直接在远程主机上执行操作。

上一节的操作，就是一个例子：

    　　$ ssh user@host ‘mkdir -p .ssh && cat » .ssh/authorized\_keys’ <
    ~/.ssh/id\_rsa.pub

单引号中间的部分，表示在远程主机上执行的操作；后面的输入重定向，表示数据通过SSH传向远程主机。

这就是说，SSH可以在用户和远程主机之间，建立命令和数据的传输通道，因此很多事情都可以通过SSH来完成。

下面看几个例子。

【例1】

将$HOME/src/目录下面的所有文件，复制到远程主机的$HOME/src/目录。

    　　$ cd && tar czv src \| ssh user@host ‘tar xz’

【例2】

将远程主机$HOME/src/目录下面的所有文件，复制到用户的当前目录。

    　　$ ssh user@host ‘tar cz src’ \| tar xzv

【例3】

查看远程主机是否运行进程httpd。

    　　$ ssh user@host ‘ps ax \| grep [h]ttpd’

**八、绑定本地端口**

既然SSH可以传送数据，那么我们可以让那些不加密的网络连接，全部改走SSH连接，从而提高安全性。

假定我们要让8080端口的数据，都通过SSH传向远程主机，命令就这样写：

    　　$ ssh -D 8080 user@host

SSH会建立一个socket，去监听本地的8080端口。一旦有数据传向那个端口，就自动把它转移到SSH连接上面，发往远程主机。可以想象，如果8080端口原来是一个不加密端口，现在将变成一个加密端口。

**九、本地端口转发**

有时，绑定本地端口还不够，还必须指定数据传送的目标主机，从而形成点对点的”端口转发”。为了区别后文的”远程端口转发”，我们把这种情况称为”本地端口转发”（Local
forwarding）。

假定host1是本地主机，host2是远程主机。由于种种原因，这两台主机之间无法连通。但是，另外还有一台host3，可以同时连通前面两台主机。因此，很自然的想法就是，通过host3，将host1连上host2。

我们在host1执行下面的命令：

    　　$ ssh -L 2121:host2:21 host3

命令中的L参数一共接受三个值，分别是”本地端口:目标主机:目标主机端口”，它们之间用冒号分隔。这条命令的意思，就是指定SSH绑定本地端口2121，然后指定host3将所有的数据，转发到目标主机host2的21端口（假定host2运行FTP，默认端口为21）。

这样一来，我们只要连接host1的2121端口，就等于连上了host2的21端口。

    　　$ ftp localhost:2121

“本地端口转发”使得host1和host3之间仿佛形成一个数据传输的秘密隧道，因此又被称为”SSH隧道”。

**十、远程端口转发**

既然”本地端口转发”是指绑定本地端口的转发，那么”远程端口转发”（remote
forwarding）当然是指绑定远程端口的转发。

还是接着看上面那个例子，host1与host2之间无法连通，必须借助host3转发。但是，特殊情况出现了，host3是一台内网机器，它可以连接外网的host1，但是反过来就不行，外网的host1连不上内网的host3。这时，”本地端口转发”就不能用了，怎么办？

解决办法是，既然host3可以连host1，那么就从host3上建立与host1的SSH连接，然后在host1上使用这条连接就可以了。

我们在host3执行下面的命令：

    　　$ ssh -R 2121:host2:21 host1

R参数也是接受三个值，分别是”远程主机端口:目标主机:目标主机端口”。这条命令的意思，就是让host1监听它自己的2121端口，然后将所有数据经由host3，转发到host2的21端口。由于对于host3来说，host1是远程主机，所以这种情况就被称为”远程端口绑定”。

绑定之后，我们在host1就可以连接host2了：

    　　$ ftp localhost:2121

这里必须指出，”远程端口转发”的前提条件是，host1和host3两台主机都有sshD和ssh客户端。

**十一、SSH的其他参数**

SSH还有一些别的参数，也值得介绍。

N参数，表示只连接远程主机，不打开远程shell；T参数，表示不为这个连接分配TTY。这个两个参数可以放在一起用，代表这个SSH连接只用来传数据，不执行远程操作。

    　　$ ssh -NT -D 8080 host

f参数，表示SSH连接成功后，转入后台运行。这样一来，你就可以在不中断SSH连接的情况下，在本地shell中执行其他操作。

    　　$ ssh -f -D 8080 host

要关闭这个后台连接，就只有用kill命令去杀掉进程。

**十二、参考文献**

　　\* SSH, The Secure Shell: The Definitive Guide: `2.4. Authentication
by Cryptographic
Key <http://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch02_04.htm>`__,
O’reilly

　　\* SSH, The Secure Shell: The Definitive Guide: `9.2. Port
Forwarding <http://docstore.mik.ua/orelly/networking_2ndEd/ssh/ch09_02.htm>`__,
O’reilly

　　\* Shebang: `Tips for Remote Unix Work (SSH, screen, and
VNC) <http://shebang.brandonmintern.com/tips-for-remote-unix-work-ssh-screen-and-vnc>`__

　　\* brihatch: `SSH Host Key
Protection <http://www.symantec.com/connect/articles/ssh-host-key-protection>`__

　　\* brihatch: `SSH User
Identities <http://www.symantec.com/connect/articles/ssh-user-identities>`__

　　\* IBM developerWorks: `实战 SSH
端口转发 <http://www.ibm.com/developerworks/cn/linux/l-cn-sshforward/>`__

　　\* Jianing
YANG：\ `ssh隧道技术简介 <http://blog.jianingy.com/2009/09/ssh%E9%9A%A7%E9%81%93%E6%8A%80%E6%9C%AF%E7%AE%80%E4%BB%8B/>`__

　　\* WikiBooks: `Internet
Technologies/SSH <http://en.wikibooks.org/wiki/Internet_Technologies/SSH>`__

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/12/ssh_port_forwarding.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com