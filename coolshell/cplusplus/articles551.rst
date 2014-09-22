.. _articles551:

C语言下的错误处理的问题
=======================

2009年4月17日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

下面是三种C语言的错误处理，你喜欢哪一种？还是都不喜欢？

::

    /* 问题: 不充分，而且很容易出错，前面成功分配的资源，后面出错需要帮助释放 */
    int foo(int bar)
    {
            int return_value = 0;
            int doing_okay = 1;
            doing_okay = do_something( bar );
            if (doing_okay)
            {
                    doing_okay = init_stuff();
            }
            if (doing_okay)
            {
                    doing_okay = prepare_stuff();
            }
            if (doing_okay)
            {
                    return_value = do_the_thing( bar );
            }
            return return_value;
    }

::

    /* 问题： 使用goto语句是很不好的 */
    int foo(int bar)
    {
            if (!do_something( bar )) {
                    goto error;
            }
            if (!init_stuff( bar )) {
                    goto error;
            }
            if (!prepare_stuff( bar )) {
                    goto error;
            }
            return do_the_thing( bar );
    error:
            return 0;
    }

::

     
    /* 问题：太多的if嵌套了，无法阅读 */
    int foo(int bar)
    {
            int return_value = 0;
            if (do_something( bar )) {
                    if (init_stuff( bar )) {
                            if (prepare_stuff( bar )) {
                                    return_value = do_the_thing( bar );
                             }
                    }
            }
            return return_value;
    }

.. |image6| image:: /coolshell/static/20140920234447617000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/551.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com