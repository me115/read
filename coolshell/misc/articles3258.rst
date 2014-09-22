.. _articles3258:

C++的字符串格式化库
===================

2010年11月2日 `陈皓 <http://coolshell.cn/articles/author/haoel>`__

这里向大家介绍一个C++的字符串格式化库，叫cpptempl，这个库支持对字符串格式的条件，循环，变量插入。看上去很不错，只不过其是基于boost库的。

下面是一个例子：

::

    // The text template
    wstring text = L"I heart {$place}!" ;
    // Data to feed the template engine
    cpptempl::data_map data ;
    // {$place} => Okinawa
    data[L"place"] = cpptempl::make_data(L"Okinawa");
    // parse the template with the supplied data dictionary
    wstring result = cpptempl::parse(text, data) ;

输出结果是：

    I heart Okinawa!

是不是很方便？让我们看一个更复杂的例子：

::

    // You'd probably load this template from a file in real life.
    wstring text = L"Locations\n\n"
        L"{% for place in places %}"
        L"{$place}\n"
        L"{% endfor %}"
        L"" ;
    // Create the list of items
    cpptempl::data_list places;
    places.push_back(cpptempl::make_data(L"Okinawa"));
    places.push_back(cpptempl::make_data(L"San Francisco"));
    // Now set this in the data map
    cpptempl::data_map data ;
    data[L"places"] = cpptempl::make_data(places);
    // parse the template with the supplied data dictionary
    wstring result = cpptempl::parse(text, data) ;

输出结果是：

    Locations
    ~~~~~~~~~

    -  Okinawa
    -  San Francisco

更为详细的说明请到这里：\ `http://bitbucket.org/ginstrom/cpptemplate/wiki/Home <http://bitbucket.org/ginstrom/cpptemplate/wiki/Home>`__\ 。

Google也有一个类似的库叫ctemplate：\ `http://code.google.com/p/google-ctemplate/ <http://code.google.com/p/google-ctemplate/>`__
提供相似的方法，你也可以试试看。与Google相对应的Java库叫Hapax：\ `http://code.google.com/p/hapax/ <http://code.google.com/p/hapax/>`__\ 。

.. |image6| image:: /coolshell/static/20140922093616781000.jpg

.. note::
    原文地址: http://coolshell.cn/articles/3258.html 
    作者: 陈皓 

    编辑: 木书架 http://www.me115.com