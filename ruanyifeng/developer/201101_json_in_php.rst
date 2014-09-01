.. _201101_json_in_php:

在php语言中使用json
======================================

`ruanyifeng.com <http://www.ruanyifeng.com/blog/2011/01/json_in_php.html>`__

目前，\ `JSON <http://www.json.org/>`__\ 已经成为最流行的数据交换格式之一，各大网站的API几乎都支持它。

我写过一篇\ `《数据类型和JSON格式》 <http://www.ruanyifeng.com/blog/2009/05/data_types_and_json.html>`__\ ，探讨它的设计思想。今天，我想总结一下PHP语言对它的支持，这是开发互联网应用程序（特别是编写API）必须了解的知识。

从5.2版本开始，PHP原生提供\ `json\_encode() <http://www.php.net/manual/en/function.json-encode.php>`__\ 和\ `json\_decode() <http://www.php.net/manual/en/function.json-decode.php>`__\ 函数，前者用于编码，后者用于解码。

**一、json\_encode()**

该函数主要用来将数组和对象，转换为json格式。先看一个数组转换的例子：

    ::

        　　$arr = array ('a'=>1,'b'=>2,'c'=>3,'d'=>4,'e'=>5);
        　　
        　　echo json_encode($arr);
        　　

结果为

    ::

        　　{"a":1,"b":2,"c":3,"d":4,"e":5}
        　　

再看一个对象转换的例子：

    ::

        　　$obj->body           = 'another post';
        　　
        　　$obj->id             = 21;
        　　
        　　$obj->approved       = true;
        　　
        　　$obj->favorite_count = 1;
        　　
        　　$obj->status         = NULL;
        　　
        　　echo json_encode($obj);
        　　

结果为

    ::

        　　{
        　　　　"body":"another post",
        　　
        　　　　"id":21,
        　　
        　　　　"approved":true,
        　　
        　　　　"favorite_count":1,
        　　
        　　　　"status":null
        　　} 
        　　

由于json只接受utf-8编码的字符，所以json\_encode()的参数必须是utf-8编码，否则会得到空字符或者null。当中文使用GB2312编码，或者外文使用ISO-8859-1编码的时候，这一点要特别注意。

**二、索引数组和关联数组**

PHP支持两种数组，一种是只保存”值”（value）的索引数组（indexed
array），另一种是保存”名值对”（name/value）的关联数组（associative
array）。

由于javascript不支持关联数组，所以json\_encode()只将索引数组（indexed
array）转为数组格式，而将关联数组（associative array）转为对象格式。

比如，现在有一个索引数组

    ::

        　　$arr = Array('one', 'two', 'three');
        　　
        　　echo json_encode($arr);
        　　

结果为：

    ::

        　　["one","two","three"] 
        　　

如果将它改为关联数组：

    ::

        　　$arr = Array('1'=>'one', '2'=>'two', '3'=>'three');
         　　
        　　echo json_encode($arr);
        　　　　

结果就变了：

    ::

        　　{"1":"one","2":"two","3":"three"} 
        　　

注意，数据格式从”[]”（数组）变成了”{}”（对象）。

如果你需要将”索引数组”强制转化成”对象”，可以这样写

    ::

        　　json_encode( (object)$arr );
        　　

或者

    ::

        　　json_encode ( $arr, JSON_FORCE_OBJECT );
        　　

**三、类（class）的转换**

下面是一个PHP的类：

    ::

        　　class Foo {
        　　
        　　　　const     ERROR_CODE = '404';
        　　
        　　　　public    $public_ex = 'this is public';
        　　
        　　　　private   $private_ex = 'this is private!';
        　　
        　　　　protected $protected_ex = 'this should be protected'; 
         　　
        　　　　public function getErrorCode() {
        　　
        　　　　　　return self::ERROR_CODE;
        　　
        　　　　}
        　　
        　　}
        　　

现在，对这个类的实例进行json转换：

    ::

        　　$foo = new Foo;
        　　
        　　$foo_json = json_encode($foo);
        　　
        　　echo $foo_json;
        　　

输出结果是

    ::

        　　{"public_ex":"this is public"} 
        　　

可以看到，除了公开变量（public），其他东西（常量、私有变量、方法等等）都遗失了。

**四、json\_decode()**

该函数用于将json文本转换为相应的PHP数据结构。下面是一个例子：

    ::

        　　$json = '{"foo": 12345}';
         　　
        　　$obj = json_decode($json);
        　　
        　　print $obj->{'foo'}; // 12345
        　　

通常情况下，json\_decode()总是返回一个PHP对象，而不是数组。比如：

    ::

        　　$json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
         　　
        　　var_dump(json_decode($json));
        　　

结果就是生成一个PHP对象：

    ::

        　　object(stdClass)#1 (5) {
        　　
        　　　　["a"] => int(1)
        　　　　["b"] => int(2)
        　　　　["c"] => int(3)
        　　　　["d"] => int(4)
        　　　　["e"] => int(5)
        　　
        　　}
        　　

如果想要强制生成PHP关联数组，json\_decode()需要加一个参数true：

    ::

        　　$json = '{"a":1,"b":2,"c":3,"d":4,"e":5}';
         　　
        　　var_dump(json_decode($json,true));
        　　

结果就生成了一个关联数组：

    ::

        　　array(5) {
        　　
        　　 　　["a"] => int(1)
        　　 　　["b"] => int(2)
        　　 　　["c"] => int(3)
        　　 　　["d"] => int(4)
        　　 　　["e"] => int(5)
        　　
        　　}
        　　

**五、json\_decode()的常见错误**

下面三种json写法都是错的，你能看出错在哪里吗？

    ::

        　　$bad_json = "{ 'bar': 'baz' }";
        　　
        　　$bad_json = '{ bar: "baz" }';
        　　
        　　$bad_json = '{ "bar": "baz", }';
        　　

对这三个字符串执行json\_decode()都将返回null，并且报错。

| 第一个的错误是，json的分隔符（delimiter）只允许使用双引号，不能使用单引号。第二个的错误是，json名值对的”名”（冒号左边的部分），任何情况下都必须使用双引号。第三个的错误是，最后一个值之后不能添加逗号（trailing
comma）。
| 
另外，json只能用来表示对象（object）和数组（array），如果对一个字符串或数值使用json\_decode()，将会返回null。

    ::

        　　var_dump(json_decode("Hello World")); //null
        　　

**六、参考材料**

    　　[1] `PHP Manual <http://php.net/manual/en/book.json.php>`__

    　　[2] Ed Finkler, `JSON is Everybody’s
    Friend <http://phpadvent.org/2008/json-is-everybodys-friend-by-ed-finkler>`__

| （完）

.. note::
    原文地址: http://www.ruanyifeng.com/blog/2011/01/json_in_php.html 
    作者: 阮一峰 

    编辑: 木书架 http://www.me115.com