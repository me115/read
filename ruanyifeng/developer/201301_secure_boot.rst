.. _201301_secure_boot:

反Secure Boot垄断：兼谈如何在Windows 8电脑上安装Linux
========================================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2013/01/secure_boot.html>`__

**一、自由软件基金会的呼吁**

上周，2012年将近结束的时候，\ `自由软件基金会 <http://www.fsf.org/campaigns/secure-boot-vs-restricted-boot/2012-appeal>`__\ （FSF）发出呼吁，要求人们继续支持反Secure
Boot垄断，希望签名者能达到5万人（目前是4万）。

我觉得，这个呼吁很重要。如果我们不支持，未来就无法自由地使用硬件、安装自己想要的软件。

这绝非危言耸听。而且，由于这个事件直接与Windows
8操作系统有关，因此意味着一切已经迫在眉睫了。

下面，我根据自己的理解，谈谈这到底怎么回事。如果你是一个Linux爱好者，或者喜欢自己安装操作系统，下面的内容与你直接相关。

**二、BIOS和UEFI**

所有电脑启动的时候，都会运行\ `BIOS <http://zh.wikipedia.org/wiki/BIOS>`__\ 程序，用于初始化硬件。

自从个人电脑诞生后，就一直如此。过去30年我们都在使用类似上图的画面，设置硬件参数。不用说，BIOS已经变得日益不适用了。

1998年，Intel牵头，联合AMD、AMI、Apple、Dell、HP、IBM、Lenovo、Microsoft和Phoenix等业界主要厂商，开始制定新一代BIOS。这个项目叫做”统一的可扩展固定接口”（Unified
Extensible Firmware
Interface），简称\ `UEFI <http://en.wikipedia.org/wiki/Unified_Extensible_Firmware_Interface>`__\ 。2005年推出1.1版，目前是2.3版。

将来一开机，电脑运行的将不是BIOS，而是UEFI
BIOS。等它运行结束，再载入操作系统。

**三、微软的态度**

UEFI是一个很先进的、面向未来的规格。但是很长时间内无法推广，原因就是微软公司不积极。

Windows操作系统是桌面市场的主流系统，如果它不推广UEFI，就没有硬件厂商会跟进。所以，普通消费者对这个新规格所知甚少。

意想不到的变化，出现在2011年9月，微软毫无预兆地突然\ `宣布 <http://blogs.msdn.com/b/b8/archive/2011/09/22/protecting-the-pre-os-environment-with-uefi.aspx>`__\ ，Windows
8将启用UEFI。

这本来是一件好事。但是，问题是微软感兴趣的不是整个UEFI，而是UEFI的一个子规格Secure
Boot。它要强行部署Secure Boot。

**四、Secure Boot**

Secure Boot只是UEFI的一个部分。两者的关系是局部与整体的关系。

Secure
Boot的目的，是防止恶意软件侵入。它的做法就是采用密钥。UEFI规定，主板出厂的时候，可以内置一些可靠的公钥。然后，任何想要在这块主板上加载的操作系统或者硬件驱动程序，都必须通过这些公钥的认证。也就是说，这些软件必须用对应的私钥签署过，否则主板拒绝加载。由于恶意软件不可能通过认证，因此就没有办法感染Boot。

这个设想是好的。但是，UEFI没规定哪些公钥是可靠的，也没规定谁负责颁发这些公钥，都留给硬件厂商自己决定。

现在，微软就是要求，主板厂商内置Windows 8的公钥。

**五、Windows 8**

首先明确，在不打开Secure Boot的情况下，Windows
8可以安装。这与安装以前版本的Windows没有差别。

但是，微软规定，所有预装Windows 8的厂商（即OEM厂商）都必须打开Secure
Boot。因此，消费者购买一台预装Windows
8的台式机或笔记本，想要在上面再安装其他操作系统（包括以前版本的Windows）是不可能的，除非关闭Secure
Boot，或者其他操作系统能够通过Windows 8公钥的认证。

如果选择关闭Secure Root，那么预装的Windows 8将无法使用，需要重新安装。

**六、实例：微星主板**

ITwire的记者Sam
Varghese，做了一个\ `实验 <http://www.itwire.com/opinion-and-analysis/open-sauce/57562-installing-windows-8-with-secure-boot/57562-installing-windows-8-with-secure-boot?start=1>`__\ ，想了解在打开Secure
Boot的主板上，如何安装操作系统。

实验对象是微星公司\ `Z77A-G41主板 <http://www.msi.com/product/mb/Z77A-G41.html>`__\ 。它带有Secure
Boot功能，默认是关闭的。

第一步，开机后按Delete键，进入BIOS，选择Windows 8 Configuration选项。

第二步，选择最后一个Secure Boot选项。

第三步，打开（Enabled）Secure Boot功能，然后选择最后一个Key
Management（密钥管理）选项。

第四步，输入厂商提供的公钥，也就是Windows
8的公钥（目前，任何其他操作系统都没有这类公钥。）

第五类，安装Windows
8之后，在命令行界面输入confirm-securebootuefi命令，结果为true，表示secureboot功能打开。

根据Sam Varghese测试，打开Secure
Boot之后，再安装其他操作系统（包括以前版本的Windows），全部被主板拒绝。

**七、对Linux的影响**

Secure
Boot规格的本意是，让操作系统厂商自行选择公钥，通过认证。但是实际上，只有微软公司才有能力，让主板厂商内置它的公钥，其他公司都不具备这种能力。

因此，如果要在打开Secure
Boot的主板上安装Linux系统，这个系统就必须通过Windows 8的认证。

目前，微软公司把Windows
8的数字签名外包给了Verisign。操作系统厂商想要通过认证，就必须花99美元，向Verisign买一张数字证书，嵌入自家的操作系统。

最新动态是，Linux的各个发行版之中，Ubuntu已经购买了数字证书，Fedora和SUSE计划购买，其他发行版还没做出决定。

因此，在预装Windows
8的电脑上安装Linux（或其他操作系统）的最佳做法，就是进入BIOS，关闭Secure
Boot。但是，这意味着你花钱买来的Windows 8将无法使用。

**八、为什么Windows 8的公钥不可接受？**

目前看上去，Linux购买Windows
8的数字证书，是眼下唯一可行的相对容易的解决方法。但是，这种做法不可接受。

首先，系统的公钥被微软控制，后果难以预料。如果微软决定更换和废除这个公钥，Linux就要被迫跟进。

其次，Linux的启动管理器Grub是GPL许可证，该许可证（第三版）\ `明文禁止 <http://www.gnu.org/licenses/gpl-faq.html#GiveUpKeys>`__\ 软件使用密钥配合硬件阻止一部分用户的使用，因此要改用非GPL许可证的启动管理器。

再次，只有几个较大的Linux发行版才有能力购买数字证书，较小的发行版和用户自己定制的版本最终还是需要有自己的公钥。

**九、关于移动设备**

Secure Boot对移动设备的影响，比PC还要严重。

微软明确规定，所有PC主板必须带有关闭Secure
Boot的选项。这不是因为微软的善意，而是因为如果不这样做，它一定会遭到反垄断起诉。

但是，在移动设备领域，微软不占优势，所以它就没有顾虑，规定所有安装Windows的移动设备的Secure
Boot必须打开，而且没有关闭选项。

微软的平板电脑Surface RT就是一个最好的例子。它的Secure
Boot是打开的，没法关闭，而且微软用了一个不同于桌面电脑Windows
8操作系统的公钥，且不提供获得数字证书的途径。因此理论上，用户\ `不可能 <http://mjg59.dreamwidth.org/21189.html>`__\ 在Surface
RT上安装其他操作系统。

还有报道称，使用Windows Phone
8操作系统的智能手机也将采用这种做法。那么，用户也就不可能在Windows
Phone上安装其他操作系统了。

**十、结束语**

Secure
Boot的本来用意是保证系统安全，但现在似乎成了厂商保护市场垄断、阻碍竞争一种手段。

除了微软公司，苹果公司也有这种倾向。在新一代的iPhone和iPad上面安装其他操作系统，似乎是不可能的。

自由软件基金会呼吁反Secure
Boot垄断，就是基于这种考虑：用户应该拥有硬件和软件的使用自由，操作系统应该是开放的，而不是封闭的。

作为一种规格，自由软件基金会并不反对Secure
Boot，它只是要求硬件厂商提供便利，使得用户可以更容易地安装和管理公钥，从而使用硬件平台对所有操作系统（以及设备驱动）保持开放。

我认为，这是完全合理的要求，对于保证用户的自由和业界的健康生态极为重要。让我们一起支持这个行动（\ `签名 <http://www.fsf.org/campaigns/secure-boot-vs-restricted-boot/statement/>`__\ 和\ `捐助 <https://my.fsf.org/donate?pk_campaign=2012-Appeal&pk_kwd=secureboot>`__\ ），密切关注事态下一步的发展。

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2013/01/secure_boot.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com