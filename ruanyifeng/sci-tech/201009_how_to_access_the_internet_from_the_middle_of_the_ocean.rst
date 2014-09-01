.. _201009_how_to_access_the_internet_from_the_middle_of_the_ocean:

如何在大海中上网？
=====================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2010/09/how_to_access_the_internet_from_the_middle_of_the_ocean.html>`__

1.

9月7日，程序员\ `Justin
Watt <http://justinsomnia.org>`__\ 登上远洋货轮\ `Cap
Cleveland <http://www.marinetraffic.com/ais/shipdetails.aspx?MMSI=636091521>`__\ 号，随船旅行。

这艘船从费城出发，目的地是新西兰的奥克兰，将在大海中航行28天。

一路上，Justin
Watt都在更新自己的网志，分享\ `旅行照片 <http://justinsomnia.org/2010/09/barbecue-party-on-the-container-ship/>`__\ 。根据最新文章，24小时之前，他的\ `位置 <http://maps.google.com/maps?f=q&source=s_q&hl=en&geocode=&q=15.248547+N,+74.746492+W&sll=15.912833,-75.2105&sspn=11.665719,14.128418&g=15%C2%B0+54.77N,+75%C2%B0+12.63W&ie=UTF8≪=15.114553,-74.707031&spn=45.737772,56.513672&z=4>`__\ 是在北纬15.248547度、西经74.746492度，也就是牙买加与哥伦比亚之间的加勒比海上。

但是，这条船没有安装上网设备。他怎么能在大海中上网呢？

2.

今天，他终于揭开了\ `谜底 <http://justinsomnia.org/2010/09/how-to-update-your-blog-from-the-middle-of-the-ocean/>`__\ ，原来用的是海事\ `卫星上网 <http://www.ruanyifeng.com/blog/2009/07/satellite_internet.html>`__\ 。

我一向以为，海事卫星是很贵的东西。看完他的文章才知道，其实个人完全可以负担。按照他说的做，你也能在大海中上网。

3.

先介绍一下，什么是海事卫星？

1979年，国际海事组织（IMO）决定成立”国际移动卫星组织”，为大海中航行的船只提供卫星通信。这个组织发射的卫星，就叫做海事卫星。

1999年，该组织脱离IMO，变成一家私人控股的商业公司，名称为\ `Inmarsat <http://www.inmarsat.com/>`__\ ，
面向全世界提供卫星通信服务。所以，严格地说，它的卫星已经不能再叫做海事卫星，而是普通的商业卫星了。2005年，这家公司在伦敦证券交易所上市。2009年的营业收入是10.38亿美元，净利润是1.53亿美元。

目前，inmarsat公司一共有三颗卫星，除了极地以外，覆盖地球上所有地区。

这三颗卫星组成了一个局域网，inmarsat把这个局域网叫做\ `BGAN <http://baike.baidu.com/view/1515337.htm?func=retitle>`__\ （宽带全球区域网，Broadband
Global Area
Network）。当你的电脑连上卫星的时候，不是直接连入互联网，而是通过BGAN这个局域网的网关，再与互联网进行通信。举例来说，三颗卫星的IP地址是http://192.168.1.35/，上线后可以访问这个地址的web界面，查看卫星状态。

4.

为了卫星上网，你首先必须搞到一个卫星modem，这样才能连上卫星。

BGAN的modem，都是专用型号，也就是说，它只能用来连海事卫星。目前，最低端的型号是\ `Wideye
Sabre
1 <http://www.inmarsat.com/Services/Land/BGAN/Terminals/Wideye_Sabre_1.aspx?language=EN&textonly=False>`__\ ，价格为1138美元。

它的体积是259mm（长）x159mm（宽）x58mm（高），重量1.65公斤，还是相当便携的。内置锂电池，不使用外置电源的情况下，能够待机36小时，连续工作1~3小时。机身上有电话的RJ-11接口和局域网的10Mbps接口，可以满足语音和数据通信。

它的上行速率是240kbps，下行速率是384kbps。根据Justin
Watt的测试，可以跑满，所以勉强还能算宽带。

5.

但是，对于普通人来说，1000多美元/个的modem，还是太贵了。不可能为了一次长途旅行，就去买一个。

怎么办呢？

很简单，买不起就租啊。

你在google里搜索”\ `BGAN
rental <http://www.google.com/search?hl=en&source=hp&q=BGAN+rental&btnG=Google+Search>`__\ “，会得到很多结果。Justin
Watt选择了\ `SatellitePhoneStore.com <http://www.satellitephonestore.com>`__\ ，那里的\ `租金价格 <http://www.satellitephonestore.com/inmarsat/inmarsat-satellite-phone-rental.php>`__\ ，已经是普通人可以承受的水平了。Wideye
Sabre 1的月租金是155.95美元，周租金是39.95美元，日租金是6.95美元。

需要注意的是，这只是设备的租金，上网费另行收取。每MB的价格是6~8美元（根据预付费的不同而不同）。

以Justin
Watt为例，他旅行一个月，设备租金是155.95美元，另外又花了150美元，购买了25MB的流量，总计支出300美元左右，也就是2000元人民币。对于个人来说，这个价格不便宜，但远远称不上高不可攀。在某些特殊情况下，这样的成本可以换来一个月不管何时何地、始终与外界保持联系，应该还是值得的。

6.

最后，总结一下使用海事卫星上网的步骤。

　　第一步：来到室外。

　　第二步：打开笔记本电脑。

　　第三步：打开卫星modem。

　　第四步：用网线将两者连起来。

　　第五步：在笔记本上，打开浏览器，访问网关http://192.168.1.35/。按照提示，键入用户名和密码。

　　第六步：选择Setup选项卡，点击”Register
Network”链接，将设备在网络中登记。

　　第七步：选择Data选项卡，点击”Primary Profiles”选项中的”Activate
Profile”按钮，确认你的设备已经获得了IP地址。

现在，你就可以在大海中上网了。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2010/09/how_to_access_the_internet_from_the_middle_of_the_ocean.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com