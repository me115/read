.. _articles2082:

Python程序员的进化
==================

2010年2月1日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

以前本站发布过一篇《\ `程序员的进化 <http://coolshell.cn/articles/172.html>`__\ 》，以一种幽默的代码展现方式调侃了程序。下面这篇是关于Python程序员的。以阶乘为例，很有意思。

新手程序员
^^^^^^^^^^

::

    def factorial(x):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)
    print factorial(6)

第一年的刚学完Pascal的新手
^^^^^^^^^^^^^^^^^^^^^^^^^^

::

    def factorial(x):
        result = 1
        i = 2
        while i <= x:
            result = result * i
            i = i + 1
        return result
    print factorial(6)

第一年的刚学完C语言的新手
^^^^^^^^^^^^^^^^^^^^^^^^^

::

    def fact(x): #{
        result = i = 1;
        while (i <= x): #{
            result *= i;
            i += 1;
        #}
        return result;
    #}
    print(fact(6))

第一年刚学完SICP的新手
^^^^^^^^^^^^^^^^^^^^^^

::

    @tailcall
    def fact(x, acc=1):
        if (x > 1): return (fact((x - 1), (acc * x)))
        else:       return acc
    print(fact(6))

第一年刚学完Python的新手
^^^^^^^^^^^^^^^^^^^^^^^^

::

    def Factorial(x):
        res = 1
        for i in xrange(2, x + 1):
            res *= i
        return res
    print Factorial(6)

爱偷懒的程序员
^^^^^^^^^^^^^^

::

    def fact(x):
        return x > 1 and x * fact(x - 1) or 1
    print fact(6)

更懒的 Python 程序员
^^^^^^^^^^^^^^^^^^^^

::

    f = lambda x: x and x * f(x - 1) or 1
    print f(6)

Python 专家
^^^^^^^^^^^

::

    import operator as op
    import functional as f
    fact = lambda x: f.foldl(op.mul, 1, xrange(2, x + 1))
    print fact(6)

Python 黑客
^^^^^^^^^^^

::

    import sys
    @tailcall
    def fact(x, acc=1):
        if x: return fact(x.__sub__(1), acc.__mul__(x))
        return acc
    sys.stdout.write(str(fact(6)) + '\n')

专家级程序员
^^^^^^^^^^^^

::

    import c_math
    fact = c_math.fact
    print fact(6)

英语系的专家级程序员
^^^^^^^^^^^^^^^^^^^^

::

    import c_maths
    fact = c_maths.fact
    print fact(6)

Web 设计者
^^^^^^^^^^

::

    def factorial(x):
        #-------------------------------------------------
        #--- Code snippet from The Math Vault          ---
        #--- Calculate factorial (C) Arthur Smith 1999 ---
        #-------------------------------------------------
        result = str(1)
        i = 1 #Thanks Adam
        while i <= x:
            #result = result * i  #It's faster to use *=
            #result = str(result * result + i)
               #result = int(result *= i) #??????
            result str(int(result) * i)
            #result = int(str(result) * i)
            i = i + 1
        return result
    print factorial(6)

Unix 程序员
^^^^^^^^^^^

::

    import os
    def fact(x):
        os.system('factorial ' + str(x))
    fact(6)

Windows 程序员
^^^^^^^^^^^^^^

::

    NULL = None
    def CalculateAndPrintFactorialEx(dwNumber,
                                     hOutputDevice,
                                     lpLparam,
                                     lpWparam,
                                     lpsscSecurity,
                                     *dwReserved):
        if lpsscSecurity != NULL:
            return NULL #Not implemented
        dwResult = dwCounter = 1
        while dwCounter <= dwNumber:
            dwResult *= dwCounter
            dwCounter += 1
        hOutputDevice.write(str(dwResult))
        hOutputDevice.write('\n')
        return 1
    import sys
    CalculateAndPrintFactorialEx(6, sys.stdout, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL)

公司里的程序员
^^^^^^^^^^^^^^

::

    def new(cls, *args, **kwargs):
        return cls(*args, **kwargs)

    class Number(object):
        pass

    class IntegralNumber(int, Number):
        def toInt(self):
            return new (int, self)

    class InternalBase(object):
        def __init__(self, base):
            self.base = base.toInt()

        def getBase(self):
            return new (IntegralNumber, self.base)

    class MathematicsSystem(object):
        def __init__(self, ibase):
            Abstract

        @classmethod
        def getInstance(cls, ibase):
            try:
                cls.__instance
            except AttributeError:
                cls.__instance = new (cls, ibase)
            return cls.__instance

    class StandardMathematicsSystem(MathematicsSystem):
        def __init__(self, ibase):
            if ibase.getBase() != new (IntegralNumber, 2):
                raise NotImplementedError
            self.base = ibase.getBase()

        def calculateFactorial(self, target):
            result = new (IntegralNumber, 1)
            i = new (IntegralNumber, 2)
            while i <= target:
                result = result * i
                i = i + new (IntegralNumber, 1)
            return result

    print StandardMathematicsSystem.getInstance(new (InternalBase, new (IntegralNumber, 2))).calculateFactorial(new (IntegralNumber, 6))

摘自：\ `来源 <http://gist.github.com/289467>`__

.. |image6| image:: /coolshell/static/20140920235352615000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/2082.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com