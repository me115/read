.. _articles9104:

    This is my goat, my goat's name is adam
    ====

c命令
'''''

c 命令是替换匹配行

::

    $ sed "2 c This is my monkey, my monkey's name is wukong" my.txt
    This is my cat, my cat's name is betty
    This is my monkey, my monkey's name is wukong
    This is my fish, my fish's name is george
    This is my goat, my goat's name is adam

    $ sed "/fish/c This is my monkey, my monkey's name is wukong" my.txt
    This is my cat, my cat's name is betty
    This is my dog, my dog's name is frank
    This is my monkey, my monkey's name is wukong
    This is my goat, my goat's name is adam

d命令
'''''

删除匹配行

::

    $ sed '/fish/d' my.txt
    This is my cat, my cat's name is betty
    This is my dog, my dog's name is frank
    This is my goat, my goat's name is adam

    $ sed '2d' my.txt
    This is my cat, my cat's name is betty
    This is my fish, my fish's name is george
    This is my goat, my goat's name is adam

    $ sed '2,$d' my.txt
    This is my cat, my cat's name is betty

p命令
'''''

打印命令

你可以把这个命令当成grep式的命令

::

    # 匹配fish并输出，可以看到fish的那一行被打了两遍，
    # 这是因为sed处理时会把处理的信息输出
    $ sed '/fish/p' my.txt
    This is my cat, my cat's name is betty
    This is my dog, my dog's name is frank
    This is my fish, my fish's name is george
    This is my fish, my fish's name is george
    This is my goat, my goat's name is adam

    # 使用n参数就好了
    $ sed -n '/fish/p' my.txt
    This is my fish, my fish's name is george

    # 从一个模式到另一个模式
    $ sed -n '/dog/,/fish/p' my.txt
    This is my dog, my dog's name is frank
    This is my fish, my fish's name is george

    #从第一行打印到匹配fish成功的那一行
    $ sed -n '1,/fish/p' my.txt
    This is my cat, my cat's name is betty
    This is my dog, my dog's name is frank
    This is my fish, my fish's name is george

几个知识点
^^^^^^^^^^

好了，下面我们要介绍四个sed的基本知识点：

Pattern Space
'''''''''''''

第零个是关于-n参数的，大家也许没看懂，没关系，我们来看一下sed处理文本的伪代码，并了解一下Pattern
Space的概念：

::

    foreach line in file {
        //放入把行Pattern_Space
        Pattern_Space <= line;

        // 对每个pattern space执行sed命令
        Pattern_Space <= EXEC(sed_cmd, Pattern_Space);

        // 如果没有指定 -n 则输出处理后的Pattern_Space
        if (sed option hasn't "-n")  {
           print Pattern_Space
        }
    }

Address
'''''''

第一个是关于address，几乎上述所有的命令都是这样的（注：其中的!表示匹配成功后是否执行命令）

[address[,address]][!]{cmd}

address可以是一个数字，也可以是一个模式，你可以通过逗号要分隔两个address
表示两个address的区间，参执行命令cmd，伪代码如下：

::

    bool bexec = false
    foreach line in file {
        if ( match(address1) ){
            bexec = true;
        }


        if ( bexec == true) {
            EXEC(sed_cmd);
        }

        if ( match (address2) ) {
            bexec = false;
        }
    }

关于address可以使用相对位置，如：

::

    # 其中的+3表示后面连续3行
    $ sed '/dog/,+3s/^/# /g' pets.txt
    This is my cat
      my cat's name is betty
    # This is my dog
    #   my dog's name is frank
    # This is my fish
    #   my fish's name is george
    This is my goat
      my goat's name is adam

命令打包
''''''''

第二个是cmd可以是多个，它们可以用分号分开，可以用大括号括起来作为嵌套命令。下面是几个例子：

::

    $ cat pets.txt
    This is my cat
      my cat's name is betty
    This is my dog
      my dog's name is frank
    This is my fish
      my fish's name is george
    This is my goat
      my goat's name is adam

    # 对3行到第6行，执行命令/This/d
    $ sed '3,6 {/This/d}' pets.txt
    This is my cat
      my cat's name is betty
      my dog's name is frank
      my fish's name is george
    This is my goat
      my goat's name is adam

    # 对3行到第6行，匹配/This/成功后，再匹配/fish/，成功后执行d命令
    $ sed '3,6 {/This/{/fish/d}}' pets.txt
    This is my cat
      my cat's name is betty
    This is my dog
      my dog's name is frank
      my fish's name is george
    This is my goat
      my goat's name is adam

    # 从第一行到最后一行，如果匹配到This，则删除之；如果前面有空格，则去除空格
    $ sed '1,${/This/d;s/^ *//g}' pets.txt
    my cat's name is betty
    my dog's name is frank
    my fish's name is george
    my goat's name is adam 

Hold Space
''''''''''

第三个我们再来看一下 Hold Space

接下来，我们需要了解一下Hold Space的概念，我们先来看四个命令：

| g： 将hold space中的内容拷贝到pattern space中，原来pattern
space里的内容清除 G： 将hold space中的内容append到pattern space\\n后 h：
将pattern space中的内容拷贝到hold space中，原来的hold
space里的内容被清除
|  H： 将pattern space中的内容append到hold space\\n后
|  x： 交换pattern space和hold space的内容

这些命令有什么用？我们来看两个示例吧，用到的示例文件是：

::

    $ cat t.txt
    one
    two
    three

第一个示例：

::

    $ sed 'H;g' t.txt
    one

    one
    two

    one
    two
    three

是不是有点没看懂，我作个图你就看懂了。

|image1|

第二个示例，反序了一个文件的行：

::

    $ sed '1!G;h;$!d' t.txt
    three
    two
    one

其中的 ’1!G;h;$!d’ 可拆解为三个命令

-  1!G —— 只有第一行不执行G命令，将hold space中的内容append回到pattern
   space
-  h —— 第一行都执行h命令，将pattern space中的内容拷贝到hold space中
-  $!d —— 除了最后一行不执行d命令，其它行都执行d命令，删除当前行

这个执行序列很难理解，做个图如下大家就明白了：

|image2|

就先说这么多吧，希望对大家有用。

（全文完）

.. |image0| image:: /coolshell/static/20140922101508571000.png
.. |image1| image:: /coolshell/static/20140922101508606000.jpg
.. |image2| image:: /coolshell/static/20140922101508652000.jpg
.. |image9| image:: /coolshell/static/20140922101508691000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/9104.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com