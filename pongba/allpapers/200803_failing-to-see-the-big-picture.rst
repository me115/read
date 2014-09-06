.. _200803_failing-to-see-the-big-picture:

Failing To See the Big Picture – Mistakes we make when learning programming
===========================================================================

`mindhacks.cn <http://mindhacks.cn/2008/03/03/failing-to-see-the-big-picture/>`__

Let’s start with an obvious fact:

    **The Inconvenient Human Nature, #1
    **\ *People are inherently more easily attracted by “interesting”
    (as opposed to “mundane”) things. (We will define “interesting” in
    the later parts)*

What can we derive from this simple axiom?

A lot of things. But since we’re talking about learning programming, we
shall focus mainly on the implications it has for how we learn
programming.

**Programming, the interesting and the mundane**

**The Interesting**

What was the first thing that struck you when you first learned how to
program? Wasn’t it the simple fact that you could order a computer to do
stuff by simply typing a bunch of characters (thinking of the “hello
world” program that we all have written)? But what happened then? You
(hopefully) would learn the things that happened under the hood and
drove your programs, which leads us to the first point:

    *If it’s something under the hood, it’s interesting (therefore
    attracts people).*

People are always curious about the forces behind the phenomenons in
nature since the dawn of human civilization. There’s a need for people
to seek the reason why something happened. We call it the desire to
understand.

After you’ve learned how to hack up a program, and the reason why your
program works all the way down to the bit level. What, then, would be
the next thing you do? You write programs, and in so doing discover more
and more features of your programming language, which means you get more
and more familiar with your language and you start to notice the sorts
of things it can do conveniently and those it can’t. That when language
tricks step into the picture. Language tricks are interesting in that
they enable you to do something you usually can’t do. Human beings are
born problem solvers, we like solving problems just as much as we like
seek out the deep reasons why stuff works. But sadly we’re also adept
problem creators.

In program language sense, the problems of which we seek for solutions
are also the ones created by us. For example, there has recently been a
remarked theory suggesting that design patterns are missing language
features. First we create a language that – of course – has some
drawbacks which we then use language tricks (such as design patterns) to
overcome, but as time goes by, we would get to a point where all those
kinds of patterns aren’t wealth anymore but instead turn into pure
burdens, which is when we build them into the language. However, by
solving the problems created by the previous language, we often create
our own new problems. For example, there’s always this “DSL & GPL”
(where GPL means general-purpose language) debate. On the one hand,
building domain specific features into a language has the obvious
advantage that it would be a lot more convenient for programmers to use
when faced with domain-specific programming tasks, but on the other hand
it would also limit the usage of the language, thus making the whole set
of runtime system only accessable by itself (yeah, of course I know
there’s inter-language operation, but that’s still another additional
step don’t you think?). As to GPLs, the main advantage of them is to use
a single runtime system to serve theoretically unlimited application
areas. This isn’t without compromises, either. The main compromise is
that when faced with domain-specific problems, a GPL only makes for a
second-class language. That’s why Microsoft “invented” the CLR system;
that’s also why Martin Fowler started advocating the so-called
`Language-Oriented
Programming <http://www.martinfowler.com/articles/languageWorkbench.html>`__.

So, to sum up, we created all kinds of language abstractions to make
programming easier. But, as it always has been, by solving one problem
(programming convenience) we create other ones. Our language will no
doubt have many drawbacks, that is, ones that make certain programming
tasks harder to do. That’s where language tricks step in and `steal our
focuses <http://www.codinghorror.com/blog/archives/001011.html>`__ (I
guess you all have a huge stack of language “techniques” books, right?).
If you don’t understand what I’m saying, please take a look at any
suggested “classic C++ books” list.

However, why on earth do we have to learn those tricks? We don’t,
actually. But we tend to. Because:

    *We’re born problem solvers, we like solving problems; problems are
    interesting, even if they’re created by ourselves.*

So, what happens after that? We learn new “techniques”. By “techniques”,
I mean literally dozens of libraries, frameworks, APIs, and several new
languages dubbed “the next big thing” (whether or not they say that
explicitly). Again, why do we have to learn these? We don’t, really. We
can learn them on an as-needed basis. One of the main reasons we’re
attracted to them is because:

    *We like new stuff. If it’s new, it’s interesting.*

Another reason is that we like to **jump on the bandwagon**.

    **The Inconvenient Human Nature, #2
    *Jumping-on-the-bandwagon***\ *: If everyone is doing it, so should
    I.*

Not only do corporations use this strategy to induce us, we do it
ourselves, that is, we create our own bandwagon. When some new language
or technique comes out, we often get so excited that we blind ourselves
to the problems it has; we’re blinded by the halo created by its
featured features. We often, as a result, regard it as a panacea. We
start eagerly to learn it. Programmers are smart animals, probably too
smart. They always yearn for new stuff (check out what’s been discussed
on the major programming forums and you will know what I’m saying), just
like beasts hungering for blood. You walk around on the programming
forums, you see thousands and thousands of technical details; it’s an
endless job learning all those, but programmers love that.\ |image|

**The Mundane**

On the other hand, what do (most) programmers not love? Principles, be
it coding principles in the small (e.g. “always give variables
meaningful names”) or development principles in the large (e.g. “write 
tests before you write the actual code”). They’re just dull. They’re not
tricky; they’re not weird; they’re not challenging. We can’t show the
world how smart we are by complying with some silly rules. What we do
love is writing some insanely tricky code or\ |image| using some
dazzling patterns that nobody else has a clue what we’re doing (or
everybody knows what we’re doing).

Right?

**The Self-handicapped Programmers**

On the one hand, programmers are learning too fast, and learning too
much (see above). On the other hand, there’re always times when we need
to learn new things. |image|

There actually are several kinds of human natures that can hinder one
from learning new things. The  one related to what we’re getting at is:

    **The Inconvenient Human Nature, #3
    *Self-serving bias***\ *: We love what we’re doing, or who we’re; we
    dislike all the things that counter it.*

Admit it or not, we’ve all been through this. After we get familiar
enough with some language or |image|\ platform, the self-serving bias
will start to affect what we like (and learn) and what we dislike (and
won’t learn). Language debates are all too common in programming
community. By blinding ourselves to the disadvantages of our languages
or platforms and to the advantages of other languages or platforms, we
limit our access to new techniques and ideas. In a sense, we limit our
potentials.

**Conclusion**

Most of the times, we’re learning just a little too much. We’re
attracted to interesting stuff like a |image|\ moth to a flame. Or
oftentimes we just learn what everybody else around us is learning or
what we’re  told to learn, not know why we should learn it. Fact is,
however, after we’ve grasped the essential knowledge, other stuff can
just be learned on an as-needed basis. Don’t fall into technical details
unless they’re essential or needed right away. There’s just unlimited
number of details to follow in this area; you can put your time to
something more useful (learning the essentials, learning the ideas, or
even just another language).

On the other hand, however, we’re learning too little. We blind
ourselves to the really important |image|\ subjects just because they
look dull. Tests? That’s like wearing condoms before having sex.
Refactoring? Why do we have to do something that’s not going to generate
new functionalities and not  shinny at all? Defensive Programming? No
thanks, I know what I’m doing here. API Design? Oh-Man, it’s just too
darn hard to consider how somebody else would be using my code when I’m
writing the splendid implementations. New Languages? What… R U saying
that mine is not good enough? Did U NOT see how I can bend the language
to do whatever the heck I want it to do?

`mindhacks.cn <http://mindhacks.cn/2008/03/03/failing-to-see-the-big-picture/>`__

.. |image| image:: /pongba/static/20140906162648422000.jpg
   :target: http://www.douban.com/subject/1417047/
.. |image| image:: /pongba/static/20140906162648761000.jpg
   :target: http://www.douban.com/subject/1432042/
.. |image| image:: /pongba/static/20140906162648895000.jpg
   :target: http://www.douban.com/subject/1451622/
.. |image| image:: /pongba/static/20140906162649009000.jpg
   :target: http://www.douban.com/subject/1229948/
.. |image| image:: /pongba/static/20140906162649141000.jpg
   :target: http://www.douban.com/subject/1419359/
.. |image| image:: /pongba/static/20140906162649507000.jpg
   :target: http://www.douban.com/subject/1771049/

.. note::
    原文地址: http://mindhacks.cn/2008/03/03/failing-to-see-the-big-picture/ 
    作者: 刘未鹏 

    编辑: 木书架 http://www.me115.com