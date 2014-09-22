.. _articles1525:

GDB 7.0 发布
============

2009年10月9日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

|image0|\ 2009年10月06日，GDB7.0正式发布，新的版本你可以在\ `这里下载 <http://www.gnu.org/software/gdb/download/>`__\ 。本次版本，不但有大家所关注的《GDB\ `回溯调试技术 <http://coolshell.cn/articles/1502.html>`__\ 》，同样还有其它大量的新特性，和对新平台的支持。

新版的GDB7.0支持如下新的平台或配置：

-  x86/x86\_64 Darwin
-  x86\_64 MinGW
-  Lattice Mico32
-  x86/x86\_64 DICOS
-  S+core 3
-  The remote stub now supports x86 Windows CE

其主要的新加入的功能有：（看上去相当地高科技啊，很多术语都不知道怎么翻译，请注意后面的相关解释）

-  Python 脚本调试
-  回溯调试，调式过程记录并重演。
-  不间隔调试。 Non-stop debugging
-  并行调试。 Multi-architecture debugging
-  多进程调试。Multi-inferior, multi-process debugging

    **注释：**

    -  Non-stop
       的意思是，当我们在调试一个进程中的某一个或某一些线程时，可以让没有被调试的线程继续运行不停止。
    -  Multi-architecture在字面上理解是多层架构，但应该是关于并行方面的（请大家指正），比如MIPS或SPARC等并行编程方面的。
    -  Multi-inferior的意思是，你可以同时调试多个不同的进程。在某些情况下，这会更容易帮助我们了解程序的内部执行情况。

当然，本版本也包括了下面的一些改进和补丁：

| \* GDB 为JIT 提供了一个编译接口 \* Tracepoints 可以加上条件 \*
支持多字节和宽字符 \* 为”disassemble”新增加/r 和/m 参数 \*
对共享库的自动获取 \* 支持内联函数 \* 新的远程协议包 \* GDB
开始可以读取压缩调试片段 \* 在Tru64平台下支持线程切换 \* 支持Ada
任务切换
|  \* gdbserver的新功能 ——GDB remote stub
|  \* 一个新的命令，当有系统调用发生时可以停止正在运行的程序

(全文完)

.. |image0| image:: /coolshell/static/20140922102115798000.jpg
   :target: http://www.gnu.org/software/gdb/mascot/
.. |image7| image:: /coolshell/static/20140922102116643000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/1525.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com