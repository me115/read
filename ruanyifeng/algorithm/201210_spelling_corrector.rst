.. _201210_spelling_corrector:

贝叶斯推断及其互联网应用（三）：拼写检查
===========================================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2012/10/spelling_corrector.html>`__

（这个系列的第一部分介绍了\ `贝叶斯定理 <http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_one.html>`__\ ，第二部分介绍了如何\ `过滤垃圾邮件 <http://www.ruanyifeng.com/blog/2011/08/bayesian_inference_part_two.html>`__\ ，今天是第三部分。）

使用Google的时候，如果你拼错一个单词，它会提醒你正确的拼法。

比如，你不小心输入了seperate。

Google告诉你，\ `这个词 <http://www.ruanyifeng.com/blog/2004/06/seperate_separate.html>`__\ 是不存在的，正确的拼法是separate。

这就叫做”拼写检查”（spelling
corrector）。有好几种方法可以实现这个功能，Google使用的是基于贝叶斯推断的统计学方法。这种方法的特点就是快，很短的时间内处理大量文本，并且有很高的精确度（90%以上）。Google的研发总监\ `Peter
Norvig <http://en.wikipedia.org/wiki/Peter_Norvig>`__\ ，写过一篇著名的\ `文章 <http://norvig.com/spell-correct.html>`__\ ，解释这种方法的原理。

下面我们就来看看，怎么利用贝叶斯推断，实现”拼写检查”。其实很简单，一小段代码就够了。

**一、原理**

用户输入了一个单词。这时分成两种情况：拼写正确，或者拼写不正确。我们把拼写正确的情况记做c（代表correct），拼写错误的情况记做w（代表wrong）。

所谓”拼写检查”，就是在发生w的情况下，试图推断出c。从概率论的角度看，就是已知w，然后在若干个备选方案中，找出可能性最大的那个c，也就是求下面这个式子的最大值。

    　　P(c\|w)

根据贝叶斯定理：

    　　P(c\|w) = P(w\|c) \* P(c) / P(w)

对于所有备选的c来说，对应的都是同一个w，所以它们的P(w)是相同的，因此我们求的其实是

    　　P(w\|c) \* P(c)

的最大值。

P(c)的含义是，某个正确的词的出现”概率”，它可以用”频率”代替。如果我们有一个足够大的文本库，那么这个文本库中每个单词的出现频率，就相当于它的发生概率。某个词的出现频率越高，P(c)就越大。

P(w\|c)的含义是，在试图拼写c的情况下，出现拼写错误w的概率。这需要统计数据的支持，但是为了简化问题，我们假设两个单词在字形上越接近，就有越可能拼错，P(w\|C)就越大。举例来说，相差一个字母的拼法，就比相差两个字母的拼法，发生概率更高。你想拼写单词hello，那么错误拼成hallo（相差一个字母）的可能性，就比拼成haallo高（相差两个字母）。

所以，我们只要找到与输入单词在字形上最相近的那些词，再在其中挑出出现频率最高的一个，就能实现
P(w\|c) \* P(c) 的最大值。

**二、算法**

最简单的算法，只需要四步就够了。

**第一步，建立一个足够大的文本库。**

网上有一些免费来源，比如\ `古登堡计划 <http://www.gutenberg.org/wiki/Main_Page>`__\ 、\ `Wiktionary <http://en.wiktionary.org/wiki/Wiktionary:Frequency_lists>`__\ 、\ `英国国家语料库 <http://www.kilgarriff.co.uk/bnc-readme.html>`__\ 等等。

**第二步，取出文本库的每一个单词，统计它们的出现频率。**

**第三步，根据用户输入的单词，得到其所有可能的拼写相近的形式。**

所谓”拼写相近”，指的是两个单词之间的”编辑距离”（edit
distance）不超过2。也就是说，两个词只相差1到2个字母，只通过——删除、交换、更改和插入——这四种操作中的一种，就可以让一个词变成另一个词。

**第四步，比较所有拼写相近的词在文本库的出现频率。频率最高的那个词，就是正确的拼法。**

根据Peter
Norvig的验证，这种算法的精确度大约为60%-70%（10个拼写错误能够检查出6个。）虽然不令人满意，但是能够接受。毕竟它足够简单，计算速度极快。（本文的最后部分，将详细讨论这种算法的缺陷在哪里。）

**三、代码**

我们使用Python语言，实现上一节的算法。

**第一步，把网上下载的文本库保存为\ `big.txt <http://norvig.com/big.txt>`__\ 文件。**\ 这步不需要编程。

**第二步，加载Python的正则语言模块（re）和collections模块，后面要用到。**

    　　import re, collections

**第三步，定义words()函数，用来取出文本库的每一个词。**

    　　def words(text): return re.findall(‘[a-z]+’, text.lower())

lower()将所有词都转成小写，避免因为大小写不同，而被算作两个词。

**第四步，定义一个train()函数，用来建立一个”字典”结构。**\ 文本库的每一个词，都是这个”字典”的键；它们所对应的值，就是这个词在文本库的出现频率。

    　　def train(features):

    　　　　model = collections.defaultdict(lambda: 1)

    　　　　for f in features:

    　　　　　　model[f] += 1

    　　　　return model

collections.defaultdict(lambda:
1)的意思是，每一个词的默认出现频率为1。这是针对那些没有出现在文本库的词。如果一个词没有在文本库出现，我们并不能认定它就是一个不存在的词，因此将每个词出现的默认频率设为1。以后每出现一次，频率就增加1。

**第五步，使用words()和train()函数，生成上一步的”词频字典”，放入变量NWORDS。**

    　　NWORDS = train(words(file(‘big.txt’).read()))

**第六步，定义edits1()函数，用来生成所有与输入参数word的”编辑距离”为1的词。**

    　　alphabet = ‘abcdefghijklmnopqrstuvwxyz’

    　　def edits1(word):

    　　　　splits = [(word[:i], word[i:]) for i in range(len(word) +
    1)]

    　　　　deletes = [a + b[1:] for a, b in splits if b]

    　　　　transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if
    len(b)>1]

    　　　　replaces = [a + c + b[1:] for a, b in splits for c in
    alphabet if b]

    　　　　inserts = [a + c + b for a, b in splits for c in alphabet]

    　　　　return set(deletes + transposes + replaces + inserts)

edit1()函数中的几个变量的含义如下：

    　　（1）**splits**\ ：将word依次按照每一位分割成前后两半。比如，’abc’会被分割成
    [(”, ‘abc’), (‘a’, ‘bc’), (‘ab’, ‘c’), (‘abc’, ”)] 。

    　　（2）**beletes**\ ：依次删除word的每一位后、所形成的所有新词。比如，’abc’对应的deletes就是
    [‘bc’, ‘ac’, ‘ab’] 。

    　　（3）**transposes**\ ：依次交换word的邻近两位，所形成的所有新词。比如，’abc’对应的transposes就是
    [‘bac’, ‘acb’] 。

    　　（4）**replaces**\ ：将word的每一位依次替换成其他25个字母，所形成的所有新词。比如，’abc’对应的replaces就是
    [‘abc’, ‘bbc’, ‘cbc’, … , ‘abx’, ’ aby’, ‘abz’ ]
    ，一共包含78个词（26 × 3）。

    　　（5）**inserts**\ ：在word的邻近两位之间依次插入一个字母，所形成的所有新词。比如，’abc’
    对应的inserts就是[‘aabc’, ‘babc’, ‘cabc’, …, ‘abcx’, ‘abcy’,
    ‘abcz’]，一共包含104个词（26 × 4）。

最后，edit1()返回deletes、transposes、replaces、inserts的合集，这就是与word”编辑距离”等于1的所有词。对于一个n位的词，会返回54n+25个词。

**第七步，定义edit2()函数，用来生成所有与word的”编辑距离”为2的词语。**

    　　def edits2(word):

    　　　　return set(e2 for e1 in edits1(word) for e2 in edits1(e1))

但是这样的话，会返回一个 (54n+25) \* (54n+25)
的数组，实在是太大了。因此，我们将edit2()改为known\_edits2()函数，将返回的词限定为在文本库中出现过的词。

    　　def known\_edits2(word):

    　　　　return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if
    e2 in NWORDS)

**第八步，定义correct()函数，用来从所有备选的词中，选出用户最可能想要拼写的词。**

    　　def known(words): return set(w for w in words if w in NWORDS)

    　　def correct(word):

    　　　　candidates = known([word]) or known(edits1(word)) or
    known\_edits2(word) or [word]

    　　　　return max(candidates, key=NWORDS.get)

我们采用的规则为：

    　　（1）如果word是文本库现有的词，说明该词拼写正确，直接返回这个词；

    　　（2）如果word不是现有的词，则返回”编辑距离”为1的词之中，在文本库出现频率最高的那个词；

    　　（3）如果”编辑距离”为1的词，都不是文本库现有的词，则返回”编辑距离”为2的词中，出现频率最高的那个词；

    　　（4）如果上述三条规则，都无法得到结果，则直接返回word。

**至此，\ `代码 <http://pastebin.com/UVwuBrcs>`__\ 全部完成，合起来一共21行。**

    　　import re, collections

    　　def words(text): return re.findall(‘[a-z]+’, text.lower())

    　　def train(features):

    　　　　model = collections.defaultdict(lambda: 1)

    　　　　for f in features:

    　　　　　　model[f] += 1

    　　　　return model

    　　NWORDS = train(words(file(‘big.txt’).read()))

    　　alphabet = ‘abcdefghijklmnopqrstuvwxyz’

    　　def edits1(word):

    　　　　splits = [(word[:i], word[i:]) for i in range(len(word) +
    1)]

    　　　　deletes = [a + b[1:] for a, b in splits if b]

    　　　　transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if
    len(b)>1]

    　　　　replaces = [a + c + b[1:] for a, b in splits for c in
    alphabet if b]

    　　　　inserts = [a + c + b for a, b in splits for c in alphabet]

    　　　　return set(deletes + transposes + replaces + inserts)

    　　def known\_edits2(word):

    　　　　return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if
    e2 in NWORDS)

    　　def known(words): return set(w for w in words if w in NWORDS)

    　　def correct(word):

    　　　　candidates = known([word]) or known(edits1(word)) or
    known\_edits2(word) or [word]

    　　　　return max(candidates, key=NWORDS.get)

使用方法如下：

    　　»> correct(‘speling’)

    　　’spelling’

    　　»> correct(‘korrecter’)

    　　’corrector’

**四、缺陷**

我们使用的这种算法，有一些缺陷，如果投入生产环境，必须在这些方面加入改进。

**（1）文本库必须有很高的精确性，不能包含拼写错误的词。**

如果用户输入一个错误的拼法，文本库恰好包含了这种拼法，它就会被当成正确的拼法。

**（2）对于不包含在文本库中的新词，没有提出解决办法。**

如果用户输入一个新词，这个词不在文本库之中，就会被当作错误的拼写进行纠正。

**（3）程序返回的是”编辑距离”为1的词，但某些情况下，正确的词的”编辑距离”为2。**

比如，用户输入reciet，会被纠正为recite（编辑距离为1）,但用户真正想要输入的词是receipt（编辑距离为2）。也就是说，”编辑距离”越短越正确的规则，并非所有情况下都成立。

**（4）有些常见拼写错误的”编辑距离”大于2。**

这样的错误，程序无法发现。下面就是一些例子，每一行前面那个词是正确的拼法，后面那个则是常见的错误拼法。

    | purple perpul curtains courtens minutes muinets successful
    sucssuful inefficient ineffiect availability avaiblity dissension
    desention unnecessarily unessasarily necessary nessasary unnecessary
    unessessay night nite
    |  assessing accesing
    |  necessitates nessisitates

**（5）用户输入的词的拼写正确，但是其实想输入的是另一个词。**

比如，用户输入是where，这个词拼写正确，程序不会纠正。但是，用户真正想输入的其实是were，不小心多打了一个h。

**（6）程序返回的是出现频率最高的词，但用户真正想输入的是另一个词。**

比如，用户输入ther，程序会返回the，因为它的出现频率最高。但是，用户真正想输入的其实是their，少打了一个i。也就是说，出现频率最高的词，不一定就是用户想输入的词。

**（7）某些词有不同的拼法，程序无法辨别。**

比如，英国英语和美国英语的拼法不一致。英国用户输入’humur’，应该被纠正为’humour’；美国用户输入’humur’，应该被纠正为’humor’。但是，我们的程序会统一纠正为’humor’。

（完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2012/10/spelling_corrector.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com