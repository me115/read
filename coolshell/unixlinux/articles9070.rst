.. _articles9070:

    Bob    2415     40       57       62      159
    =============================================
      TOTAL:       319      393      350
    AVERAGE:     63.80    78.60    70.00

环境变量
''''''''

即然说到了脚本，我们来看看怎么和环境变量交互：（使用-v参数和ENVIRON，使用ENVIRON的环境变量需要export）

::

    $ x=5

    $ y=10
    $ export y

    $ echo $x $y
    5 10

    $ awk -v val=$x '{print $1, $2, $3, $4+val, $5+ENVIRON["y"]}' OFS="\t" score.txt
    Marry   2143    78      89      87
    Jack    2321    66      83      55
    Tom     2122    48      82      81
    Mike    2537    87      102     105
    Bob     2415    40      62      72

几个花活
^^^^^^^^

最后，我们再来看几个小例子：

::

    #从file文件中找出长度大于80的行
    awk 'length>80' file

    #按连接数查看客户端IP
    netstat -ntu | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -nr

    #打印99乘法表
    #打印99乘法表
    seq 9 | sed 'H;g' | awk -v RS='' '{for(i=1;i<=NF;i++)printf("%dx%d=%d%s", i, NR, i*NR, i==NR?"\n":"\t")}' 

自己撸吧
^^^^^^^^

关于其中的一些知识点可以参看\ `gawk的手册 <http://www.gnu.org/software/gawk/manual/gawk.html>`__\ ：

（全文完）

.. |image0| image:: /coolshell/static/20140920235850723000.jpg
.. |image7| image:: /coolshell/static/20140920235850770000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/9070.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com