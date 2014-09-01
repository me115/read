.. _200902_basic_html_template_and_css_styling_part_ii:

Html模板和css基准样式（二）
==============================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2009/02/basic_html_template_and_css_styling_part_ii.html>`__

今天，我要写的是CSS文件的模块化。

如果你看过CSS文件，就会知道很难看懂它。每个CSS文件有许多行，每一行就是一条命令，可以放在文件的任何位置，都能够同样生效，而且后面的行随时可以覆盖前面的行的设置。所以，阅读CSS文件就好像猜谜一样，必须努力将不同的线索拼起来，令人非常痛苦，这直接导致了日后难于维护和修改。

考虑到这一点，很早就有人提出了CSS文件的模块化，就是将相关的设置都放在一起。一般来说，CSS中的设置可以分成下面几个模块：

    \* typography（字体）

    \* colour（颜色）

    \* link（链接）

    \* forms（表单）

    \* layout（布局）

    \* navigation（导航）

这些模块当然不是固定不变的，你可以根据自己的需要进行增删。有时候，单单一个模块中就有许多行，这时候，你就可以把它独立出来，作为一个单独的CSS子文件，然后在父文件中进行调用。

比如，昨天的HTML模板中，调用CSS文件是这样写的：

    @import url(style.css);

在这里，style.css就是父文件，然后我们在其中调用子文件：

    | /\* typography styles \*/
    |  @import url(“typo.css”);

    | /\* form elements \*/
    |  @import url(“forms.css”);

    | /\* main layout \*/
    |  @import url(“layout.css”);

    | /\* navigation \*/
    |  @import url(“horizontal-nav.css”);

    | /\* colour scheme \*/
    |  @import url(“skin.css”);

除了上面这些模块以外，CSS中有些设置是全局性的，主要用于覆盖浏览器的默认样式，这被称作CSS基准样式。我们可以把基准样式单独做成一个base.css，将它也加入主样式表。

    | /\* basic styling \*/
    |  @import url(“base.css”);

网上有很多别人已经写好的CSS基准样式，我下面采用的是\ `Crucial Web
Hosting <http://www.crucialwebhost.com/blog/master-stylesheet-the-most-useful-css-technique/>`__\ 提供的一份，我觉得写得比较规范，内容也很充分。

    | /\*\*\*\*\* Global Settings \*\*\*\*\*/ html, body { border:0;
    margin:0; padding:0; } body { font:100%/1.25 Arial, Helvetica,
    sans-serif; } /\*\*\*\*\* Headings \*\*\*\*\*/ h1, h2, h3, h4, h5,
    h6 { margin:0; padding:0; font-weight:normal; } h1 { padding:30px
    0 25px 0; letter-spacing:-1px; font-size:2em; } h2 { padding:20px 0;
    letter-spacing:-1px; font-size:1.5em; } h3 { font-size:1em;
    font-weight:bold; } /\*\*\*\*\* Common Formatting \*\*\*\*\*/ p, ul,
    ol { margin:0; padding:0 0 1.25em 0; } ul, ol { padding:0 0 1.25em
    2.5em; } blockquote { margin:1.25em; padding:1.25em 1.25em 0 1.25em;
    } small { font-size:0.85em; } img { border:0; } sup {
    position:relative; bottom:0.3em; vertical-align:baseline; } sub {
    position:relative; bottom:-0.2em; vertical-align:baseline; }
    acronym, abbr { cursor:help; letter-spacing:1px; border-bottom:1px
    dashed; } /\*\*\*\*\* Links \*\*\*\*\*/ a, a:link, a:visited,
    a:hover { text-decoration:underline; } /\*\*\*\*\* Forms \*\*\*\*\*/
    form { margin:0; padding:0; display:inline; } input, select,
    textarea { font:1em Arial, Helvetica, sans-serif; } textarea {
    width:100%; line-height:1.25; } label { cursor:pointer; }
    /\*\*\*\*\* Tables \*\*\*\*\*/ table { border:0; margin:0 0 1.25em
    0; padding:0; } table tr td { padding:2px; } /\*\*\*\*\* Wrapper
    \*\*\*\*\*/ #wrap { width:960px; margin:0 auto; } /\*\*\*\*\* Global
    Classes \*\*\*\*\*/ .clear { clear:both; } .float-left { float:left;
    } .float-right { float:right; } .text-left { text-align:left; }
    .text-right { text-align:right; } .text-center { text-align:center;
    } .text-justify { text-align:justify; } .bold { font-weight:bold; }
    .italic { font-style:italic; } .underline { border-bottom:1px solid;
    } .highlight { background:#ffc; } .wrap { width:960px;margin:0 auto;
    } .img-left { float:left;margin:4px 10px 4px 0; } .img-right {
    float:right;margin:4px 0 4px 10px; } .nopadding { padding:0; }
    |  .noindent { margin-left:0;padding-left:0; }
    |  .nobullet { list-style:none;list-style-image:none; }

有了HTML模板和CSS基准样式以后，最后就剩下一个页面布局的问题了，这将是我明天要写的内容。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2009/02/basic_html_template_and_css_styling_part_ii.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com