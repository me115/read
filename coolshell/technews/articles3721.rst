.. _articles3721:

Stack Exchange 的架构
=====================

2011年2月23日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

近日，Stack Exchange系统管理员blog上发布了一篇关于\ `Stack
Exchange的架构一瞥 <http://blog.serverfault.com/post/stack-exchanges-architecture-in-bullet-points/>`__\ ，其包括了Stack
Overflow, Server Fault 和 Super User的 Stack Exchange
网络。注意最后一个关于人员的配置。希望能给大家一些相关的参考。

网络流量
^^^^^^^^

-  每月9千5百万个PV
-  每秒800 HTTP 请求
-  每秒180 DNS 请求
-  每秒55Mb 的带宽

数据中心
^^^^^^^^

-  1 机柜 位于俄勒冈的 \ `Peak
   Internet <http://www.peakinternet.com/>`__
   (用于`chat <http://chat.stackexchange.com/>`__ 和\ `Data
   Explorer <http://data.stackexchange.com/>`__)
-  2 机框 位于 纽约的 \ `Peer 1 <http://www.peer1.com/>`__ ( 用于其它的
   Stack Exchange Network)

生产服务器
^^^^^^^^^^

-  12 Web Servers (Windows Server 2008 R2)
-  2 Database Servers (Windows Server 2008 R2 and SQL Server 2008 R2)
-  2 Load Balancers (Ubuntu Server and HAProxy)
-  2 Caching Servers (Redis on CentOS)
-  1 Router / Firewall (Ubuntu Server)
-  3 DNS Servers (Bind on CentOS)

(生产服务器不含故障备份和管理服务器)

使用了的相关的软件和技术
^^^^^^^^^^^^^^^^^^^^^^^^

-  `C# / .NET <http://www.microsoft.com/net/>`__
-  `Windows Server 2008
   R2 <http://www.microsoft.com/windowsserver2008/en/us/default.aspx>`__
-  `SQL Server 2008
   R2 <http://www.microsoft.com/sqlserver/en/us/default.aspx>`__
-  `Ubuntu Server <http://www.ubuntu.com/server>`__
-  `CentOS <http://www.centos.org/>`__
-  `HAProxy <http://haproxy.1wt.eu/>`__ 用于负载均衡
-  `Redis <http://redis.io/>`__ 用于缓存
-  `CruiseControl.NET <http://sourceforge.net/projects/ccnet/>`__
   用于做builds
-  `Lucene.NET <http://lucene.apache.org/lucene.net/>`__ 用于搜索
-  `Bacula <http://www.bacula.org/en/>`__ 用于做备份
-  `Nagios <http://www.nagios.org/>`__ (with n2rrd and drraw plugins)
   用于系统监控
-  `Splunk <http://www.splunk.com/>`__ 用于日志
-  `SQL Monitor from Red
   Gate <http://www.red-gate.com/products/dba/sql-monitor/>`__
   用于监控SQL Server
-  `Mercurial <http://mercurial.selenic.com/>`__
   / `Kiln <http://www.fogcreek.com/kiln/>`__ 用于源码管理
-  `Bind <http://www.isc.org/software/bind>`__ 用于 DNS

程序员和系统管理员
^^^^^^^^^^^^^^^^^^

-  14 程序员
-  2 系统管理员

（全文完）

.. |image6| image:: /coolshell/static/20140921222128746000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/3721.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com