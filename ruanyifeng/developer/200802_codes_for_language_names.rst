.. _200802_codes_for_language_names:

语种名称代码
===============================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2008/02/codes_for_language_names.html>`__

我们经常需要用缩写的代码来表示一种语言，比如用en表示英语，用de表示德语。\ `ISO
639 <http://www.loc.gov/standards/iso639-2/>`__\ 就是规定语种代码的国际标准。

最早的时候，ISO 639规定的代码是，用两个拉丁字母表示一种语言，这被称为ISO
639-1。但是，两个拉丁字母最多只有26\ :sup:`2`\ =676种组合，而世界上已知的语言总数可能有六七千种，因此明显是不够的。所以，后来又规定了ISO
639-2，用三个拉丁字母的组合表示一种语言。

常见语言的ISO 代码如下表。

ISO639-1 CodeISO639-2
Code中文名英文名arara阿拉伯语Arabickokor朝鲜语Koreandedeu德语Germanrurus俄语Russianfrfra法语Frenchzhzho汉语Chineselalat拉丁语Latinptpor葡萄牙语Portuguesejajpn日语Japaneseesspa西班牙语Spaineseeneng英语Englishitita意大利语Italianhihin印地语Hindiyiyid意第绪语Yiddish

完整的语言代码表请看\ `这里 <http://www.loc.gov/standards/iso639-2/php/code_list.php>`__\ 。

但是只规定语种代码还不够，在同一种语言中，往往还包括许多种变体，比如中文分为简体中文和繁体中文两种，因此还必须规定子代码。

以往，人们常用zh-CN表示在中国大陆地区使用的中文，也就是简体中文，用zh-TW表示在台湾地区使用的中文，也就是繁体中文。但是，这种表示法很不完善，试问中国大陆地区出版的繁体中文书籍，应该如何用代码表示呢？

目前，语言的标签表示法的国际标准是\ `RFC
4646 <http://www.ietf.org/rfc/rfc4646.txt>`__\ ，名称是《Tags for
Identifying Languages》。

简单说，这个文件规定，一种语言的标签应该按照如下方式排列：

    **language-script-region-variant-extension-privateuse**

    1. language：这部分就是ISO 639规定的代码，比如中文是zh。

    2. script：表示变体，比如简体汉字是zh-Hans，繁体汉字是zh-Hant。

    3.
    region：表示语言使用的地理区域，比如zh-Hans-CN就是中国大陆使用的简体中文。

    4. variant：表示方言。

    5. extension-privateus：表示扩展用途和私有标识。

    一般约定，language标签全部小写，region标签全部大写，script标签只有首字母大写。不同标签之间用连字号-链接。

下面列出一些与中文有关的语言标签。

    | zh-Hans 简体中文 zh-Hans-CN 大陆地区使用的简体中文 zh-Hans-HK
    香港地区使用的简体中文 zh-Hans-MO 澳门使用的简体中文 zh-Hans-SG
    新加坡使用的简体中文 zh-Hans-TW 台湾使用的简体中文 zh-Hant 繁体中文
    zh-Hant-CN 大陆地区使用的繁体中文 zh-Hant-HK 香港地区使用的繁体中文
    zh-Hant-MO 澳门使用的繁体中文
    |  zh-Hant-SG 新加坡使用的繁体中文
    |  zh-Hant-TW 台湾使用的繁体中文

此外，还有一些目前仍在使用，但因不符合规范，将被逐步替代（grandfathered）的标签。

    | zh-hakka 客家话 zh-cmn 普通话 zh-cmn-Hans 简体普通话 zh-cmn-Hant
    繁体普通话 zh-gan 江西话 zh-guoyu 国语 zh-min 福建话 zh-min-nan
    闽南话 zh-wuu 吴语（上海话）
    |  zh-xiang 湖南话
    |  zh-yue 粤语

有一点需要注意，任何合法的标签都必须经过IANA的认证，已通过认证的标签可以在这个\ `网页 <http://www.iana.org/assignments/language-subtag-registry>`__\ 查到。此外，网上还有一个非官方的\ `标签搜索引擎 <http://people.w3.org/rishida/utils/subtags/>`__\ 。

[延伸阅读]

\* `W3C: Language tags in HTML and
XML <http://www.w3.org/International/articles/language-tags/#bytheway>`__

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2008/02/codes_for_language_names.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com